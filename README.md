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


#### 07.9 Namespacing URLs

        Activities:

        1. Modified readme file
        README.md

        2. Namespacing URLs
        modified:   myapp/urls.py

        3. Modified the link
        modified:   myapp/templates/myapp/detail.html

        4. Modified the link
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 07.10 Section Notes- Views & Templates


#### 07.10 Section Notes- Views & Templates

        Activities:

        1. Modified readme file
        README.md

        Views & Templates

        What are templates ?
        Templates in Django allow us to generate HTML dynamically.

        To render these templates, Django needs a templating engine.

        Django comes with its own templating engine called the Django templating engine.

        A template must always be created inside the templates directory of an app.

        The path where these templates resides must be clearly defined.

        In order to render these templates, Django needs to know where exactly these templates are located.

        A template can be rendered my making use of the render method.

        A template always has to be returned as a response from a view.

        Example:

        return render(request,'myapp/index.html')
        To the render method, we need to pass the request object and the exact path where the template is located.

        Passing dynamic data to templates.
        We can render templates as plain simple HTML pages.

        We can also make them dynamic by adding dynamic database data into it.

        For example, if we have a list of products in our database, we first extract that list and then pass it as context to the template.

        Here is an example

        Step 1: Getting the list of products from the database
        products = Product.objects.all()
        Step 2: Create a context out of it
        context = {'products':products}
        Here ‘products’ is the name by which we will refer to the context inside of our template.

        Step 3: Pass this context to the template while rendering it
        return render(request,'myapp/products.html',context)

        Accessing the context in the HTML template.
        Once the context object has been passed, it can be de-structured inside the HTML template using the templating language.

        Here is how to do it:

        {% for product in products %}
                {{product}}
        {% endfor %}
        We loop through every product inside the products, products is a list of products that is passed to the template as context and hence we are able to access it in the HTML template.

        Similarly we can also get a single object from the database and pass it as context to the template as well.

        We can also retrieve objects from more than one model, combine them together and pass it as context to the template.

        Namespacing in Django
        Whenever we refer any URL we refer to it by its name.

        This is alright when you have a single app in your Django project.

        But when you have multiple apps, each app will have its own URLs py file.

        These URL patterns in different apps might have similar names and that might be a problem.

        Hence, we use namespacing and associate every URL pattern with the app name.

        To download this note in PDF format, please check the file attached to this lecture.

        NEXT: ## 08. Adding Styling To Django Project With CSS & Tailwind


## 08. Adding Styling To Django Project With CSS & Tailwind


#### 06.1 Introduction To Styling (PASSED)

        PASS

        NEXT: #### 06.2 Adding CSS To Django Project


#### 06.2 Adding CSS To Django Project

        Activities:

        1. Modified readme file
        README.md

        2. Create static file
        new file:   myapp/static/myapp/style.css

        3. Adding Styling To Django Project
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 06.3 Installing Node For Tailwind


#### 06.3 Installing Node For Tailwind

        Activities:

        1. Modified readme file
        README.md

        2. Upgrade node
        C:\Users\hp>node -v
        v18.14.0

        NEXT: #### 06.4 Setting Up Tailwind For Django


#### 06.4 Setting Up Tailwind For Django

        Activities:

        1. Modified readme file
        README.md

        2. Modified
        modified:   .gitignore

        3. Setting Up Tailwind For Django
        new file:   myapp/static/myapp/src/tw.css

        4. New file created after running npm run build
        new file:   myapp/static/myapp/styles.css

        5. Using tailwind (load tailwind)
        modified:   myapp/templates/myapp/index.html

        6. New files created using npm init -y
        new file:   package-lock.json
        new file:   package.json

        DONE :)

        NEXT: #### 06.5 Designing Navbar Part 1


#### 06.5 Designing Navbar Part 1

        Activities:

        1. Modified readme file
        README.md

        2. Add logo
        new file:   myapp/static/myapp/images/logo-shopping-bag.png

        3. Start using tailwind css for navbar
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 06.6 Designing Navbar Part 2


#### 06.6 Designing Navbar Part 2

        Activities:

        1. Modified readme file
        README.md

        2. Styling the navbar
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT:#### 06.7 Using Base Template


#### 06.7 Using Base Template

        Activities:

        1. Modified readme file
        README.md

        2. Create base template
        new file:   myapp/templates/myapp/base.html

        3. Extend base template
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 06.8 Using Base Template In Detail View


