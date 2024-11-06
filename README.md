# Task_report
 6 day report of task completed each day


 #Day 3: Understanding the Internet (Start to Backend)
 ● __Objective__: Learn how the Internet works, covering fundamental
 concepts from client requests to server responses.
 Topics to Cover:
 ● Basic Internet architecture (IP, DNS, HTTP/HTTPS)
 ● Understanding client-server model
 ● HTTP methods (GET, POST, PUT, DELETE)
 ● Overview of APIs and RESTful services
 ● Overview of backends, servers, and databases
 ##Activities:
 1. Study HTTP request and response structures using your browser's
 developer tools.
 2. Explore REST APIs like JSONPlaceholder to understand GET/POST
 requests.
 3. Create simple HTTP requests using Python’s requests library.
 4. Recommended resources: MDN Web Docs (on HTTP and APIs),
 freeCodeCamp tutorials


##What is internet and how it works
between two machines or computers, to make communication between them possible, there are probably about a dozen other computers bridging the gap. Collectively, all the world's linked-up computers are called the Internet.
The Internet is a worldwide network of computers, linked mostly by telephone lines; the Web is just one of many things (called applications) that can run on the Internet. When you send an email, you're using the Internet: the Net sends the words you write over telephone lines to your friends. When you chat to someone online, you're most likely using the Internet too—because it's the Net that swaps your messages back and forth. But when you update a blog or Google for information to help you write a report, you're using the Web over the Net. You can read more in our article about how the Internet works.
Most data moves over the Internet in a completely different way called packet switching. Suppose you send an email to someone in China. Instead of opening up a long and convoluted circuit between your home and China and sending your email down it all in one go, the email is broken up into tiny pieces called packets. Each one is tagged with its ultimate destination and allowed to travel separately. In theory, all the packets could travel by totally different routes. When they reach their ultimate destination, they are reassembled to make an email again.

###Circuit and Packet switching
__circuit switching__ means when a connection is made between two machines. nothing else happens as long as the connection is live. for example, for telephone call circuit switching is used in the earlier days and the problem with that was that no-one is allowed to make contact with either of the clients as long as the they are on call.
__packet switching__ means the message is broken into tiny packages and is then sent with the destination to where it should end. at the destination the packages are combined in the original. email is an example for packet switching.

###Clients and Servers
There are hundreds of millions of computers on the Net, but they don't all do exactly the same thing. Some of them are like electronic filing cabinets that simply store information and pass it on when requested. These machines are called servers. Machines that hold ordinary documents are called file servers; ones that hold people's mail are called mail servers; and the ones that hold Web pages are Web servers. There are tens of millions of servers on the Internet.

A computer that gets information from a server is called a __client__. When your computer connects over the Internet to a mail server at your ISP (Internet Service Provider) so you can read your messages, your computer is the client and the ISP computer is the server. 

Apart from clients and servers, the Internet is also made up of intermediate computers called __routers__, whose job is really just to make connections between different systems. If you have several computers at home or school, you probably have a single router that connects them all to the Internet. The router is like the mailbox on the end of your street: it's your single point of entry to the worldwide network.

###TCP/IP and DNS
__Internet Protocol (IP)__ is simply the Internet's addressing system. All the machines on the Internet are identified by an Internet Protocol (IP) address that takes the form of a series of digits separated by dots or colons. If all the machines have numeric addresses, every machine knows exactly how (and where) to contact every other machine. When it comes to websites, we usually refer to them by easy-to-remember names (like www.explainthatstuff.com) rather than their actual IP addresses—and there's a relatively simple system called __DNS__ (Domain Name System) that enables a computer to look up the IP address for any given website. In the original version of IP, known as IPv4, addresses consisted of four pairs of digits, such as 12.34.56.78 or 123.255.212.55, but the rapid growth in Internet use meant that all possible addresses were used up by January 2011. That has prompted the introduction of a new IP system with more addresses, which is known as IPv6, where each address is much longer and looks something like this: 123a:b716:7291:0da2:912c:0321:0ffe:1da2.
The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources.
In order to communicate, we need our data to be encapsulated as Internet Protocol (IP) packets. These IP packets travel across number of hosts in a network through routing to reach the destination.

The other part of the control system, Transmission Control Protocol (TCP), sorts out how packets of data move back and forth between one computer (in other words, one IP address) and another. It's TCP that figures out how to get the data from the source to the destination, arranging for it to be broken into packets, transmitted, resent if they get lost, and reassembled into the correct order at the other end.

