# Building Interactive Web Apps with Python

![qrgit](/images/qrcode_streamlit_github.png)

## Module 1: Introduction to Streamlit

### What is Streamlit?

[Streamlit](<(https://streamlit.io/)>) is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes.

![qrgit](/images/streamlit_star.png)
ref: [https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila](https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila)

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

### Create Streamlit on Colab (Optional)

[Colab Streamlit Link](https://to.datahungry.dev/colab-streamlit)

## Module 2: Streamlit Fundamentals

- Structure of a Streamlit app
- Widgets and user input
- Displaying data
- Customization and styling

## Module 3: Data Visualization with Streamlit

## Module 4: Building Interactive Web Apps

- Web scraping: gold price
- Login with session state
- Clone ChatGPT app
- Form app

## Sqlite
- [docs](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html)
## Setup sql server using docker

[docker image](https://hub.docker.com/_/microsoft-mssql-server)

```bash
docker run --name="mssql" -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Password!" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2022-latest
```

### Environment

- ACCEPT_EULA: accept license
- MSSQL_SA_PASSWORD: password for mssql

### Connection

- Host: localhost
- Port: 1433
- Database: master
- Username: sa
- Password: Password!

# Reference

- [sqlconnection](https://docs.streamlit.io/library/api-reference/connections/st.connections.sqlconnection)
- [Theme](https://docs.streamlit.io/library/advanced-features/theming)
- [Cheatsheet](https://docs.streamlit.io/library/cheatsheet)

## Third-party Modules

- [Components](https://streamlit.io/components)
- [Pydantic](https://github.com/lukasmasuch/streamlit-pydantic)
- [Pages](https://github.com/blackary/st_pages)
