# THE LIVING RESUME
This is a web site / app to showcase the portfolio and resume of developers, UX/UI designers or even consultants in general: [MY LIVING RESUME](https://.herokuapp.com/) . 
<br>
<br>
<img src=""  width="650" height="auto" alt="Portfolio home">
<img src=""  width="300" height="auto" alt="Portfolio home">

...

## Requirements/Personas and EPICS
.. r <b>personas</b>:

    (1) ..
    (2) ...

In order to best showcase their experience and portfolio, consultants have the following needs:

1. ..:
    1. **Home**: ...
    2. **About**: ..:
        - I..
        - ..
        - ..

...
    4. **Project Details**: .:
        - ..
        - ..
        -

2. ..:
    4. **..**:...

3. ..:
    1. **..**: . 
    2. **...**: ..

## SEO and Marketing
### Keywords


## User Experience

### Target Audience:

1. **Companies/employers** ...
2. **Developers, UX/UI designers or consultants** ..


### User Stories:
The epics above are broken down in to user stories here: [Github User Stories](https://github.com/users/troeske/projects/7/views/2?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D/)


### Future Use-Cases

    (1) ...
    (2) ..   

## Design
### Site Structure
... app is structured into the following apps:

1. **Home**. This shows the general information of the consultant incl. work history, roles, interests etc. split into two main views: Home and About
2. **P..**. T...
3. **C...ontact**. ..
4. **Sign-up**. Client/user sign-up (allauth).


### Wireframes
__Mobile First approach:__

<img src=""  width="300" height="auto" alt="home page mobile">
<img src=""  width="300" height="auto" alt="about page mobile">

<br>

__Tablet and Desktop:__

<img src=""  width="300" height="auto" alt="home page desktop">
<img src=""  width="300" height="auto" alt="about page desktop">


## Database Entity Relationship Diagram ##

[ERD (Lucidchart)](https://lucid.app/lucidchart/a84194fd-bb5b-4516-8860-a5ce5b77cad4/edit?beaconFlowId=5B48F8E11F7B68FE&invitationId=inv_49416297-33a5-4be2-9a57-03776dd9937d&page=0_0#)

<img src=""  width="1000" height="auto" alt="home page desktop">
<img src=""  width="1000" height="auto" alt="home page desktop">
<br>
<img src=""  width="500" height="auto" alt="home page desktop">
<br>

### Imagery used
Simple iconography for intuitive and clean UI.

### Color Scheme
configurable: currently shades of gray
        
### Typography
For the showcase, al normal text is based on the sans-serif free Google font Inter while headings are based on the free font Rychardwalker

## Current Features:

### ...
... 

<br>
<img src="."  width="300" height="auto" alt="collaboration request">
<br>

....

<br>
<img src="."  width="300" height="auto" alt="collaboration request">
<br>

### Home
<br>
<img src="."  width="500" height="auto" alt="Portfolio home">

### About
<br>
<img src="."  width="500" height="auto" alt="About First Viewport">

<br>
<img src="."  width="500" height="auto" alt="About Second Viewport">



### Sign-up/Sign-in/Sign-out

<br>
<img src=""  width="300" height="auto" alt="sign-up">

<br>
<img src="ng"  width="300" height="auto" alt="sign in">


### Status of  the current login state

<br>
<img src=""  width="300" height="auto" alt="sign-out">

### Access to .. after login

...

### ..

T..r.

<br>
<img src="."  width="300" height="auto" alt="registration approval">


## Manual/End-to-End Testing

__Various Browsers on mobile and desktop devices:__


All Javascript functions are tested via manual test listed above


### Open/Known Issues

    (1) ...
    (2) 
    

## Code Validation
### CI Python Lint PEP8 Validator https://pep8ci.herokuapp.com/
__Results:__
All python files were checked by the CI Python Linter and no errors remain.
<br>

### W3 HTML Validator https://validator.w3.org/nu/#textarea
__Results:__
All html pages were checked by the w3 html validator, and no errors remain.
<br>
<img src=""  width="300" height="auto" alt="W3 HTML Validator Results">
<br>
<img src=""  width="300" height="auto" alt="W3 HTML Validator Results">
<br>


### CSS Validator https://jigsaw.w3.org/css-validator/validator
__Results:__
All CSS files were checked by the w3c CSS validator and no errors remain. Remaining warnings are due to the use of CSS variables.
<br>
<img src=""  width="300" height="auto" alt="W3 CSS Validator Results">
<br>

### jshint Validator https://jshint.com/
__Results:__
The js file project_details was checked by the jshint validator, and no errors remain.
<br>
<img src="">
<br>

## Deployment
The app is deployed via Heroku.

Deployment method: Github, Repository: troeske/Portfolio-Web-App 

To LIVING RESUME needs the following _Config Var_:

- CLOUDINARY_URL. link to the cloudinary storage for all media files.
- CURRENT_CONSULTANT. the consultant_id of the consultant this deployment showcases.
- DATABASE_URL. Link to the external postgreSQL database for all other content.
- SECRET_KEY. Project secret key.
- SMTP_PASSWORD- password for the email account used to send email confirmations to clients and consultants


The live link can be found here: [HOLYSPIRITS](https://.herokuapp.com/) 

## Credits
### Tutorials
no tutorials were used.

### Code
W3Schools: https://www.w3schools.com/
MDN Web Docs: https://developer.mozilla.org/en-US/
GeeksForGeeks: https://www.geeksforgeeks.org/
Bootstrap: https://getbootstrap.com/docs/5.3/getting-started/introduction/
django: https://www.djangoproject.com/start/overview/


The functions that are based on Github Copilot or ChatGPT are market in the code. 
The basis for most of the inline function/class documentation was provided by Github Copilot.
   
### Graphics
icons: https://fontawesome.com/
favicon: https://www.freepik.com/icon

### Photos

### Any other resources
https://validator.w3.org/nu/#textarea

https://jigsaw.w3.org/css-validator/validator

https://jshint.com/

I used https://tabletomarkdown.com/convert-spreadsheet-to-markdown/ to convert my Google Sheets manual testing matrix into a to table for this readme.

