import streamlit as st
import time
import random

# Streamlit Page Config
st.set_page_config(page_title="Eid Mubarak Greetings", page_icon="🌙", layout="wide")

# CSS for 3D Text Animation & Background
st.markdown(
    """
    <style>
    @keyframes glow {
        0% { text-shadow: 0 0 5px #fff, 0 0 10px #ffcc00, 0 0 20px #ffcc00; }
        50% { text-shadow: 0 0 10px #ffcc00, 0 0 20px #ff6600, 0 0 30px #ff6600; }
        100% { text-shadow: 0 0 5px #fff, 0 0 10px #ffcc00, 0 0 20px #ffcc00; }
    }
    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    h1 {
        text-align: center;
        font-size: 50px;
        color: #228B22;
        animation: glow 2s infinite alternate;
    }
    .message-box {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        animation: floating 3s infinite;
    }
    body {
        background: url('https://source.unsplash.com/1600x900/?eid,muslim,celebration') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Eid Mubarak Banner
st.markdown("""
    <h1>🌙 Eid Mubarak! 🎉</h1>
    <p style='text-align: center; font-size: 20px;'>Create and share personalized Eid greetings with stunning effects!</p>
""", unsafe_allow_html=True)

# User Input
name = st.text_input("Enter your name:", "")
custom_message = st.text_area("Enter your Eid message:", "Wishing you a joyful and blessed Eid! 🌙✨")

if name:
    eid_greeting = f"Eid Mubarak, {name}! 🎉\n{custom_message}"
    with st.container():
        st.markdown(f"""
        <div class='message-box'>
            <h2 style='color: #FFD700;'>🌟 {eid_greeting} 🌟</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Download Greeting as Text File
    st.download_button(label="📥 Download Greeting", data=eid_greeting, file_name=f"Eid_Greeting_{name}.txt", key="download")

# Footer
st.markdown("<p style='text-align: center; font-size: 14px;'>Developed with ❤️ for Eid 2025</p>", unsafe_allow_html=True)
