import streamlit as st , pandas as pd , datetime

with open('is_loged.txt','r')as read_file:
    file = read_file.read()


st.markdown(
    '''
<style>

span{

text-align:center;
}

label , input,.st-b3  {
direction :RTL;
}


</style>
''',
    unsafe_allow_html=True
)


def the_supp_names():
    df = pd.read_csv('suppliers.csv')

    return df['المورد'].tolist()



def get_supp_names(choose = 'names',supplier = ''):
    df = pd.read_csv('suppliers.csv')
    if choose == 'names':
        return list(df['المورد'])
    elif choose == 'ID':
        return list(df[df['المورد']==supplier]['الكود'])[0]



def add_items(id,date , categ , quan , price , mdfo3 , time ,note ='لا يوجد' ):
    df = pd.read_csv(f'suppliers/{id}.csv')

    df_inv = pd.read_csv('suppliers/suppliers_history.csv')

    if date and categ and quan and price and mdfo3 and time :

        data = pd.DataFrame({
                        'رقم العمليه':[len(df)+1],
                        'التاريخ':[date],
                        'الصنف':[categ],
                        'الكمية':[float(quan)],
                        'السعر':[float(price)],
                        'الإجمالي':[float(quan) * float(price)],
                        'المدفوع':[float(mdfo3)],
                        'المتبقي':[(quan * price)-mdfo3],
                        'المتبقي الكلي':[list(df['المتبقي'].cumsum())[-1]  + ((quan * price)-mdfo3)],
                        'ملاحظه':[note],
                        'الوقت':[time],
                    })
        data_for_inv = pd.DataFrame({
                        'رقم العمليه':[len(df)+1],
                        'التاريخ':[date],
                        'الصنف':[categ],
                        'الكمية':[float(quan)],
                        'السعر':[float(price)],
                        'الإجمالي':[float(quan) * float(price)],
                        'المدفوع':[float(mdfo3)],
                        'المتبقي':[(quan * price)-mdfo3],
                        'ملاحظه':[note],
                        'الوقت':[time],
                        'الكود':[id]
                    })
        
        df = pd.concat([df , data])
        df_inv = pd.concat([df_inv , data_for_inv])

        df.to_csv(f'suppliers/{id}.csv',index=False)
        df_inv.to_csv('suppliers/suppliers_history.csv',index=False)


    else:
        st.write('هناك ادخال غير صحيح')
        return



def submit():
    add_items(id , date , catego , quan , price , mdfo3 , time )
    if date and catego and quan and price and mdfo3 :
        st.success('تمت الإضافه بنجاح')




def add_function():
        # Create two columns
        col1, col2,col3 , col4 = st.columns(4)
        col11, col12,col13  = st.columns(3)

        global date , catego , quan , price , mdfo3 , time


        # Add text input elements to the columns
        with col1:
            date = st.date_input("ادخل تاريخ الإضافه ",datetime.datetime.now())

        with col2:
            catego = st.selectbox(label='اختر اسم الصنف' , options=['استيكر تحيا مصر 900',2,3,4])

        with col3:
            quan = st.text_input('ادخل الكميه',placeholder='الكميه')
            if quan:
                try:
                    quan = float(quan)
                except Exception as e:
                    st.write('هناك ادخال غير صحيح في حقل الكمية')
        with col4:
            price = st.text_input('ادخل السعر',placeholder='السعر')
            if price:
                try:
                    price = float(price)
                except Exception as e:
                    st.write('هناك ادخال غير صحيح في حقل السعر')

        with col13:
            mdfo3 = st.text_input('ادخل المبلغ المدفوع',placeholder='المبلغ المدفوع')
            if mdfo3:
                try:
                    mdfo3 = float(mdfo3)
                except Exception as e:
                    st.write('هناك ادخال غير صحيح في حقل المدفوع')
        with col11:
            note = st.text_input('ادخل الملاحظات',placeholder='ملاحظات')
        
        with col12:
            time = st.time_input('ادخل الوقت')
        

        st.button('إضافه',on_click=submit)

        

        

        df = pd.read_csv(f'suppliers/{id}.csv')

        st.write('')
        st.write('')

        st.write(df)




def delete_function():
    

        try:
                df = pd.read_csv(f'suppliers/{id}.csv')
                df_inv = pd.read_csv('suppliers/suppliers_history.csv')

                if process_num in list(df['رقم العمليه']):

                    df = df[df['رقم العمليه'] != process_num]
                    df_inv_2 = list(df_inv[((df_inv['رقم العمليه'] == process_num)&(df_inv['الكود'] == id))].index)[0]
                    df_inv.drop(index=df_inv_2,inplace=True)

                    df_inv.to_csv('suppliers/suppliers_history.csv',index = False)
                    df.to_csv(f'suppliers/{id}.csv',index = False)


                else:
                    st.write('رقم عمليه غير موجود')

        except Exception as e:
            return st.write('ادخال خاطئ')
    
    
    






if file == 'False':
    st.title('قم بتسجيل الدخول من فضلك')

else:
    st.title('إضافة مشتريات')
    supp_name = st.selectbox(label='اختر اسم المورد',options=the_supp_names())
    st.write('')
    st.write('')
    st.write('')
    

    if supp_name:
        id = get_supp_names('ID' , supp_name)
        

        option = st.radio('هل تريد الإضافه ام الحذف' , options=['إضافه','حذف'])

        if option == 'إضافه':
            try:
                add_function()
                    

            except Exception as e:
                st.write('لم تتم الإضافه بشكل صحيح')
        else:
            
            try:
                process_num = int(st.text_input('ادخل رقم العمليه التي تريد حذفها',placeholder='رقم العمليه'))
                st.write(f'رقم العمليه هو {process_num}') 
                st.button('حذف',on_click=delete_function)
                st.write(pd.read_csv(f'suppliers/{id}.csv'))
                st.success(f'تم حذف العمليه رقم {process_num}')

            except Exception as e:
                st.write('لم يتم ادخال رقم العمليه')
                st.write(pd.read_csv(f'suppliers/{id}.csv'))

                
            










