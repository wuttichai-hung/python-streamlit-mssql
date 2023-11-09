import streamlit as st
from sqlalchemy.sql import text
# pip install sqlalchemy
conn = st.connection("sqlite", type="sql")

# Create
click_create = st.button("Create table")
if click_create:
    with conn.session as s:
        sql = """CREATE TABLE IF NOT EXISTS mytable(
        uid int,
        first_name text
        )
        """
        s.execute(text(sql))
    st.success("Create table successfully!")

# Insert
uid = st.number_input("UID", min_value=0, max_value=100, 
                      value=30, step=1)
first_name = st.text_input("First Name")

click_insert = st.button("Insert")
if click_insert:
    with conn.session as s:
        sql = f"""INSERT INTO mytable (uid, first_name)
        VALUES ({uid}, '{first_name}')
        """
        s.execute(text(sql))
        s.commit()
    st.success("Insert successfully!")

# Select
click_select = st.button("Select")
if click_select:
    st.cache_data.clear()
    df = conn.query("SELECT * FROM mytable")
    st.dataframe(df)

# Update
st.cache_data.clear()
unique_uid = conn.query("SELECT distinct uid FROM mytable")['uid']
# st.write(list(unique_uid))
select_uid = st.selectbox(
   "Update UID?",
   list(unique_uid),
   index=None,
   placeholder="Select contact method...",
)
if select_uid:
    update_name = st.text_input("New First Name")
click_update = st.button("Update")
if click_update:
    with conn.session as s:
        sql = f"""UPDATE mytable
        SET first_name = '{update_name}'
        WHERE uid = {select_uid}
        """
        s.execute(text(sql))
        s.commit()
    st.success("Update successfully!")

# Delete
click_delete = st.button("Delete")
if click_delete:
    with conn.session as s:
        sql = """DELETE FROM mytable
        WHERE uid = 2
        """
        s.execute(text(sql))
        s.commit()
    st.success("Delete successfully!")

    # upsert = insert + update

with open("./scripts/select.sql") as f:
    script = f.read()
st.write(script)

uploaded = st.file_uploader("Upload", type=["jpg", 'png'])


# emp_id
# first_name
# last_name
# address
# male / female
# age