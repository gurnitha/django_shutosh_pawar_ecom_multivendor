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


#### 05.3 Creating Database and A Database Table

        Activities:

        1. Modified readme file
        README.md

        2. Create db
        mysql> CREATE DATABASE django_shutosh_pawar_ecom_multivendor;

        3. Register the myapp and setup db connection
        modified:   mysite/settings.py

        4. Create Produc model and run migraions
        modified:   myapp/models.py
        new file:   myapp/migrations/0001_initial.py

        DONE :)

        NEXT: #### 05.4 How Tables Are Created In Backend


#### 05.4 How Tables Are Created In Backend (PASSED)

        Activities:

        1. Modified readme file
        README.md

        PASS

        NEXT: #### 05.5 Section Notes- Database & Models In Django


#### 05.5 Section Notes- Database & Models In Django

        Activities:

        1. Modified readme file
        README.md

        How are databases and database tables created in Django ?
        In a regular web app, you would have to create a SQL database by writing SQL queries.

        Or you would have to use a NOSQL solution like firebase to store your data.

        But NOSQL solutions aren’t as powerful as SQL once.

        But with Django, you get the advantage of using a SQL database without having to write a single line of SQL queries.

        This is possible because Django has something called models.

        What are models and how they work ?
        Let’s suppose you need to save student’s data in your web application.

        For storing such data, in a regular app you would have to create a database, then a database table named student by writing SQL queries.

        But in case of Django, we could directly define the student database table structure in form of a model.

        In Django, models are a blueprint to create database table.

        You simply define the database table structure in terms of Django model and Django will automatically execute the SQL queries in the backend to create those tables.

        Where and how to define these models ?
        Models could be defined in the models.py file which is already created when you create a Django app.

        A model has to be defined in terms of a Python class.

        Once a model has been created, to create a database table out of it we have to use a migrate command.

        This command will map every database table in your models.py file to an actual database table in the backend.

        But where is this database actually created? We have not configured any!
        By default when we create a Django project, a sqlite database is already created.

        sqlite is a file based databased and should only used for learning and testing purposes on our local machine.

        This database stores data in a simple file format inside your Django project itself.

        To download this note in PDF format, please check the file attached to this lecture.


## 06. Django ORM


#### 06.1 Introduction to Django ORM

        Activities:

        1. Modified readme file
        README.md

        Welcome to this new section on Shango Ora.

        Just as you don't have to write sequel queries to create a model, you don't have to write any queries
        for querying data from the database either.

        Django comes with a built in ORM, which stands for Object Relational Mapper, which allows you to
        create database stable entries as individual objects.

        In this section, we will learn how to add data to the database using the order and also learn how to
        retrieve that data as well from the database using the autumn itself.

        We will also learn how to access the Django Admin panel by creating a super user from where data could
        be added by the site administrator.

        So let's go ahead and let's get started with this section.

        NEXT: #### 06.2 Saving Products Using Django ORM


#### 06.2 Saving Products Using Django ORM

        Activities:

        1. Modified readme file
        README.md

        2. Activate python shell
        (venv3932) λ ls
        README.md  _docs  db.sqlite3  manage.py  myapp  mysite  venv3932

        F:\_workspace2023\ecom\shutosh_pawar_ecom_multivendor (master)
        (venv3932) λ python manage.py shell
        ...
       
        In [1]: from myapp.models import Product

        In [2]: # Retrieve all the Product objects

        In [3]: Product.objects.all()
        Out[3]: <QuerySet []>

        In [4]: # QuerySet is empty: it meads there is no objects in the Product table

        In [5]: # Insert data to Product table

        In [6]: product = Product(name="iPhone", price=900, desc="This is an iPhone")

        In [7]: product.save()

        In [8]: product2 = Product(name="iPad", price=1200, desc="This is an iPad")

        In [9]: product2.save()

        mysql> desc myapp_product;
        +-------+--------------+------+-----+---------+----------------+
        | Field | Type         | Null | Key | Default | Extra          |
        +-------+--------------+------+-----+---------+----------------+
        | id    | bigint(20)   | NO   | PRI | NULL    | auto_increment |
        | name  | varchar(100) | NO   |     | NULL    |                |
        | price | int(11)      | NO   |     | NULL    |                |
        | desc  | varchar(200) | NO   |     | NULL    |                |
        +-------+--------------+------+-----+---------+----------------+
        4 rows in set (0.00 sec)

        mysql> SELECT * FROM myapp_product;
        +----+--------+-------+-------------------+
        | id | name   | price | desc              |
        +----+--------+-------+-------------------+
        |  1 | iPhone |   900 | This is an iPhone |
        +----+--------+-------+-------------------+
        1 row in set (0.00 sec)

        mysql> SELECT * FROM myapp_product;
        +----+--------+-------+-------------------+
        | id | name   | price | desc              |
        +----+--------+-------+-------------------+
        |  1 | iPhone |   900 | This is an iPhone |
        |  2 | iPad   |  1200 | This is an iPad   |
        +----+--------+-------+-------------------+
        2 rows in set (0.00 sec)

        NEXT: #### 06.3 Retrieving Products Using ORM


