import streamlit as st


st.markdown('''
<style>
label , input {
    direction:RtL;
    }

.st-emotion-cache-nahz7x{
   position:absolute;
   right:10px;        
}
    
span{
    text-align : center;
}
            

            
</style>
''' , unsafe_allow_html=True)



st.title('تسجيل الدخول')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')


with st.form('Form1'):
    user_name = st.text_input('ادخل اسم المستخدم', placeholder='اسم المستخدك')
    password = st.text_input('ادخل كلمة المرور',type='password',placeholder='كلمة المرور')

    st.form_submit_button('دخول' , use_container_width=True)


if user_name and password:
    if user_name == 'محمد خطاب' and password == '1111':
        with open('is_loged.txt' , 'w') as write_file:
            write_file.write('True')
        st.success('تم تسجيل الدخول بنجاح', icon="✅")
    
    else:
        with open('is_loged.txt' , 'w') as write_file:
            write_file.write('False')
else:
        with open('is_loged.txt' , 'w') as write_file:
            write_file.write('False')


