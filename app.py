import streamlit as st
from reviewer import run_review
from utils import save_review

st.set_page_config(page_title="Code Reviewer", layout="centered")

st.title("🔍 Code Reviewer — LLM-Powered")
st.caption("Local code reviews using DeepSeek via Ollama")

# Upload code
uploaded_file = st.file_uploader("Upload a .py or .txt file", type=["py", "txt"])
mode = st.selectbox("Review Mode", ["default", "beginner_friendly", "strict"])

if uploaded_file:
    code_str = uploaded_file.read().decode("utf-8")
    st.code(code_str, language="python")

    if st.button("Run Review"):
        with st.spinner("Running review with DeepSeek..."):
            review = run_review(code_str, mode)
            st.markdown(review)

            # Save option
            if st.checkbox("Save review to /reviews"):
                filename = uploaded_file.name.rsplit(".", 1)[0] + "_review.md"
                save_review(review, f"reviews/{filename}")
                st.success(f"✅ Saved to reviews/{filename}")