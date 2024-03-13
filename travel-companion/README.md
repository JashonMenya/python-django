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

### Files Generated Explained

When initiating a new Django project, several files and directories are automatically generated:

- **`manage.py`**: A command-line tool for executing various Django project tasks.

- **`myproject/` directory**: Holds your project's settings and configurations.

  - **`__init__.py`**: An empty file indicating the directory is a Python package.

  - **`asgi.py` & `wsgi.py`**: Entry points for ASGI and WSGI-compliant web servers.

  - **`settings.py`**: Contains all project settings, including database and security configurations.

  - **`urls.py`**: Defines URL patterns for your project.

Understanding the purpose of these files is crucial for effective Django development.
