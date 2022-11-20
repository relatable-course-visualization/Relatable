Product Description

- Relatable is an interactive course detailer for University of Saskatchewan course. A user searches for a course, and the application displays prerequisites, dependencies and other useful information for that course. Data for the courses is gotten from the usask cours
- Technology used: React.js, Node.js, Python Django, mySQL
- Method: We scrape the data from the course catalogue using a python library called beautiful soup. Then we stored the data in our mySQL database, api calls are made from the client side to the database when a user searches for a course.

Installation Steps (all done in the terminal)

- Client Side
  -NODE.JS - Install node.js version 19.1.0 from https://nodejs.org/en/

- REACT
  - Install react using <b>npx-create-react-app</b>
  - Install all the package.json dependencies using <b>npm install</b>

Server Side

- Django Dependencies

  - Install Django

    - <b> pip install django </b>
    - <b> pip install django restframework </b>

- Non Django(Webscraping) Dependencies
  - <b> pip install bs4 </b>
  - <b> pip install requests</b>
  - <b> pip install re </b>
  - <b> pip install nltk </b>

Running the server

- In the client folder use the command <b>npm start </b>

- Make sure you are in the server directory, then use the command <b> python manage.py runserver </b>

- Note: The first you make changes to models.py or settings.py, you would have to do <b> python manager.py makemigrations </b> and then <b> python manage.py migrate </b>
