# Project001

Application scrapes data for real estates in Montenegro and Serbia, stores data in database and present analytics.

Backend workflow
![image](https://github.com/user-attachments/assets/38b584ab-7607-4ee7-84c5-9763fce52a4e)

##Set the project
You need Node.js, MySql Workbench, MySql
git init
git clone git@github.com:ognjenMagicni/Project001.git
git pull origin main
cd backend
pip3 install -r requirements.txt
cd ..
cd frontend/stanovi/
npm config set legacy-peer-deps true
npm install

Download database backup
Create new schema "properties"
Import backups in "properties"

npm start
cd ..
fastapi dev main.py
