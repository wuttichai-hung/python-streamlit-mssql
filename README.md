# Building Interactive Web Apps with Python
## Module 1: Introduction to Streamlit
### What is Streamlit?
Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes.
### Installation and setup
- Python 3.8-3.11 [Install link](https://docs.anaconda.com/free/anaconda/install/windows/)
- IDE vscode [install link](https://code.visualstudio.com/)
### Your first Streamlit app
1. Create conda environment
   1. conda create <env_name>
   2. conda activate <env_name>
   3. create requirements.txt
      ```requirements.txt
      streamlit
      pandas
      sqlalchemy
      pymssql
      ```
   4. pip install -r requirements.txt
2. create file main.py and add code below
   ```python
   import streamlit as st
   st.write("Hello World!")
   ```
3. streamlit run main.py




# Setup sql server using docker
[docker image](https://hub.docker.com/_/microsoft-mssql-server)
```bash
docker run --name="mssql" -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Password!" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest
```
## Environment
- ACCEPT_EULA: accept license
- MSSQL_SA_PASSWORD: password for mssql

# Connection
- Host: localhost
- Port: 1433
- Database: master
- Username: sa
- Password: Password!

# Streamlit
- [sqlconnection](https://docs.streamlit.io/library/api-reference/connections/st.connections.sqlconnection)



conda activate <env_name>
streamlit run streamlit_app/main.py
python -m streamlit run streamlit_app/main.py

## Third-party Modules
- [https://streamlit.io/components](https://streamlit.io/components)
- [Pydantic](https://github.com/lukasmasuch/streamlit-pydantic)
- [Page](https://github.com/blackary/st_pages)


## Configuration
- [Theme](https://docs.streamlit.io/library/advanced-features/theming)

# Cheat sheet
- [https://docs.streamlit.io/library/cheatsheet](https://docs.streamlit.io/library/cheatsheet)
