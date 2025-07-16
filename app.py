import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Langchain: Chat with SQL Database")
st.title("Langchain: Chat with SQL Database")

MYSQL = "USE_MYSQL"
LOCALDB = "USE_LOCALDB"

radio_opt = ["Chat with SQLite3 Database - Student.db", "Chat with SQL Database"]

chosen_opt = st.sidebar.radio(label="Choose which database you want to chat with:", options=radio_opt)

if radio_opt.index(chosen_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Enter MySQL Host")
    mysql_username = st.sidebar.text_input("Enter MySQL Username")
    mysql_password = st.sidebar.text_input("Enter MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("Enter MySQL Database")
    
else:
    db_uri = LOCALDB
    
    
api_key = st.sidebar.text_input("Enter Groq API Key")
    
    
if not db_uri:
    st.info("Please enter the Database Information")
    
if not api_key:
    st.error("Please enter the Groq API Key to continue");
    st.stop()


llm_model = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)


@st.cache_resource(ttl="2h")
def configure_db(db_uri, mysql_host = None, mysql_username=None, mysql_password = None, mysql_db = None):
    if db_uri == LOCALDB:
        db_file_path = (Path(__file__).parent/"student.db").absolute()
        print(db_file_path)
        creator = lambda: sqlite3.connect(f"file:{db_file_path}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        if not(mysql_username and mysql_password and mysql_host and mysql_db):
            st.error("Please provide all the MySQL Details")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_db}"))
    
    
if db_uri == MYSQL:
    db = configure_db(db_uri, mysql_host=mysql_host, mysql_username=mysql_username, mysql_password=mysql_password, mysql_db=mysql_db)
else:
    db = configure_db(db_uri)
    
  
toolkit = SQLDatabaseToolkit(db=db, llm=llm_model)

agent = create_sql_agent(llm=llm_model, toolkit=toolkit, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors = True)

if "messages" not in st.session_state or st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    
user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
        

    

    
