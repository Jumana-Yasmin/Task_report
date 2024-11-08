# Task_report
 6 day report of task completed each day

# Day 5: Building a Basic REST API with Flask
 ● __Objective__: Develop a functional REST API with multiple endpoints
 and simple CRUD operations.
 Topics to Cover:
 ● REST API design principles
 ● Flask route methods (GET, POST, PUT, DELETE)
 ● Handling JSON data and request parameters
 ● Writing basic CRUD endpoints (Create, Read, Update, Delete)
 Activities:
 1. Create a Flask API with endpoints for a simple data model (e.g.,
 a "Books" API with title, author, year fields).
 2. Implement CRUD operations to interact with the data model.
 3. Test API endpoints using a tool like Postman or Curl.
 4. Recommended resources: Postman documentation, REST API tutorials
 with Flask


 API endpoints are the URLs that your API clients will use to interact with your application. In Flask, you can define endpoints using route decorators.
## JSON
 JSON stands for JavaScript Object Notation

 JSON is a lightweight format for storing and transporting data

 JSON is often used when data is sent from a server to a web page

 JSON is "self-describing" and easy to understand

## FLASK ROUTE METHODS
 GET - The most common method. A GET message is send, and the server returns data
 POST - Used to send HTML form data to the server. The data received by the POST method is not cached by the server.
 PUT - 	Replace all current representations of the target resource with uploaded content.
 DELETE - Deletes all current representations of the target resource given by the URL.

 step 1: created a dictionary named books and added title, author , year as keys and currosponding answers as values.
 step 2: created a route with('/') with method get to get the book.s details.
 step 3: 