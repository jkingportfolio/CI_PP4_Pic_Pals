# pic-pals
Developer: Jamie King

![Mockup image](docs/images/features/landing-page.png)

The Pic Pals Social website has been developed to provide users the chance to post images online and have the ability to view other users posts also. 

[View live website](https://pic-pals-pp4.herokuapp.com/)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
3. [Technical Design](#technical-design)
    1. [Colours](#colours)
    2. [Fonts](#fonts)
    3. [Structure](#structure)
    4. [Database](#database)
    5. [Data Models](#data-models)
    6. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
    1. [Coding Languages](#coding-languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
    3. [Libraries](#libraries)
5. [Features](#features)
6. [Validation](#validation)
    1. [HTML](#html-validation)
    2. [CSS](#css-validation)
    3. [Javascript](#javascript-validation)
    4. [Python](#python-validation)
    5. [Chrome Dev Tools Lighthouse](#chrome-dev-tools-lighthouse-validation)
    6. [WAVE Validation](#wave-validation)
7. [Testing](#testing)
    1. [Device Testing](#device-testing)
    2. [Browser Compatibility](#browser-compatibility)
    3. [Manual Testing](#manual-testing)
    4. [Automated Testing](#automated-testing)
8. [Bugs](#bugs)
9. [Configuration](#configuration)
    1. [Google emails](#google-emails)
10. [Deployment](#deployment)
11. [Credits](#credits)
    1. [Tutorial](#tutorials)
    2. [Code](#code)
    3. [Literature](#literature)
    4. [Misc](#misc)
12. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- To be able to share pictures on the pic pals site
- To be able to comment on other users posts
- To be able to use CRUD functionality whilst logged onto the site 

### Site Owner Goals

- To provide a platform in which users can share pictures
- To provide an enjoyable user experience which would make users wish to return to the site
- To have the ability to be given feedback via a contact form
- To have the ability to connect with site users via GitHub and LinkedIn via links in the sites footer

## User Experience

### Target Audience

- People who enjoy photography and would like to share their images
- People who enjoy photography and would like to view other peoples images
- People who wish to find an easy way to share images with family and friends
- People who are looking for a way to interact with other people over the internet

### User Requirements and Expectations

- A great site which provides a high level of interactiveness between users
- Links and functions to act as expected
- Notification to provide feedback on expected function outcomes
- Simple "to the point" content that a user can easily digest
- Accessibility for impaired users
- Responsiveness to allow pleasant use across devices of different screen sizes 

### User stories

1. As a user, I want to use the navigation bar so that i can seamlessly navigate around the app.
2. As a user, I want to see a visual indicators for example of having liked a post / followed a user so that i can tell if I have previously like that post.
3. As a user, I want to like and unlike posts so that *i can show my appreciation of another users post.
4. As a user, I want to delete my posts so that i can permanently remove posts I do not wish to keep
5. As a user, I want to edit my posts so that i can correct spelling mistakes or I may have enter into the post caption.
6. As a user, I want to view post comments so that i can fulfill the aim of the app
7. As a user, I want to comment on other posts so that i can interact with other users
8. As a user, I want to manage my posts so that i can add, edit or delete posts as needed.
9. As a user, I want to request a password so that i can log back into my account if i have forgotten my password.
10. As a user, I want to log in so that i can access my account, view my profile, pictures and other users pictures.
11. As a user, I want to log out so that other users using the same device cannot access my account.
12. As a new user, I want to register an account with Pic Pals so that i can become a member and use the app as intended.
13. As a user, I want to change my password so that i can secure my account.
14. As a user, I want to have a profile page so that I and other users can view my list of posts
15. As a user, I want to update my profile so that my profile can stay up to date with my latest information.
16. As a user, I want to add a profile picture so that my followers can easily recognize my posts or comments
17. As a user, I want to view the Home Page so that i can understand what the website is about, create an account or log in.
18. As a user, I want to view how many likes a post has so that i can gauge how popular a post is
19. As a user, I want to add a bio to my profile page so that other members can learn more about me
20. As a user, I want to follow other accounts so that i can view their posts on my feed
21. As a user, I want to fill in a help form so that i can enquire about issues I may have regarding the app
22. As a user, I want to change my email address so that i can maintain the same account if I change email address
23. As a user, I want to receive feedback so that i can confirm the help form submission was successful or not.
24. As a user, I want to scroll through the latest images on my feed so that i can keep up to date with accounts I follow
25. As a user, I want to browse my list of followed accounts so that i can view that particular user account
26. As a user, I want to see a visual indicator of following an account so that i can tell if I currently follow that account.



### Site Owner Stories

27. As the site owner, I would want to validate users data entries on sign up **so that users can create a log in which meets the requirements.
28. As the site owner, I would want to ensure only logged in users can post from their account and edit their profile so that data privacy is ensured.
29. As the site owner, I would want to have the ability to remove posts so that i can keep the app clean and friendly
30. As the site owner, I would want the site to be fully responsive so that user can use it across multiple devices and create a good user experience.
31. As the site owner, I would want to use the app search function so that i can search for particular posts by hashtags or search for users by their user name.
32. As the site owner, I would want 404 and 500 error pages so that users do not have to use the back navigation button if an error occurs.



## Technical Design

### Colours

The colour scheme used in this project was chosen with simplicity in mind. The colour scheme is used through out all pages to ensure contrast readability and an overall good user experience. 

!!! DECIDE ON A COLOUR PALETTE !!!

<details>
<summary>Colour Palete</summary>
<img src="docs/colours/colour-palette.png">
</details>

### Fonts

Google fonts was used to decided on the font for the website. 'Do Hyeon' with a back up of sans-serif was decided as the ideal font for the site.

### Structure

#### Web pages

User experience was one of the main driving factors in this project. A simple, clear and easy to navigate app was the desired outcome. To acheive this at the top of each page is a Nav Bar with links to the right hand side or in the form of a hamburger toggle button if using a small screen device in which all links will be listed vertically. At the bottom of each page the developers social links can be found to allow further networking with users of the site.

The site consists of the following sections:
- Home page in which a logged in user will be displayed their profile and if no user is logged in will display the log in form, reset password and register a new account buttons
- Reset Password page where a user can request a link to reset their password
- Register page where new users can register an acocunt with pic pals
- My Profile page where a logged in user can view all their posts, edit their profile, change their password and view stats on their followers and accounts followed.
- My posts where a list of all currently logged in users posts will be displayed as cards
- Feed page where posts of all currently "followed" accounts will be show, posts will be displayed in order by date of most recent.
- People page where a list of all current pic pal users can be found along with  a search bar to search for profile.
- Contact where users can contact the site admin by filling out the form displayed on the page
- Post detail page where a more in depth view of a post will be shown, this will include a like button, like count and comments section. Also if the current user owns the post they will have additional options to edit the caption or delete the post.
- Contact page with a contact form which allows users to create a contact object in which the admin can view on the django admin dashboard
- Add post page where a logged in user can create a new post
- Edit profile page where a logged in user can edit information in the form which will update their profile information on save
- Change Password page where a logged in user can change their password
- Reset Password page where a user can request a one time email to reset their password if they have forgotten it (please refer to known bugs regarding this page)

#### Database

The site uses a backend database built with the Django framework and the use of ElephantSQL Postgres for the deployed site.

<details>
<summary>Database diagram</summary>
<img src="docs/database/database-diagram.png">
</details>

The following data models were created to represent the database model structure for the site.

#### Data Models

#### User Model

The User model contains information about the user. It is part of the built in Django allauth library

#### Profile Model

The Profile model object contains additional information on the user and consist of the following fields
- user (AUTH_USER_MODEL)
- date_of_birth (DateField)
- profile_pic (CloudinaryField)
- bio (Charfield)

#### Follow Model

The Follow model object represents a follow connection between users which is not symetrical and consists of the following fields
- user (ForeignKey - auth.User)
- followed_account (ForeignKey - auth.User)
- created (DateTimeField)

#### Post Model

The Post model object represents a users post and consists of the following fields
- id (UUIDFiel)
- created_date (DateTimeField)
- user (ForeignKey)
- image (CloudinaryField)
- caption (TextField)
- caption_edited (BooleanField)
- caption_edited_time (DateTimeField)
- likes (IntegerField)

#### Like Model

The Like model object represents a user has liked an individual post contains and consists of the following fields
- user (ForeignKey - User)
- post (Foreign Key - Post)

#### Comment Model

The Comment model object represents a comment a user has posted on an individual post contains and consists of the following fields
- post (ForeignKey - Post)
- user (ForeignKey - User)
- comment_body (TextField)
- created_on (DateTimeField)
- updated (BooleanField)

#### Contact Model

The Contact model object represents a contact message from the user to the admin and and consists of the following fields
- reason (CharField)
- name - Charfield
- email - EmailField
- message_body (TextField)
- message_date (DateTimeField)

### Wireframes

Balsamiq was used to create wireframes of the sites pages

<details>
<summary>Wireframes</summary>
<img src="docs/wireframes/1.png">
<img src="docs/wireframes/2.png">
<img src="docs/wireframes/3.png">
<img src="docs/wireframes/4.png">
</details>


## Technologies Used

### Coding Languages
- HTML
- CSS
- Python 3
- Javascript

### Frameworks and Tools

- [Django 3.2.16](https://www.djangoproject.com/) - Used to rapidly develop the site.
- [Psycopg2](https://pypi.org/project/psycopg2/) - Used as a PostgreSQL adaptor
- [Gunicorn](https://gunicorn.org/) - Used for being a pure-Python HTTP server for WSGI applications
- [Git](https://git-scm.com/) - Used for version control.
- [GitHub](https://github.com/) - Used to deploy the projects code.
- [Gitpod](https://www.gitpod.io/) - Used to develop and test code.
- [Heroku Platform](https://id.heroku.com/) - Used to deploy the live project.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used to format forms.
- [Am i Responsive](https://ui.dev/amiresponsive) - Used to create a mock up image of the site on different screen sizes.
- [Balsamiq](https://balsamiq.com/) - Used to produce wireframes of the site.
- [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Used to develop the layout of the site.
- [Cloudinary](https://cloudinary.com/) - Used to store post images.
- [Font Awesome](https://fontawesome.com/) - Used to produce icons on the site.
- [Graphviz](https://dreampuf.github.io/GraphvizOnline) - Used to generate pydot file / database diagram image.
- [Google Fonts](https://fonts.google.com/) - Used to import the sites font family.
- [Affinity Designer](https://affinity.serif.com/en-gb/) - Used to create the logo and delete buttons.
- Validation
    - [WC3 Validator](https://validator.w3.org/) - Used to validate the HTML code of the site.
    - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)- Used to validate the CSS of the site.
    - [Jshint](https://jshint.com/) - Used to validate the Javascript of the site.
    - [Pycodestyle](https://pypi.org/project/pycodestyle/) - Used to validate code against Python conventions.
    - [Chrome dev tools (Lighthouse)](https://developer.chrome.com/docs/lighthouse/overview/) - Used to measure site performance, SEO and accessiblity
    - [WAVE Validator](https://wave.webaim.org/) - Used to evaluate site accessibility

## Libraries

### Python Libraries

- os - Used to determine operating system and clear CLI.
- time - Used to create a delay effect.
- datetime - Used to get current time stamp and assign times to orders.
- <> - <>

### Third Party Libraries

- <NAME> - JUSTIFICATION: I used this library to <>.
- <NAME> - JUSTIFICATION: I used this library to <>.
- <NAME> - JUSTIFICATION: I used this library to <>.
- <NAME> - JUSTIFICATION: I used this library to <>.
- <NAME> - JUSTIFICATION: I used this library to <>..


## Features

In its entirety the website consists of a variety of features across the many site pages as listed below.

### Authentication

Authentication is a feature of the Pic Pals site, users will have to be authenticated whilst attempting to log in or else they will not be able to use any functionality of the site or view any information that pic pals users have posted.

<details>
<summary>Authentication image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 28

### Bio-Section

The bio section is an optional feature to appear on a users profile page. A user can chose to write a little bit about themselves if they so desire. The location of the bio section is just above the users posts.

<details>
<summary>Bio section image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 19

### Change Password

The change password feature can be accessed from the current users profile page. A form will prompt the user to enter their current password followed by their new password and a confirmation of the new password.

<details>
<summary>Change password image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 13

### Post comment

The post comment feature can be accessed from any users post detail page, below the post image is a form to enter a comment. The comment will then be posted alongside the users profile picture and username.

<details>
<summary>Post comment image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 6 & 7

### Contact

The contact feature can be found from the nav bar and allows both signed in users and annonymous users to contact the site admin.

<details>
<summary>Contact image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 21

### Create Post

The create post feature can be found from the current logged in users profile page. This will allow a logged in user to post an image to their profile.

<details>
<summary>Create Post image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 8

### Delete Post

The delete post feature can be found above the image on the post detail page of a currently logged in user. The delete post button will only be visible to owners of that post to avoid other users deleting posts they do not own.

<details>
<summary>Delete Post image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 4, 8 & 29

### Edit Post

The edit post feature can be found above the image on the post detail page of a currently logged in user and allows the captoion of the post to be updated. The edit post button will only be visible to owners of that post to avoid other users editing posts they do not own.

<details>
<summary>Edit image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 5 & 8

### Edit Profile

The edit profile feature can be found on the profile page of the current logged in user beside the Add post button. Clicking the edit profile button will redirect to a form in which the user can update their details.

<details>
<summary>Edit Profile image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 15 & 22

### Error Pages

The error pages features will display 400, 403, 404 and 500 error pages and allow the user to easily navigate back to the site.

<details>
<summary>Error Pages image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 32

### Feed

The feed feature can be found from the Nav Bar. The feed feature will display the posts of all followed users by the current user in a list sorted by latest to oldest.

<details>
<summary>Feed image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 24

### Follow / Unfollow user

The follow / unfollow user feature allows users to follow or unfollow other users, if a user is followed their posts will appear in current users feed.

<details>
<summary>Follow / Unfollow user image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 20

### Follow / Unfollow button 

The follow / unfollow user button feature can be found on the profile of any user just below their profile picture. The button text will reflect the current status of the user as FOLLOW or UNFOLLOW.

<details>
<summary>Follow / Unfollow button image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 2 & 26

### Followed List

The followed list feature can be accessed from the currently logged in users profile. This feature will display a list of all users that the current user follows.

<details>
<summary>Followed list image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 25

### Followers List

The followers list feature can be accessed from the currently logged in users profile. This feature will display a list of all users that the current user is followed by.

<details>
<summary>Followers list image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: X ADD USER STORY

### Home Page

The home page feature displays upon initial arrival to the pic pals site and will allow users to log into Pic Pals, Rest password, Register an account and Contact the admin.

<details>
<summary>Home page image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 17

### Input Validation

Input Validation as a feature is used throughout the site for form inputs.

<details>
<summary>Input validation image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 27

### Like count

The like count feature can be found under a post image in the post details page. The total number of likes on the current post will be displayed.

<details>
<summary>Like count image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 18

### Like / Unlike button

The like / unlike button feature can be found under a post image in the post details page. A user can click on the like button and it will add / subtract a like based on the users current like status for that post.

<details>
<summary>Like / Unlike Button image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 2 & 3

### Register

The register feature can be found on the landing page for the site. This feature allows users to register and create an account with pic pals via a form.

<details>
<summary>Register image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 12

### Reset Password

The reset password feature can be found on the landing page for the site. This feature allowed users to be emailed with a one use token to the email registered to their account. *Please note that this feature works on the CLI only, Google Mail times out, please see known bugs.

<details>
<summary>Reset Password image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 9

### Responsiveness

Throughout the site the feature of being responsive for various device sizes can be shown whilst navigating the site.

<details>
<summary>Responsiveness image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 30

### Site Feedback

Site feedback features are presented at various times in the form of Successfull html pages and Django messages.

<details>
<summary>Welcome message image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 23

### User Search

The user search bar feature can be found on the People page of the site. At the top of the People page a search bar can be used to search for users by username.

<details>
<summary>User Search image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: 31

## Validation

### HTML Validation

[W3C Validation](https://validator.w3.org/) was used to validate the HTML code used in the project.

<details>

<summary>HTML file - xxx.html</summary>
<img src="docs/images/validation/w3c.png">

<summary>HTML file - xxxx.html</summary>
<img src="docs/images/validation/w3c.png">

<summary>HTML file - xxx.html</summary>
<img src="docs/images/validation/w3c.png">

<summary>HTML file - xxxx.html</summary>
<img src="docs/images/validation/w3c.png">

</details>

### CSS Validation

[W3C Validation](https://validator.w3.org/) was used to validate the CSSL code used in the project.

<details>
<summary>CSS file - style.css</summary>
<img src="docs/images/validation/style-css.png">
</details>

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the Javascript code used in the app.

<details>
<summary>Javascript file - script.js</summary>
<img src="docs/images/validation/jshint-validation.png">
</details>

### Python Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app.

<details>
<summary>Python file - run.py</summary>
<img src="docs/images/validation/pep8-validation-run.png">
</details>



### Chrome Dev Tools Lighthouse Validation

[Chrome Dev Tools lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to validate the performance of the app.

<details>
<summary>PAGE NAME</summary>
<img src="docs/images/validation/cdtl-page-name.png">
</details>

### WAVE Validation

[WAVE Validation](http://pep8online.com/) was used to validate the accessiblity of the app.

<details>
<summary>PAGE NAMEy</summary>
<img src="docs/images/validation/wave-page-name.png">
</details>

## Testing

### Device Testing

This site was tested on the following devices:
- Windows 10 PC with a 24" MSI Curved gaming monitor
- Raspberry Pi 4 with a 24" MSI Curved gaming monitor

### Browser Compatibility

The website was tested on the following web browsers:
- Google Chrome (Version 108.0.5359.125)
- DuckDuckGo

### Manual Testing

<summary>See Testing User Stories</summary>

#### Testing User Stories Users

To avoid unnecessary repetition of images, only the feature being referred to will have screenshots. Information on how to navigate to the feature referred to will be described within its relevant table reference. 

1. As a user, I want to use the navigation bar so that i can seamlessly navigate around the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Nav Bar  | Log in and scroll to the top of any page  | Nav Bar to be displayed along the top of the page or via a hamburger toggle if on a smaller screen    | Works as expected |

<details>
<summary>Screenshots User Story 1</summary>

<details>
<summary>Feature - Nav Bar</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>



2. As a user, I want to see a visual indicators for example of having liked a post / followed a user so that i can tell if I have previously like that post.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Like Button  | Log in and navigate to a post detail page via feed or a users profile by clicking on the post. Below the post click on the heart icon to like or unlike the post  | Post heart indicator to visually reflect the current users status with regards to liking the post and the total like tally to plus or minus one like dependant on if the click is a like or unlike  | Works as expected |
|  Follow Button  | Log in and navigate to a users profile page via followed users list, following users list or clicking on the users name on a post detail. Below the users profile picute click on the follow button to follow or unfollow the user.  | User to follow or unfollow the account of the currently viewed profile | Works as expected |

<details>
<summary>Screenshots User Story 2</summary>

<details>
<summary>Feature - Like / Follow Button</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

3. As a user, I want to like and unlike posts so that i can show my appreciation of another users post.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Like Button  | Log in and navigate to a post detail page via feed or a users profile by clicking on the post. Below the post click on the heart icon to like or unlike the post  | Post heart indicator to visually reflect the current users status with regards to liking the post and the total like tally to plus or minus one like dependant on if the click is a like or unlike | Works as expected |

<details>
<summary>Screenshots User Story 3</summary>

<details>
<summary>Feature - Like / Unlike Button</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

4. As a user, I want to delete my posts so that i can permanently remove posts I do not wish to keep.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Delete Post  | Log in and navigate to the post detail by clicking on the post in question. At the top of the post card click on the delete button, click ok on the confirmation modal to delete the post. | Post to be deleted | Works as expected |

<details>
<summary>Screenshots User Story 4</summary>

<details>
<summary>Feature - Delete Post</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

5. As a user, I want to edit my posts so that i can correct spelling mistakes or hashtags I may have enter into comments.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Edit Post  | Log in and navigate to the post detail by clicking on the post in question. At the top of the post card click on the edit button, the edit post form will show, update the caption field to the desired caption and click update to save changes and redirect back to the post detail page.  | Caption for the post to be updated | Works as expected |

<details>
<summary>Screenshots User Story 5</summary>

<details>
<summary>Feature - Edit Post</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

6. As a user, I want to view post comments so that i can fulfill the aim of the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Comment on post  | Log in and navigate to a post detail page via feed or a users profile by clicking on the post. Below the post image view the comments.  | User to be able to read all comments on the post or be made aware of no comments if there are none | Works as intended |

<details>
<summary>Screenshots User Story 6</summary>

<details>
<summary>Feature - Comment on post</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

7. As a user, I want to comment on other posts so that i can interact with other users.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Comment on post  | Log in and navigate to a post detail page via feed or a users profile by clicking on the post. Below the post image fill in the comment form and click on the add comment button.  | User to fill in the comment form and when submitted will be added to the comments like for the post. | Works as expected |

<details>
<summary>Screenshots User Story 7</summary>

<details>
<summary>Feature - Comment on post</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

8. As a user, I want to manage my posts so that i can add, edit or delete posts as needed.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Edit Post  | Log in and navigate to the post detail by clicking on the post in question. At the top of the post card click on the edit button, the edit post form will show, update the caption field to the desired caption and click update to save changes and redirect back to the post detail page.  | Caption for the post to be updated    | Works as expected |
|  Delete Post  | Log in and navigate to the post detail by clicking on the post in question. At the top of the post card click on the delete button, click ok on the confirmation modal to delete the post. | Post to be deleted | Works as expected |

<details>
<summary>Screenshots User Story 8</summary>

<details>
<summary>Feature - Edit Post / Delete Post</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

9. As a user, I want to request a password so that i can log back into my account if i have forgotten my password.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Reset Password  | Navigate to the pic pals site and click on the Reset Password button located below the log in section. Fill in the form with the email used when creating your pic pals account and submit the form. Navigate to your email inbox and find the email from Pic Pals. Click on the link which will direct you to a form on pic pals to enter a new password. Confrim the password and submit the form.  | User will reset their password allowing them to log into their account | Works as intended *See known bugs |

<details>
<summary>Screenshots User Story 9</summary>

<details>
<summary>Feature - Reset Password</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

10. As a user, I want to log in so that i can access my account, view my profile, pictures and other users pictures.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Log in  | Naviagte to the pic pals site and from the landing page enter your username and password then click on the log in button.  | User to log in and be redirected to their profile page | Works as expected |

<details>
<summary>Screenshots User Story 10</summary>

<details>
<summary>Feature - Log in</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

11. As a user, I want to log out so that other users using the same device cannot access my account.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Log out  | From any page whilst logged in click on the log out button located in the right hand corner of the nav bar, or if using a small screen device from the last item in the list from the hamburger menu toggle.  | User to log out successfully and be presented with the logged out page | Works as intended |

<details>
<summary>Screenshots User Story 11</summary>

<details>
<summary>Feature - Log out</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

12. As a new user, I want to register an account with Pic Pals so that i can become a member and use the app as intended.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Register  | Navigate to the pic pals site and click on the Sign up button located below the log in section. Fill in the form with the required fields for registration and click on the create account button.  | User to create an account with the information provided in the form    | Works as intended |

<details>
<summary>Screenshots User Story 12</summary>

<details>
<summary>Feature - Register</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

13. As a user, I want to change my password so that i can secure my account.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Change Password  | Log in and navigate to the My profile page by clicking My Profile from the nav bar. Click on the edit profile button located under the Users profile picture. Fill in the form with updated profile detail and click on the update profile button  | Users profile to be updated with the information entered into the edit profile form | Works as expected |

<details>
<summary>Screenshots User Story 13</summary>

<details>
<summary>Feature - Change Password</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

14. As a user, I want to have a profile page so that I and other users can view my list of posts.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Profile Page  | Create an account with Pic Pals or sign in if already a member, navigate to the My Profile page from the Nav Bar  | User to have their own profile on the site | Works as intended |

<details>
<summary>Screenshots User Story 14</summary>

<details>
<summary>Feature - Profile Page</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

15. As a user, I want to update my profile so that my profile can stay up to date with my latest information.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Edit Profile  | Log in and navigate to the My profile page via the nav bar. Click on the Edit profile button located below the users profile picture. The user will then be redirected to the edit profile form, fill out new information as intedned and click on the update profile button   | Users profile information to be updated and saved | Works as intended |

<details>
<summary>Screenshots User Story 15</summary>

<details>
<summary>Feature - Edit profile</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

16. As a user, I want to add a profile picture so that my followers can easily recognize my posts or comments.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Profile Picture  | Sign up with pic pals and whilst entering user information upload a picture to be a profile picture, if no image is selected the static default profile picture will be used. If a user already has an account, log in and navigate to the My Profile page from the nav bar. Click on the edit profile button located below the users profile image. Upload the desired image and click on update profile  | User will have a personally selected image as their profile image | Works as intended |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - Profile Picture</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

17. As a user, I want to view the Home Page so that i can understand what the website is about, create an account or log in.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Home Page  | Navigate to the pic pals landing page  | Users will be presented with a small description of the sites purpose | Works as intended |

<details>
<summary>Screenshots User Story 17</summary>

<details>
<summary>Feature - Home Page</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

18. As a user, I want to view how many likes a post has so that i can gauge how popular a post is.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Like count  | Log in and navigate to any post detail page via one of the methods to do so as explained above. Scroll down to below the post image and the like count will be displayed  | To view the total amount of likes a post has. | Works as expected |

<details>
<summary>Screenshots User Story 18</summary>

<details>
<summary>Feature - Like count</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

19. As a user, I want to add a bio to my profile page so that other members can learn more about me.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Bio Section  | Log in and navigate to the My profile page via the nav bar. Click on the Edit profile button located below the users profile picture. The user will then be redirected to the edit profile form, fill out out the bio field and click on the update profile button  | Users profile to display their bio field above their posts | Works as intended |

<details>
<summary>Screenshots User Story 19</summary>

<details>
<summary>Feature - Bio Section</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

20. As a user, I want to follow other accounts so that i can view their posts on my feed.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Follow  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 20</summary>

<details>
<summary>Feature - Follow</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

21. As a user, I want to fill in a help form so that i can enquire about issues I may have regarding the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Contact  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 21</summary>

<details>
<summary>Feature - Contact</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

22. As a user, I want to change my email address so that i can maintain the same account if I change email address.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Edit Profile  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 22</summary>

<details>
<summary>Feature - Edit profile</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

23. As a user, I want to receive feedback so that i can confirm the help form submission was successful or not.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Site Feedback  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 23</summary>

<details>
<summary>Feature - Site feedback</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

24. As a user, I want to scroll through the latest images on my feed so that i can keep up to date with accounts I follow.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Feed  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 24</summary>

<details>
<summary>Feature - Feed</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

25. As a user, I want to browse my list of followed accounts so that i can view that particular user account.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Followed List  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 25</summary>

<details>
<summary>Feature - Followed List</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

26. As a user, I want to see a visual indicator of following an account so that i can tell if I currently follow that account.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Follow / Unfollow button  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 26</summary>

<details>
<summary>Feature - Follow / Unfollow button</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>



#### Site Owner

27. As the site owner, I would want to validate users data entries on sign up **so that users can create a log in which meets the requirements.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Input Validation  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - Input Validation</summary>
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-1.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
</details>
</details>

28. As the site owner, I would want to ensure only logged in users can post from their account and edit their profile so that data privacy is ensured.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Authentication  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - Authentication</summary>
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-1.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
</details>
</details>

29. As the site owner, I would want to have the ability to remove posts so that i can keep the app clean and friendly.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Delete Post  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - Delete Post</summary>
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-1.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
</details>
</details>

30. As the site owner, I would want the site to be fully responsive so that user can use it across multiple devices and create a good user experience.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Responsiveness  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - Responsiveness</summary>
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-1.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
</details>
</details>

31. As the site owner, I would want to use the app search function so that i can search for particular posts by hashtags or search for users by their user name.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  user Search  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - User Search</summary>
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-1.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
</details>
</details>

32. As the site owner, I would want 404 and 500 error pages so that users do not have to use the back navigation button if an error occurs.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  Error Pages  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - Error pages</summary>
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-1.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
</details>
</details>





### Automated Testing

<details>
<summary>See unit testing</summary>

Using Djangos Unit tests from Pythons standard library module unittest i wrote a series of unit test to test for correct operation of Classes and functions. The overall report findings were produced using the coverage tool.

<details>
<summary>Unit testing Code</summary>
<img src="docs/images/testing/unit-testing/unit-testing-code.png">
</details>

<details>
<summary>Unit testing Result</summary>
<img src="docs/images/testing/unit-testing/unit-testing.png">
</details>

</details>

## Bugs

During the project I encountered a number of bugs some of which were solved some of which were not as stated below:

| Bug           | Fix           |
| ------------- | ------------- |
| Like button acting globally and not on a user basis | |
| Delete post confirmation modal would still delete post when cancelled | | 
| Reset password wont send an email via Google Mail | |
| Follow button would not update to reflect the current follow status  | |
| Post cards would be the height of the largest image in the lists row leaving whitespace below images in cards that are shorter | |

## Configuration

### Google emails

To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required:

1. Create an email account at google.com, login, click you user icon and then on 'Manage Your Google Account'
2. Click on the Security tab
3. Turn on 2-step verification and follow the steps to enable
4. Click on App passwords, click on Select app and choose Other
5. Give your app a name and click on 'Generate'
<br>![App password](docs/images/gmail-app-password.png)
6. A 16 digit password will be generated, note the password down
7. Set the below variables within the settings.py file to successfully send emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')</code>
<br><code>EMAIL_PORT = '587'</code>
<br><code>EMAIL_USE_TLS = True</code>
8. Set up the variables EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in your Render application Config vars

## Deployment

### Heroku

This project was deployed to Heroku in the project's early stages to allow continual responsive testing. This was achieved via the following steps:

The website was deployed using Heroku by "following these steps:

1. Use the "pip freeze -> requiremnts.txt" command in the terminal to save any libraries that need to be installed in the file.
2. Navigate to https://www.heroku.com/ and login or create an account. 
3. Click the "new" button in the upper right corner and select "create new app".
<details>
<summary>Screenshot</summary>
<img src="docs/images/deployment/new-app.png">
</details>

4. Choose an app name and your region and click "Create app".
<details>
<summary>Screenshot</summary>
<img src="docs/images/deployment/app-name.png">
</details>

5. Under Config Vars store any sensitive data you saved in .json file. Name 'Key' field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
<details>
<summary>Screenshot</summary>
<img src="docs/images/deployment/config-vars.png">
</details>

6. Go to the "settings" tab, add the Python build pack and then the node.js build pack (please note they need to be in the correct order of Python above node.js).
<details>
<summary>Screenshot</summary>
<img src="docs/images/deployment/settings.png">
</details>
<details>
<summary>Screenshot</summary>
<img src="docs/images/deployment/add-buildpack.png">
</details>
<details>
<summary>Screenshot</summary>
<img src="docs/images/deployment/build-pack-order.png">
</details>

7. Go to the "deploy" tab and pick GitHub as a deployment method.
8. Search for a repository to connect to and select the branch you would like to build the app from.
9. If preferred enable automatic deploys and then deploy branch.
10. Wait for the app to build and then click on the "View" link which will redirect you to the deployed link.

### Forking the GitHub Repository

We can make a copy of the original repository on our GitHub account to view or make changes too without affecting the original repository, this is known as forking. Forking in GitHub can be done via the following steps:

1. Navigate to www.github.com and log in.
2. Once logged in navigate to the desired [GitHub Repository](https://github.com/jkingportfolio/CI_PP4_Pic_Pals) that you would like to fork.
3. At the top right corner of the page click on the fork icon.
4. There should now be a copy of your original repository in your GitHub account.

Please note if you are not a member of an organisation on GitHub then you will not be able to fork your own repository.

### Clone a GitHub Repository

You can make a local clone of a repository via the following steps: 

1. Navigate to www.github.com and log in.
2. Once logged in navigate to the desired [GitHub Repository](https://github.com/jkingportfolio/CI_PP4_Pic_Pals) that you would like to clone.
3. Locate the code button at the top, above the repository file structure.
4. Select the preferred clone method from HTTPS. SSH or GitHub CLI then click the copy button to copy the URL to your clipboard.
5. Open Git Bash
6. Update the current working direction to the location in which you would like the clone directory to be created.
7. Type `git clone` and paste the previously copied URL at Step 4.
8. `$ clone https://github.com/jkingportfolio/CI_PP4_Pic_Pals`
9. Now press enter and the local clone will be created at the desired local location

## Credits

### Tutorials

- <TUTORIAL NAME/DESCRIPTION> - [LINK NAME](Link URL)
- <TUTORIAL NAME/DESCRIPTION> - [LINK NAME](Link URL)
- <TUTORIAL NAME/DESCRIPTION> - [LINK NAME](Link URL)
- <TUTORIAL NAME/DESCRIPTION> - [LINK NAME](Link URL)

### Code

 Code from external sources were used as a basis and built on top of in this project, they are credited below:

 - <CODE NAME/DESCRIPTION> - [LINK NAME](Link URL)
 - <CODE NAME/DESCRIPTION> - [LINK NAME](Link URL)
 - <CODE NAME/DESCRIPTION> - [LINK NAME](Link URL)

### Literature

The use of reference books were used throughout the creation of this project and are credited below:

- <TITLE> by <AUTHOR>, published by <PUBLISHER>
- <TITLE> by <AUTHOR>, published by <PUBLISHER>
- <TITLE> by <AUTHOR>, published by <PUBLISHER>
### Misc

The source of where I learned how to produce a GitHub fork and clone was from the following pages of the GitHub Documentation. Although I did not use a fork or clone in this project it is something I hope to implement to future projects now I have the knowledge to do so.

- https://docs.github.com/en/get-started/quickstart/fork-a-repo
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository


## Acknowledgements

I would like to also thank the following:
- My wife and family for their support and feedback whilst doing this project
- [Andy Guttridge](https://github.com/andy-guttridge) for his help through out the project
- Code Institute tutor support who helped with an issue i had with having to reset my database.
- My Code Institute mentor Mo Shami for his guidance through this project.


[Back to Top](#pic-pals)