import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon=":shark:", layout="wide")

# Title & Headers
st.title("🚀 Growth Mindset Challenge")
st.header("📌 Header Section")
st.subheader("💡 Subheader Section")
st.write("✨ Welcome to the Growth Mindset Challenge!")  # Markdown

# Quote Section
st.header("💬 Quote of the Day")
st.markdown("> *Success is not final, failure is not fatal: It is the courage to continue that counts.*")
st.write("— Winston Churchill")

# Code Input Section
st.header("💻 Code Challenge")
user_input = st.text_input("Enter your code snippet here:")

if user_input:
    st.success(f"✅ Your code: `{user_input}`. Keep pushing forward towards your goal! 💪")
else:
    st.warning("⚠️ Please enter your code to proceed.")

# Reflection Section
st.header("🤔 Reflection")
reflection = st.text_area("Share your thoughts on today's progress:")

if reflection:
    st.success(f"🌟 Great insight! Your reflection: *{reflection}*")
else:
    st.info("📝 Reflecting on past experiences helps you grow! Share your difficulties.")

# Achievements Section
st.header("🏆 Achievements")
achievements = st.text_area("List your achievements here:")

if achievements:
    st.success(f"🎉 Amazing! Your achievements: *{achievements}*")
else:
    st.warning("🚀 Please share your achievements to celebrate progress!")

# Footer
st.markdown("---")
st.write("📌 **Created by Muhammad Sarim **")


# Mobile Responsive Design:
st.markdown(
    """
    <style>
        body { font-family: 'Arial', sans-serif; }
        .stTextInput, .stTextArea { width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True
)
