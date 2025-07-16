# 💬 LangChain: Chat with SQL Database

This project allows users to interact with a SQL database using natural language. Built using **Streamlit**, **LangChain**, and **Groq LLM (LLaMA3)**, it supports both **SQLite3** and **MySQL** databases.

---

## 🚀 Features

- 🔌 Connect to a local SQLite3 database (`student.db`) or your own MySQL database
- 🧠 Chat with your database using LLaMA3 via the **Groq API**
- 🗃️ Retrieve, filter, or analyze data using natural language queries
- 🔒 Supports secure credential input (host, username, password)
- 🧰 Powered by LangChain's `SQLDatabaseToolkit` and `ChatGroq` LLM wrapper

---

## 🖥️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq API](https://console.groq.com/)
- [SQLite3](https://www.sqlite.org/index.html)
- [MySQL](https://www.mysql.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

---

## 📦 Installation

### 1. Clone the repository
git clone https://github.com/your-username/chat-with-sql-db.git
cd chat-with-sql-db

### 2. Create a Virtual Environment
conda create -p venv python==3.12 (or whatever python version you want to use)
conda activate venv/

### 3. Install Dependencies
pip install -r requirements.txt

## 🔑 Requirements
### 🔹 Groq API Key
Sign up at Groq Console

Generate an API Key

Paste it in the sidebar input of the app

### 🔹 MySQL Database (Optional)
If you want to connect to a MySQL database:

Ensure MySQL Server is installed and running

Create a database and table using MySQL Workbench or CLI

Example:

sql
Copy
Edit
CREATE DATABASE testdb;
USE testdb;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    marks INT
);

INSERT INTO students (name, marks) VALUES 
('Alice', 85),
('Bob', 92),
('Charlie', 78);

## 🧪 Running the App
bash
Copy
Edit
streamlit run app.py
Then open in your browser: http://localhost:8501

## 🕹️ How to Use
Select a database from the sidebar:

Chat with SQLite3 Database - Student.db

Chat with SQL Database (MySQL)

Enter the required connection info

Enter your Groq API Key

Ask questions like:

"Show all students"

"Who scored the highest marks?"

"What's the average score?"

## 🧠 Project Structure
csharp
Copy
Edit
📁 chat-with-sql-db/
├── app.py                # Main Streamlit app
├── student.db            # Sample SQLite3 database
├── requirements.txt      # Python dependencies
└── README.md             # This file

## 🔒 Security Note
Your database credentials and API key are handled securely using Streamlit's sidebar inputs.

Avoid hardcoding sensitive information in the source code.

## 🤝 Acknowledgements
LangChain Documentation

Groq API

Streamlit

## 📃 License
This project is open-source and available under the MIT License.
