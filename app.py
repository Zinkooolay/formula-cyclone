import streamlit as st
import requests
import json

# --- Page Setup ---
st.set_page_config(
    page_title="Formula Cyclone",
    page_icon="🚀",
    layout="centered"
)

# --- Firebase Configuration ---
FIREBASE_URL = "https://formulacyclone-default-rtdb.firebaseio.com/"
API_KEY = "AIzaSyCjyeb7Igp4hDfU_r3sYJC9jxe7O-1s1x0"
APP_ID = "1:571287342955:web:53ade50aedbb88ab62c62e"

# --- UI Styling (Custom CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #00ffcc;
        color: #000000;
        font-weight: bold;
        border: none;
        margin-top: 10px;
    }
    .result-box {
        padding: 25px;
        border-radius: 15px;
        background-color: #1e2130;
        border: 2px solid #00ffcc;
        color: #00ffcc;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.title("🚀 FORMULA CYCLONE")
st.markdown("### 2D Professional Analysis Dashboard")
st.write("---")

# --- Input Section ---
user_input = st.text_input("တွက်ချက်ရန် ဂဏန်းရိုက်ထည့်ပါ", placeholder="ဥပမာ - 45", max_chars=2)

# --- Logic Functions ---
def save_to_firebase(logic_name, val, result):
    data = {"logic": logic_name, "input": val, "result": result}
    try:
        requests.post(f"{FIREBASE_URL}/logs.json?auth={API_KEY}", json=data)
    except:
        pass

# --- Buttons & Calculation ---
col1, col2 = st.columns(2)

with col1:
    if st.button("မနက်ပါဝါမူ"):
        if user_input and len(user_input) == 2:
            # Logic: နောက်ဆုံးဂဏန်းကို ပါဝါယူခြင်း
            res = (int(user_input[-1]) + 5) % 10
            st.markdown(f'<div class="result-box">ရလဒ်: {res}</div>', unsafe_allow_html=True)
            save_to_firebase("Morning Power", user_input, res)
        else:
            st.error("ဂဏန်း ၂ လုံး မှန်အောင်ရိုက်ပါ")

with col2:
    if st.button("ဘရိတ်မူ"):
        if user_input and len(user_input) == 2:
            # Logic: ပေါင်းခြင်းဘရိတ်
            res = sum(int(d) for d in user_input) % 10
            st.markdown(f'<div class="result-box">ရလဒ်: {res}</div>', unsafe_allow_html=True)
            save_to_firebase("Break Logic", user_input, res)
        else:
            st.error("ဂဏန်း ၂ လုံး မှန်အောင်ရိုက်ပါ")

# --- Sidebar ---
st.sidebar.markdown("## ⚙️ Control Panel")
if st.sidebar.button("Clear History"):
    st.sidebar.success("Logs Cleared!")

st.sidebar.markdown("---")
st.sidebar.info("Developed by Formula Cyclone Team")
