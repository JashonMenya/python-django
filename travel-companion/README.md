# Building a Django App From Scratch

## Table of Contents

- [Getting Started](#getting-started)
  - [Generate The Project](#generate-the-project)
  - [Files Generated Explained](#files-generated-explained)
  
### Getting Started

### Generate The Project

To kickstart your Django project, follow these steps:

1. **Navigate to Your Project Folder:**
   Open your terminal and navigate to the folder where you want to create your Django project.

2. **Run the Command:**
   Use the following command to generate the basic structure of your Django project:

   ```bash
   django-admin startproject trips_r_us .
   ```

   Files that get generated are explained  [Here](#files-generated-explained)

### Files Generated Explained
When you create a new Django project, several files and directories are automatically generated. Here's a brief overview to help you understand their purpose:

- **`manage.py`**: A command-line utility that lets you interact with your Django project in various ways, like running the development server or managing database migrations.

- **`myproject/` directory**: Contains settings and configurations for your Django project, such as database settings and URL configurations.

    - **`myproject/__init__.py`**: An empty file that tells Python that this directory should be treated as a Python package.

    - **`myproject/asgi.py` and `myproject/wsgi.py`**: Files for deploying your project using ASGI-compatible servers (like Daphne) or WSGI-compatible servers (like Gunicorn), respectively.

    - **`myproject/settings.py`**: A crucial file containing all the settings for your project, including database configuration, security settings, and more.

    - **`myproject/urls.py`**: Defines the URL patterns for your project, mapping URL paths to views.

Understanding these files and their purposes is essential for effectively building and managing your Django applications.