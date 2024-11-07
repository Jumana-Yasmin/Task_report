# Task_report
 6 day report of task completed each day

# Day 4: Introduction to Flask and Basic Backend Concepts
 ● __Objective__: Understand Flask and create a simple backend API.
 Topics to Cover:
 ● Introduction to Flask and how it works
 ● Setting up a basic Flask application
 ● Routing in Flask: handling GET and POST requests
 ● Creating a simple REST API endpoint
 Activities:
 1. Install Flask and set up a basic project.
 2. Create simple routes (/hello, /user/<name>) to handle different
 requests.
 3. Implement a simple REST API with Flask (e.g., return data from a
 dictionary or list).
 4. Recommended resources: Flask documentation, Flask for Beginners
 tutorials on YouTube

#FLASK
Flask is a lightweight and flexible web framework for Python. It’s designed to make getting started with web development quick and easy, while still being powerful enough to build complex web applications.
##Route
App Routing means mapping the URLs to a specific function that will handle the logic for that URL. Modern web frameworks use more meaningful URLs to help users remember the URLs and make navigation simpler. 

Example: In our application, the URL (“/”) is associated with the root URL. So if our site’s domain was www.example.org and we want to add routing to “www.example.org/hello”, we would use “/hello”. 

To bind a function to an URL path we use the app.route decorator.

##ACTIVITIES
step 1: downloaded flask using pip install flask.
step 2: opened visual studio and create a folder named practice
step 3: created a file named main.py and imported the flask library.
step 4: created an instance named app (app = Flask(__name__))
step 5: created a route with ('/') as url and wrote 'hello world' to print.
(@app.route('/')
 def home():
    return "Hello World!")
step 6: run the python code and got a link to a browser with Hello World printed on the home page.
step 7:created another route with ('/hello') as url.
@app.route('/hello')
def www():
    return "Hi! Nice to meet U"
step 8: hit run and on the browser wrote /home beside the path(127.0.0.1:5000).
step 9: yet again created another path with('/user/<name>'). this is a dynamic url to use variables in the url.To add variables to URLs, use <variable_name> rule. The function then receives the <variable_name> as keyword argument.
@app.route('/user/<name>')
def username(name):
    return "Welcome"+ name + '!'
step 10: after running the code and opening in browser wrote /user/Jumana Yasmin beside path(http://127.0.0.1:5000/user/Jumana%20Yasmin)
and got the output:
Welcome Jumana Yasmin !
step 11: to use get, post requests in flask: create a folder and under templates create two html pages for a simple calculator, calculate.html is used to prompt the user to input the numbers for addition. answer.html ives the answer to the user.
step 12: a pyhon file named main.py is created to do the operation.
step 13: get, post methods are used for request and resposes

###REFERENCES: Flask Documentation,geeksforgeeks.com
