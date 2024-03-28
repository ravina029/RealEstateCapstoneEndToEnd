import streamlit as st
import plotly.express as px
import pandas as pd
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Property Analysis", page_icon="📈")

#data to be used
with open("website/data_with_price.pkl",'rb') as file:
    df=pickle.load(file)

feature_text = pickle.load(open('/Users/ravina/Desktop/RealEstateProject/website/feature_text.pkl','rb'))
#complete text data for all sectors
with open("website/transformed_wordcloud_df.pkl",'rb') as file:
   transformed_wordcloud_df = pickle.load(file)


st.title('Analytics')


#Number of flats vs House
st.header("Number of flats vs House")
sector_options = df['sector'].unique().tolist()
sector_options.insert(0, 'all Sectors')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'all Sectors':
    filtered_df = df
else:
    filtered_df = df[df['sector'] == selected_sector]

fig_property_type = px.bar(filtered_df, x='property_type', color='property_type', title=f'Count of flats and house in {selected_sector}')
st.plotly_chart(fig_property_type, use_container_width=True)


# AgePossession
st.header('Property Age Possession')
property_type = st.selectbox("Select House or Flat", ['flat', 'house'])
filtered_df = df[df['property_type'] == property_type]

fig = px.histogram(filtered_df, x='agePossession', title='Property Age Distribution')
st.plotly_chart(fig, use_container_width=True)


# Wordcloud

st.header('Provided Facilities')

selected_sector_options = transformed_wordcloud_df['sector'].unique().tolist()
selected_sector_options.insert(0, 'Overall Gurgaon')
selected_sector = st.selectbox('Select a sector', selected_sector_options)

if selected_sector == 'Overall Gurgaon':
    selected_sector_df = transformed_wordcloud_df
else:
    selected_sector_df = transformed_wordcloud_df[transformed_wordcloud_df['sector'] == selected_sector]

if selected_sector == 'Overall Gurgaon':
    features_text = ' '.join(transformed_wordcloud_df['features'].astype(str))
else:
    features_text = ' '.join(selected_sector_df['features'].astype(str))

wordcloud = WordCloud(width=800, height=800, background_color='black').generate(features_text)
fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)

wordcloud_plot = ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)

st.pyplot(fig)



#Area Vs Price
st.header('Area Vs Price')
property_type = st.selectbox("Select Property Type", ['flat', 'house'])

if property_type == 'house':
    fig1 = px.scatter(df[df['property_type'] == 'house'],
                      x="built_up_area",
                      y="price",
                      color="bedRoom", title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(df[df['property_type'] == 'flat'],
                      x="built_up_area",
                      y="price",
                      color="bedRoom", title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)


#BHK Pie Chart
st.header('BHK Pie Chart')

sector_options = df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(df[df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

st.header('BHK price comparison')

fig3 = px.box(df[df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


#Distplot for property type
st.header('Distplot for property type')

fig4 = plt.figure(figsize=(10, 4))
sns.distplot(df[df['property_type'] == 'house']['price'],label='house')
sns.distplot(df[df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig4)