#### 06.3 Retrieving Products Using ORM

        Activities:

        1. Modified readme file
        README.md

        F:\_workspace2023\ecom\shutosh_pawar_ecom_multivendor (master)
        (venv3932) λ python manage.py shell
        ...

        In [1]:

        In [1]: # Retrieving Product objects

        In [2]: from myapp.models import Product

        In [3]: Product.objects.all()
        Out[3]: <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>

        In [4]: # Note: It displays  Product object (1) and  Product object (2)

        In [5]: # Lets display name of each the objects

        In [6]: # Modify the Product model and add __str__ method and return Product name

        In [7]: Product.objects.all()
        Out[7]: <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>

        In [8]: # __str__ method added, but it still return the same.

        In [9]: # To solve this issue, re-start the shell

        In [10]:


        # Retrieving Product objects

        To solve the above issue, re-start the python shell

        F:\_workspace2023\ecom\shutosh_pawar_ecom_multivendor (master)
        (venv3932) λ python manage.py shell
        ...

        In [1]: from myapp.models import Product

        In [2]: # Retrieve Product objects

        In [3]: Product.objects.all()
        Out[3]: <QuerySet [<Product: iPhone>, <Product: iPad>]>

        In [4]: # Get a single product (iPhone)

        In [5]: Product.objects.get(id=1)
        Out[5]: <Product: iPhone>

        In [6]: # Get a single product (iPad)

        In [7]: Product.objects.get(id=2)
        Out[7]: <Product: iPad>

        In [8]: # Create a variable for product object 1

        In [9]: product 1 = Product.objects.get(id=1)
          File "<ipython-input-9-ebce15319471>", line 1
            product 1 = Product.objects.get(id=1)
                    ^
        SyntaxError: invalid syntax


        In [10]: product_1 = Product.objects.get(id=1)

        In [11]: product_1.name
        Out[11]: 'iPhone'

        In [12]: product_1.price
        Out[12]: 900

        In [13]: product_1.desc
        Out[13]: 'This is an iPhone'

        In [14]:

        NEXT: #### 06.4 Accessing Django Admin Panel


#### 06.4 Accessing Django Admin Panel

        Activities:

        1. Modified readme file
        README.md

        2. Create superuser
        (venv3932) λ python manage.py createsuperuser
        Username (leave blank to use 'hp'): admin
        Email address: admin@admin.com
        Password:
        Password (again):

        3. Register Product model to admin.py
        modified:   myapp/admin.py

        NEXT: #### 06.5 Section Notes- Django ORM


#### 06.5 Section Notes- Django ORM

        Activities:

        1. Modified readme file
        README.md

        Django ORM

        What is an ORM ?
        With Django we don’t need SQL queries to create database tables.

        But what about reading and writing data to the database ?

        Usually we would have to write SQL queries to do so.

        But Django provides an Object Relational Mapper which considers every database table entry as an individual object.

        Using which we can access data inside of any database table which we want.

        We could also perform other operations like reading, updating and deleting that data as well.

        To get access to any database data, we first access the objects of that table’s model.

        We then treat the table’s model name as class and access the objects out of it.

        Example, if we have a model named Product, we create access the objects as follows

        products = Product.objects.all()
        This gives us access to all the entries in the database table named Product.

        Here Product is the model name which we have used to create the product table.

        In the above code, products is now a list of product that contains every single product.

        Using the ORM, we can also access an individual product as well depending on its id.

        product = Product.objects.get(id=1)
        The above code saves a single product with an id 1 in the product variable.

        We could also perform other operations like creating a product.

        Suppose you want to create a new product, you do it as:

        p1 = Product(name="iphone",price="999")
        We first give our object some name, here we have named it p1.

        We defined that p1 is a Product object.

        We have passed the model fields that are required to create the product such as name and price.

        The above code just creates the product object, and does not save the data into database table.

        To actually save it, we say:

        p1.save()
        Similarly to delete it we would say.

        To download this note in PDF format, please check the file attached to this lecture.


## 07. Views & Templates


#### 07.1 Getting Products Inside View

        Activities:

        1. Modified readme file
        README.md

        2. Load Product objects to Products view
        modified:   myapp/views.py

        DONE :)

        NOTE: 

        1. It has no format
        2. Should use tempate to show them.

        NEXT: #### 07.2 Creating A Template


#### 07.2 Creating A Template

        Activities:

        1. Modified readme file
        README.md

        2. Create a template
        new file:   myapp/templates/myapp/index.html

        <html>
        <head>
                <title>Products List</title>
        </head>
        <body>

        </body>
        </html>

        NEXT: #### 07.3 Rendering Template & Passing Context


#### 07.3 Rendering Template & Passing Context

        Activities:

        1. Modified readme file
        README.md

        2. Passing context
        modified:   myapp/views.py

        Rendering context to template        
        modified:   myapp/templates/myapp/index.html

        NEXT: #### 07.4 Looping through objects


#### 07.4 Looping through objects

        Activities:

        1. Modified readme file
        README.md

        2. Looping through objects
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 07.5 Detail View Part 1


#### 07.5 Detail View Part 1

        Activities:

        1. Modified readme file
        README.md

        2. Create url
        modified:   myapp/urls.py

        3. Create product_detail view
        modified:   myapp/views.py

        NEXT: #### 07.6 Detail View Part 2


#### 07.6 Detail View Part 2

        Activities:

        1. Modified readme file
        README.md
        
        2. Add logic to detail_detail view
        modified:   myapp/views.py 

        3. Render product instance to detail page       
        new file:   myapp/templates/myapp/detail.html

        DONE :) 

        NEXT: #### 07.7 Creating Links For Product Detail


#### 07.7 Creating Links For Product Detail

        Activities:

        1. Modified readme file
        README.md

        2. Create product detail page
        modified:   myapp/templates/myapp/detail.html

        3. Add link to detail page
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 07.8 Removing Hardcoded URLs


#### 07.8 Removing Hardcoded URLs

        Activities:

        1. Modified readme file
        README.md

        2. 07.8 Removing Hardcoded URLs
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 07.9 Namespacing URLs
