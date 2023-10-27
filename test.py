import streamlit as st
import pandas as pd



df = pd.read_csv('suppliers.csv')

st.title("قائمة الموردين")

# Create a list of supplier names
supplier_names = df["المورد"].tolist()
supplier_codes = df["الكود"].tolist()


# Create a list to track which suppliers are expanded
expanded_suppliers = [False] * len(supplier_names)

# Iterate through the supplier names and display them
for i, supplier in enumerate(supplier_names):
    # Create a button with the supplier name
    if st.button(supplier):
        # When the button is clicked, toggle the expanded state
        expanded_suppliers[i] = not expanded_suppliers[i]

    # Display additional content when expanded
    if expanded_suppliers[i]:
        
        # You can customize the content here
        st.write(pd.read_csv(f'suppliers/{supplier_codes[i]}.csv'))
        

