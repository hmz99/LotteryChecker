# LotteryChecker
A web application to check if you have won the Megamillions.

## Steps to run application
1) Download the project folder.
2) Run "python manage.py runserver"

## Models in the application
1) Django default User model is used for user creation.
2) WinningNumbers model is used to store winning tickets.
3) Ticket model is used to store a user's tickets

## Views in the application 
1) The base view is responsible for:
    a) Updating the winning numbers in the database everytime a user visits the home page. (This can be done better with celery)
    b) Rendering the index page on a GET request.
    c) Rendering the results page if a user checks an individual ticket.
2) The home view is responsible for:
    a) Storing and validating user tickets on a POST request
    b) Analyzing the winning numbers and returning data in JSON format for graph creation.
3) The users view is responsible for:
    a) Registering users to the web application
    b) There is no login/logout view. The default Django views were used for this.

## Technologies on which the application was built on
1) Python 3.8.0
2) Django 2.2.6

