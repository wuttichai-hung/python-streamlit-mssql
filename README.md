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
   3. pip install streamlit
2. create file main.py
3. add code to main.py
   ```python
   import streamlit as st
   st.write("Hello World!")
   ```

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
streamlit run main.py
python -m streamlit run main.py

## Third-party Modules
- [https://streamlit.io/components](https://streamlit.io/components)