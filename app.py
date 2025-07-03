
import openai
import streamlit as st

# Securely use OpenAI API
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💼 LinkedIn Post Generator")

# Input fields
topic = st.text_input("Enter a topic (e.g., Airline AI Strategy)")
goal = st.selectbox("What is the goal of this post?", ["Spark discussion", "Summarize news", "Share an insight", "Tell a story"])
tone = st.selectbox("Choose a tone", ["Professional", "Analytical", "Witty", "Casual"])

if st.button("Generate LinkedIn Post"):
    with st.spinner("Generating post..."):
        prompt = f"""
        Write a LinkedIn post about: {topic}
        The tone should be: {tone}.
        The goal is to: {goal}.

        Use a confident, human voice — not generic or robotic.
        Include 1 original insight or surprising angle.
        Avoid generic phrases like “In today’s fast-paced world.”
        End with a thought-provoking question or call to action.
        Make it sound like it was written by someone who actually works in this industry

        Make sure the post is 1–2 paragrpahs, engaging, starts with an interesting hook, and ends with a conversation starter or call to action.
        Do not fabricate information and cite your sources. Do not include emojis. 
        """

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a seasoned LinkedIn strategist who writes thoughtful, engaging, and insight-driven posts. Your tone should be professional but not stiff, with real personality. Posts must include an original point of view or analysis, avoid clichés, and end with a clear question or CTA to drive comments and engagement. You cite your sources."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=400
            )
            post = response.choices[0].message.content
            st.text_area("Generated LinkedIn Post", value=post, height=250)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
