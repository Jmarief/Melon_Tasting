# Melon Tasting Reservation App

Melon Tasting Reservation Scheduler
							
Project Summary:

Melon Tasting is a web application that allows users to create an account and make reservations at Melon Tasting. 

Melon Tasting offers coverage 24/7/365 (including weekends and holidays) but due to the current CDC guidlines and regulations at this time only 1 user can book an reservation on a given day and time. 			

Features:

- Users can create an account using their email address, username and unique password. 
- Registered users once logged in can reserve a date and time they would like to Melon Taste. 
- If the preferred date and time are already booked the user will be prompted to select a new date and time to reserve. 
- Users also have the ability to view all of their past and pending reservations.

Technologies and Stack:

Backend - Python, Flask, Jinja, SQLAlchemy, PostgreSQL and Faker
Frontend - HTML and CSS

Set-Up and Install:

1) Install VS code
2) Install Python3
3) Install pip3 requirements.txt 
4) Install postgresSQL

Clone GitHub Repository 

						
INSTRUCTIONS: 
Details
We are intentionally not dictating what technical requirements you should use. You will need some kind of database (to persist the user and appointment information), a backend server, and frontend.
If you are familiar with a date library, such as Python's datetime or Node/Express's moment or date-fns , feel free to use that. You can assume all timestamps are in the same timezone (no timezone handling required).
For the frontend, you can use plain HTML (by itself or alongside Vanilla Javascript) or a library such as React to build a single page app. 	
If you are less familiar with these libraries, no problem! Use what you are comfortable with. 							
The application should be easy to use but CSS and styling should not be a priority. Feel free to use a front-end framework or UI library such as Bootstrap or Material UI to help with this, but built-in HTML elements are totally fine as well. You can assume the user will have a modern web browser with no major browser compatibility issues.			
You do not need to handle user sign up – you can create one or more test users in your database. If you write a seed file, please include it in the final submission. If you need sample user data to get started, you can use https://jsonplaceholder.typicode.com/users or a tool like Faker. 
There is no need to implement login using passwords – you can assume a user can just log in using their username or email. If you do want to build password authentication as a bonus feature, you can use a library if that is helpful.
Your server should preserve data across restarts (in other words you should persist information in some kind of database or other permanent storage space). 		
Feel free to add any extra features, validations, or error handling if you have time. If you do add extra things, do make sure you mention them in your README.						
Submission						
Please push your code to Github (can be a public repository). To submit, you can post a link to the finished Github repository in your personal Discord channel.		
In addition to your source code, README, and dependencies files (like requirements.txt or package.json), you may include other files like helper scripts or unit tests. However, these additional files are NOT required.					

Deployment
You should deploy your finished site and send us a link.

 We recommend a service like Heroku for ease of deployment. You do not need a custom domain. If you do use Heroku, the free Hobby Dev plan for the database will be sufficient.

Time					
This exercise is intended to take less than a day (4-6 hours). Please spend no more than 6 hours total, including finalizing and sending your submission.
If you don't get around to everything you'd like to do, describe in your README or add TODO comments to indicate what you'd like to add/change given more time. 
But do not spend more than 6 hours – at that point please submit what you have done.
