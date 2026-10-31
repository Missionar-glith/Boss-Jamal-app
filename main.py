import streamlit as st

st.set_page_config(page_title="Boss Jamal Store", page_icon="📱", layout="wide")
st.title("📱 Boss Jamal Phones & Laptops 👑")
st.write("No.1 Phone Seller for Lagos! Fast Delivery!")

# --- PRODUCTS - YOU FIT CHANGE PRICE ---
products = [
    {"name": "iPhone 14 Pro Max", "price": 850000, "img": "📱"},
    {"name": "Samsung S23 Ultra", "price": 750000, "img": "📱"},
    {"name": "HP Laptop 15", "price": 450000, "img": "💻"},
    {"name": "iPhone 13", "price": 550000, "img": "📱"},
    {"name": "Tecno Camon 20", "price": 150000, "img": "📱"},
    {"name": "Lenovo ThinkPad", "price": 380000, "img": "💻"},
]

# --- SEARCH ---
search = st.text_input("🔍 Search phone or laptop...")
if search:
    products = [p for p in products if search.lower() in p["name"].lower()]

# --- SHOW PRODUCTS ---
if "cart" not in st.session_state:
    st.session_state.cart = []

cols = st.columns(2)
for i, p in enumerate(products):
    with cols[i % 2]:
        st.markdown(f"### {p['img']} {p['name']}")
        st.markdown(f"**₦{p['price']:,}**")
        if st.button(f"Add to Cart - {p['name']}", key=f"btn_{i}"):
            st.session_state.cart.append(p)
            st.success(f"{p['name']} added!")
            st.balloons()

st.markdown("---")

# --- CART ---
st.subheader(f"🛒 Your Cart ({len(st.session_state.cart)} items)")
total = 0
for item in st.session_state.cart:
    st.write(f"- {item['name']} - ₦{item['price']:,}")
    total += item['price']

if total > 0:
    st.markdown(f"### Total: ₦{total:,}")
    whatsapp_msg = f"Hello Boss Jamal! I want to buy: {[x['name'] for x in st.session_state.cart]} Total ₦{total:,}"
    link = f"https://wa.me/2348141957048?text={whatsapp_msg.replace(' ', '%20')}"
    st.link_button("📱 Order Now on WhatsApp", link)
    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()

# --- YOUR ADVERT ---
st.markdown("---")
st.markdown("### 🚀 Need An App Like This For Your Business?")
st.success("Your customers fit order online like Jumia!")
st.link_button("📱 DM Boss Jamal On WhatsApp", "https://wa.me/2348141957048")
st.caption("Built by Boss Jamal - Lagos Tech Boss 👑")
