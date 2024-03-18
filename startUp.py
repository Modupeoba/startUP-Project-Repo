import streamlit as st
import pandas as pd
import joblib
import warnings 
warnings.filterwarnings('ignore')

# st.title('START UP PROJECT')
# st.subheader('Built By Gomycode Daintree')

st.markdown("<h1 style = 'color: #5F0F40; text-align: center; font-family:TaHoma'>STARTUP PROFIT PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #FFB0B0; text-align: center; font-family: Birds of Paradise '>Built By Gomycode Data Science Daintree Cohort</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('pngwing.com.png')

st.header('Project Background Information', divider = True)
st.write(" overarching objective of this ambitious projeThect is to meticulously engineer a highly sophisticated predictive model meticulously designed to meticulously assess the intricacies of startup profitability. By harnessing the unparalleled power and precision of cutting-edge machine learning methodologies, our ultimate aim is to furnish stakeholders with an unparalleled depth of insights meticulously delving into the myriad factors intricately interpretewoven with a startup's financial success. Through the comprehensive analysis of extensive and multifaceted datasets, our mission is to equip decision-makers with a comprehensive understanding of the multifarious dynamics shaping the trajectory of burgeoning enterprises. Our unwavering commitment lies in empowering stakeholders with the indispensable tools and knowledge requisite for making meticulously informed decisions amidst the ever-evolving landscape of entrepreneurial endeavors.")


st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

data = pd.read_csv('startUp.csv')
st.dataframe(data)

st.sidebar.image('pngwing.com (2).png', caption = 'Welcome User')


st.sidebar.markdown("<br>", unsafe_allow_html= True)
st.sidebar.markdown("<br>", unsafe_allow_html= True)

# Declare user Input variables
st.sidebar.subheader('Input Variables', divider = True)
rd_spend = st.sidebar.number_input('Research And Development Expense')
admin = st.sidebar.number_input('Administrative Expense')
mkt = st.sidebar.number_input('Marketing Expense')cd 

# to confirm if the scalers has been transformed:   
st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

model = joblib.load('StartUpMod.pkl')
predicted = model.predict(input_var)

# Creating prediction and interpretepretation tab
prediction, inter = st.tabs(["Model Prediction","Model interpretepretation"])
with prediction:
    if prediction.button('Predict Profit'):
        prediction.snow()
        st.success(f'The predicted profit for your organisation is: {predicted[0].round(2)}')

with inter:
    intercept = model.intercept_
    coef = model.coef_
    inter.write(f'A percentage increase in Reseach and Development Expense makes Profit to increase by {coef[0].round(2)} naira')
    inter.write(f'A percentage increase in Administration Expense makes Profit to reduce by {coef[1].round(2)} naira')
    inter.write(f'A percentage increase in Marketting Expense makes Profit to increase by {coef[2].round(2)} naira')
    inter.write(f'The value of Profit when none of these expenses were made is {intercept.round(2)} naira')



