import streamlit as st

st.set_page_config(page_title="Boss Jamal Store", page_icon="👑", layout="centered")

# --- PASSWORD PROTECTION ---
st.title("👑 Boss Jamal Phones & Laptops")
password = st.text_input("Enter Password to enter shop:", type="password")

if password != "letmein.so":
    st.warning("🔒 Enter password: letmein.so to continue")
    st.stop()

st.success("Welcome Boss!")
st.balloons()

# --- YOUR SHOP ---
st.markdown("## 📱 Boss Jamal Phones & Laptops")
st.write("No.1 Phone Seller for Lagos! Fast Delivery!")
st.markdown("---")

# --- ADVERT / CONTACT SECTION - THIS NA THE MAIN THING ---
st.markdown("## 🚀 DO YOU NEED AN APP LIKE THIS?")

st.markdown("""
### 👑 Contact Boss Jamal - I Go Build Am For You!

**I dey build apps for any business:**
- 📱 Phone Shops
- 🍔 Restaurants & Food
- 👗 Boutiques & Fashion
- 💈 Salons & Barbers
- 🛒 Supermarkets

**Starting from ₦20,000 only!**
""")

# --- YOUR CONTACT FORM ---
with st.form("contact_form"):
    st.markdown("### 📝 Fill This Form If You Need App")
    name = st.text_input("Your Full Name")
    email = st.text_input("Your Email Address")
    whatsapp_num = st.text_input("Your WhatsApp Number")
    business = st.text_input("What Business You Get?")
    
    st.markdown("#### Follow Boss Jamal:")
    st.text_input("Facebook Username", placeholder="Boss Jamal Facebook")
    st.text_input("TikTok Username", placeholder="@bossjamal")
    st.text_input("Instagram Username", placeholder="@bossjamal_lagos")
    
    submitted = st.form_submit_button("📱 Send To Boss Jamal on WhatsApp")
    
    if submitted:
        if name and whatsapp_num:
            msg = f"Hello Boss Jamal! My name is {name}, I need app for my {business}. My email {email} and WhatsApp {whatsapp_num}"
            link = f"https://wa.me/2348141957048?text={msg.replace(' ', '%20')}"
            st.success(f"Thanks {name}! Click below to chat Boss Jamal")
            st.link_button("📱 Chat Boss Jamal Now!", link)
        else:
            st.error("Please enter Name and WhatsApp number")

st.markdown("---")

# --- BOSS JAMAL REAL CONTACTS ---
st.markdown("### 👑 REACH BOSS JAMAL DIRECTLY")
st.markdown("""
**📱 WhatsApp:** 08141957048  
**📧 Email:** bossjamal@gmail.com  
**👍 Facebook:** Boss Jamal Lagos  
**🎵 TikTok:** @bossjamal  
**📸 Instagram:** @bossjamal_lagos  

**Click Below To Chat Me Now!**
""")

whatsapp_link = "https://wa.me/2348141957048?text=Hello%20Boss%20Jamal!%20I%20need%20app%20like%20yours!"
st.link_button("🔥 📱 CHAT BOSS JAMAL ON WHATSAPP - 08141957048", whatsapp_link)

st.markdown("---")
st.caption("Built by Boss Jamal - Lagos Tech Boss 👑 | Password: letmein.so")
