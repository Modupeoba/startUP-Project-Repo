import streamlit as st
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

# st.title('START UP PROJECT')
# st.subheader('Built By Gomycode Daintree')

st.markdown("<h1 style = 'color: #5F0F40; text-align: center; font-family:TaHoma'>STARTUP PROFIT PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #FFB0B0; text-align: center; font-family: Great Vibes '>Built By Gomycode Data Science Daintree Cohort</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('pngwing.com.png')

st.header('Project Background Information', divider = True)
st.write("The overarching objective of this ambitious project is to meticulously engineer a highly sophisticated predictive model meticulously designed to meticulously assess the intricacies of startup profitability. By harnessing the unparalleled power and precision of cutting-edge machine learning methodologies, our ultimate aim is to furnish stakeholders with an unparalleled depth of insights meticulously delving into the myriad factors intricately interwoven with a startup's financial success. Through the comprehensive analysis of extensive and multifaceted datasets, our mission is to equip decision-makers with a comprehensive understanding of the multifarious dynamics shaping the trajectory of burgeoning enterprises. Our unwavering commitment lies in empowering stakeholders with the indispensable tools and knowledge requisite for making meticulously informed decisions amidst the ever-evolving landscape of entrepreneurial endeavors.")


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
mkt = st.sidebar.number_input('Marketing Expense')

import streamlit as st
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')

# st.title('START UP PROJECT')
# st.subheader('Built By Gomycode Daintree')

st.markdown("<h1 style = 'color: #FE7A36; text-align: center; font-family: helvetica '>STARTUP PROJECT</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #191717; text-align: center; font-family: Trebuchet MS (sans-serif)': cursive '>Built By Gomycode Daintree</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('pngwing.com.png')

st.markdown("""<style>.custom-header{font-family:'Garamond',serif;font-size:24px;color:#191717;text-align:left;padding-bottom:10px;}</style>""", unsafe_allow_html=True)
st.markdown('<h1 class="custom-header">Project Background Information</h1>', unsafe_allow_html=True)


st.write("""
    <style>
        .custom-text {
            font-family: 'Arial', sans-serif;
            font-size: 16px;
            line-height: 1.5;
        }
    </style>
    <div class='custom-text'>
        The overarching objective of this ambitious project is to meticulously engineer a highly sophisticated predictive model meticulously designed to meticulously assess the intricacies of startup profitability. By harnessing the unparalleled power and precision of cutting-edge machine learning methodologies, our ultimate aim is to furnish stakeholders with an unparalleled depth of insights meticulously delving into the myriad factors intricately interwoven with a startup's financial success. Through the comprehensive analysis of extensive and multifaceted datasets, our mission is to equip decision-makers with a comprehensive understanding of the multifarious dynamics shaping the trajectory of burgeoning enterprises. Our unwavering commitment lies in empowering stakeholders with the indispensable tools and knowledge requisite for making meticulously informed decisions amidst the ever-evolving landscape of entrepreneurial endeavors.
    </div>
    """, unsafe_allow_html=True)



st.markdown("""<style>.custom-header{font-family:'Garamond',serif;font-size:24px;color:#191717;text-align:left;padding-bottom:10px;}</style>""", unsafe_allow_html=True)
st.markdown('<h1 class="custom-header">Historical Data</h1>', unsafe_allow_html=True)
data = pd.read_csv('startUp.csv')
st.dataframe(data)

st.sidebar.image('pngwing.com (2).png', caption = 'Welcome User')

st.sidebar.markdown("<br>", unsafe_allow_html= True)
st.sidebar.markdown("<br>", unsafe_allow_html= True)

# Declare user Input variables
st.sidebar.subheader('Input Variables', divider = True)
rd_spend = st.sidebar.number_input('Research And Development Expense')
admin = st.sidebar.number_input('Administrative Expense')
mkt = st.sidebar.number_input('Marketing Expense')

