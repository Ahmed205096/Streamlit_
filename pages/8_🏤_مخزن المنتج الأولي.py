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


def filter_to_the_inv():
    df = pd.read_csv('suppliers/suppliers_history.csv')

    keywords = ['كرتون', 'زجاج', 'استيكر']

    # Create a filter that checks if any keyword is present in the 'description' column
    keyword_filter = df['الصنف'].str.contains('|'.join(keywords), case=False, regex=True)

    # Apply the filter to get the matching rows
    filtered_df = df[keyword_filter]



    
    # Group the DataFrame by 'name' and calculate the sum of 'quantity' and average 'price'
    result_df = filtered_df.groupby('الصنف').agg({'الكمية': 'sum', 'الإجمالي': 'sum'}).reset_index()



    
    # Define the regular expression pattern to match "sticker," "glass," or "cardboard"
    pattern = r'(استيكر|زجاج|كرتون)'

    # Use str.extract to create a new column with the extracted words
    result_df['النوع'] = result_df['الصنف'].str.extract(pattern, expand=False)

    # Fill missing values with an appropriate placeholder (e.g., "No match" for no match)
    result_df['النوع'].fillna("No match", inplace=True)


    import re
    # Define the words to remove
    words_to_remove = ['استيكر', 'كرتون', 'زجاج']

    # Create a regular expression pattern to match any of the words
    pattern = r'\b(?:' + '|'.join(map(re.escape, words_to_remove)) + r')\b'

    # Use str.replace to remove the matched words
    result_df['الصنف'] = result_df['الصنف'].str.replace(pattern, '', regex=True)
    result_df.rename(columns={'الإجمالي':'القيمه'},inplace=True)


 

    

    # Sort the DataFrame by 'Element' column to group by the same name
    df = result_df.sort_values(by=['الصنف'])

    # Display the sorted DataFrame
    return df.T


def extract_products(name = 'زيت سائب' , count = False , is_list = False):
    df = pd.read_csv('suppliers/suppliers_history.csv')
    if not is_list:
        keywords = [name]
    else:
        keywords = name

    # Create a filter that checks if any keyword is present in the 'description' column
    keyword_filter = df['الصنف'].str.contains('|'.join(keywords), case=False, regex=True)

    # Apply the filter to get the matching rows
    filtered_df = df[keyword_filter]

    # Group the DataFrame by 'name' and calculate the sum of 'quantity' and average 'price'
    result_df = filtered_df.groupby('الصنف').agg({'الكمية': 'sum', 'الإجمالي': 'sum'}).reset_index()

    if count: 
        try:
            # Display the filtered DataFrame
            quan = list(filtered_df['الكمية'])[0]
            price = list(filtered_df['الإجمالي'])[0]
        except Exception as e:
            quan,price =0,0
        

        return [quan , price]
    else:
        return result_df



if file == 'False':
    st.title('قم بتسجيل الدخول من فضلك')


else:
    st.divider()
    st.write('# قسم الزيت')
    st.divider()
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.write(filter_to_the_inv())



    st.write(f'## زيت سائب')

    st.write(f"#### الكميه = ",extract_products('زيت سائب',True)[0])

    st.write(f'#### القيمه = ',extract_products("زيت سائب",True)[1])



    st.write(f'##  فارغ جراكن زيت')


    st.write(f"#### الكميه = ",extract_products(name ='فارغ جراكن زيت',count = True)[0])

    st.write(f"#### القيمه = ",extract_products(name ='فارغ جراكن زيت',count = True)[1])
    
    st.write('')
    st.write('')
    st.divider()

    st.write('# قسم الشكائر')

    st.divider()
    st.write('')
    st.write('')

    st.table(extract_products('شكائر'))

    st.write('')
    st.write('')
    st.divider()

    st.write('# قسم الأكياس')

    st.divider()
    st.write('')
    st.write('')
    st.table(extract_products(['اكياس','بكتات'],is_list=True))

    st.write('')
    st.write('')
    st.divider()

    st.write('# قسم اللاصق')

    st.divider()
    st.write('')
    st.write('')
    st.write('#### الكميه = ',extract_products('لاصق',count=True)[0])
    st.write('#### القيمه = ',extract_products('لاصق',count=True)[1])











