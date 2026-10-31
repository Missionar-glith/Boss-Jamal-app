import streamlit as st
st.set_page_config(page_title="Boss Jamal App", page_icon="👑")
st.title("👑 Boss Jamal App")
st.write("Welcome Boss! This works on PHONE too!")
name = st.text_input("What is your name?")
password = st.text_input("Enter password:", type="password")
if st.button("LOGIN"):
    if password == "letmein":
        st.success(f"Access Granted! Welcome {name}!")
        st.balloons()
        st.info("You are a great programmer, Boss Jamal!")
    else:
        st.error("Wrong password! Try again.")
st.markdown("---")
st.caption("Made by Boss Jamal - Phone & Laptop Ready!")
