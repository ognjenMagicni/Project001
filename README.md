# Project001

Application scrapes data for real estates in Montenegro and Serbia, stores data in database and present analytics.

Backend workflow
![image](https://github.com/user-attachments/assets/38b584ab-7607-4ee7-84c5-9763fce52a4e)

## Project Setup Guide  

This guide will help you set up the project locally on your machine. Follow the steps carefully to get everything running.

---

### **🛠️ Prerequisites**  
Before you begin, make sure you have the following installed:  
- [Node.js](https://nodejs.org/) (for frontend)  
- [MySQL](https://dev.mysql.com/downloads/mysql/) (database)  
- [MySQL Workbench](https://www.mysql.com/products/workbench/) (optional, for managing the database)  
- [Python](https://www.python.org/) (for backend)  

---

### **1. Cloning the Repository**  
To clone the project from GitHub, open a terminal and run:  

```sh
git init  
git clone git@github.com:ognjenMagicni/Project001.git  
cd Project001  
git pull origin main
```

### **2. Setting database**

1. Open MySQL Workbench.
2. Create a new schema named properties.
3. Navigate to Server → Data Import → Import from Disk.
4. Set the import path to the database folder inside the cloned Git project.
5. Click Start Import and wait for the process to complete.

### 3. Setting Up the Backend

For Linux:
```sh
cd backend
python3 -m venv venv_p
source venv_p/bin/activate
pip3 install -r requirements.txt  
fastapi dev main.py
```

For Windows:
```sh
cd backend
python -m venv venv_p
venv_p/Scripts/activate
pip install -r requirements.txt  
fastapi dev main.py
```
For Windows users you have to go in requirements.txt and delete uvloop, since it is not support for Windows

### 4. Setting Up the Frontend

1. Open new terminal
2. Navigate to the frontend directory
```sh
cd frontend/stanovi/  
npm install  
npm start
```

### 5. Configuration: MySQL Credentials
You need to manually update your MySQL username and password in the following files:
backend/main.py
backend/realitica.py
backend/fourZid.py
backend/process.py
Note: In the next patch, environment variables will be used for credentials.


### 6. Running the Application
Once both backend and frontend are running, open your browser and go to:
🔗 http://localhost:3000/menu
