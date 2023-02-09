## BUILDING MULTIVENDOR ECOMMERCE USING DJANGO


## 01. Introduction

	1. Intoduction
	2. Introduction to Django
	3. Section Notes- Introduction To Django


## 02. Installing Django on Windows

	1. Installing Python On Windows
	2. Installing Virtualenv on Windows
	3. Creating Virtualenv On Windows
	4. Installing Django On Windows
	5. Creating A Django Project


## 03. Installing Django on Mac

	1. Installing Python On Mac
	2. Preview
	3. Creating Virtualenv On Mac
	4. Installing Django On Mac


## 04. Creating a Django Project, Views & URL Patterns


#### 04.1. Understanding significance of project files

        Activities:

        1. Create these files
        .gitignore
        README.md

        2. Create django project
        
        > (venv3932) λ django-admin startproject mysite .

        mysite/
        manage.py


#### 02. Running Project On Local Server

        Activities:

        1. Modified readme file
        README.md

        2. Running Project On Local Server
        > (venv3932) λ python manage.py runserver
        new file:   db.sqlite3
        new file:   mysite/__pycache__/__init__.cpython-39.pyc
        new file:   mysite/__pycache__/settings.cpython-39.pyc
        new file:   mysite/__pycache__/urls.cpython-39.pyc
        new file:   mysite/__pycache__/wsgi.cpython-39.pyc


#### 03. Creating A Django App

        Activities:

        1. Modified readme file
        README.md

        2. Creating A Django App
        > (venv3932) λ python manage.py startapp myapp

        new file:   myapp/__init__.py
        new file:   myapp/admin.py
        new file:   myapp/apps.py
        new file:   myapp/migrations/__init__.py
        new file:   myapp/models.py
        new file:   myapp/tests.py
        new file:   myapp/views.py

        3. Modified
        modified:   .gitignore

        NEXT: #### 04. Creating Our First View


#### 04. Creating Our First View

        Activities:

        1. Modified readme file
        README.md

        2. Creating Our First View 
        modified:   myapp/views.py

        3. Add home path
        modified:   mysite/urls.py

        DONE: )

        NEXT: #### 05. Adding URL Patterns To App


#### 05. Adding URL Patterns To App

        Activities:

        1. Modified readme file
        README.md

        2. Adding URL Patterns To App
        new file:   myapp/urls.py

        3. Modified index view
        modified:   myapp/views.py

        4. Include the urls
        modified:   mysite/urls.py

        DONE :)

        NEXT: #### 06. Creating Another View