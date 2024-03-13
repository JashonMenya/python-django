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
