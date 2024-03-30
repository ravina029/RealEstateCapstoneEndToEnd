import streamlit as st
import pickle 
import pandas as pd
import numpy as np
#import xgboost 


st.set_page_config(page_title="Visualization of the data")


with open("website/df.pkl",'rb') as file:
    df=pickle.load(file)

with open("website/pipelineXGB.pkl",'rb') as file:
    pipeline=pickle.load(file)

#st.dataframe(df)  for visualizing the data


#Column names 
#property_type	sector	bedRoom	bathroom	balcony	agePossession	built_up_area	servant room	store room	furnishing_type	luxury_category	floor_category

st.header('Enter your inputs')
Property_Type=st.selectbox('Property Type',['flat','house'])

#select sector 
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

#bedroom
bedRoom=float(st.selectbox('Select number of BedRoom',sorted(df['bedRoom'].unique().tolist())))  #converted to float because stremtli gave string

#bathroom
bathroom=float(st.selectbox('Select number of Bathroom',sorted(df['bathroom'].unique().tolist())))

#Balcony
balcony= st.selectbox('Select number of Balcony',sorted(df['balcony'].unique().tolist()))

#agePossession
agePossession= st.selectbox('Select Property age',sorted(df['agePossession'].unique().tolist()))

#built_up_area
built_up_area=float(st.number_input("Built_up_Area"))

#servant room
servant_room=float(st.selectbox('Require servant room',[0.0,1.0]))

#store room
store_room=float(st.selectbox('Require store room',[0.0,1.0]))

#furnishing_type
furnishing_type= st.selectbox('select furnish type',sorted(df['furnishing_type'].unique().tolist()))

#luxury_category
luxury_category= st.selectbox('Select luxury_category',sorted(df['luxury_category'].unique().tolist()))

#floor_category
floor_category= st.selectbox('Select floor_category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    #form a dataframe
    data = [[Property_Type, sector, bedRoom, bathroom, balcony, agePossession, built_up_area,servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=columns)
    #st.dataframe(df)

    #Predict
    base_price_text = np.expm1(pipeline.predict(df))[0]
    base_price = float(base_price_text)
    low_range = base_price - 0.20
    high_range = base_price + 0.20

    st.text("price of the property lies in the range {}Cr and {}Cr".format(round(low_range, 2), round(high_range, 2)))






