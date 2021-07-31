import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image
#from apps import deep_model, random_model



#pickle_in = open("classifier.pkl","rb")
#classifier=pickle.load(pickle_in)

st.set_page_config(page_title="STORE ANALYSIS", layout="wide")
st.title("STORE SALES PREDICTION")

display_visual= st.sidebar.selectbox('options',('Predict store sales','predict 6 weeks ahead'))


    
       