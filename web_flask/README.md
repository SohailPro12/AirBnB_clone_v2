<h1> 0x04. AirBnB clone - Web framework </h1>
# General

- **What is a Web Framework**
  A web framework is a software framework designed to aid in the development of web applications including web services, web resources, and web APIs.

- **How to build a web framework with Flask**
  Flask is a lightweight WSGI web application framework in Python. To build a web framework with Flask, you need to define routes, handle requests, and responses using Flask's functionalities.

- **How to define routes in Flask**
  Routes in Flask are defined using the `@app.route()` decorator in Python. This decorator binds a function to a URL so that when the URL is accessed, the function is executed.

- **What is a route**
  A route in web development refers to the URL pattern that maps to specific functions in a web application. It defines how the application responds to client requests.

- **How to handle variables in a route**
  In Flask, variables in routes are defined by enclosing parts of the URL in `<variable_name>`. These variables can then be accessed within the corresponding view function.

- **What is a template**
  A template is an HTML file that includes placeholders for dynamic data. It allows for the separation of content from presentation in web applications.

- **How to create an HTML response in Flask by using a template**
  In Flask, you can render templates using the `render_template()` function. This function takes the name of the template file as an argument and renders it with any necessary context data.

- **How to create a dynamic template (loops, conditions…)**
  Flask supports Jinja2 templating engine, which allows for dynamic content generation using loops, conditions, and other control structures directly within HTML templates.

- **How to display in HTML data from a MySQL database**
  To display data from a MySQL database in HTML using Flask, you first need to query the database to retrieve the data. Then, pass this data to the template rendering function to display it dynamically on the webpage.

