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


#### 04.1 Understanding significance of project files

        Activities:

        1. Create these files
        .gitignore
        README.md

        2. Create django project
        
        > (venv3932) λ django-admin startproject mysite .

        mysite/
        manage.py


#### 04.2 Running Project On Local Server

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


#### 04.3 Creating A Django App

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


#### 04.4 Creating Our First View

        Activities:

        1. Modified readme file
        README.md

        2. Creating Our First View 
        modified:   myapp/views.py

        3. Add home path
        modified:   mysite/urls.py

        DONE: )

        NEXT: #### 05. Adding URL Patterns To App


#### 04.5 Adding URL Patterns To App

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


#### 04.6 Creating Another View

        Activities:

        1. Modified readme file
        README.md
        
        2. Modified ruls
        modified:   mysite/urls.py        

        3. Create a new url
        modified:   myapp/urls.py

        3. Create Products view
        modified:   myapp/views.py

        DONE :)

        NEXT: #### 07. Section Notes- Creating A Django Project, Views & URL Patterns.


#### 04.7 Section Notes- Creating A Django Project, Views & URL Patterns.

        Activities:

        1. Modified readme file
        README.md

        Creating A Django Project, Views & URL Patterns.


        What is a Django project ?
        It is a container that hold all the files together.

        It is a container to hold all our Django apps.


        What is a Django app ?
        An app is a part of a Django project.

        There could be multiple apps in a single Django project.

        A big Django project could be split into multiple small apps.

        Example: An e-commerce website could be split into smaller apps like store, blog, forum etc.


        Significance of project files.
        manage.py : Allows you to manage or interact with your Django project.

        For example, we will be using this file to run our Django project on local server.

        init.py : It is an empty file and it tells Python that the current directory which the file is in is a Python package and not just a regular directory.

        urls.py : It contains URL patterns which are to be matched with the incoming URL requests.


        Running the local server
        To run the app on local server we make use of a special command called runserver.

        Here is how:

        On windows

        python manage.py runserver
        On Mac

        python3 manage.py runserver


        We need to ensure that server is running to test our web application.

        The above command starts a localhost server and to stop the server we need to press ctrl+c


        Creating a Django app.
        Once a project is created we need to create an app inside of it.

        Always ensure that you navigate inside the project directory before creating an app.


        cd mysite
        There are two ways of creating an app.

        One is via mange and other is via django-admin

        Via manage py file:


        python manage.py startapp myapp
        Via django-admin


        django-admin startapp myapp
        Once an app is created, we need to add the app name to the INSTALLED_APPS inside settings.py file.


        Views in Django
        Views in Django are created in views.py file which is present in the app directory.

        This file contains all the views associated with our app.

        A view is nothing but a Python function which accepts the incoming request and returns some response.

        This view should typically return an HTTP response as here we are referring to the client-server architecture which uses the HTTP protocol for communication.

        In a view, you could return a simple string or return some HTML content as well.

        This returned data could then be displayed on the webpage.


        URL patterns
        Once a view is created, it needs to be displayed on a webpage.

        But a webpage must be associated with a web address and this is what exactly the URL patterns do.

        The help us attach a view with a URL pattern, such that when we visit a URL which matches with the said pattern, the concerned view is rendered.

        You can either directly attach the view from your app to URL patterns file of your project.

        Or you can create a separate URLs.py file in your app, connect it to the URLs.py file of your main Project and then make use of the app’s URLs file to create a URL pattern and then attach it to the view.


        To download this note in PDF format, please check the file attached to this lecture.

        NEXT: #### 05.1 Introduction To Database & Models


## 05. Database & Models in Django


#### 05.1 Introduction To Database & Models (PASSED)


        Activities:

        1. Modified readme file
        README.md

        PASS

        NEXT: #### 05.2 How Data Is Stored In Django


#### 05.2 How Data Is Stored In Django (PASSED)


        Activities:

        1. Modified readme file
        README.md

        PASS

        NEXT: #### 05.3 Creating A Database Table