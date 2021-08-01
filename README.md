# Soymate
An open source social web app focused on allowing users to share or find new recipes!
![Home](/rme-img/Capture.JPG)  
![Profile](/rme-img/soymate-profile.JPG) 
[Heroku Deployment](https://soymate.herokuapp.com/)


## Features
`following system (like Instagram or Twitter)`
* Feature only avaliable after the user has logged in
* Users can navigate to _Find Users_ and follow other users that they might like  
* Users then can see the posts of the users that they're following on the _Feed_ page  
* Users can also unfollow if they choose so  

`User registation and login` 
* Users can register if their choosen username and email aren't taken
* Users can login after registation and begin exploring or uploading their own recipes
* Users can also change their bios, email, and profile pictures on the _Profile_ page

`Upload and edit recipes`
* Users that are logged in can add a recipe to the database
* If they click on the recipe they posted, they can edit or remove it from the database

`Search and sort other user recipes`  
* Users can sort posts by _title name_, _author name_, or _alphabetical_ using sort by
* Users can also search for a title using the search bar
s
## Tech Stack
* [Python](https://www.python.org/)  
* [Django](https://www.djangoproject.com/)  
* [PostgreSQL](https://www.postgresql.org/)  
* [Heroku](https://www.heroku.com/)
* [S3 Buckets](https://aws.amazon.com/s3/)

## Installation 
    git clone https://github.com/davidngo123/Soymate.git   
    cd Soymate     
    pip install -r requirements.txt  
    python manage.py runserver
    

    