#### 06.8 Using Base Template In Detail View

        Activities:

        1. Modified readme file
        README.md

        2. Extending base template
        modified:   myapp/templates/myapp/detail.html

        DONE :)

        NEXT: #### 06.9 Adding Image Field To Model


#### 06.9 Adding Image Field To Model

        Activities:

        1. Modified readme file
        README.md        

        2. Adding image field to Product model
        modified:   myapp/models.py

        3. Run and apply migrations
        modified:   myapp/migrations/0001_initial.py

        4. Cofigure media root and url
        modified:   mysite/settings.py

        5. Setup the media path
        modified:   mysite/urls.py

        6. Add new products and images from admin panel
        new file:   media/images/cat-12.png
        new file:   media/images/cat-2.png
        new file:   media/images/cat-9.png            

        7. Load product and image in detail page 
        modified:   myapp/templates/myapp/detail.html

        DONE :)

        NEXT: #### 06.10 Adding Site Hero Using Tailwind


#### 06.10 Adding Site Hero Using Tailwind

        Activities:

        1. Adding Site Hero Using Tailwind

        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 06.11 Adding Card Layout To Products


#### 06.11 Adding Card Layout To Products

        Activities:

        1. Adding html card
        modified:   myapp/templates/myapp/index.html

        2. Add some product
        new file:   media/images/imac_kmsZxc0.png
        new file:   media/images/ipad.jpeg
        new file:   media/images/ipad.png
        new file:   media/images/iphone-4.png
        new file:   media/images/iphone-5.png
        new file:   media/images/iphone12.jpeg

        3. Modified
        modified:   README.md

        DONE :)

        NEXT:#### 06.12 Styling The Detail Page
        

#### 06.12 Styling The Detail Page

        Activities:
        
        1. Styling detail page
        modified:   myapp/templates/myapp/detail.html  

        DONE :)

        NEXT: ## 09. Forms & CRUD Operations in Django
      

## 09. Forms & CRUD Operations in Django


#### 09.1 Introduction To CRUD (PASSED)


#### 09.2 Creating A Form To Accept Products - Get method

        Activities:

        1. Create form
        new file:   myapp/templates/myapp/addproduct.html

        2. Define url to add product
        modified:   myapp/urls.py

        3. Define add_product method
        modified:   myapp/views.py

        DONE :)

        NEXT: #### 09.2 Creating A Form To Accept Products - POST method


#### 09.2 Creating A Form To Accept Products - POST method

        Activities:

        1. Adding POST method and csrf_token
        modified:   myapp/templates/myapp/addproduct.html

        NOTE:

        1. Using POST method and csrf_token data is more secure.
        2. We could submit the form.
        3. But where did the submited data go?

        DONE :)

        NEXT: #### 09.3 Getting Form Data


### 09.3 Getting Form Data

        Activities:

        1. Modified the form
        modified:   myapp/templates/myapp/addproduct.html

        2. Add logic to add_product view
        modified:   myapp/views.py

        DONE :)

        NEXT: #### 09.4 Testing The Form


#### 09.4 Testing The Form

        Activities:

        1. Added a new product
        new file:   media/images/imac.png

        DONE :)

        NEXT: #### 09.5 Styling Add Product Form


#### 09.5 Styling Add Product Form

        Activities:

        1. Add style to form
        modified:   myapp/templates/myapp/addproduct.html   

        2. Testing: adding a product     
        new file:   media/images/airpods.jpeg

        DONE :)

        NEXT: #### 09.6 Update Part 1


#### 09.6 Update Part 1

        Activities:

        1. Create update product page
        new file:   myapp/templates/myapp/updateproduct.html

        2. Create path for product update
        modified:   myapp/urls.py

        3. Define update_product view
        modified:   myapp/views.py

        DONE :)

        NEXT: #### 09.7 Update Part 2


#### 09.7 Update Part 2

        Activities:

        1. Add logic to get a product instance
        modified:   myapp/views.py

        2. Render the instance in updateproduct.html
        modified:   myapp/templates/myapp/updateproduct.html

        DONE :)

        NOTE:

        1. The from could not yet update product.
        2. To make it work, add more logic to update_product view

        NEXT: #### 09.8 Update Part 3


#### 09.8 Update Part 3

        Activities:

        1. Add logic to update_product view
        modified:   myapp/views.py

        DONE :)

        NEXT: #### 09.9 Delete Part 1


#### 09.9 Delete Part 1

        Activities:

        1. Create delete path
        modified:   myapp/urls.py

        2. Create delete_product view
        modified:   myapp/views.py

        3. Create deleteproduct page
        new file:   myapp/templates/myapp/deleteproduct.html

        4. Testing: delete a product

        DONE :)

        NEXT: #### 09.10 Delete Part 2


