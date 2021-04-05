# OFS Starter template.

Basic Django app starter template. 


## How to build and run OFS using docker

 1. Go to docker.com and download docker to your local machine.
 2. Open terminal and CD to your local git directory.
 3. Run 'docker-compose up' to run docker image.
 4. Open browser and go to http://localhost:80 to test.

## Notes
- We don't need to rebuild container everytime we make changes. You only need to refresh the webpage.
- Every time we make changes to database. We have to perform makemigrations and migrate for our project to work properly. Execute these 2 commands:
    docker-compose run app python manage.py makemigrations
    docker-compose run app python manage.py migrate

## Instructions
- How to create and link website to our web_app:
    1. Add your html file to web_app/templates/ 
    2. Go to web_app and open views.py. Create a function similar to index def.
    3. Go to project_setting -> open urls.py -> adding your path (can be anything you like but I suggest make it the same with your html file name). For example:
        path('YOUR HTML FILE NAME/',views.YOUR FUNCTION) <- remember to put your view function here.
    4. Done -> Go to localhost/NAME OF YOUR URL to view your html file.

- How to save data to sqlite3 database:
    1. Create your new class in models.py
    2. Import to views.py
    3. Run these two commands to stage and create your models.
    3. Create an object of created class and use object.save() to save to db.sqlite3
    4. Download sqlite browser https://sqlitebrowser.org/dl/ .Use it to open db.sqlite3 and view data.
    
## References
- https://github.com/LondonAppDeveloper/demo-django-docker-nginx-prod
- https://www.youtube.com/watch?v=nh1ynJGJuT8
