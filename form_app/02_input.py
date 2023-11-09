import streamlit as st
import pandas as pd
# text_input
# button
# checkbox
# toggle
username = st.text_input("Username")
password = st.text_input("Password", type="password")

st.write(username)
st.write(password)

click_login = st.button("Login")
if click_login:
    st.write(click_login)

col1, col2 = st.columns(2)
with col1:
    agree1 = st.checkbox("I Agree1")
with col2:
    agree2 = st.checkbox("I Agree2")
if agree1:
    st.write(agree1)

toggle_on = st.toggle("Toggle")
if toggle_on:
    st.write(toggle_on)


select_radio = st.radio("Genre", ["Comedy", "Drama", "ETC"])
if select_radio == "ETC":
    detail = st.text_input("Detail")
    st.write(detail)

select_selectbox = st.selectbox("Genre", ["Comedy", "Drama", "ETC"])
# if select_selectbox == "ETC":
#     detail = st.text_input("Detail")
# st.write(detail)
st.write(select_selectbox)

select_multiselect = st.multiselect("Genre", ["Comedy", "Drama", "ETC"], default=["Comedy", "Drama"])
# print(select_multiselect)
if "ETC" in select_multiselect:
    detail = st.text_input("Detail")

st.write(select_multiselect)

uploaded = st.file_uploader("Upload", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    var_unique = df['variety'].unique()
    # st.write(var_unique)
    
    select_multiselect = st.multiselect("Variety", list(var_unique), default=list(var_unique))
    selected_df = df[df['variety'].isin(select_multiselect)]
    st.dataframe(selected_df)
    ##
    if "ETC" in select_multiselect:
        detail = st.text_input("Detail")
    # selected_df.head(22)
    st.write("uploaded")
    df.to_csv("./data/myfile.csv", index=False)
    with open("./data/myfile.csv") as f:
        st.download_button('Download CSV', file_name="filtered_data.csv", 
                           data=f, mime='text/csv')
    # df.to_csv("./myfile.csv", index=False)
    st.divider()
    select_cols = st.multiselect("Columns", list(df.columns), default=list(df.columns))
    selected_col_df = df[select_cols]
    st.dataframe(selected_col_df)
    st.write(select_cols)
    st.divider()


age = st.slider('How old are you?', max_value=0, min_value=130, value=25)
st.write("I'm ", age, 'years old')

date_input = st.date_input("Select Date")
st.write(date_input.replace(day=1))
# yyyy-mm-dd
# google >> github iris dataset >> iris.csv >> Raw >> right click + save as


phone = st.text_input("Phone number", placeholder="081-234-5678", max_chars=12)
if phone:
    if phone[3] == '-' and phone[7] == '-':
        st.success("Done")
    else:
        st.error("please input follow this template 081-234-5678")


# regex
# pydantic validator