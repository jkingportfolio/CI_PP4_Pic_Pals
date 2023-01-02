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
    1. [Existing Features](#existing-features)
    2. [Future Implementations](#future-implementations)
6. [Python Valiadation](#python-validation)
7. [Testing](#testing)
    1. [Device Testing](#device-testing)
    2. [Browser Compatibility](#browser-compatibility)
    3. [Manual Testing](#manual-testing)
    4. [Automated Testing](#automated-testing)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
    1. [Tutorial](#tutorials)
    2. [Code](#code)
    3. [Literature](#literature)
    4. [Misc](#misc)
11. [Acknowledgements](#acknowledgements)

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
2. As a user, I want to see a visual indicator of having like a post so that i can tell if I have previously like that post.
3. As a user, I want to like and unlike posts so that *i can show my appreciation of another users post.
4. As a user, I want to delete my posts so that i can permanently remove posts I do not wish to keep
5. As a user, I want to edit my posts so that i can correct spelling mistakes or hashtags I may have enter into comments.
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

29. As the site owner, I would want to validate users data entries on sign up **so that users can create a log in which meets the requirements.
30. As the site owner, I would want to ensure only logged in users can post from their account and edit their profile so that data privacy is ensured.
31. As the site owner, I would want to have the ability to remove posts so that i can keep the app clean and friendly
32. As the site owner, I would want the site to be fully responsive so that user can use it across multiple devices and create a good user experience.
33. As the site owner, I would want to use the app search function so that i can search for particular posts by hashtags or search for users by their user name.
34. As the site owner, I would want 404 and 500 error pages so that users do not have to use the back navigation button if an error occurs.



## Technical Design

### Colours

The colour scheme used in this project was chosen with simplicity in mind. The colour scheme is used through out all pages to ensure contrast readability and an overall good user experience. 

!!! DECIDE ON A COLOUR PALETTE !!!

<details>
<summary>Colour Pallete</summary>
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

<details>
<summary>Database diagram</summary>
<img src="docs/database/database-diagram.png">
</details>




This app was designed using Code Institutes <> Template. The template creates a <>. 

### Database

A flowchart was created during the design process to help identify functions that would be required in the Python files.

<details>
<summary>Database diagram</summary>
<img src="docs/flowcharts/flow-chart.png">
</details>

### Data Models

This project uses Object Orientated Programming to interact and manipulate the following:

- Classes - This project uses two classes. The first class called 'User' is used to create an instance of a new user based on inputs and append the details to a Google Sheets file. The second class called 'Order' is used to create an instance of an order based on inputs and then display the receipt of the order and append the order details to a Google Sheets file.
- Lists and dictionaries - This project uses list and dictionaries to aid the storage of data from the Google Sheets file to variables and vice versa. Using list comprehension dictionaries are used to validate if a new user name is not already in use, the user input for ordering an item exists and to store/view order records.
- Google Sheets API - Google Sheets was used in this project to store all required data outwidth the container and provide a level of security in user name and passwords.

### Wireframes

## Technologies Used

### Coding Languages
- HTML
- CSS
- Python 3
- Javascript

### Frameworks and Tools
- Git - Used for version control.
- GitHub - Used to deploy the projects code.
- Gitpod - Used to develop and test code.
- Heroku Platform - Used to deploy the live project.
- Django - Used to 
- Am i Responsive
- Balsamiq
- Boostrap 5
- Cloudinary
- Font Awesome
- Graphviz
- Google Fonts
- Validation
    - WC3 Validator
    - Jigsaw W3 Validator
    - Jshint
    - PEP8 - Used to validate code against Python conventions.
    - Lighthouse
    - WAVE Validator

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

In its entirety the website consists of one main page, with a mock terminal within that page to run The Taco Trailer app.

### Existing features

#### FEATURE NAME 

<FEATURE DESCTRIPTION>

<details>
<summary>Welcome message image</summary>
<img src="docs/images/features/landing-page.png">
</details>

- Covered in user stories: X & X

## Future implementations

In the future as my skills grow I would like to implement the following features:

- <IMPLEMENTATION DESCRIPTION / REASON>.
- <IMPLEMENTATION DESCRIPTION / REASON>.
## Validation
### HTML Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app.

<details>
<summary>Python file - run.py</summary>
<img src="docs/images/validation/pep8-validation-run.png">
</details>


### CSS Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app.

<details>
<summary>Python file - run.py</summary>
<img src="docs/images/validation/pep8-validation-run.png">
</details>


### Python Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app.

<details>
<summary>Python file - run.py</summary>
<img src="docs/images/validation/pep8-validation-run.png">
</details>

### JavaScript Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app.

<details>
<summary>Python file - run.py</summary>
<img src="docs/images/validation/pep8-validation-run.png">
</details>

### Chrome Dev Tools Lighthouse Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app.

<details>
<summary>Python file - run.py</summary>
<img src="docs/images/validation/pep8-validation-run.png">
</details>

### WAVE Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app.

<details>
<summary>Python file - run.py</summary>
<img src="docs/images/validation/pep8-validation-run.png">
</details>

## Testing

### Device Testing

As this app is only intended to be used on desktops the website was tested on the following devices:
- Windows 10 PC with a 24" MSI Curved gaming monitor
- Raspberry Pi 4 with a 24" MSI Curved gaming monitor

### Browser Compatibility

The website was tested on the following web browsers:
- Google Chrome (Version 104.0.5112.102)
- DuckDuckGo

### Manual Testing

<details>
<summary>See Testing User Stories</summary>

#### Testing User Stories Users

To avoid unnecessary repetition of images, only the feature being referred to will have screenshots. Information on how to navigate to the feature referred to will be described within its relevant table reference. 

1. As a user, I want to <USER STORY 1>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  <FEATURE>  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

Due to the sheet amount of images required to cover all please see this user story in action via the extensive amount of images within the rest of the Manual Testing images.

2. As a user, I want <USER STORY 2>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  <FEATURE>  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 2</summary>

<details>
<summary>Feature - Quit</summary>
<img src="docs/images/image.jpeg ">
<img src="docs/images/image.jpeg ">
</details>

</details>

#### Site Owner

3. As the site owner, I would want to <USER STORY 3>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  <FEATURE>  | <ACTION>  | <EXPECTED>    | <ACTUAL> |

<details>
<summary>Screenshots User Story 16</summary>

<details>
<summary>Feature - Admin Dashboard</summary>
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-1.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-2.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-3.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-4.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-5.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-6.png">
<img src="docs/images/testing/testing-user-stories/testing-user-story-16-admin-dashboard-7.png">
</details>
</details>
</details>
</details>


### Automated Testing

<details>
<summary>See unit testing</summary>

Using Pythons unittest library i wrote a unit test to test for correct operation of users entering passwords.

A new test file was created and imported the unittest library and also the <> module as it is where the function to be tested originates from.

One test function to test for valid user input and one test function to test for invalid user input was created. 

The test ran and was successful.

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
| | |
| | | 
|  | |
|   | |
| | |
|  | |
| | |

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
- My fellow Code Institute students whom I have bounced ideas and problems back and forth with via Slack
- [Andy Guttridge](https://github.com/andy-guttridge) for his help through out the project
- Code Institute tutor support who helped with an issue i had with having to reset my database.
- My Code Institute mentor Mo Shami for his guidance through this project.


[Back to Top](#pic-pals)