###Http 
The web server delivers the desired data to the user in the form of web pages when the user initiates an HTTP request through their browser. Above the TCP layer lies an application layer protocol called HTTP. It has given web browsers and servers certain standard principles that they can use to talk to one another.
Because each transaction on the HTTP protocol is carried out independently of the others and without reference to the history, the connection between the web browser and the server ends after the transaction is finished. This makes HTTP a stateless protocol.
###Https
While HTTPS guarantees data security, the HTTP protocol does not provide data security.
As a result, HTTPS can be defined as a secure variant of the HTTP protocol. Data can be transferred using this protocol in an encrypted format.
In most cases, the HTTPS protocol must be used while entering bank account information.
The HTTPS protocol is mostly utilised in situations when entering login credentials is necessary. Modern browsers like Chrome distinguish between the HTTP and HTTPS protocols based on distinct markings.
HTTPS employs an encryption mechanism called Secure Sockets Layer (SSL), also known as Transport Layer Security, to enable encryption.  
It forms the basis for how web pages communicate from the web server to the client’s browser.
###HTPPS Methods
GET, POST, PUT, PATCH, and DELETE are the most commonly used and form the foundation of communication between clients and servers over the HTTP protocol. These methods define the actions that can be performed on a resource identified by a URL during client-server communication over the World Wide Web.
__GET__: for retrieving. Parameters for GET requests are usually passed in the URL, and they can be appended to the end of the URL in the form of a query string. For example, you can use a GET request to obtain information about a specific user: https://api.example.com/users?id=123. The server will return the corresponding user information based on the parameter's value.
__POST__: POST Method is a commonly used HTTP method for sending data to an API. Unlike the PUT and DELETE methods, POST is typically used to create new resources and does not require the client to provide a complete representation of the resource.
__PUT__: The PUT method is used to update or replace an existing resource on the server. It requires the client to send the complete representation of the resource to be updated.
__DELETE__: The DELETE method is an HTTP method used to remove or delete a resource from a server. It is commonly used to instruct the server to delete a specific resource identified by the provided URL or resource identifier.
__PATCH__: used to request a set of modifications in the request entity to be applied for the resource recognized by the Request-URI. 

##API
An API (Application Programming Interface) is a set of features and rules that exist inside a software program (the application) enabling interaction with it through software - as opposed to a human user interface. The API can be seen as a simple contract (the interface) between the application offering it and other items, such as third-party software or hardware.
You can think of a web API as a gateway between clients and resources on the web.

__Clients__
Clients are users who want to access information from the web. The client can be a person or a software system that uses the API. For example, developers can write programs that access weather data from a weather system. Or you can access the same data from your browser when you visit the weather website directly.


__Resources__
Resources are the information that different applications provide to their clients. Resources can be images, videos, text, numbers, or any type of data. The machine that gives the resource to the client is also called the server. Organizations use APIs to share resources and provide web services while maintaining security, control, and authentication. In addition, APIs help them to determine which clients get access to specific internal resources.

###RESTful API
It is an interface that two computer systems use to exchange information securely over the internet. Most business applications have to communicate with other internal and third-party applications to perform various tasks. For example, to generate monthly payslips, your internal accounts system has to share data with your customer's banking system to automate invoicing and communicate with an internal timesheet application. RESTful APIs support this information exchange because they follow secure, reliable, and efficient software communication standards.
API developers can design APIs using several different architectures. APIs that follow the REST architectural style are called REST APIs. Web services that implement REST architecture are called RESTful web services. The term RESTful API generally refers to RESTful web APIs. However, you can use the terms REST API and RESTful API interchangeably.

##Backend
The back end is a combination of servers and databases. Servers control how users access files. Databases are organized and structured collections of data.
an example: When you log into a website and enter your username or email and password. This information is sent to the server-side software which validates the structure of your email and password. If everything looks good, it checks the data with the database to ensure someone with that username and password exists. If it does, the database will log you in and sends information back to you in the form of your user page.


##__ACTIVITIES__

step 1: Open browser Developer Tools with Ctrl + Shift + I and select the Network tab, I opened a website to observe the process. When a client searches for something, an HTTP request is sent to the server, which responds with HTML and other resources(CSS, JavaScript, images..etc) needed to render the page. This process loads the web page in the browser, displaying the final output to the user. created an account in a website and saw that the method is post
step 2: Opened jasonplaceholder to learn how to use get, post, put, delete commands
step 3: installed requests library. imported it to jupyter notebook. used simple html request functions to get the raw html data that is not yet rendered.

###REFERENCES: google, MDN Web Docs, AWS, JASONPlaceholder