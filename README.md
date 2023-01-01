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
    5. [User Manual](#user-manual)
3. [Technical Design](#technical-design)
    1. [Structure](#structure)
    2. [Flowchart](#flowchart)
    3. [Data Models](#data-models)
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

1. As a user, I want to 
2. As a user, I want to 
3. As a user, I want to 
4. As a user, I want to 
5. As a user, I want to 
6. As a user, I want to 
7. As a user, I want to 
8. As a user, I want to 
9. As a user, I want to 
10. As a user, I want to 
11. As a user, I want to 
12. As a user, I want to 
13. As a user, I want to 
14. As a user, I want to 


### Site Owner Stories

15. As the site owner, I would want users to 
16. As the site owner, I would want to 
17. As the site owner, I would want to 
18. As the site owner, I would want to 
19. As the site owner, I would want 
20. As the site owner, I would want 
21. As the site owner, I would want 
22. As the site owner, I would want 

### User Manual

<details><summary>Click here for app use instructions</summary>

#### Overview

Pic Pals is for users who wish “” and also for “”.

#### Welcome Page

Purpose: To greet users.

Description: On the Welcome page users are 

- Yes 
- No

Operation: User keyboard input. Selecting Yes will take the user to the Main Screen whilst selecting No will exit the app.

#### Main Page

Purpose: To provide users with a range of options.

Description: On the Main page users are be provided with 4 options.

- Login 
- Create an account
- Continue as guest
- Return to main menu

Operation: User keyboard input.

</details>

## Technical Design

### Structure

This app was designed using Code Institutes <> Template. The template creates a <>. 

### Flowchart

A flowchart was created during the design process to help identify functions that would be required in the Python files.

<details>
<summary>Flow Chart</summary>
<img src="docs/flowcharts/flow-chart.png">
</details>

### Data Models

This project uses Object Orientated Programming to interact and manipulate the following:

- Classes - This project uses two classes. The first class called 'User' is used to create an instance of a new user based on inputs and append the details to a Google Sheets file. The second class called 'Order' is used to create an instance of an order based on inputs and then display the receipt of the order and append the order details to a Google Sheets file.
- Lists and dictionaries - This project uses list and dictionaries to aid the storage of data from the Google Sheets file to variables and vice versa. Using list comprehension dictionaries are used to validate if a new user name is not already in use, the user input for ordering an item exists and to store/view order records.
- Google Sheets API - Google Sheets was used in this project to store all required data outwidth the container and provide a level of security in user name and passwords.

## Technologies Used

### Coding Languages
- Python 3 - Used to create the command line based app.

### Frameworks and Tools
- Git - Used for version control.
- GitHub - Used to deploy the projects code.
- Gitpod - Used to develop and test code.
- Heroku Platform - Used to deploy the live project.
- PEP8 - Used to validate code against Python conventions.
- <> - <>

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