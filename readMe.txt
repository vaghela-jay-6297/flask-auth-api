The Task is:
Create a three tables(User)

User Table:
***********
id (pk)
name
email
gender
phone number
password
created_on (datetime autofield)
updated_on (datetime autofield)
is_delete
is_active

Tasks:
Create a flask web application.
Make registration & login API.

Project Structure:
------------------
/project
    /migrations
    /auth_app
        /__init__.py
        /models.py
        /schemas.py
        /views.py
    app.py
    requirements.txt
    


Run the Migrations:
-------------------
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
flask run       =====> app run 
flask --app app --debug run     =====> run app in debug mode

Note: postmen collection added for your reference.