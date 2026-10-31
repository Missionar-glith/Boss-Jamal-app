import streamlit as st

st.set_page_config(page_title="Boss Jamal Tech", page_icon="👑", layout="wide")

# --- PASSWORD ---
st.title("👑 Boss Jamal - App & Website Developer")
pwd = st.text_input("Enter Password to enter:", type="password")
if pwd != "letmein.so":
    st.warning("🔒 Password na: letmein.so")
    st.stop()

st.success("Welcome to Boss Jamal Tech!")
st.balloons()

# --- HEADER ---
st.markdown("""
## 🚀 I Build Apps, Websites & Advert Designs!

**I dey help businesses for Lagos turn to ONLINE BOSSES!**

### 💻 MY SERVICES:
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 📱 App Development\n- Business Apps\n- Online Shops\n- Like Jumia Apps\n**From ₦20k**")
with col2:
    st.markdown("### 🌐 Website Design\n- Business Website\n- Portfolio Website\n- E-commerce Site\n**From ₦15k**")
with col3:
    st.markdown("### 📢 Advert App Design\n- Advert Apps\n- Promo Apps\n- Landing Pages\n**From ₦10k**")

st.markdown("---")
st.markdown("### 🎯 WHY CHOOSE BOSS JAMAL?")
st.markdown("""
- ✅ Fast Delivery - 1 to 3 days
- ✅ I go build am for PHONE - No laptop needed!
- ✅ Cheap price for Lagos business
- ✅ Support after I build am
- ✅ I teach you how to use am
""")

# --- CONTACT FORM ---
st.markdown("---")
st.markdown("## 📝 Need App or Website? Fill Form!")

with st.form("dev_form"):
    name = st.text_input("Your Full Name *")
    email = st.text_input("Your Email")
    whatsapp_num = st.text_input("Your WhatsApp Number *")
    facebook = st.text_input("Facebook Username")
    tiktok = st.text_input("TikTok Username")
    instagram = st.text_input("Instagram Username")
    project = st.selectbox("Wetin you need?", ["App Development", "Website Design", "Advert App Design", "All of them"])
    details = st.text_area("Tell me about your business/project")
    
    submit = st.form_submit_button("🚀 Send To Boss Jamal")
    
    if submit:
        if name and whatsapp_num:
            msg = f"Hello Boss Jamal! I be {name}. I need {project}. My business: {details}. My number: {whatsapp_num}"
            link = f"https://wa.me/2348141957048?text={msg.replace(' ', '%20')}"
            st.success(f"Thanks {name}! Boss Jamal go reply you now!")
            st.link_button("📱 Click To Chat Boss Jamal on WhatsApp", link)
        else:
            st.error("Put Name and WhatsApp number Boss")

# --- YOUR CONTACT ---
st.markdown("---")
st.markdown("### 👑 REACH BOSS JAMAL DIRECTLY - THE DEVELOPER!")
st.markdown("""
**📱 WhatsApp (Chat Me Now): 08141957048**  
**📧 Email: bossjamal.dev@gmail.com**  
**👍 Facebook: Boss Jamal Tech**  
**🎵 TikTok: @bossjamal_tech**  
**📸 Instagram: @bossjamal.tech**
""")

link = "https://wa.me/2348141957048?text=Hello%20Boss%20Jamal!%20I%20need%20App/Website!"
st.link_button("🔥 CHAT BOSS JAMAL NOW - 08141957048", link, use_container_width=True)

st.markdown("---")
st.caption("👑 Boss Jamal Tech | Lagos App & Website Developer | Password: letmein.so | WhatsApp: 08141957048")
