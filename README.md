# THE LIVING RESUME
This is a web site / app to showcase the portfolio and resume of developers, UX/UI designers or even consultants in general: [MY LIVING RESUME](https://.herokuapp.com/) . 
<br>
<br>
<img src=""  width="650" height="auto" alt="Portfolio home">
<img src=""  width="300" height="auto" alt="Portfolio home">

...

## User Experience

### User Stories:
The basis for the implementation of the HolSpirits online whiskey store was the Boutique Ado project and it's user stories:

| User Story ID                | As a/an     | I want to be able to ...                                            | So that I can...                                                                                                 |
| ---------------------------- | ----------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| VIEWING & NAVIGATION         |             |                                                                     |                                                                                                                  |
| 1                            | Shopper     | View a list of products                                             | Select something to purchase                                                                                     |
| 2                            | Shopper     | View a specific category of products                                | Quickly find products I'm interested in without having to search through all products.                           |
| 3                            | Shopper     | View individual product details                                     | Identify the price, description, product rating, product image and available sizes.                              |
| 4                            | Shopper     | Quickly identify deals, clearance items and special offers          | Take advantage of special savings on products I'd like to purchase.                                              |
| 5                            | Shopper     | Easily view the total of my purchases at any time                   | Avoid spending too much.                                                                                         |
| REGISTRATION & USER ACCOUNTS |             |                                                                     |                                                                                                                  |
| 6                            | Site User   | Easily register for an account                                      | Have a personal account and be able to view my profile                                                           |
| 7                            | Site User   | Easily log in or out                                                | Access my personal account information                                                                           |
| 8                            | Site User   | Easily recover my password in case I forget it                      | Recover access to my account                                                                                     |
| 9                            | Site User   | Receive an email confirmation after registering                     | Verify that my account registration was successful                                                               |
| 10                           | Site User   | Have a personalised user profile                                    | View my personal order history and order confirmations, and save my payment information                          |
| SORTING & SEARCHING          |             |                                                                     |                                                                                                                  |
| 11                           | Shopper     | Sort the list of available products                                 | Easily identify the best rated, best priced and categorically sort products                                      |
| 12                           | Shopper     | Sort a specific category of product                                 | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| 13                           | Shopper     | Sort multiple categories of products simultaneously                 | Find the best-priced or best-rated products across broad categories, such as clothing or homeware                |
| 14                           | Shopper     | Search for a product by name or description                         | Find a specific product I'd like to purchase                                                                     |
| 15                           | Shopper     | Easily see what I've searched for and the number of results         | Quickly decide whether the product I want is available                                                           |
| PURCHASING & CHECKOUT        |             |                                                                     |                                                                                                                  |
| 16                           | Shopper     | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size                                           |
| 17                           | Shopper     | View items in my bag to be purchased                                | Identify the total cost of my purchase and all items I will receive                                              |
| 18                           | Shopper     | Adjust the quantity of individual items in my bag                   | Easily make changes to my purchase before checkout                                                               |
| 19                           | Shopper     | Easily enter my payment information                                 | Check out quickly and with no hassles                                                                            |
| 20                           | Shopper     | Feel my personal and payment information is safe and secure         | Confidently provide the needed information to make a purchase                                                    |
| 21                           | Shopper     | View an order confirmation after checkout                           | Verify that I haven't made any mistakes                                                                          |
| 22                           | Shopper     | Receive an email confirmation after checking out                    | Keep the confirmation of what I've purchased for my records                                                      |
| ADMIN & STORE MANAGEMENT     |             |                                                                     |                                                                                                                  |
| 23                           | Store Owner | Add a product                                                       | Add new items to my store                                                                                        |
| 24                           | Store Owner | Edit/update a product                                               | Change product prices, descriptions, images and other product criteria                                           |
| 25                           | Store Owner | Delete a product                                                    | Remove items that are no longer for sale                                                                         |

To finalize the HolySpirits Shop I added to following user stories including acceptance criteria and breakdown into tasks: [Github User Stories](https://github.com/users/troeske/projects/10/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D)

### Future Use-Cases

    (1) Blog Section to provide curated articles and videos  
    (2) Comment/Tasting notes Section for shoppers on whiskeys in our store

## Design
### Site Structure

HolySpirits is structured into the following apps:

1. **Home**. This the landing page of the shop.main views: Home and About
2. **Products..**. Searchable and sortable overview of all products in the store.
3. **Profile**. During the checkout process the user can decide to create an account in the store to simplify future purchases and to have access to purchase history.
4. **Checkout**. All functionality to actually buy a product on the site including integration into Stripe (their test sandbox).
5. **Bag**. All functionality to manage the shopping bag of the user.
4. **Account**. Shopper/user sign-up/sign-in (allauth).


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
Simple iconography for intuitive and clean UI. The images used are chosen with darker, warm colors in line with a good glass of whiskey.

### Color Scheme
The golden glow of a good whiskey; dark with white text.
        
### Typography
All text is based on the sans-serif free Google font Inter while headings are based on the free font DM Serif Display

## Current Features:

### Product overview
Product overview that can be sorted by name, price, region, brand, category (Rye Whiskey, Bourdon, Single Malt and Irish Whiskey)  

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

