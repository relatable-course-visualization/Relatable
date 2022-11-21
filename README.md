![alt text](relatable.png)

<h1> Product Description </h1>

- Relatable is an interactive course detailer for University of Saskatchewan course. A user searches for a course, and the application displays prerequisites, dependencies and other useful information for that course. Data for the courses is gotten from the usask cours
- Technology used: React.js, Node.js, Python Django, mySQL
- Method: We scrape the data from the course catalogue using a python library called beautiful soup. Then we stored the data in our mySQL database, api calls are made from the client side to the database when a user searches for a course.

<h1> Installation Steps (all done in the terminal) </h1>

Client side

- <b> NOTE: MAKE SURE TO PERFORM THIS STEPS IN THE CLIENT FOLDER </b>

- NODE.JS - Install node.js version 19.1.0 from https://nodejs.org/en/

- REACT
  - Install react using <b>npx create-react-app</b>
  - Install all the package.json dependencies using <b>npm install</b>
    - npm install @material-ui/core
    - npm install @mui/icons-material
    - npx json-server -p 3000 -w data/db.json
    - npm install axios npm install --save react-helmet
    - npm install @material-ui/core
    - npm install @mui/icons-material
    - npx json-server -p 3000 -w data/db.json
    - npm install axios
    - npm install --save react-helmet

Server Side

- <b> NOTE: MAKE SURE TO PERFORM THIS STEPS IN THE SERVER FOLDER </b>
- <h2> Django Dependencies </h2>

  - Install Django

    - <b> pip install django </b>
    - <b> pip3 install djangorestframework-jsonapi </b>

    - <b> pip install mysqlclient </b>
    - <b> pip3 install djangorestframework </b>

- <h2> Non Django(Webscraping) Dependencies </h2>
  <b> NOTE: MAKE SURE TO DO THIS IN THE DIRECTORY Relatable/server/webscraping </b>
   <p> <b> pip install bs4 </b> </p>
    <p> <b> pip install requests</b> </p>
    <p> <b> pip install regex </b> </p>
    <p> <b> pip install nltk </b> </p>

Database

- Installing MySQL

  - Install the community version from https://www.mysql.com/downloads/ (Go to Community addition at the bottom)
  - Download the “MySQL Installer for Windows”
  - Download the second one
  - In the MySQL installer
  - Select the developer version
  - Ignore the warning
  - Install everything by clicking execute
  - Click next through everything
  - Create a root password; root is the main user, and we add a password for it (keep the password, you would need it)
  - Click next through everything and execute
  - In the “Connect To Server” page, type in password
  - Install the MySQL Workbench for a GUI. You can use the terminal to interact with MySQL if sought; in this case, add MySQL to your device's PATH variable ([tutorial](https://dev.mysql.com/doc/mysql-windows-excerpt/5.7/en/mysql-installation-windows-path.html#:~:text=On%20the%20Windows%20desktop%2C%20right,System%20Variable%20dialogue%20should%20appear))

- Setting up the database

  - Create a new user
  - Create a new user for each new database
  - However, they do not have all privileges, so they need to be granted privileges (see below)
  - CREATE USER ‘username’@‘localhost’

  - Create a new database (keep track of the name) using command `CREATE DATABASE`

- Connecting django to the server
- Add database details in the corresponding server .env file

</br>
<h3> Setting up .env files </h3>
  <p> There are three .env files to populate with corresponding data </p>
 <p> - Create a <b>.env</b> file in <b>Relatable/server/webscraping</b>, set the variable <b> SERVER_URL={the url of ther server running} </b> </p>
  - Create a <b>.env</b> file in the directory <b> Relatable/server/server </b>, set the corresponding variables:
    <p> <b> SECRET_KEY={the secret key of the database} </b> </p>
    <p><b> DATABASE_NAME={the name of the database} </b> </p>
    <p> <b> DATABASE_USER={the user of the database} </b> </p>
    <p> <b> DATABASE_PASSWORD={the password of the database} </b> </p>
    <p> <b> DATABASE_HOST=localhost </b> </p>
    <p> <b> DATABASE_PORT={whatever port you choose to use} </b> </p>
<p> </p>
 <p> - Create a <b>.env</b> file in <b> Relatable/client</b>, set the variable <b> REACT_APP_SERVER_ENDPOINT={the url of ther server running, must correspond to the one used in the webscraping folder} </b> </p>
</br>

Running the server/app

- Make sure you are in the server directory, then use the command <b> python manage.py runserver </b>

- Note: The first you make changes to models.py or settings.py, you would have to do <b> python manager.py makemigrations </b> and then <b> python manage.py migrate </b>

- Scraping data and updating the database
  - Run (e.g., python path_to_file) the following files inside the webscraping directory (note, the first two files will take 10-20 minutes each as they pull 4609 courses from UofS's webpages):
    - initializeCourse.py
    - initializeDependency.py
    - initializePrerequisite.py
- run the three files using <b>python {the directory path of the file}</b>

- In the client folder use the command <b>npm start </b>
