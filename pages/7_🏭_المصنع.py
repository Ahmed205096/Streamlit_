import streamlit as st , pandas as pd

with open('is_loged.txt','r')as read_file:
    file = read_file.read()

st.markdown(
    '''
<style>

span{

text-align:center;
}

   
</style>
''',
    unsafe_allow_html=True
)



if file == 'False':
    st.title('قم بتسجيل الدخول من فضلك')


else:
    st.title('صفحة المصنع')
    
