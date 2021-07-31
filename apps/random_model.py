import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image




pickle_in = open(r"C:\Users\Jakinda\Documents\Python Scripts\10Academy\PharmaceuticalSalesForecast\pickle\model.pkl","rb")
reg=pickle.load(pickle_in)



def random_forest_predict(DayOfWeek, Open, Promo, StateHoliday, SchoolHoliday,
       StoreType, Assortment, CompetitionDistance,
       CompetitionOpenSinceMonth, CompetitionOpenSinceYear, Promo2,
       Promo2SinceWeek, Promo2SinceYear, PromoInterval, Month, Year,
       Day, WeekOfYear, weekday):
    
    """this will hold the regressor model 
    """
    prediction=reg.predict([[DayOfWeek, Open, Promo, StateHoliday, SchoolHoliday,
       StoreType, Assortment, CompetitionDistance,
       CompetitionOpenSinceMonth, CompetitionOpenSinceYear, Promo2,
       Promo2SinceWeek, Promo2SinceYear, PromoInterval, Month, Year,
       Day, WeekOfYear, weekday]])
    print(prediction)
    return prediction




def main():
    st.title("RANDOM MODEL")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> STORE SALES ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    DayOfWeek = st.text_input("DayOfWeek","Type Here")
    Open = st.text_input("Open","Type Here")
    Promo = st.text_input("Promo","Type Here")
    StateHoliday = st.text_input("StateHoliday","Type Here")
    SchoolHoliday = st.text_input("SchoolHoliday","Type Here")
    StoreType= st.text_input("StoreType","Type Here")
    Assortment = st.text_input("Assortment","Type Here")
    CompetitionDistance = st.text_input("CompetitionDistance","Type Here")
    CompetitionOpenSinceMonth = st.text_input("CompetitionOpenSinceMonth","Type Here")
    CompetitionOpenSinceYear = st.text_input("CompetitionOpenSinceYear","Type Here")
    Promo2 = st.text_input("Promo2","Type Here")
    Promo2SinceWeek = st.text_input("Promo2SinceWeek","Type Here")
    Promo2SinceYear = st.text_input("Promo2SinceYear","Type Here")
    PromoInterval_Feb = st.text_input("PromoInterval_Feb","Type Here")
    Month = st.text_input("Month","Type Here")
    Year = st.text_input("Year","Type Here")
    Day = st.text_input("Day","Type Here")
    WeekOfYear = st.text_input("WeekOfYear","Type Here")
    weekday = st.text_input("weekday","Type Here")
    
    

    result=""
    if st.button("Predict"):
        result=random_forest_predict(DayOfWeek, Open, Promo, StateHoliday, SchoolHoliday,StoreType, Assortment,CompetitionDistance,
        CompetitionOpenSinceMonth, CompetitionOpenSinceYear, Promo2,
        Promo2SinceWeek, Promo2SinceYear, PromoInterval_Feb,Month, Year,
        Day, WeekOfYear, weekday)

    st.success('sales {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()