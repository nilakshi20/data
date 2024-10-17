import streamlit as st
st.title('Loan application App')
l=st.number_input('Enter your amount for loan amount')
s=st.number_input('Enter your salary')
c=st.number_input('Enter your credit score ')
if s>=40000 and c>=500:
    st.write('congratulations')
else:
    st.write ('we are sorry')