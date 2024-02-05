# Comprehensive Python-Django Project Documentation

## Table of Contents

1. [Starting A Project](#introduction-to-django)
2. [Running the App](#running-the-app)
3. [Creating an app(component)](#creating-an-appcomponent)
4. [Modifying the view](#modifying-the-view)
5. [Migrations](#migrations)
   -[initial migration](#initial-migration)
   -[create superuser](#create-superuser)

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

## Migrations

The way django knows if the database is behind the system changes is through
a couple of files called migrations.

Migrations explain what king of changes a database needs to perform such as
create a new table, establish a new relationship e.t.c

By default, Django already has the migrations for the authentication system ready.

### initial migration

```shell
 python manage.py migrate
```

### create superuser

```shell
 python manage.py createsuperuser
```

