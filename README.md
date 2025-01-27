# Project001

Application scrapes data for real estates in Montenegro and Serbia, stores data in database and present analytics.

Backend workflow
![image](https://github.com/user-attachments/assets/38b584ab-7607-4ee7-84c5-9763fce52a4e)

## Set the project
You need Node.js, MySql Workbench, MySql, Pyhon


### Cloning Git project

git init   
git clone git@github.com:ognjenMagicni/Project001.git   
git pull origin main   

### Setting database

Open MySQL Workbench
Create new schema "properties"
Server -> Data Import -> Import from Disk
Set path to folder "database" inside cloned Git project
Click Start Import  

### Setting backend

For Linux:
cd backend
python3 -m venv venv_p
source venv_p/bin/activate
pip3 install -r requirements.txt  
fastapi dev main.py  

For Windows:
cd backend
python -m venv venv_p
venv_p/Scripts/activate
pip install -r requirements.txt  
fastapi dev main.py  

### Setting frontend

Open new terminal
cd frontend/stanovi/  
npm install  
npm start

### Important
You have to go to
main.py
realitica.py
fourZid.py
process.py
And manually change user and password for your MySQL.
In next patch I will add environment variables

For Windows users you have to go in requirements.txt and delete uvloop, since it is not support for Windows

### You can start application on localhost:3000/menu in browser
