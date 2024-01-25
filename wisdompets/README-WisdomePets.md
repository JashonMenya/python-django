# Wisdom Pets Project

## Quick Start Guide

### Setting Up a Virtual Environment

Using a virtual environment is strongly recommended to manage and isolate dependencies specific to this project.

#### For macOS Users:

Run the following script in your terminal to set up the virtual environment and install dependencies:

```shell
# Navigate to the projects root

# Navigate to the projects root wisdompets/ then create the Virtual Environment
python3 -m venv venv

# Activate the Virtual Environment
. venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Generate requirements.txt with current project's dependencies (optional)
pip freeze > requirements.txt
```
