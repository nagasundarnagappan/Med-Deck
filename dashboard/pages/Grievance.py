import streamlit as st

with st.form("Med Deck"):
   st.write("Med Deck Grievance Addressal Form")
   name = st.text_input("Enter Your name")
   email = st.text_input("Enter Your Email Address")
   category = st.multiselect("Category: ",['Review', 'Complaint', 'Suggestion'])
   n = st.text_input("Enter Your grievance")
   file = st.file_uploader("Please choose a file(optional)")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("Form submitted succesfully")