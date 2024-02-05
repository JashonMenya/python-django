# Comprehensive Python-Django Project Documentation

## Table of Contents

1. [Starting A Project](#introduction-to-django)
2. [Running the App](#running-the-app)
3. [Creating an app(component)](#creating-an-appcomponent)
4. [Modifying the view](#modifying-the-view)

## Starting a project

Navigate to desired directory. Run this command and it will generate the default items you will need to get started in
the directory you are on.

```shell
django-admin startproject project_name.
```

## Running the App
```shell
python manage.py runserver
```

## Creating an app(component)
```shell
django-admin startapp home
```

## Modifying the view
- `views.py`: Handles the request-response cycle for your web application. This is where you define how your application
  responds to user requests. Once you add your new view... you import and add it to the `urls.py` file