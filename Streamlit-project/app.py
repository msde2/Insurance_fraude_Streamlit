import streamlit as st
from pycaret.classification import *
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('modelCB')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image = Image.open('fd.jpg')
    image_fd = Image.open('ifd.jpg')
    image_JA = Image.open('J&A.jpg')
    image_fraude = Image.open('Fraude.jpg')

    st.image(image_JA,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('As part of our consulting offer in Fraud Detection, at J&A we help industrial companies, banks, insurances and other financial institutions define strategies depending on their size and future perspectives, in order to better adapt to their needs. This not only permits us to deliver the best solution for every client as it is today (current level of maturity in Fraud Detection), but also establishes a path for its evolution in Fraud Detection solutions through time.')
    st.sidebar.success('J&A')
    
    st.sidebar.image(image_fraude)

    st.title("Insurance fraud Prediction App by J&A")

    if add_selectbox == 'Online':

        incident_severity=st.selectbox('incident_severity', [0,1,2,3])
        insured_hobbies=st.selectbox('insured_hobbies', ['reading', 'paintball', 'exercise', 'bungie-jumping', 'camping', 'movies', 'golf', 'kayaking', 'yachting', 'hiking', 'video-games', 'skydiving', 'base-jumping', 'board-games', 'polo', 'chess', 'dancing', 'sleeping', 'cross-fit', 'basketball'])
        capital_loss=st.number_input('capital_loss', min_value=0, max_value=115000, value=25)
        policy_annual_premium=st.number_input('policy_annual_premium', min_value=400, max_value=2100, value=1000)
        collision_type=st.selectbox('collision_type', ['Rear Collision','Side Collision','Front Collision','undocumented'])
        incident_state=st.selectbox('incident_state', ['NY','SC','WV','VA','NC','PA','OH'])
        loss_by_claims=st.number_input('loss_by_claims', min_value=-40000, max_value=110000, value=0)
        property_claim=st.number_input('property_claim', min_value=0, max_value=24000, value=0)
        

        output=""

        input_dict = {'incident_severity' : incident_severity, 'insured_hobbies' : insured_hobbies, 'capital_loss' : capital_loss, 'policy_annual_premium' : policy_annual_premium, 'collision_type' : collision_type, 'incident_state' : incident_state, 'property_claim' : property_claim, 'loss_by_claims' : loss_by_claims}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '(Fraud -> 1 or Not Fraud -> 0) The fraud prediction is :' + str(output)

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()
