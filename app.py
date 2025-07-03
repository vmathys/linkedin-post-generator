
import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("LinkedIn Post Generator")

# Input fields
topic = st.text_input("Enter a topic (e.g., Airline AI Strategy)")
goal = st.selectbox("What is the goal of this post?", ["Spark discussion", "Summarize news", "Share an insight", "Tell a story"])
tone = st.selectbox("Choose a tone", ["Professional", "Analytical", "Witty", "Casual"])

if st.button("Generate LinkedIn Post"):
    with st.spinner("Generating..."):
        prompt = f"""
        Write a LinkedIn post about: {topic}
        Tone: {tone}
        Goal: {goal}

        Make sure the post is 3–5 sentences, engaging, and ends with a conversation starter or call to action.
        Include 3–5 relevant hashtags at the end.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a LinkedIn thought leader."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        post = response["choices"][0]["message"]["content"]
        st.text_area("Your Generated LinkedIn Post", post, height=200)
