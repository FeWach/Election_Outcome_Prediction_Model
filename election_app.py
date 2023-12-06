import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
from sklearn.preprocessing import StandardScaler
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Political Election Simulator', page_icon=':crystal_ball:', layout='wide')

def load_animation_header(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_animation_contact(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
local_css('StreamlitApp\style\style.css.txt')        

# --- Loading the model and assets ---#

with open(r"C:\Users\felix\StreamlitApp\calib_election_model.pckl", "rb") as p:
    model = pickle.load(p)

animation_header = load_animation_header('https://lottie.host/2cbc25f7-cdf5-4435-a84d-45f4d1a34f39/xVF80LC0b8.json')
animation_contact = load_animation_contact('https://lottie.host/7404a4a3-f844-47f5-96f3-d16ca15f379b/D6LjKZxBfb.json')

## --- App section ---##

# Creating the main function #

str1 = 'The incumbent party is more likely to stay in power'
str2 = 'The incumbent party is more likely to lose power'

def election_prediction(input_data):

    # Changing the input_data to numpy array #

    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # Scaler disabled #

    #scaler = StandardScaler()
    #scaled_data = scaler.fit_transform(input_data_reshaped)

    # Making the prediction #
    prediction = model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return str1
    return str2

   
def main():
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.title('Political Election Simulator')
            st.subheader('United States of America, Federal Presidential Election')
            st.write('„Nothing in life is certain except death and taxes“ - Benjamin Franklin')
            st.write('''The aim of this app is to be able to accurately predict whether it is more likely that the ruling party, in the case of the United States of America either the Democratic or the Republican Party, will lose or stay in power depending on various factors. The model will make a prediction after being fed with the required data. It is assumed that all of the elements listed below in the questionnaire will impact the outcomes of elections on the federal level. For more information go to my [GitHub >](https://github.com/FeWach).
            \nDemocracy should not be boring and, in this spirit, I hope that you have fun using this app.''')   
        with right_column:
            st.lottie(animation_header, height=350)
    st.write('---')
 
    # Getting input data from the user
    outgoing = st.number_input('If the sitting president is in his or her final term choose 1, if not choose 0', 0, 1)
    majority_change = st.number_input('If the most recent midterm elections led to a majority change in the House of Representatives choose 1, if not choose 0', 0, 1)
    GDP_growth = st.number_input('Enter the most recent annual GDP growth rate, i.e. 4.50')
    unemployment_rate = st.number_input('Enter the most recent annual unemployment rate, i.e. 5.95')
    inflation_rate = st.number_input('Enter the most recent annual inflation rate, i.e. 3.25')
    approval_rating_incumbent = st.number_input('Enter the most recent presidential approval rating, i.e. 50.00')
    war_period = st.number_input('In the case of the occurrence of wars, significantly impacting U.S. politics, choose 1, if not choose 0', 0, 1)
    major_events = st.number_input('In the case of the occurrence of other extraordinary events, significantly impacting U.S. politics, i.e. political scandals, financial crises, terror attacks, choose 1, if not choose 0', 0, 1)
 
    # Code for prediction #
    outcome = ''
 
    # Creating button for prediction #
    if st.button('Election Outcome Result'):
        outcome = election_prediction([outgoing,majority_change,GDP_growth,unemployment_rate,inflation_rate,approval_rating_incumbent,war_period,major_events])
 
        st.success(outcome)
    st.write('##')

if __name__ == '__main__':
    main()

##--- Contact form ---##
                                                                                                
with st.container():
    st.write('---')
    st.header('Pleased with what you saw? Constructive criticism? Get in touch!')
    st.write('##')
    
    contact_form = '''<form action="https://formsubmit.co/felix.wach@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="False">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder = "Your message here" required></textarea>
     <button type="submit">Send</button>
</form>'''
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.lottie(animation_contact, height=350)
st.write('---')
st.write(':copyright:''2023'' ''Felix Wach')
st.write('Wolfratshausen, Germany')
            