#### 09.10 Delete Part 2

        Activities:

        1. Styling the deleteproduct form and added cancel button
        modified:   myapp/templates/myapp/deleteproduct.html

        2. Testing

        DONE :)

        NEXT: ## 10. Authentication


## 10. Authentication


#### 10.1 Section Intro (PASSED)


#### 10.2 Introduction To Authentication (PASSED)

        NEXT: #### 10.3 Creating The Users App


#### 10.3-4 Creating The Users App & Register Form

        Activities:

        1. Create users app
        > (venv3932) λ python manage.py startapp users
        
        modified:   mysite/settings.py
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/views.py

        2. Create NewUserForm
        new file:   users/forms.py

        NEXT: #### 10.5 Template To Render Registration Form



#### 10.5 Template To Render Registration Form


        Activities:

        1. Fixing the issue
        modified:   users/forms.py
        
        2. Defining register view and get instances from the NewUserForm
        modified:   users/views.py 

        3. Create register page       
        new file:   users/templates/users/register.html

        DONE :)

        NEXT: #### 10.6 URL Patterns For Registration


#### 10.6 URL Patterns For Registration


        Activities:

        1. Create path for register form
        new file:   users/urls.py

        2. Include the above path here        
        modified:   mysite/urls.py

        DONE :)

        NEXT: #### 10.7 Designing The Registration Form


#### 10.7 Designing The Registration Form


        Activities:

        1. Styling the Registration Form
        modified:   users/templates/users/register.html

        DONE :)

        Note: Form focus has issues of focus outline

        NEXT: #### 10.8 Removing Focused Outline


#### 10.8 Removing Focused Outline

        Activities:

        1. Add form widgets
        modified:   users/forms.py

        DONE :)

        NOTE: The form does not functioning yet

        NEXT: #### 10.9 Completing Register Functionality


#### 10.9 Completing Register Functionality

        Activities:

        1. Create user instances
        modified:   users/forms.py

        2. Add logic to save user data
        modified:   users/views.py

        DONE :)

        NOTE: Could not register a new user if using the email address as the password

        NEXT: #### 10.10 Login Part 1


#### 10.10 Login Part 1

        Activities:

        1. Create login using LoginView 
        modified:   users/urls.py

        2. Create login page
        new file:   users/templates/users/login.html

        DONE :)

        NEXT: #### 10.11 Login Part 2


#### 10.11 Login Part 2

        Activities:

        1. Create login form
        modified:   users/templates/users/login.html

        2. Testing

        NOTE:

        1. Superadmin can login via the login form and can
           directly see the admin panel
        2. Normal user can login, but can not login to admin
        3. So normal user is restricted to see admin panel

        DONE :)

        NEXT: #### 10.12 Logout


#### 10.12 Logout

        Activities:

        1. Create LogoutView 
        modified:   users/urls.py

        2. Create logout page
        new file:   users/templates/users/logout.html

        NOTE:

        1. Login and logout as normal:
           . Can login and logout from the front.
           . Can not login/logout via admin panel.

        2. Login and logout as superuser
           . Can login and logout via admin panel.
           . Can also login and logout via front.

        3. It means, it works perfectly.

        4. But the logged in user, always redirect to profile page.

        DONE :)

        NEXT: #### 10.13 Login Redirect URL


#### 10.13 Login Redirect URL

        Activities:

        1. Add parameter LOGIN_REDIRECT_URL 
        modified:   mysite/settings.py

        DONE :)

        NEXT: #### 10.14 Adding Login Button To Navbar


#### 10.14 Adding Login Button To Navbar

        Activities:

        1. Add conditional to navbar to show login/logout menu
        modified:   myapp/templates/myapp/base.html

        2. Delete unnecessary part of the page
        modified:   myapp/templates/myapp/index.html

        NOTE: User still can access any page

        DONE :)

        NEXT: #### 10.15 Login Required Decorator


#### 10.15.1 Create profile page

        Activities:

        1. Create profile view
        modified:   users/views.py

        2. Create profile path
        modified:   users/urls.py

        3. Create profile page
        new file:   users/templates/users/profile.html

        4. Add profile menu in navbar
        modified:   myapp/templates/myapp/base.html

        DONE :)

        NEXT: #### 10.15 Login Required Decorator


#### 10.15.2 Login Required Decorator - Page not found (404)

        Activities:

        1. Adding @login_required to profile view
        modified:   users/views.py

        2. Modified 
        modified:   users/templates/users/profile.html


        NOTE: Un-logged in user now can not access the profile page



