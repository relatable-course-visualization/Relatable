<h1> Product Description </h1>

Relatable is an interactive course detailer for the University of Saskatchewan. A user searches for a course, and the application displays its prerequisites, dependencies, and other useful information. Data is captured from the UofS [Course Catalogue](https://catalogue.usask.ca/).

- Technology used: Python, Django, React.js, MySQL, and HTML/CSS.
- Method: We scrape the data from the course catalogue using [beautiful soup](https://beautiful-soup-4.readthedocs.io/en/latest/). Then, we clean the data and store it in our MySQL database. Finally, users search and interact with courses on the front-end, making API calls to the server to capture relevant data from the database.


<h1> Preview </h1>

<p>
  <img 
    src="https://user-images.githubusercontent.com/90867690/204102402-fdc2975d-3120-4ddf-a9c3-e6819db16a8b.png"
    width="380px"
    alt="Relatable Example One"
  /> <img 
    src="https://user-images.githubusercontent.com/90867690/204102426-74c9e4c2-0611-4e9d-a2fb-7255ce8e5e92.png"
    width="350px"
    alt="Relatable Example Two"
  />
</p>


<h1> Installation Steps </h1>

All done in the terminal

<br>

Client

- Note: MAKE SURE TO PERFORM THIS STEPS IN THE CLIENT FOLDER 

- Node.js - Install node.js version 19.1.0 from https://nodejs.org/en/

- React.js
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

Server

- Note: MAKE SURE TO PERFORM THIS STEPS IN THE SERVER FOLDER
- Django Dependencies

  - Install Django

    - <b> pip install django </b>
    - <b> pip3 install djangorestframework-jsonapi </b>

    - <b> pip install mysqlclient </b>
    - <b> pip3 install djangorestframework </b>

- Non-Django (Webscraping) Dependencies
  - Note: MAKE SURE TO DO THIS IN THE DIRECTORY relatable/server/webscraping
  - <b> pip install bs4 </b>
  - <b> pip install requests</b>
  - <b> pip install regex </b>
  - <b> pip install nltk </b>

Database

- Installing MySQL
  - Install the community version from https://www.mysql.com/downloads/ (Go to Community addition at the bottom)
  - Download the “MySQL Installer for Windows”
    - Download the second one
  - In the MySQL installer
    - Select the developer version
    - Ignore the warnings
    - Install everything by clicking execute
    - Click next through everything
    - Create a root password; root is the main user
  - Click next through everything and execute
  - In the “Connect To Server” page, type in your password
  - Install the MySQL Workbench for a GUI. You can use the terminal to interact with MySQL if sought; in this case, add MySQL to your device's PATH variable ([tutorial](https://dev.mysql.com/doc/mysql-windows-excerpt/5.7/en/mysql-installation-windows-path.html#:~:text=On%20the%20Windows%20desktop%2C%20right,System%20Variable%20dialogue%20should%20appear))

- Setting up the database
  - Create a new user: <b> CREATE USER ‘username’@‘localhost’ </b>
  - Create a new database (keep track of the name): <b> CREATE DATABASE 'name'</b>

- Connecting django to the server
  - Add database details in the corresponding server .env file (see below)

<br>
Setting up .env files

  - There are three .env files to populate with corresponding data
    - Create a .env file in Relatable/server/webscraping directory. Set the variable <b> SERVER_URL={the url of the server running} </b>
    - Create a .env file in the directory Relatable/server/server. Set the corresponding variables:
      - <b> SECRET_KEY={the secret key of the database} </b>
      - <b> DATABASE_NAME={the name of the database} </b>
      - <b> DATABASE_USER={the user of the database} </b>
      - <b> DATABASE_PASSWORD={the password of the database} </b>
      - <b> DATABASE_HOST=localhost </b>
      - <b> DATABASE_PORT={whatever port you choose to use} </b>
  - Create a .env file in Relatable/client. Set the variable <b> REACT_APP_SERVER_ENDPOINT={the url of the server running; must coincide with the one used in the webscraping folder} </b>
 - Restart your IDE

<br>

Running the application

- Running the server
  - CD to the server directory, then use the command <b> python manage.py runserver </b>
  - Note: The first you make changes to models.py or settings.py, you would have to do <b> python manage.py makemigrations </b> and then <b> python manage.py migrate </b>
- Scraping data and updating the database
  - CD to the server directory
  - Run (i.e., python path_to_file) the following files inside the webscraping directory (note, the first two files will take 10-20 minutes each as they pull 4609 courses from UofS's webpages):
    - initializeCourse.py
    - initializeDependency.py
    - initializePrerequisite.py
- Running the client
  - CD to the client directory
  - Use the command <b>npm start</b>

<br>

RESTART YOUR IDE BEFORE RUNNING OR IF YOU'VE DONE ALL THE STEPS CURRENTLY AND IT DOESN'T STILL WORK
