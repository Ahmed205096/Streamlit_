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

    df = pd.read_csv('customers.csv')

    st.title("قائمة العملاء")

    st.divider()
    st.write('')
    st.write('')


    # Create a list of supplier names
    supplier_names = df["العميل"].tolist()
    supplier_codes = df["الكود"].tolist()


    # Create a list to track which suppliers are expanded
    expanded_suppliers = [False] * len(supplier_names)

    # Iterate through the supplier names and display them
    for i, supplier in enumerate(supplier_names):
        # Use st.expander to create an expandable section
        with st.expander(supplier):
            # Customize the content here
            supplier_data = pd.read_csv(f'customers/{supplier_codes[i]}.csv')
            st.dataframe(supplier_data)  # Display the supplier's data
                
                    
            

        # Display additional content when expanded
        if expanded_suppliers[i]:
            
            # You can customize the content here
            st.write(pd.read_csv(f'customers/{supplier_codes[i]}.csv'))
            


    