#### 10.15.3 Login Required Decorator - Redirect un-logged in user to login page

        Activities:

        1. Add LOGIN_URL parameter
        modified:   mysite/settings.py

        DONE :)

        NOTE:

        1. Un-logged in user will redirect to login page
        2. Logged in user will redirect to products page

        NEXT: ## 11. Creating User Profile


## 11. Creating User Profile


#### 11.1 Introduction To Creating User Profile (PASSED)


#### 11.2 Creating A Profile Model

        Activities:

        1. Create Profile model and run migrations

        modified:   users/models.py        
        new file:   users/migrations/0001_initial.py
        
        2. Register Profile model
        modified:   users/admin.py

        3. Create a profile from admin panel
        new file:   media/profile_pictures/ing.PNG

        4. Render profile image to profile page
        modified:   users/templates/users/profile.html

        DONE :)

        NEXT: #### 11.3 Designing Profile Page


### 11.3 Designing Profile Page

        Activities:

        1. Styling profile page
        modified:   users/templates/users/profile.html

        DONE :)

        NEXT: #### 11.4 Creating Profile Form


#### 11.4 Creating Profile Form

        Activities:

        1. Create path for createprofile
        modified:   users/urls.py

        2. Create create_profile view
        modified:   users/views.py 

        3. Create Profile Form       
        new file:   users/templates/users/createprofile.html

        DONE :)

        NEXT: #### 11.5 Handling Post Request


#### 11.5 Handling Post Request

        Activities:
        
        1. Handling Post Request
        modified:   users/views.py 

        2. Add image and contact number to testuser1       
        new file:   media/profile_pictures/darling.PNG

        DONE :)

        NEXT: #### 11.6 Associating User With Product


#### 11.6 Associating User With Product - Part 1: Preventing un-loggeg in user to add product

        Activities:

        1. Add login_required
        modified:   myapp/views.py

        DONE :)

        NEXT: 11.6 Associating User With Product


#### 11.6 Associating User With Product - Part 2 Adding seller_name field to Product model

        Activities:

        1. Add seller_name field to Product model
        modified:   myapp/models.py

        2. Run and apply migrations        
        new file:   myapp/migrations/0002_product_seller_nme.py

        DONE :)


        NEXT: #### 11.6 Associating User With Product


#### 11.6 Associating User With Product - Part 3 Display seller_name to products page


        Activities:

        1. Modified field name from seller_nme to seller_name        
        modified:   myapp/models.py

        2. Run migrations
        new file:   myapp/migrations/0003_rename_seller_nme_product_seller_name.py

        3. Display seller_name
        modified:   myapp/templates/myapp/index.html

        DONE :)

        NEXT: #### 11.6 Associating User With Product


#### 11.6 Associating User With Product - Part 4 Add seller_name to add_product view

        Activities:

        1. Add seller_name to add_product view
        modified:   myapp/views.py       

        2. Testing: loging in > add product 
        new file:   media/images/iphone-8.png

        DONE :)

        NEXT: #### 11.7 Displaying Seller Details


#### 11.7 Displaying Seller Details

        Activities:

        1. Add seller_name to add_product view
        modified:   myapp/views.py

        2. Add a new product by logged in user
        new file:   media/images/iphone-8.png

        3. Load user detail to the detail page
        modified:   myapp/templates/myapp/detail.html

        DONE :)

        NEXT: #### 11.8 Creating Seller Profile Page


#### 11.8 Creating Seller Profile Page

        Activities:

        1. Create path for sellerprofile
        modified:   users/urls.py

        2. Create seller_profile view
        modified:   users/views.py

        3. Add seller_name to add_product view
        modified:   myapp/views.py

        4. Create a new selllerprofile page
        new file:   users/templates/users/selllerprofile.html

        5. Add a new product by logged in user
        new file:   media/images/iphone-8.png

        6. Display product detail
        modified:   myapp/templates/myapp/detail.html

        DONE :)

        NEXT: #### 11.9 Designing Seller Profile Page


#### 11.9 Designing Seller Profile Page

        Activities:

        1. Designing Seller Profile Page
        modified:   users/templates/users/selllerprofile.html

        DONE :)

        NEXT: #### 11.10 Adding Design Touches To Navbar


#### 11.10 Adding Design Touches:  Part 1 - To Navbar

        Activities:

        1. Adding design to navbar
        modified:   myapp/templates/myapp/base.html

        DONE :)

        NEXT: #### 11.10 Adding Design Touches:  Part 1 - To Login


