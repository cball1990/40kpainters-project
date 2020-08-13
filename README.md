#40k Painters
The idea behind this project was to create a full stack website which includes eccomerce capabilities using Django.  
The main functionality of the website is to allow customers to research and purchase a painting service for    
thier warhammer armies and then leave reviews of that service.

##UX
The main aim of the website was to give customers the ability to choose a level of painting based  
on the amount of money they would like to spend, to do this I decided to give 3 options for full armies  
and single characters and split these into seperate products. To give more information on each product  
I created a gallery app with pictures and a full description of each service/product, this pairs well with the  
reviews page to give people confidence in thier purchase and choice. Before the user can make a purchase  
they have to log in or create an account, this then gave the ability to have all previous order the user placed  
to be seen on thier account page and also get updates on the order status. For the website owner I added  
a seperate account page where they can see all orders that have been placed and also update the staus of the order  
for the customer to see. I designed the website to be fully responsive on all devices and I have tested  
this on mutliple devices, my desktop pc, my laptop, my mobile and tablet, for the design of the website I  
wanted to go for a simple design with few colours so the user could find what they were looking for   
and could find the information they needed easily. To help me achieve this I used Draw.io to create  
wire frames(included in files on github) and a database schema, I mostly stuck to my original  
design ideas but when it came to the products I changed them completely, my first idea was to have a  
form with different options, for example number of models, I decided that a simpler approach of  
having 6 product to choose from was better because when people pay for this service they either  
have full armies painted or just a single character model so alot of the options I was giving the  
user wasnt needed, This also helped to steamline the purchasing and ordering process. Other design  
changes made where just small tweaks to layouts of the pages to make them more responsive or to  
keep inline with my design goals.

##Features
###Existing Features
The main feature of the website are the ability to view painting options and order what is right for  
you, you can then add a review to give feed back on the service. Once a purchase has been made you  
can follow its progress untill completion on the account page.

###Features for the future
I would of liked to of added a few more features in the future. In the reviews section I would  
add the ability for the review to be add via the accounts page by having a button on each  
order tht would allow you to leave a review on each order placed, this would also allow me to  
ensure only users who had actually made a purchase to leave a review on the product. Another feature  
for the review page would of been to order the reviews by score or date to let users get all  
the information they needed.  
From a design angle having an order confirmation page would of allowed users to see that  
the order had been placed rather then having to navigate to thier account page to see the order.  
The abilty for users to edit the order or leave comments for the painters would of been a usefull  
feature incase of any special requests or changes of address etc. The admin account page would  
benifit from having the ability to only have the most recent orders showing and ordaer that are still  
in progress, I could do this by having a seperate page that had all the completed orders on.  
This could be done by having the orders automatically being hidden once the status is changed to  
completed.

##Technologies Used
####Bootstrap
Used to simplify making the app responsive and other small bits of css such as floats, padding and border rounding.
####Google Fonts
Used to find fonts to use for the text on the webpage.
####HTML
Used to create content on the webpage.
####Javascript and jquery
Javascript was used for styling, such as the gallery aswell as all the code for the stripe API.
####Python
Python was used for all of the backend code.
####Django
Django was used for all the templating and routing of the project aswell as talking to the database. 
####Postgresql
Postgres was the database I used to hold all the information on the users and products etc.  
####Travis  
Travis was used for testing purposes, it is a convinient way to test a django website  
####Stripe  
Stripe handle all the payments on the website  
####Draw.io  
I used draw to create the wire frames for my project

##Testing  
To run tests on my project I used Jarvis, this runs tests everytime you commit to github,  
it also has inbuilt tests it runs aswell as running tests you write yourself. To  
test my site further i did physical tests but going through each feature on different  
devices, this allowed me to find issues such as the collapse navbar not working due  
to a problem with the version on jquery I was using, this was fixed by updating the version  
of jquery I was using. Along with this I asked other people to test out the site because they  
had devices I didn't have such as an Iphone and Ipad.

##Deployment
To deploy this app I used Herouku. To do this I had to add a requirements.txt file and
a Procfile in order for heroku to be able to run the code and get it deployed. In  
development I used dotenv to store my enviroment variables such as the stripe API  
keys and other sensitive information I did not want uploading to github. Heroku gives  
you the ability to add in enviroment variable for the project in the settings. To host  
my static files and media uploads I used aws s3 because heroku clears all file uploads  
daily.
to log into the website owners page to view all orders you just need to enter in  
username - admin, password - Django123. to make a purchase using stripe test card you  
use 4242 4242 4242 4242 as the card number, enter any date thats in the future and and  
3 digit CVV

Credits
Media
Page Logo - Taken from https://www.flaticon.com/authors/freepik and edited to be the right colour.
Images - Various pictures from google image search  

[![Build Status](https://travis-ci.com/cball1990/40kpainters-project.svg?branch=master)](https://travis-ci.com/cball1990/40kpainters-project)  
