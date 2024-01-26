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

#### Overview of the Project

##### Template Syntax

- `{{ }}` - Used to output the result of an expression
- `{% %}` - Used to run statements and control logic
- `{# #}` - Used to add comments
- `{{ pet.name|title }}` - The `|` is a pipe and is used to apply a filter to the variable `pet.name`. In this case,
  the `title` filter is used to capitalize the first letter of each word in the pet's name.
- `{{ pet.name|title|truncatewords:1 }}` - Multiple filters can be chained together. In this case, the `truncatewords`
  filter is used to truncate the pet's name to 1 word.
- `{% if pet.vaccinations.all %}` - The `if` statement is used to check if the pet has any vaccinations. The `all`
  keyword is used to check if all vaccinations are true.
- `{% for pet in pets %}` - The `for` loop is used to iterate over a list of pets. The `pets` variable is passed in from
  the view function.
- `{% url 'pet_detail' pet.id %}` - The `url` template tag is used to generate a URL for the pet detail page. The
  `pet_detail` is the name of the URL pattern and `pet.id` is the pet's ID.
- `{% block content %}` - The `block` tag is used to define a block of content that can be overridden in a child
  template. The `content` is the name of the block.
- `{% extends 'base.html' %}` - The `extends` tag is used to extend a parent template. The `base.html` is the name of
  the parent template.
- `{% endblock %}` - The `endblock` tag is used to end a block of content.

##### Examples

In adoptions/templates/pet_detail.html, add the following code to display the pet's name:

```html
<h3>{{pet.name}}</h3>
```

Resulting HTML:

```html
<h3>Scooter</h3>
```

##### Filters

```html
<h3>{{pet.name | capfirst }}</h3>
```

Resulting HTML:

```html
<h3>Scooter</h3>
```

##### Template Loops

```html
{%for pet in pets%}
<li>{{pet.name}}</li>
{%endfor%}
```

Resulting HTML:

```html

<li>Scooter</li>
<li>Pepe</li>
...
```

##### URL Tags

In wisdompets/urls.py, add the following code to create a URL pattern for the pet detail page:

```python
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('admin/', admin.site.urls)
]
```

In adoptions/templates/pet_detail.html, add the following code to display the pet's name:

```html
{% url 'pet_detail' pet.id %}
```

resulting HTML:

```html
/adoptions/1/
```

putting it all together:

```html

<ul>
    {% for pet in pets %}
    <li>
        <a href="{% url 'pet_detail' pet.id %}">
            {{ pet.name }}
        </a>
    </li>
    {% endfor %}
</ul>
```

resulting HTML:

```html

<ul>
    <li>
        <a href="/adoptions/1/">
            Scooter
        </a>
    </li>
    <li>
        <a href="/adoptions/2/">
            Pepe
        </a>
    </li>
</ul>
```
