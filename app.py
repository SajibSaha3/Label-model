import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))


st.title("Polynomial Problem solve")
val1=st.slider("feature1",  min_value=10.0,max_value=50.0,step=0.01)
val2=st.slider("feature2", 1.0,50.0,.01)
val3=st.slider("feature12", 1.0,50.0,.01)
val4=st.slider("feature22", 1.0,50.0,.01)
val5=st.slider("feature3", 1.0,50.0,.01)		

data = [[val1,val2,val3,val4,val5]]
pred = model.predict(data)

if st.button("submit"):
    st.write("Prediction", pred)
