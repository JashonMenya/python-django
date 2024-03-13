# Building a Django App From Scratch

## Table of Contents

- [Getting Started](#getting-started)
  - [Generate The Project](#generate-the-project)
  - [Files Generated Explained](#files-generated-explained)
  - [Creating Your First App](#creating-your-first-app)

## Getting Started

### Generate The Project

To begin your Django project, follow these straightforward steps:

1. **Navigate to Your Project Folder:** Open your terminal and go to the folder where you wish to create your Django project.

2. **Start a Project:** Generate the basic structure of your Django project with this command:

   ```bash
   django-admin startproject trips_r_us .
   ```

   The files that get generated are detailed [here](#files-generated-explained).

3. **Run the App Locally:** To start your app on your local machine, use:
   ```bash
   python manage.py runserver
   ```

### Creating Your First App

1. **Generate a New App:** Create a new app within your project by running:

   ```bash
   django-admin startapp itinerary
   ```

   Once the app is created, you need to include it in your project's settings.

2. **Update `settings.py`:** Open the `settings.py` file located in your project directory. This file is created automatically when you start a new Django project. Add your new app to the `INSTALLED_APPS` section by including its name as a string:

   ```python
   INSTALLED_APPS = [
      ...
      'itinerary',
   ]
   ```

   This step tells your Django project to recognize and include the `itinerary` app, making its functionalities available to the entire project.

   **Best Practice Alert:** It's recommended to structure your apps in a way that the project remains functional even if an app is removed. This modular approach ensures that each app can operate independently within the larger project framework.

3. **Incorporate App URLs into the Project's `urls.py`:** To integrate your app's URLs with your project, modify the project's `urls.py` file to include the app's URL configurations. Use the `include` function to import your app's URLs, allowing for a clean separation of URLs by app:

   ```python
   from django.urls import path, include  # Don't forget to import include

   urlpatterns = [
      ...
      path('itinerary/', include('itinerary.urls')),  # Include your app's URLs
   ]
   ```

   This setup helps maintain organized URL structures and makes it easier to navigate and manage different app components within your project.

4. **Run Migrations:**
   Django uses migrations to apply changes to your database schema. These migrations make sure your database is up-to-date with your models. When you first set up your project, you need to apply the initial migrations for Django's built-in apps, such as `admin` and `auth`, which provide the admin panel and user authentication, respectively. Run the following command to apply these initial migrations:

   ```python
   python manage.py migrate
   ```

   This command configures your database to work with Django's default apps, setting up necessary tables for user management and admin functionalities.

5. **Creating a Superuser:**
   A superuser has full access to your project's admin site, allowing you to manage aspects like user accounts and groups. After your database is set up, create a superuser account by running:

   ```python
   python manage.py createsuperuser
   ```

   Follow the prompts to set a username, email, and password for the superuser. This step is essential for accessing the Django admin interface and managing your project's data.

6. **User Authentication:**
   Implementing user authentication allows your application to manage user sessions, providing a personalized and secure user experience. Here's how you can set up authentication, complete with rerouting unauthenticated users:

   - **Templates for Authentication:** Create HTML templates for the login and registration forms. These will be the front-end components where users can input their login details.

   - **Authentication Views:** Develop views in your Django app to handle user authentication processes such as logging in and logging out.

   - **Access Control:** Use Django's `@login_required` decorator to protect views by ensuring only authenticated users can access them.

   - **Redirecting Unauthenticated Users:** To redirect unauthenticated users trying to access restricted pages, specify a `login_url` in the `@login_required` decorator. This determines where to send users who are not logged in. For example, if you want to redirect unauthenticated users to the admin login page before they can access a specific view, you can do so as follows:

   ```python
   from django.contrib.auth.decorators import login_required
   from django.shortcuts import render

   @login_required(login_url='/admin')
   def authorized(request):
       # This view is now protected, and unauthenticated users are redirected.
       return render(request, 'home/authorized.html', {})
   ```

7. **Working with Django ORM:**

   Django's ORM (Object-Relational Mapping) allows you to interact with your database using Python code instead of SQL. By defining models, you create a Pythonic representation of your database structure. Here's how to use Django's ORM to create models and reflect them as tables in your database:

   - **Creating Models:** Each model you define in your Django app represents a database table. The attributes of the class (model) correspond to columns in the database table. This approach allows you to work with databases in a more intuitive and Pythonic way.

   - **Migrations:** Migrations are Django's way of propagating changes you make to your models (like adding a new field or creating a new model) into the database schema. There are two steps involved:

     1. **Making Migrations:** This step generates migration files based on the changes you've made to your models. These files describe how to adjust the database to match your current models. Run the following command to create migration files:

        ```python
        python manage.py makemigrations
        ```

        The first migration file created will be named `0001_initial.py`, indicating the initial setup for your models.

     2. **Applying Migrations:** After creating migration files, you need to apply them to update the database schema. This step executes the instructions defined in the migrations to alter the database structure. Execute the migrations by running:
        ```python
        python manage.py migrate
        ```

   - **Example Model:** To see an example of how to define a model, refer to [here](../smartnotes/notes/models.py)

   By following these steps, you successfully create tables in your database based on your Django models, utilizing the full power of Django's ORM for managing database operations.

   This ORM-centric approach facilitates the efficient management of database schemas and data manipulation, making it an essential part of developing applications with Django.

8. **Using the Django Shell:**

   The Django shell is a powerful feature for directly interacting with your project's Django models and database. It provides a Python shell with your Django project's environment loaded, allowing for real-time data manipulation and querying. Here's a step-by-step guide, including launching the shell and performing more advanced queries:

   - **Launching the Django Shell:**
     To open the Django shell, run the command below in your terminal. This brings up an interactive Python console configured for your Django project:

     ```shell
     python manage.py shell
     ```

     You're now in an interactive environment where you can execute Python code directly in the context of your Django project.

   - **Filtering Records in the Shell:**
     Once in the shell, you can use Django's ORM to perform complex queries with ease. For example, to filter notes based on their titles, you can do the following:

     ```python
     from notes.models import Notes
     # Find notes with titles starting with 'N'
     notes_starting_with_n = Notes.objects.filter(title__startswith='N')
     for note in notes_starting_with_n:
         print(note.title)

     # Find notes with titles that contain the word 'note', case-insensitive
     notes_containing_note = Notes.objects.filter(title__icontains='note')
     for note in notes_containing_note:
         print(note.title)
     ```

     These commands utilize Django's ORM `filter` method with field lookups like `__startswith` and `__icontains` to query the database efficiently. This makes it easy to retrieve data that matches specific patterns or criteria.

The Django shell is invaluable for testing, exploring, and manipulating your database in a controlled and Pythonic way. Whether you're debugging or just exploring your data, the Django shell provides the flexibility and power needed to interact with your application's underlying data structures effectively.

Using the Django shell like this provides a powerful and flexible way to interact with your project's database. It's especially useful for debugging, experimenting with model queries, and quickly modifying database records during development.

By completing these steps, your Django project is not only up and running but also configured with a superuser account, granting you access to the powerful Django admin interface. This setup allows for easier management of your project's users and settings right from the start.

### Files Generated Explained

When initiating a new Django project, several files and directories are automatically generated:

- **`manage.py`**: A command-line tool for executing various Django project tasks.

- **`myproject/` directory**: Holds your project's settings and configurations.

  - **`__init__.py`**: An empty file indicating the directory is a Python package.

  - **`asgi.py` & `wsgi.py`**: Entry points for ASGI and WSGI-compliant web servers.

  - **`settings.py`**: Contains all project settings, including database and security configurations.

  - **`urls.py`**: Defines URL patterns for your project.

Understanding the purpose of these files is crucial for effective Django development.
