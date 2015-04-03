0. Purpose:
    The purpose of this tutorial is to better understand client-server
    architecture. This will help me implement my License project.
1. Notes:
    0. For the FlaskApp.conf file, I used the IP of the Compute Instance.
    1. For the url for the bootstrap css, I use Jinja Templating.

        {{ var }} - The double curly braces tell me that this is a variable.
        A variable can also be controlled via logic. This is implemented like this:

        {% logic %}
        {% endlogic %}

        The line: {{url_for('static',filename='css/bootstrap.min.css')}}
        is telling the browser to set the reference for the bootstrap (href)
        as the url for static/css/bootstrap.min.css

        
