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



def get_cust_names():
    df = pd.read_csv('customers.csv')
    return list(df['العميل'])



if file == 'False':
    st.title('قم بتسجيل الدخول من فضلك')

else:

    st.title('اضافة عميل جديد')
    st.write('')
    st.write('')
    st.write('')
    st.write('')



    add_cust = st.radio(label='هل تريد إضافة عميل',options=['إضافه','حذف'])

    st.write('')


    customers_name = st.text_input('ادخل اسم العميل' , placeholder='اسم العميل')

    if add_cust == 'إضافه':
        customers_date = st.date_input("ادخل تاريخ اضافة العميل",datetime.datetime.now())

        df = pd.read_csv('customers.csv')
        id = len(df) + 1
        money = 0

        if customers_name and customers_date:
            data = pd.DataFrame({
                'الكود':[id],
                'العميل':[customers_name],
                'رصيد مدين':[money],
                'التاريخ':[customers_date]
            })

            df = pd.concat([df , data])
            df.to_csv('customers.csv',index=False)

            df_for_indexing = pd.DataFrame(
                {
                    'رقم العمليه':[],
                    'التاريخ':[],
                    'الصنف':[],
                    'الكمية':[],
                    'السعر':[],
                    'الإجمالي':[],
                    'المدفوع':[],
                    'المتبقي':[],
                    'المتبقي الكلي':[],
                    'ملاحظه':[],
                    'الوقت':[],
                }
            )

            df_for_indexing.to_csv(f'customers/{id}.csv',index=False)


            st.success('تم إضافة العميل بنجاح')
            st.write(df)

    else:
        cust_names = get_cust_names()

        df = pd.read_csv('customers.csv')

        if customers_name:
            if customers_name in cust_names:
                df = df[df['العميل']!=customers_name]
                df.to_csv('customers.csv',index=False)
                st.success('تم حذف العميل بنجاح')
                st.write(df['العميل'])

            else:
                st.error('لا يوجد عميل بهذا الاسم')
                st.write(df['العميل'])


