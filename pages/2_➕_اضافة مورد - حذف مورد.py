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



def get_supp_names():
    df = pd.read_csv('suppliers.csv')
    return list(df['المورد'])



if file == 'False':
    st.title('قم بتسجيل الدخول من فضلك')

else:

    st.title('اضافة مورد جديد')
    st.write('')
    st.write('')
    st.write('')
    st.write('')



    add_sup = st.radio(label='هل تريد إضافة مورد',options=['إضافه','حذف'])

    st.write('')


    suplier_name = st.text_input('ادخل اسم المورد' , placeholder='اسم المورد')

    if add_sup == 'إضافه':
        suplier_date = st.date_input("ادخل تاريخ اضافة المورد",datetime.datetime.now())

        df = pd.read_csv('suppliers.csv')
        id = len(df) + 1
        money = 0

        if suplier_name and suplier_date:
            data = pd.DataFrame({
                'الكود':[id],
                'المورد':[suplier_name],
                'رصيد دائن':[money],
                'التاريخ':[suplier_date]
            })

            df = pd.concat([df , data])
            df.to_csv('suppliers.csv',index=False)

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

            df_for_indexing.to_csv(f'suppliers/{id}.csv',index=False)


            st.success('تم إضافة المورد بنجاح')
            st.write(df)

    else:
        supp_names = get_supp_names()

        df = pd.read_csv('suppliers.csv')

        if suplier_name:
            if suplier_name in supp_names:
                df = df[df['المورد']!=suplier_name]
                df.to_csv('suppliers.csv',index=False)
                st.success('تم حذف المورد بنجاح')
                st.write(df['المورد'])

            else:
                st.error('لا يوجد مورد بهذا الاسم')
                st.write(df['المورد'])


