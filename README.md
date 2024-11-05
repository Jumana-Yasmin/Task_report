# Task_report
 6 day report of task completed eachday


#Day 2: Data Science Basics
 ● __Objective__: Understand foundational data science concepts,
 including data processing, visualization, and basic statistical
 analysis.
 ##Topics to Cover:
 ● Overview of data science and the data science pipeline
 ● Types of data (structured, unstructured)
 ● Basic statistics (mean, median, mode, standard deviation)
 ● Data wrangling and cleaning
 ● Introduction to data visualization
 ##Activities:
 1. Use Python libraries (like Pandas and Matplotlib) to load, clean,
 and visualize a simple dataset.
 2. Calculate basic statistics on the dataset.
 3. Practice creating different types of visualizations (histograms,
 line plots, scatter plots).
 4. Recommended resources: Pandas, NumPy, and Matplotlib
 documentation, beginner-level DataCamp courses.


##__DATA SCIENCE__
data science is a set of methodologies for taking in thousands of forms of data that are available to us today, and using them to draw meaningful conclusions. Data is being collected all around us. Every like, click, email, credit card swipe, or tweet is a new piece of data that can be used to better describe the present or predict the future.
###__Data Science workflow__
in data science, we generally have four steps to any project. First, we collect data from many sources, such as surveys, web traffic results, geo-tagged social media posts, and financial transactions. Once collected, we store that data in a safe and accessible way.
Then, we explore and visualize the cleaned data. This could involve building dashboards to track how the data changes over time or performing comparisons between two sets of data.
Finally, we run experiments and predictions on the data. For example, this could involve building a system that forecasts temperature changes or performing a test to find which web page acquires more customers.
###__Internet of Things (IoT)__
The Internet of Things also known as IoT, which is often combined with Data Science. IoT refers to gadgets that are not standard computers, but still have the ability to transmit data. This includes smart watches, internet-connected home security systems, electronic toll collection systems, building energy management systems, and much, much more.

###__Deep Learning__
In deep learning, multiple layers of mini-algorithms, called "neurons", work together to draw complex conclusions. Deep learning takes much, much more training data than a traditional machine learning model, but is also able to learn relationships that traditional models cannot. Deep learning is used to solve data-intensive problems, such as image classification or language understanding.
for example, in self driving cars image recognition is necessary.We could express the picture as a matrix of numbers where each number represents a pixel. However, this approach would probably fail if we fed the matrix into a traditional machine learning model. There's simply too much input data. so deep learning is used.

###Quantitative vs qualitative data__
There are two general types of data: qualitative and quantitative data. It’s important to understand the key differences between both. Quantitative data can be counted, measured, and expressed using numbers. Qualitative data is descriptive and conceptual. Qualitative data can be observed but not measured.

###__Structured vs Unstructured data
Structured data, as it sounds, is the most organized form of data, designed for easy storage, access, and analysis. This data type is typically formatted into predefined rows and columns, making it highly searchable and easily organized within databases or spreadsheets. Each element in structured data is addressable, which means it can be precisely defined and easily grouped or related to other elements. Typically, structured data is housed in relational database management systems, which allows for complex querying and analysis using SQL. 
Unstructured data represents the largest category of data, and it’s growing exponentially as more digital content is created. Unlike structured data, unstructured data doesn’t follow a specific format or schema, which makes it more challenging to store and analyze. 
This type of data comes from a wide variety of sources, including emails, social media content, and multimedia files. Due to its lack of structure, unstructured data cannot be stored in traditional row-column databases and often requires more advanced storage solutions like data lakes. 

Mean: Average of the data
Median: Mid value
Mode: Repeated value
Standard Deviation: Measure of how spread out the values in a data set are around the mean (average)

Data cleaning focuses on removing inaccurate data from your data set.
Data wrangling involves transforming the data’s format, typically converting “raw” data into another format more suitable for use.
Data Visualisation is the graphical representation of data, to understand the data clearly or to make meaningfull insights.

#__ACTIVITY REPORT__
Step 1:Downloaded a user behaviour dataset from google containing informations about mobile usage.it contains user id, device model, os, app usage, screen on time, battery drain, no. of apps installed, data usage, age, gender and user behaviour class columns. there are 700 entries.
Step 2: Opened jupyter notebook and imported necessary libraries such as numpy, pandas, matplotlib and .
Step 3: Imported the downloaded csv file to jupyter notebook.
Step 4:checked for null values(there wasn't any)
Step 5: used the describe() function to find the total count, mean, std, min, first quartile, second quartile, third quartile and maximum values.
Step 6: Checked for duplicates(there wasn't any).
Step 7: plotted a graph showing the total number of users using the operating system(Android/Ios). made the conclusion that more than 500 people use Android and less than 200 people use Ios.81% of users use Android and 19% of users uses ios
Step 8: plotted a histogram showing the distribution of battery drain. came to the conclusion that 100+ devices have low battery drain and 65 devices have the highest battery life.this suggest that 80% of devices have moderate battery life and 20% devices have high battery drain.
Step 9 : plotted a histogram showing the distribution of app usage time. the conclusion made is that almost 120 spend less than 100 usage minutes per day. 58 users spend 600 minutes per day on apps. this suggests that 70% of users spend less time on apps.
Step 10: plotted a boxplot of device models battery drain and got the conclusion that oneplus9 and iphone12 have the highest battery drain. google pixel 5 and samsung galaxy s21 has the lowest battery  drain.
Step 11: plotted a scatterplot of people using screen time usage according to age.
Step 12: plotted a line plot visualizing the battery drain across diff ages, with seperate line for each gender. the code groups the dataset by 'Age' and 'Gender'.  calculates the mean values for app usage time, screen-on time, and battery drain for each group and then the graph is plotted using the data.



##REFERENCES: free DataCamp course