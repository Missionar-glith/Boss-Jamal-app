import streamlit as st

st.set_page_config(page_title="Boss Jamal Tech", page_icon="👑", layout="wide")

# --- PRO CSS ---
st.markdown("""
<style>
    h1 { font-size: 55px !important; text-align: center; }
    h2 { color: #FFD700; }
    .stButton > button { font-size: 22px !important; height: 60px !important; font-weight: bold; border-radius: 12px; }
    .whatsapp-btn { background-color: #25D366 !important; color: white !important; }
    .card { padding: 20px; border-radius: 15px; background: #f8f9fa; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>👑 Boss Jamal</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>App & Website Developer | Lagos, Nigeria</h3>", unsafe_allow_html=True)
st.write("---")

# --- PASSWORD GATE ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("### 🔒 Client Access")
        pwd = st.text_input("Enter Password:", type="password", placeholder="Enter password")
        if st.button("🔓 ENTER PORTFOLIO", use_container_width=True):
            if pwd.strip() == "letmein.so": # YOU FIT CHANGE THIS PASSWORD HERE
                st.session_state.unlocked = True
                st.rerun()
            else:
                st.error("Wrong password Boss!")
else:
    # --- WELCOME ---
    st.success("✅ YOU DON ENTER! WELCOME BOSS!")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 HOME", "💼 SERVICES", "🖼️ PORTFOLIO", "📞 CONTACT"])

    with tab1:
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("## Who Be Boss Jamal?")
            st.markdown("""
            I be professional **App & Website Developer** based for Lagos.
            I dey build:
            - 📱 Mobile Apps (Android & iOS)
            - 🌐 Modern Websites & E-commerce
            - 🤖 Streamlit & AI Apps like this one!
            - ⚡ Fast, Clean, Full Screen Apps
            
            **I no dey build small page - I dey build FULL SCREEN experience!**
            """)
            st.balloons()
        with col2:
            st.markdown("### 👑")
            st.info("**Status:** Available for new projects\n\n**Location:** Lagos, NG\n\n**Response:** Under 1 hour")

    with tab2:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="card"><h3>📱 App Development</h3><p>Flutter, React Native, Streamlit Apps - Fast & Full Screen!</p><p><b>From ₦150k</b></p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="card"><h3>🌐 Website Design</h3><p>Business, Portfolio, E-commerce, Church, School websites</p><p><b>From ₦80k</b></p></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="card"><h3>⚡ Fix & Upgrade</h3><p>Make your small page become BIG full screen like this one!</p><p><b>From ₦30k</b></p></div>', unsafe_allow_html=True)

    with tab3:
        st.markdown("## My Recent Work")
        p1, p2, p3 = st.columns(3)
        with p1:
            st.image("https://images.unsplash.com/photo-1551650975-87deedd944c3?w=500", caption="E-commerce Website")
        with p2:
            st.image("https://images.unsplash.com/photo-1512941937669-90a1b58e7e9a?w=500", caption="Mobile App Project")
        with p3:
            st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500", caption="Business Dashboard")
        st.info("👉 Replace these 3 images with YOUR own work later!")

    with tab4:
        st.markdown("## 📞 Contact Boss Jamal Now!")
        st.markdown("### Make we build your own FULL SCREEN app!")
        
        col_a, col_b = st.columns(2)
        with col_a:
            # CHANGE YOUR NUMBER HERE - Put your real WhatsApp number
            whatsapp_number = "2348012345678" # <--- CHANGE AM TO YOUR NUMBER
            whatsapp_link = f"https://wa.me/{whatsapp_number}?text=Hello%20Boss%20Jamal,%20I%20see%20your%20portfolio!"
            st.link_button("💬 CHAT ME ON WHATSAPP", whatsapp_link, use_container_width=True)
            st.link_button("📞 CALL ME", "tel:+2348012345678", use_container_width=True)
        with col_b:
            st.link_button("📧 SEND EMAIL", "mailto:bossjamal@gmail.com", use_container_width=True)
            st.text_input("Or leave your number, I go call you:", placeholder="080...")

    st.write("---")
    if st.button("🔒 LOGOUT"):
        st.session_state.unlocked = False
        st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 👑 Boss Jamal Tech")
    st.write("App & Website Developer")
    st.write("---")
    st.caption("To change password, open main.py line 35 - change `letmein.so` to your own password!")
    st.caption("To change WhatsApp number, change line 95")

