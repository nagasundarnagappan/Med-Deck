import streamlit as st

with st.form("Med Deck"):
   st.write("Med Deck Registration Form")
   name = st.text_input("Enter Patient's name")
   age = st.text_input("Enter Your Age")
   file = st.file_uploader("Please choose a file(optional)")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("Form submitted succesfully")