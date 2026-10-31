import streamlit as st

# THIS MAKE AM FULL WIDE + BIG
st.set_page_config(
    page_title="Boss Jamal Tech", 
    page_icon="👑", 
    layout="wide"
)

# MAKE EVERYTHING BIG WITH CSS
st.markdown("""
<style>
    h1 { font-size: 60px !important; text-align: center; }
    .stTextInput > div > div > input { font-size: 25px !important; height: 60px !important; }
    .stButton > button { font-size: 30px !important; height: 70px !important; background-color: #FFD700; color: black; font-weight: bold; }
    p { font-size: 22px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>👑 Boss Jamal</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>App & Website Developer</h2>", unsafe_allow_html=True)

st.write("---")

# PASSWORD
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        pwd = st.text_input("Enter Password to enter:", type="password")
        if st.button("🔓 ENTER", use_container_width=True):
            if pwd.strip() == "letmein.so":
                st.session_state.unlocked = True
                st.rerun()
            else:
                st.error("Wrong password!")
else:
    st.balloons()
    st.markdown("<h1 style='text-align:center; color:green;'>✅ YOU DON ENTER! WELCOME BOSS!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>This na your FULL SCREEN APP - E DON BIG NOW!</h2>", unsafe_allow_html=True)
