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
## References
- https://github.com/LondonAppDeveloper/demo-django-docker-nginx-prod
- https://www.youtube.com/watch?v=nh1ynJGJuT8
