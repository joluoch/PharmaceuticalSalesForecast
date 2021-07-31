import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image




pickle_in = open(r"C:\Users\Jakinda\Documents\Python Scripts\10Academy\PharmaceuticalSalesForecast\pickle\model.pkl","rb")
reg=pickle.load(pickle_in)



def random_forest_predict(DayOfWeek, Open, Promo, StateHoliday, SchoolHoliday, CompetitionDistance,
       CompetitionOpenSinceMonth, CompetitionOpenSinceYear, Promo2,
       Promo2SinceWeek, Promo2SinceYear, Month, Year,
       Day, WeekOfYear, weekday,StoreType_a, StoreType_b, StoreType_c, StoreType_d,
       Assortment_a, Assortment_b, Assortment_c,
       PromoInterval_Feb, PromoInterval_Jan,
       PromoInterval_Mar):
    
    """this will hold the regressor model 
    """
    prediction=reg.predict([[DayOfWeek, Open, Promo, StateHoliday, SchoolHoliday, CompetitionDistance,CompetitionOpenSinceMonth, CompetitionOpenSinceYear, Promo2,Promo2SinceWeek, Promo2SinceYear, Month, Year,Day, WeekOfYear, weekday,StoreType_a, StoreType_b, StoreType_c, StoreType_d,Assortment_a, Assortment_b, Assortment_c,PromoInterval_Feb, PromoInterval_Jan,PromoInterval_Mar]])
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
    CompetitionDistance = st.text_input("CompetitionDistance","Type Here")
    CompetitionOpenSinceMonth = st.text_input("CompetitionOpenSinceMonth","Type Here")
    CompetitionOpenSinceYear = st.text_input("CompetitionOpenSinceYear","Type Here")
    Promo2 = st.text_input("Promo2","Type Here")
    Promo2SinceWeek = st.text_input("Promo2SinceWeek","Type Here")
    Promo2SinceYear = st.text_input("Promo2SinceYear","Type Here")
    Month = st.text_input("Month","Type Here")
    Year = st.text_input("Year","Type Here")
    Day = st.text_input("Day","Type Here")
    WeekOfYear = st.text_input("WeekOfYear","Type Here")
    weekday = st.text_input("weekday","Type Here")
    StoreType_a = st.text_input("StoreType_a","Type Here")
    StoreType_b = st.text_input("StoreType_b","Type Here")
    StoreType_c = st.text_input("StoreType_c","Type Here")
    StoreType_d = st.text_input("StoreType_d","Type Here")
    Assortment_a = st.text_input("Assortment_a","Type Here")
    Assortment_b = st.text_input("Assortment_b","Type Here")
    Assortment_c = st.text_input("Assortment_c","Type Here")
    PromoInterval_Feb = st.text_input("PromoInterval_Feb","Type Here")
    PromoInterval_Jan = st.text_input("PromoInterval_Jan","Type Here")
    PromoInterval_Mar = st.text_input("PromoInterval_Mar","Type Here")
    

    result=""
    if st.button("Predict"):
        result=random_forest_predict(DayOfWeek, Open, Promo, StateHoliday, SchoolHoliday, CompetitionDistance,
        CompetitionOpenSinceMonth, CompetitionOpenSinceYear, Promo2,
        Promo2SinceWeek, Promo2SinceYear, Month, Year,
        Day, WeekOfYear, weekday,StoreType_a, StoreType_b, StoreType_c, StoreType_d,
        Assortment_a, Assortment_b, Assortment_c,
        PromoInterval_Feb, PromoInterval_Jan,
        PromoInterval_Mar)

    st.success('sales {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()