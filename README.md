# Bookmania- Book reviews application

Stream Three Project: Data Centric Development - Milestone Project

![alt text](https://github.com/chris92vr/book-mania/blob/master/project-documentation/images/bookmania.jpg "bookmania")


Project consists of the following sections:

1. Homepage - Containing 'sign up' and 'sign in' button when user is not authenticated and 'All Reviews', 'Add Book' buttons when user is logged into his / her account. A slider shows the last 5 books added

2. Login form - Page containing the form that enables user to log into their account to use the app.

3. Sign up form - Page containing the form that enables user to sign up for the Booksy app.
 
4. Collection - Page displaying list of paginated reviews.

5. Add review - Page containing the form that enables users to input and submit their book reviews. 

6. Edit review - Page containing the form that pulls a given review that was previously submitted by a user. User is able to amend information and resubmit the review.

7. View review - Page that contains all information about a given book, including review and description. Page enables user to edit/delete review, comments on the review.

8. Profile - Page that contains a 'My Reviews' button to view added reviews, an 'Add Book' button and a 'Delete Account' button to delete the user profile. Below are the statistics of the books and comments added and the number of book reviews viewed.

## Table of Contents

- [Demo](#demo)
- [UX](#ux)
- [Database](#database)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)



## Demo

A live demo is available [here](https://bookmania1.herokuapp.com/ "bookmania").



## UX

### Users stories

- As a user I would like to be able to add my own book reviews and share them with other users.

- As a user I would like to create an account to access reviews available in the app

- As a user I would like to be able to delete my account and all content added by me at any point.

- As a user I would like to have an option to login and logout of my account so nobody else can access it.

- As a user I would like to explore different books.

- As a user I would like to be able to go back to the top of the page.

- As a user I would like to be able to go back to any review added by me and edit information about it.

- As a user I would like to be able to delete any content added by me (i.e. reviews, comments).

- As a user I would like to see all collection of reviews in an organised, easy to navigate way.

- As a user I would like to be able to interact with other users and share opinions by comment about various books.

- As a user I would like to see all of my inputs within the app (i.e. comments, reviews, rating) in case I would like to edit or delete them.

- As a user I would like to search any particular book using book title or author.

- As a user I would like to be sure that no other user is able to edit or delete my input.




### Design and colors

#### Fonts:

I used **Gentium Book Basic**, from Google Fonts.


#### Colors:

* ![#8989bb](https://placehold.it/15/8989bb/000000?text=+) #8989bb - used for nav and footer

* ![#f1f1fd](https://placehold.it/15/f1f1fd/000000?text=+) #f1f1fd - background color

* ![#000000](https://placehold.it/15/000000/000000?text=+) black - all the text on the body

* ![#FFFFFF](https://placehold.it/15/FFFFFF/000000?text=+) white - all the text on the nav and footer

* ![#3299ff](https://placehold.it/15/3299ff/000000?text=+) blue - used for buttons and hyperlink text

### Strategy

My goal in the design was to create a simple and intuitive interface to be able to easily access through the various pages of the site.

### Scope

This website is designed for all users who enjoy reading books. A portal in which it is possible to share the books read by attributing an rating and description.
The main purpose is to bring book lovers together in a virtual community where it is possible to discover new and interesting readings that, in case it is possible to buy.

### Wireframes

The following [wireframe](https://github.com/chris92vr/book-mania/tree/master/project-documentation/wireframes)  were created to design the project layout options for large, medium and mobile displays.


## Database

### Database Type

For this project I used  **MongoDB Atlas**.

My database consists of four collections, namely: book, categories, comment, users.

Book collection contains information about each book, person who added it and voting information. Categories collection represents the various genres that can be attributed to books. Comments collection contains comment text, username of person who added it, and id of the book about commented review. Users collection contains information about each user who signed up for the app. 

### Database Design

Picture below presents the database schema outlining structure of each collection and relationship between each collection.

![alt text](https://github.com/chris92vr/book-mania/blob/master/project-documentation/images/bookmaniadb.png "database-schema")

Relationships between collections are as follows:

- book and categories - one to one relationship as one record in book collection can be associated with one record in the categories collection;

- users and book - one to many relationship as one record in user collection can be associated with many records in the book collection;

- book and comment - one to many relationship as one record in book collection can be associated with many records in the comment collection.

- users and comment -  one to many relationship as one record in user collection can be associated with many records in the comment collection;


## Features

### Existing Features

#### Buttons

- **All Reviews button** - buttons that redirects user from the homepage to the paginated collection page;

- **View review button** - button that is linked to the view review page;

- **Buy button** - link redirecting a user to amazon search for a given review;

- **Edit / Delete buttons** - buttons that enable editing and deleting reviews and comments;

- **My Reviews buttons** - button that redirects user to the own paginated collection page;

- **Delete account button** - button that performs action of deleting an account and all votes, comments and reviews associated with it;

- **Delete comment buttons** - button that delete a comment;

- **Add review button** - button that submits the new review into the mongoDB database;

- **Update review button** - button that submits the updated review in to the mongoDB database;

- **Back to top button** - dynamic back to top button  so user can go back to the top of the page without scrolling back.


#### Forms

- **Register form** - flask register form that enables user to use the app. User input includes username, email address, and password;

- **Log in form** - flask login form that enables user to sig into the user account;

- **Post comment form** - form that enables user to post a comment for a given review;

- **Add review form** - form that enables user to add a new review to the website;

- **Edit review form** - form that pulls information about the existing review and enables the user to edit it;

#### Structure

- **Navbar** - the navbar stays collapsed on medium and small devices. To create Materialize mobile collapsed button `class=sidenav-trigger` was applied. The navbar contains links to associated sections i.e. Home, All Reviews, Add Book, Profile, Log Out;

- **Footer** - contains disclaimer GitHub link;

#### Other

- **Pagination** - `flask_paginate` extension used to paginate book reviews, so users view 6 reviews per page;

- **Search bar** - search bar that enables users to search any book by  title and author.



### Features left to implement



## Technologies used

### Programming languages

- **HTML** - the project used HTML to define structure and layout of the web page;

- **CSS** - the project used CSS stylesheets to specify style of the web document elements;

- **JavaScript** - the project used JavaScript to implement Maps JavaScript API and customize it.

- **Python** - the project back-end functions are written using Python. Flask and Python is used to build route functions;

### Libraries

- [jQuery](https://code.jquery.com/jquery-3.5.1.min.js) - used to initialize elements of Materialize framework, to manage spinner overlay (fade out), search bar (submit input on enter), back to top button (smooth scroll), comment counter (re-count comments), and deletion confirmation (with ajax);

- [Google Fonts](https://fonts.google.com/) - Google Fonts library was used to set up font type for the document;

### Frameworks & Extensions

- [Materialize](https://materializecss.com/) - responsive CSS framework based on Material Design by Google. Materialize was used to create grid layout and to style various features such as cards, accordion, buttons, forms, navbar, and footer.

- [Flask](http://flask.palletsprojects.com/en/1.1.x/) - web application framework used to create functions with Python that are injected into html templates. Various flask extensions were used to validate login / register form, create routes, paginate reviews, manage login and logout and create toast messages;

- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) - flask extension used for flexible forms validation;

- [Flask-paginate](https://pythonhosted.org/Flask-paginate/) - flask extension used to paginate reviews;

- [Flask-login](https://flask-login.readthedocs.io/en/latest/) - flask extension used to handle the common tasks of logging in, logging out, and remembering users’ sessions;



### Database

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - a fully-managed cloud database used to store manage and query datasets;

### Other

- [Am I Responsive](http://ami.responsivedesign.is/#) - Online tool was used to display the project on various devices;

- [Balsamiq](https://balsamiq.com/) - Software that was used to create wireframes;

- [DBDiagram](https://dbdiagram.io/home) - A relational database diagram design tool used to create database schema.

## Testing

### Code validation

In order to to check the validity of the website code, I have used the following:

    - HTML Validation: https://validator.w3.org/ - no errors identified.
    - CSS Validation: https://jigsaw.w3.org/css-validator/ - Identified issues with materializecss not with my project.
    - PYTHON Validation: https://pep8online.com/ no errors identified.


### Functionality Test

All the features were tested manually throughout the application development process. Table below outlines all features and tests performed on them, as well as all resolved and remaining bugs associated with tested features.


Category | Description | Expected Outcome | Pass/Fail
| ---| ---|:-----------------------------------------:| :---: | 
|Buttons (including anchor links)| Register| The browser navigates to the Register page| pass
|| Login | The browser navigates to the Login page| pass
|| All Reviews |The browser navigates to the All reviews added | pass
|| Add Book| The browser navigates to the Add Book page| pass
|| Buy book | generate Amazon link of the book in a new tab | pass
| | Edit Book | The browser navigates to the Edit Book page | pass
| | Delete Book| Delete the book after confirming | pass
| | View Review | The browser navigates to the Book Review page | pass
| | Back to the Top (Arrow up icon)) | The browser goes back to the top of the page | pass
|Forms| Register | Input fields must be validated and not empty. the data entered is correctly saved in the database with the encrypted password field | pass
| | Login | A user can login only wit the right username and password | pass
| | Add book | Input fields must be validated and not empty. the data entered is correctly saved in the database | pass
| | Edit Book | Input fields must be validated and not empty. the data entered is correctly saved in the database | pass
|Structure| Navbar | All navbar menu items redirect user to the appropriate page, collapses on smaller devices | pass
| | Footer | All footer menu items redirect user to the appropriate page | pass
|Other| Pagination | Limit viewing reviews to 6 per page | pass
| | search bar | Search for books in the database based on author name and title | pass


### Responsiveness testing

Several tests were carried out to verify the correct functioning of the project with positive results.
The functionality of the site is optimal. Browser compatibility is verified for Firefox and Chrome on Windows 10 home; Firefox, Chrome on Ubuntu 19.10 and Firefox, Chome on Android 10. The responsiveness of the pages is suitable on desktop screens, tablets and mobile phones.
In the folder [project-documentation/testing](https://github.com/chris92vr/book-mania/blob/master/project-documentation/testing/ "testing"), there are screenshots named in the following format: (screen resolution) - Operating system (browser) - screen description.


## Deployment

### GitHub

The site was developed using Gitpod IDE. 

To initialize the local repository the command `$ git init` was used. After adding initial files and committing them `$ git remote add origin 'GitHub repo name'` command was used to add new remote repository. Code was then pushed to the master branch of the remote repository using `$ git push -u origin master`.

In order to track the changes in the local repository the following steps were taken:

- command `$ git add 'filename'` - to update what will be committed;

- command `$ git commit` - to commit the changes.

Using `$ git push` command all changes from the local repository were pushed to the remote one on GitHub.

### Heroku

This project is hosted using Heroku, deployed directly from the `master` branch. 

To deploy my project I followed these steps:

1. Create App: 

     - On Heroku website I logged onto my account and created [my app](https://dashboard.heroku.com/apps/bookmania1);
     - Under the **Settings** tab I clicked button **Reveal Config Vars** and I set the IP to 0.0.0.0 and the PORT to 5000;
     - At the later stage configuration for the MongoDB database were added, namely 'MONGO URI' and 'SECRET KEY';

2. Install the Heroku CLI: 

     - To install Heroku CLI I typed `$ sudo snap install --classic heroku` command into the terminal; 
     - In order to log in to the Heroku account I typed `$ heroku login` command into the terminal;

3. Git repository:

     - If repository not created already the following commands should be used in order to initialize a git repository in a new or existing directory: 
        ```
        $ cd 'directory-name'/
        $ git init
        $ heroku git:remote -a 'app-name''
        ```
        
    - For existing repositories add the Heroku remote should be used: `$ heroku git:remote -a 'app-name'`;

4. Requirements:

    - In order to run the app Heroku needs to install the required dependencies so make sure that 'requirements.txt' file was created and committed;
    - In order to create 'requirements.txt' file run `$ sudo pip3 freeze --local > requirements.txt` command in the terminal;

5. Procfile:

    - Procfile is a Heroku specific type of file that tells Heroku how to run our project;
    - For the 'Procfile' run `$ echo web: python > Procfile` command in the terminal;
    - In order to start web processes run `heroku ps:scale web=1` command in the terminal;

5. Deployment: Committed code was deployed to Heroku using the following command: `$ git push heroku master`.

           
## Credits

### Content

- **Flask-WTF**, introduction to Flask-WTF from youtube channel [Pretty Printed](https://www.youtube.com/watch?v=vzaXBm-ZVOQ)

- **Replace a string with linebreaks in Jinja2**, [Link](https://stackoverflow.com/questions/41006119/how-to-replace-a-string-with-linebreaks-in-jinja2)

## Author

**Christian Garofoli** 

### Acknowledgements

Thanks to my mentor **Brian Macharia** for support and advice throughout the project.






