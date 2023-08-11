import streamlit as st
import requests

st.title('Calculator App')

num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')

operation = st.selectbox('Select an operation', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

if st.button('Calculate'):
    response = requests.get('http://127.0.0.1:8000/calculate', data={'number1': num1, 'number2': num2, 'operation': operation})

    # st.write(response)
    result = response.json()['result']
    st.write('Result:', result)