#### 11.10 Adding Design Touches:  Part 2 - To Login and Register

        Activities:

        1. Adding design and link to register page
        modified:   users/templates/users/login.html

        2. Adding design and link to login page
        modified:   users/templates/users/register.html

        DONE :)

        NEXT: #### 11.11 Creating My Listings Page Part 1


#### 11.11 Creating My Listings Page Part 1

        Activities:

        1. Create my_listings view
        modified:   myapp/views.py

        2. Create path for mylistings        
        modified:   myapp/urls.py

        3. Create mylistings page and render the objects
        new file:   myapp/templates/myapp/mylistings.html

        DONE :)

        NEXT: #### 11.12 Creating My Listings Page Part 2


#### 11.12 Creating My Listings Page Part 2

        Activities:

        1. Styling the mylistings page
        modified:   myapp/templates/myapp/mylistings.html

        DONE :)

        NEXT: #### 11.13 Creating My Listings Page Part 3


#### 11.13 Creating My Listings Page Part 3

        Activities:

        1. Adding Edit and Delete button
        modified:   myapp/templates/myapp/mylistings.html

        2. Adding mylistings menu
        modified:   myapp/templates/myapp/base.html

        3. Testing: Update product
        new file:   media/images/airpods_B1fA3j5.jpeg
        new file:   media/images/airpods_v231w9J.jpeg
        new file:   media/images/iphone-6.png
        new file:   media/images/iphone-9.png

        NOTE:

        1. Update a product without change/replace the image,
           it will rise error like this:

           MultiValueDictKeyError at /myapp/products/update/8/
          'upload'

        2. But update a product by replacing/change the image,
           it worked.

        3. So, to update something for a product, MUST
           replace/change the image, eventhough to
           use the same image.


        DONE (:

        NEXT: ## 12. Class Based Views in Django


## 12. Class Based Views in Django


#### 12.1 Introduction To Class Based Views (PASSED)


#### 12.2 Class Based ListView

        Activities:

        1. Create Classed Based ProductListView
        modified:   myapp/views.py

        2. Create the path        
        modified:   myapp/urls.py

        DONE :)

        NEXT: #### 12.3 Class Based DetailView


#### 12.3 Class Based DetailView

        Activities:

        1. Create Classed Based ProductDetailView
        modified:   myapp/views.py

        2. Create the path        
        modified:   myapp/urls.py

        DONE :)

        NEXT: #### 12.4 CreateView Part 1


#### 12.4 CreateView Part 1

        Activities:

        1. Create Classed Based ProductCreateView
        modified:   myapp/views.py

        2. Create the path for ProductCreateView
        modified:   myapp/urls.py

        3. Render the form instance
        new file:   myapp/templates/myapp/product_form.html

        DONE :)

        NEXT: #### 12.5 CreateView Part 2


#### 12.5 CreateView Part 2

        Activities:

        1. Designin product_form page
        modified:   myapp/templates/myapp/product_form.html   

        2. Testing create a new product     
        new file:   media/images/imac_kmsZxc0_XHenDlC.png

        NOTE: 

        1. Product created, but it create error. It says:
                'ImproperlyConfigured at /myapp/products/add/
                No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.'

        2. When go to http://127.0.0.1:8000/myapp/products/, you can see the created product

        NEXT: #### 12.6 UpdateView


#### 12.6 UpdateView

        Activities:

        1. Create ProductUpdateView
        modified:   myapp/views.py 

        2. Create the path       
        modified:   myapp/urls.py

        3. Create the page
        new file:   myapp/templates/myapp/product_update_form.html
       
        4. Update a product
        new file:   media/images/iphone-13-pro-silver-select.jpeg

        NOTE:

        1. It worked.
        2. But the form showed the seller_name options.
        3. Any user can change the seller.

        NEXT: #### 12.7 DeleteView


#### 12.7 DeleteView

        Activities:
        
        1. Create ProductDelete view
        modified:   myapp/views.py  

        2. Create path for it      
        modified:   myapp/urls.py

        3. Create product_confirm_delete
        new file:   myapp/templates/myapp/product_confirm_delete.html

        DONE :)

        NEXT: #### 12.8 Redirect URL Remaining Lecture


#### 12.8 Redirect URL 

        Activities:

        1. Create get_abosolute_url
        modified:   myapp/models.py   
        
        2. Testing update new product
        new file:   media/images/iphone12_57EGzjT.jpeg

        DONE :)

        NEXT: ## 13. Customising Admin Panel

