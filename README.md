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
| Test Case ID                  | Description                                                                                                                                                                                                               | Expected Result                                                                                                   | Comments                                                           | android- chrome | android- firefox | android- edge | iOS - Safari | iOS-Chrome | desktop- Safari | desktop- chrome | desktop- firefox |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------- | ---------------- | ------------- | ------------ | ---------- | --------------- | --------------- | ---------------- |
| 1\. Home Page                 |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 1.1                           | Verify that the home page loads successfully.                                                                                                                                                                             | Home page loads without errors.                                                                                   |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.2                           | Verify that the navigation menu links are present and functional: My Account, Shopping Bag, Sorting/Filtering                                                                                                             | All links are functional.                                                                                         |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.3                           | verify mailchimp sign up works (good case / bad case)                                                                                                                                                                     | success or error messages are displayed                                                                           |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.4                           | Verify that the footer contains the email signup, link to privacy statement and facebook                                                                                                                                  | Footer information is correct.                                                                                    |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.5                           | verify that the search bar is positioned at the bottom of the screen and when a search term is entered and either enter or the magnifying class is clicked, the products page opens to show the filtered list of products | products page opens with products matching the search criteria                                                    |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.6                           | Click on Shopping bag opens the shopping bag                                                                                                                                                                              | Shopping bag is opened                                                                                            |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.7                           | Click on My Account allows registration or login if the user has not logged in and My Profile and logout when already logged in                                                                                           | Registration and login or Profile and logout is shown and respective action is carried out                        |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.8                           | Trying non existing sub page                                                                                                                                                                                              | the site's 404 page is displayed                                                                                  |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 1.7                           | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Page is responsive                                                                                                |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2\. Products Page             |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 2.1                           | Verify that the products page loads successfully.                                                                                                                                                                         | About page loads without errors.                                                                                  |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.2                           | Verify the various filter and sorting function are working and the filter-status info shows the correct filter and number of results                                                                                      | filtered/sorted list is displayed                                                                                 |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.3                           | if superuser is logged in the product cards display Edit Delete Buttons                                                                                                                                                   | Buttons/links are present                                                                                         |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.4                           | Try Edit and Delete button as superuser                                                                                                                                                                                   | Product is deleted / edit product page opens                                                                      |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.5                           | Verify that the BTT button works                                                                                                                                                                                          | When scrolled down clicking the btt button scrolls the screen back to the top                                     |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 2.6                           | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Page is responsive                                                                                                |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3\. Edit Product Page         |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 3.1                           | Verify that the edit product page loads successfully and is showing all product information for editing when a superuser clicks on [Edit] in the product card                                                             | Edit product page opens                                                                                           |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.2                           | Verify that all drop down boxes for related models (e.g. Product Category, Type, Brand, Bottler) are showing the available options                                                                                        | All entries of related models are displayed                                                                       |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.3                           | Verify that the stored Brand or Bottler of the product can be edited through a click on the Edit Button below the dropdown-box                                                                                            | A pop-form opens to allow editing the related model entry that was stored for the product                         |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.4                           | Verify that a new Brand or Bottler can be added through a click on the Add Button below the dropdown-box                                                                                                                  | A pop-form opens to allow adding a new Brand/Bottler. When the form is submitted the new entry becomes selected   |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.5                           | Verify that the form displays error messages for invalid inputs.                                                                                                                                                          | Error messages are displayed.                                                                                     | Price of 0 is currently allowed                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.6                           | Verify that the existing images for the product can be deleted and new ones can be added                                                                                                                                  | Deletion and adding of images works                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.7                           | Verify that the existing taste categories for the product can be deleted and new ones can be added (multi-select possible)                                                                                                | Deletion and adding of taste categories works                                                                     |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.8                           | Try to access edit product page of a product without superuser privilege                                                                                                                                                  | User is redirected to login page                                                                                  |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 3.8                           | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Page is responsive                                                                                                |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4\. New Product Page          |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 4.1                           | Verify that the new product page loads successfully when a superuser clicks on Add Product in the [My Account] menu                                                                                                       | Add product page opens                                                                                            |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.2                           | Verify that all drop down boxes for related models (e.g. Product Category, Type, Brand, Bottler) are showing the available options                                                                                        | All entries of related models are displayed                                                                       |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.3                           | Verify that a new Brand or Bottler can be added through a click on the Add Button below the dropdown-box                                                                                                                  | A pop-form opens to allow adding a new Brand/Bottler. When the form is submitted the new entry becomes selected   |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.4                           | Verify that the form displays error messages for invalid inputs.                                                                                                                                                          | Error messages are displayed.                                                                                     |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.5                           | Verify that one or more product image can be added                                                                                                                                                                        | Deletion and adding of images works                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.6                           | Verify that taste categories for the product can be added (multi-select possible)                                                                                                                                         | Deletion and adding of taste categories works                                                                     |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 4.7                           | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Page is responsive                                                                                                |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5\. Product Details Page      |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 5.1                           | Verify that the product details page loads successfully and all data is displayed                                                                                                                                         | Product details page loads without errors.                                                                        |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.2                           | Verify that if a product has additional pictures they are displayed on larger screens and the user can enlarge a thumbnail image by clicking on it                                                                        | New image is selected and becomes the enlarged image                                                              |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.3                           | Verify that the user can increase/decrease the quantity and a click on Add To Bag, adds the correct amount of products to the bag. After successful adding a message confirms the add to bag                              | Message confirms adding the product in the desired quantity is added to the shopping bag                          |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.4                           | Verify that a click on the Product Category link opens the products page filtered for this product category                                                                                                               | Filter products page opens                                                                                        |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 5.5                           | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Project details page is responsive.                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6\. Login Page                |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 6.1                           | Verify that the login page loads successfully.                                                                                                                                                                            | Login page loads without errors.                                                                                  |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.2                           | Verify that the user can log in with valid credentials.                                                                                                                                                                   | Login is successful.                                                                                              |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.3                           | Verify that the user receives an error message for invalid credentials.                                                                                                                                                   | Error message is displayed.                                                                                       |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.4                           | Verify that the user is redirected to the home page after successful login.                                                                                                                                               | User is redirected to the dashboard.                                                                              |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 6.5                           | Verify that the login page is responsive and displays correctly on different devices.                                                                                                                                     | Login page is responsive.                                                                                         |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7\. Registration/Sign-Up Page |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 7.1                           | Verify that the registration page loads successfully.                                                                                                                                                                     | Registration page loads without errors.                                                                           |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.2                           | Verify that the user can register with valid details.                                                                                                                                                                     | Registration is successful.                                                                                       |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.3                           | Verify that the user receives an error message for invalid inputs.                                                                                                                                                        | Error message is displayed.                                                                                       |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.4                           | Verify user receives a confirmation email upon registration with verification link                                                                                                                                        | email received with verification link                                                                             |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.5                           | Try login without confirming email                                                                                                                                                                                        | user will be informed that he should have received a confirmation email with a verification link                  |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.4                           | Verify that the user is redirected to the home page after successful registration.                                                                                                                                        | User is redirected to the login page.                                                                             |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 7.5                           | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Registration page is responsive.                                                                                  |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8\. Shopping Bag Page         |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 8.1                           | Verify that the shopping bag page loads successfully.                                                                                                                                                                     | Shopping bag page loads without errors.                                                                           |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.2                           | Verify that when the bag shows either the contents of the shopping bag or informs the user that it is empty                                                                                                               | Bag empty or list of items selected for purchase is displayed                                                     |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.3                           | Click on [keep shopping] - only option if bag is empty                                                                                                                                                                    | Products page loads                                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.4                           | Click on increase/decrease quantity                                                                                                                                                                                       | Quantity of product is decreased/increased with each click on the respective button                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.5                           | If quantity is decreased to one the button becomes white/disabled                                                                                                                                                         | decrease below 1 is not possible                                                                                  |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.6                           | Click on [Update] after decreasing/increasing the quantity                                                                                                                                                                | Update is saved to the bag Subtotal and Grand Total is updated                                                    |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.7                           | Click on [Remove]                                                                                                                                                                                                         | Product is removed from the bag, Grant Total is updated                                                           |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.8                           | Click on GO TO SECURE CHECKOUT                                                                                                                                                                                            | Checkout form opens                                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 8.9                           | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Page is responsive.                                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9\. Checkout Page             |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 9.1                           | Verify that the checkout page loads successfully                                                                                                                                                                          | The order summary and content of the shopping bag are displayed                                                   | if a selected product has a price of 0, a server error is returned | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.2                           | Verify that the form for entering Shipping info displays error messages for invalid inputs.                                                                                                                               | All fields can be filled and entries are checked for validity                                                     |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.3                           | Verify that when the user is logged in any stored info is pre-filled into the form                                                                                                                                        | User data is loaded from the profile                                                                              |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.4                           | If not logged in, the user is presented with a link to register or login                                                                                                                                                  | User can register or login                                                                                        |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.5                           | Login/Registration preserves shopping bag                                                                                                                                                                                 | after login the shopping bag a message of successful login is displayed and a link to the shopping bag is visible |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.6                           | Pay with a Credit/Debit card                                                                                                                                                                                              | user can successfully complete the payment process through stripe                                                 |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.7                           | Upon successful completion of the order, the user will receive a on screen message that the order was successfully completed as well as a confirmation email to the email address provided                                | eMail confirmation is sent                                                                                        |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.8                           | Force an error of the payment process through usage of stripe's respective card numbers                                                                                                                                   | Any errors during the payment process will be displayed in the form                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 9.9                           | Prevent the checkout form from closing correctly after payment was approved                                                                                                                                               | Order is created and user confirmation email is send regardless                                                   |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10                            | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Page is responsive.                                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10\. Profile Page             |                                                                                                                                                                                                                           |                                                                                                                   |                                                                    |                 |                  |               |              |            |                 |                 |                  |
| 10.1                          | Click on [My Account] My Profile                                                                                                                                                                                          | Profile Page opens and all available data is loaded                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.2                          | Enter Default Shipping Information                                                                                                                                                                                        | user receives an error message for invalid inputs.                                                                |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.3                          | Click on UPDATE INFORMATION to save data to the profile                                                                                                                                                                   | updated data is stored in the profile table for the user                                                          |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.4                          | Verify any Order History of the user is displayed                                                                                                                                                                         | complete order history is displayed                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.5                          | Click on Order Number                                                                                                                                                                                                     | a page with all order information of the past order is displayed including a message that this is a past order    |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |
| 10.6                          | Verify that the page is responsive and displays correctly on different devices.                                                                                                                                           | Page is responsive.                                                                                               |                                                                    | ok              | ok               | ok            | ok           | ok         | ok              | ok              | ok               |

All Javascript functions are tested via manual test listed above


### Open/Known Issues

    (1) Price of 0 is allowed when saving a product. When this product is added to a shopping bag and the user tries to perform a checkout, a server error is triggered without a graceful exit leads ...
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

