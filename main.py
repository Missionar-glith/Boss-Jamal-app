import streamlit as st

st.set_page_config(page_title="Boss Jamal Tech", page_icon="👑", layout="wide")

st.title("👑 Boss Jamal - App & Website Developer")

# --- PASSWORD WITH ENTER BUTTON ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    pwd = st.text_input("Enter Password to enter:", type="password", placeholder="letmein.so")
    
    # ENTER BUTTON UNDER PASSWORD
    if st.button("🔓 ENTER", use_container_width=True):
        if pwd.strip() == "letmein.so":
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("❌ Wrong password! Password na: letmein.so")
    
    st.warning("🔒 Password na: letmein.so - Type am and press ENTER button below")
    st.stop()

# --- AFTER PASSWORD CORRECT ---
st.success("Welcome to Boss Jamal Tech! ✅")
st.balloons()

st.markdown("## 🚀 I Build Apps, Websites & Advert Designs!")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 📱 App Development\n- Business Apps\n- Online Shops\n**From ₦20k**")
with col2:
    st.markdown("### 🌐 Website Design\n- Business Website\n- Portfolio\n**From ₦15k**")
with col3:
    st.markdown("### 📢 Advert App Design\n- Advert Apps\n- Promo Apps\n**From ₦10k**")

st.markdown("---")
st.markdown("## 📝 Need App or Website? Fill Form!")

with st.form("dev_form"):
    name = st.text_input("Your Full Name *")
    email = st.text_input("Your Email")
    whatsapp_num = st.text_input("Your WhatsApp Number *")
    facebook = st.text_input("Facebook Username")
    tiktok = st.text_input("TikTok Username")
    instagram = st.text_input("Instagram Username")
    project = st.selectbox("Wetin you need?", ["App Development", "Website Design", "Advert App Design"])
    details = st.text_area("Tell me about your business")
    
    submit = st.form_submit_button("🚀 Send To Boss Jamal")
    if submit:
        if name and whatsapp_num:
            msg = f"Hello Boss Jamal! I be {name}. I need {project}. Details: {details}. My number: {whatsapp_num}"
            link = f"https://wa.me/2348141957048?text={msg.replace(' ', '%20')}"
            st.success(f"Thanks {name}!")
            st.link_button("📱 Chat Boss Jamal on WhatsApp", link)
        else:
            st.error("Put Name and WhatsApp")

st.markdown("---")
st.markdown("### 👑 REACH BOSS JAMAL DIRECTLY")
st.markdown("**📱 WhatsApp: 08141957048**")
st.link_button("🔥 CHAT BOSS JAMAL NOW - 08141957048", "https://wa.me/2348141957048?text=Hello%20Boss%20Jamal!%20I%20need%20App/Website!", use_container_width=True)

if st.button("🔒 Logout"):
    st.session_state.unlocked = False
    st.rerun()

st.caption("👑 Boss Jamal Tech | WhatsApp: 08141957048 | Password: letmein.so")
