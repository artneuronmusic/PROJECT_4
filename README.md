Capstone
-----

## Introduction
It is the last project of Non Degree Full Stack Program in Udacity, which include skills(implementing data, dealing with API and deploying through the thrid party) for entry level of full stack developer.
## Overview

This app requires to use PostgreSQL database, SqlAlchemy, Flask and Heroku in the project. 

* creating movie and casting databases
* Checking Endpoints
* Checking Authorization for different users and roles
* Deploying it

## Tech Stack (Dependencies)

### 1. Required Dependencies for Backend
Our tech stack will include the following:
 * **virtualenv**  isolated Python environments
 * **vagrant**  isolated Python environments
 * **SQLAlchemy ORM** ORM library 
 * **PostgreSQL** database
 * **Python3** and **Flask** server language and server framework
 * **Flask-Migrate** schema migrations

### 2. Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** use "python app.py" to run after installing dependencies
                    
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── models.py *** database
  ├── auth.py *** set up for checking authentification and token
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── test_flasks.py *** test the authorization and permission from three different roles: casting assistant, casting director, and product executive, use "python3 test_flasks.py"
  ├── manage.py *** deal with migration
  ├── movies.sql *** optional data for testing use 1. "dropdb movies" 2. "createdb movies" 3."psql movies < movie.sql"
  ├── setting.py *** assign variales to local 

  ```
### 3. **Initialize and activate a virtualenv using:**
```
brew cask install virtualbox
brew cask install vagrant
vagrant init
vagrant up
vagrant ssh
```
cd /vagrant

```
pip install virtualenv
python3 -m virtualenv env
source env/bin/activate
```

### 4. Installations before start
```
pip install SQLAlchemy
pip install postgres
pip install Flask
pip install Flask-Migrate
psql movies < movies.sql
```
```
pip install -r requirements.txt    (actually, this step can be ignored, since the attached Vagrantfile in the project has the requirements.txt which helps to install those dependencies)
```

## Development Setup
4. **Download the project starter code locally**
```
git clone https://github.com/artneuronmusic/Udacity_Capstone.git
```
5. **empty repository in Github account online. To change the remote repository path in your local repository, use the commands below:**
```
git remote -v 
git remote remove origin 
git remote add origin <https://github.com/<USERNAME>/<REPO_NAME>.git>
git branch -M main
```
Once you have finished editing your code, you can push the local repository to your Github account using the following commands.
```
git add . --all   
git commit -m "your comment"
git push -u origin main
```
## Run the server
6. **Run the development server:**
```
cd /vagrant
export FLASK_APP=app.py
export FLASK_ENV=development # enables debug mode
flask run 
or
cd /vagrant
python3 app.py
```

7. **End points and Roles(Permissions)**
Create a new Auth0 Account
Select a unique tenant domain
Create a new, single page web application
Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
Create new API permissions:
  - `get:castings`
  - `get:movies`
  - `post:casting`
  - `post:movie`
  - `patch:casting`
  - `patch:movie`
  - `delete:casting`
  - `delete:movies`

Create new roles for:
  - Casting Assistant
     - can `get:castings`
     - can `get:movies`
  - Casting Director
      - `get:castings`
      - `get:movies`
      - `post:casting`
      - `patch:casting`
      - `patch:movie`
      - `delete:casting`
  - Producer
      - `get:castings`
      - `get:movies`
      - `post:casting`
      - `post:movie`
      - `patch:casting`
      - `patch:movie`
      - `delete:casting`
      - `delete:movies`
    
Endpoints
   - GET '/movies'
   - GET '/castings'
   - POST '/movies'
   - POST '/castings'
   - PATCH '/castings/<int:casting_id>'
   - PATCH '/movies/<int:movie_id>'
   - DELETE '/castings/<int:casting_id>'
   - DELETE '/movies/<int:movie_id>'

## Testing
8. **Unittest Test:**
```
python3 test_flasks.py
```

## 
10. **PEP 8 style guide:**
```
pip install pycodestyle
pycodestyle .
pip install --upgrade autopep8
autopep8 --in-place --aggressive --aggressive <filename>

```


## Deployment
10. **Deploying through Heroku:**
```
brew tap heroku/brew && brew install heroku
heroku login  --> input your info according the requirments
pip freeze > requirements.txt
touch setup.sh   -->set up all of your environment variables here
```





