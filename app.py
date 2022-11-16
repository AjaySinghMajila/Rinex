import streamlit as st
import joblib

model = joblib.load('spam-ham')#we are loading the pipeline model using joblib
st.title('SPAM-HAM CLASSIFIER')#It creates a title in webapp
ip = st.text_input('Enter the message')#It creates a text box in the webapp
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) #st.button Creates a button with the name predict
  #st.title([0]) #the 0th element in op variable is displayed as a title
