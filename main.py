import streamlit as st
st.set_page_config(page_title="Boss Jamal App")
st.title("👑 Boss Jamal App")
st.write("Welcome Boss! This works on PHONE!")
name = st.text_input("What is your name?")
password = st.text_input("Enter password:", type="password")
if st.button("LOGIN"):
    if password == "letmein":
        st.success(f"Access Granted! Welcome {name}!")
        st.balloons()
        st.info("You are a great programmer Boss!")
    else:
        st.error("Wrong password! Try again Boss!")
st.markdown("---")
st.caption("Made by Boss Jamal - Phone & Laptop Seller")

# --- BOSS JAMAL ADVERT ---
st.markdown("### 🚀 Need An App Like This For Your Business?")
st.markdown("I build business apps for shop owners!")
st.success("Your customers fit order online like Jumia!")
st.link_button("📱 DM Boss Jamal On WhatsApp", "https://wa.me/2348141957048")
st.markdown("My Live App: https://boss-jamal-app-b82f6my3fukdq88mnh3d3f.streamlit.app/")
st.caption("Built by Boss Jamal - Lagos Tech Boss 👑")
st.markdown("If you need business app, DM Boss Jamal!")
