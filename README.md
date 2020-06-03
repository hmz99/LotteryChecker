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
    - Updating the winning numbers in the database everytime a user visits the home page. (This can be done better with celery)
    - Rendering the index page on a GET request.
    - Rendering the results page if a user checks an individual ticket.
2) The home view is responsible for:
    - Storing and validating user tickets on a POST request
    - Analyzing the winning numbers and returning data in JSON format for graph creation.
3) The users view is responsible for:
    - Registering users to the web application
    - There is no login/logout view. The default Django views were used for this.

## Modules needed to run the application
1) asgiref==3.2.7
2) certifi==2020.4.5.1
3) chardet==3.0.4
4) Django==3.0.6
5) idna==2.9
6) pytz==2020.1
7) requests==2.23.0
8) sqlparse==0.3.1
9) urllib3==1.25.9

