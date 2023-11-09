import streamlit as st
import pandas as pd

uploaded = st.file_uploader("Upload", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    
    # filter rows
    var_unique = df['variety'].unique()
    select_row = st.multiselect("Variety", list(var_unique), 
                                default=list(var_unique))
    selected_row_df = df[df['variety'].isin(select_row)]
    st.dataframe(selected_row_df)

    # filter cols
    select_cols = st.multiselect("Columns", list(selected_row_df.columns), 
                                 default=list(selected_row_df.columns))
    selected_row_col_df = selected_row_df[select_cols]
    st.dataframe(selected_row_col_df)

    # Save csv
    selected_row_col_df.to_csv("./data/myfile.csv", index=False)
    with open("./data/myfile.csv") as f:
        st.download_button('Download CSV', file_name="filtered_data.csv", 
                           data=f, mime='text/csv')