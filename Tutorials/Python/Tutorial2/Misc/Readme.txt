=====
THIS TUTORIAL IS A FORK OF TUTORIAL 1
IT IS USED TO CHANGE THE WEBSITE, MAKE IT MORE CLOSE TO MY PURPOSE
=====
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

    2. gcloud compute copy-files College/Tutorials/Python/Server/main.html root@server:/var/www/FlaskApp/FlaskApp/templates
    
       This is a working upload command, from Linux ( not tested on Windows )
       
Basic Idea:
    
    Before main.html is rendered by the __init__.py script, I need to
    programmaticly modify it and add the recorded sound.
