Click [here](./README.md) to be redirected back to the original Readme document

# Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Add Article](#add-article-page)
  * [Add Review](#add-review-page)
  * [Add Release](#add-release-page)
  * [Editing articles](#editing-articles)
  * [Deleting articles](#deleting-articles)
  * [Editing reviews](#editing-reviews)
  * [Deleting reviews](#deleting-reviews)
  * [Editing releases](#editing-releases)
  * [Deleting releases](#deleting-releases)
  * [User interactivity](#user-interactivity)
  * [User authentication](#user-authentication)
  * [Register](#register)
  * [Login](#login)
  * [Logout](#logout)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed bugs](#unfixed-bugs-)


## User story testing
Below are the most crucial features of my site that had to be implemented for it to meet the essential project criteria laid out in the guidelines. For the full exhaustive list of user stories, please refer to my project board [here](https://github.com/users/Shaf8808/projects/4). Additionally, every single individual feature that I created for my site has been thoroughly tested which can be seen in the [Manual Testing](#manual-testing) section below.


#### User story: Account Registration

*As a site user I can register to the gaming news site so that I can log in and comment on stories and reviews as well as like them*

<img src="./docs/readme_images/navbar-no-user.jpg">

The option to register and login is always visible to the user as it is viewable on the navigation bar displayed at the top of every page

If they click the register link at the top, the sign-up page taken from the Django framework is displayed which can be seen below: 

<img src="./docs/readme_images/register-page.jpg">

Once they have successfully registered and logged in to their account, a success message is displayed for a few seconds as well as the name of their profile alongside an icon to clearly show whether or not a user has successfully logged in and who the user is

<img src="./docs/readme_images/login-message.jpg">

#### User story: Approve comments

*As a site admin I can approve or disapprove comments so that I can control and filter out any inappropriate comments made by other users on the site*

When it comes to leaving comments, I have decided to implement the same feature used in the Codestar blog tutorial of comment approval. The reason as to why I have done this is so that I as the administrator have greater control over the types of comments that are posted on the site in case some are inappropriate or offensive.

As the gif shows below, this works as intended:

<img src="./docs/readme_clips/commenting.gif">


#### User story: Like/Unlike

*As a site user I can like or unlike a story so that I can easily convey whether I like the article or not with the click of a button*

I have also added the feature of liking and unlike articles and reviews, which can be done at the mere click of a button in the shape of a thumbs-up icon. Once a user has clicked the button, the number next to it goes up by one. If clicked again the number goes down by one and reverts to the original amount. This is shown in the clip below:

<img src="./docs/readme_clips/liking.gif">

Depending on the number of likes that an article or a review has, the amount is displayed on each 'card' on the homepage (or review page, depending on what it is). This can be seen in the image below.

<img src="./docs/readme_images/review-card.jpg">

#### User story: Managing articles

*As a site admin I can create, read, update and delete articles/reviews so that I can manage and control my content*

In terms of the content of my website, it is split into three main categories. Articles, Reviews and Releases. It was of course important that I was able to add this content successfully without throwing any errors, as well as cover the rest of crud functionality successfully. 

The image below shows that all three categories of content displayed throughout my site are changeable at the click of a button. I can easily edit as well as delete each item quickly without needing to access the admin panel. These have all been tested and work as intended. I can also create new content such as articles at the top of the page on the navbar seen in the image below. This is only visible to me as the administrator, and also all function correctly.

<img src="docs/readme_images/homepage-admin.jpg">


#### User Story: Open an article

*As a site user I can click on a story so that it opens for me to read*

This particular user story is fairly self-explanatory, where each article or review could be opened for the user to read and view at their leisure. This has been tested with every piece of content on the page and has successfully passed the test. The image below shows my article detail page.  

<img src="docs/readme_images/article-detail-page.jpg">

#### User Story: Comment on a story

*As a site user I can comment on a story/review so that I can engage with each story and convey my feelings and ideas on the subject matter*

This was also a very important feature of my site where users could leave comments on an article or a review if they had an account on the site. These comments would of course have to be approved by me first before being posted and viewed on the page. This has been tested thoroughly to see if everything works as intended, which it does. Evidence of this can be seen on different pages where users created by me have left different comments throughout the site once approved.

[Back to top](#table-of-contents)


## Validator Testing

### HTML

Every HTML page was validated using [W3C HTML Validator](https://validator.w3.org/) with no errors.

### Css

No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### Javascript

No errors were found when passing my javascript through [Jshint](https://jshint.com/)

### Python

No errors were found when passing my Python files through [Pep8](https://pep8ci.herokuapp.com/) except for some whitespace 

[Back to top](#table-of-contents)

## Browser Testing

The website was tested on different browsers such as Google Chrome, Safari and Firefox with no issues apparent

## Device Testing

My site was meticulously tested and viewed multiple times on desktop, laptop and mobile phones to see if the structure and layout of the site remained uncompromised. It holds up well regardless of the device it is being viewed on. I also utilised Chrome developer tools to check this, with positive results.

## Manual Testing

### Site navigation

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                |            |                                                                    |           |
| Site Name (logo)      | Click      | Redirect to home page                                              | Pass      |
| Home Link             | Click      | Redirect to home page                                              | Pass      |
| Reviews Link          | Click      | Redirect to Reviews page                                           | Pass      |
| Register Link         | Click      | Redirect to Register page                                          | Pass      |
| Login Link            | Click      | Redirect to Login page                                             | Pass      |
| User profile name     | Display    | Displays name of authenticated user once logged in                 | Pass      |
| Logout link           | Display    | Only visible if user is logged in                                  | Pass      |
| Logout link           | Click      | Redirects to logout page                                           | Pass      |
| Add article link      | Display    | Only visible for myself the administrator                          | Pass      |
| Add article link      | Click      | Redirects to add article form                                      | Pass      |
| Add review link       | Click      | Redirects to add review form                                       | Pass      |
| Add review link       | Display    | Only visible for myself the administrator                          | Pass      |
| Add release link      | Display    | Only visible for myself the administrator                          | Pass      |
| Add release link      | Click      | Redirects to add release form                                      | Pass      |
| Article detail link   | Click      | Opens the article to the article detail page                       | Pass      |
| Review detail link    | Click      | Opens the review to the review detail page                         | Pass      |
| Register Link         | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
| All Nav Links         | Hover      | Brightens text                                                     | Pass      |
|                       |            |                                                                    |           |
| Mobile View           |            |                                                                    |           |
| Hamburger Menu        | Responsive | Displays when screen size is reduced to medium                     | Pass      |
| Dropdown menu         | Responsive | Menu with nav links transform to dropdown when screen size reduces to medium       | Pass      |
| Home Link             | Click      | Redirect to home page                                              | Pass      |
| Reviews Link          | Click      | Redirect to Reviews page                                           | Pass      |
| Register Link         | Click      | Redirect to Register page                                          | Pass      |
| Login Link            | Click      | Redirect to Login page                                             | Pass      |
| User profile name     | Display    | Displays name of authenticated user once logged in                 | Pass      |
| Logout link           | Display    | Only visible if user is logged in                                  | Pass      |
| Logout link           | Click      | Redirects to logout page                                           | Pass      |
| Add article link      | Display    | Only visible for myself the administrator                          | Pass      |
| Add article link      | Click      | Redirects to add article form                                      | Pass      |
| Add review link       | Click      | Redirects to add review form                                       | Pass      |
| Add review link       | Display    | Only visible for myself the administrator                          | Pass      |
| Add release link      | Display    | Only visible for myself the administrator                          | Pass      |
| Add release link      | Click      | Redirects to add release form                                      | Pass      |
| Article detail link   | Click      | Opens the article to the article detail page                       | Pass      |
| Review detail link    | Click      | Opens the review to the review detail page                         | Pass      |
| Register Link         | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
| All Nav Links         | Hover      | Brightens text                                                     | Pass      |
|                       |            |                                                                    |           |

### Add Article page

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                | Display    | Shows navbar on form page                                          | Pass      |
| Title field           | Display    | Displays title field                                              | Pass      |
| Slug field            | Display      | Displays slug field                                              | Pass      |
| Image field          | Display      | Displays image field                                           | Pass      |
| Content field         | Display      | Displays content field                                          | Pass      |
| Excerpt field            | Display      | Displays excerpt field                                            | Pass      |
| Status field    | Display    | Displays status field with the relevant options                  | Pass      |
| Submit button    | Click    | Creates new article 'card' and displays it on home screen                 | Pass      |
| Submit button    | Click    | Informs the user of any empty fields if there are any before submitting                | Pass      |
| Cancel button    | Click    | Redirects to homepage                 | Pass      |


### Add Review page

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                | Display    | Shows navbar on form page                                          | Pass      |
| Title field           | Display    | Displays title field                                              | Pass      |
| Slug field            | Display      | Displays slug field                                              | Pass      |
| Review date field            | Display      | Displays field                                              | Pass      |
| Score field            | Display      | Displays field                                              | Pass      |
| Image field          | Display      | Displays image field                                           | Pass      |
| Content field         | Display      | Displays content field                                          | Pass      |
| Excerpt field            | Display      | Displays excerpt field                                            | Pass      |
| Status field    | Display    | Displays status field with the relevant options                  | Pass      |
| Submit button    | Click    | Creates new review 'card' and displays it on review page                 | Pass      |
| Submit button    | Click    | Informs the user of any empty fields if there are any before submitting                | Pass      |
| Cancel button    | Click    | Redirects to review page                 | Pass      |


[Back to top](#table-of-contents)

### Add Release page

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                | Display    | Shows navbar on form page                                          | Pass      |
| Name field           | Display    | Displays field                                              | Pass      |
| Slug field            | Display      | Displays field                                              | Pass      |
| Release date field            | Display      | Displays field                                              | Pass      |
| Platform field            | Display      | Displays field                                              | Pass      |
| Badges             | Display      | Adds appropriately styled badge depending on the release platform                                              | Pass      |
| Submit button    | Click    | Creates new release item and displays it on the homepage releases section                 | Pass      |
| Submit button    | Click    | Informs the user of any empty fields if there are any before submitting                | Pass      |
| Cancel button    | Click    | Redirects to homepage                 | Pass      |

### Editing articles

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Button                | Display    | Shows the button only for the administrator at the bottom of each article/review                                          | Pass      |
| NavBar                | Display    | Shows navbar on form page                                          | Pass      |
| Fields            | Display    | Displays all fields filled with the correct data                       | Pass      |
| Submit button    | Click/Display    | Updates correct article with new data and displays it on homepage                 | Pass      |
| Submit button    | Click/Display    | Informs user of any empty fields if there are any before submitting                | Pass      |
| Cancel button    | Click/Display    | Redirects to homepage                 | Pass      |


### Deleting articles

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Button                | Display    | Shows the button only for the administrator at the bottom of each article/review                                          | Pass      |
| NavBar                | Display    | Shows navbar on page                                          | Pass      |
| Message            | Display    | Displays an appropriate delete message                       | Pass      |
| Delete button    | Click/Display    | Deletes correct article and removes it from the homepage                 | Pass      |
| Cancel button    | Click/Display    | Redirects to homepage                 | Pass      |


### Editing reviews

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Button                | Display    | Shows the button only for the administrator at the bottom of each article/review                                          | Pass      |
| NavBar                | Display    | Shows navbar on form page                                          | Pass      |
| Fields            | Display    | Displays all fields filled with the correct data                       | Pass      |
| Submit button    | Click/Display    | Updates correct review with new data and displays it on homepage                 | Pass      |
| Submit button    | Click/Display    | Informs user of any empty fields if there are any before submitting                | Pass      |
| Cancel button    | Click/Display    | Redirects to review page                 | Pass      |


### Deleting reviews

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Button                | Display    | Shows the button only for the administrator at the bottom of each article/review                                          | Pass      |
| NavBar                | Display    | Shows navbar on page                                          | Pass      |
| Message            | Display    | Displays an appropriate delete message                       | Pass      |
| Delete button    | Click/Display    | Deletes correct review and removes it from the review page                 | Pass      |
| Cancel button    | Click/Display    | Redirects to review page                 | Pass      |


[Back to top](#table-of-contents)

### Editing releases

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Button                | Display    | Shows the button only for the administrator at the bottom of each article/review                                          | Pass      |
| NavBar                | Display    | Shows navbar on form page                                          | Pass      |
| Fields            | Display    | Displays all fields filled with the correct data                       | Pass      |
| Submit button    | Click/Display    | Updates correct release with new data and displays it on homepage                 | Pass      |
| Submit button    | Click/Display    | Informs user of any empty fields if there are any before submitting                | Pass      |
| Cancel button    | Click/Display    | Redirects to homepage                 | Pass      |


### Deleting releases

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Button                | Display    | Shows the button only for the administrator at the bottom of each article/review                                          | Pass      |
| NavBar                | Display    | Shows navbar on page                                          | Pass      |
| Message            | Display    | Displays an appropriate delete message                       | Pass      |
| Delete button    | Click/Display    | Deletes correct release data and removes it from the homepage                 | Pass      |
| Cancel button    | Click/Display    | Redirects to homepage                 | Pass      |


### User interactivity

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Article/Review detail            | Display/Click    | Lets the user open an article/review after selecting it                       | Pass      |
| Like and comment icon              | Display    | Shows the number of likes and comments for each article/review on the appropriate 'card'                                          | Pass      |
| Like            | Display/Click    | Lets the user 'like' an article/review                       | Pass      |
| Comments section            | Display    | Displays the Comments section for both users and non-users at the bottom of each article/review detail page                       | Pass      |
| Comment form    | Display    | Displays the comment form on an article/review only for authenticated users                 | Pass      |
| Comment submit    | Click/Display    | Allows the user to comment on an article/review                 | Pass      |
| Comment approval message    | Display    | Informs user their comment is awaiting approval once posted                 | Pass      |
| Edit comment button           | Display    | Only displays edit comment button for each comment posted by the logged-in user                       | Pass      |
| Edit comment form          | Display    | Redirects user to an 'Edit Comment' form with the correct comment in the field once clicked                       | Pass      |
| Update button          | Display/Click    | Displays an Update button when once clicked, edits the appropriate comment before displaying it on the relevant page                       | Pass      |
| Cancel button           | Display/Click    | Displays a Cancel button that redirects the user back to the relevant page once clicked                       | Pass      |
| Delete comment button           | Display    | Only displays delete comment button for each comment posted by the logged-in user                       | Pass      |
| Delete comment          | Display    | Redirects user to a 'Delete Comment' page with a delete message                      | Pass      |
| Delete button          | Display/Click    | Displays a Delete button that deletes the correct comment                     | Pass      |
| Cancel button          | Display/Click    | Redirects user back to the previous page                      | Pass      |



### User authentication

#### Register

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Register fields              | Display    | Shows all relevant fields to sign up and create an account                                          | Pass      |
| Sign Up button            | Display/Click    | Displays the sign-up button and informs the user of any empty fields                      | Pass      |
| Sign Up   | Display/Click    | Successfully creates a user account and displays an appropriate message that says successfully signed in as the user                | Pass      |

#### Login

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Login              | Display    | Shows all relevant fields to sign in to an existing account (Username and Password)                                         | Pass      |
| Sign In button            | Display/Click    | Displays the login button and informs the user of any empty fields if any                      | Pass      |
| Sign In   | Click    | Successfully logs in and displays an appropriate message                | Pass      |

#### Logout

| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Logout              | Display    | Shows a relevant message asking if the user wants to log out                                         | Pass      |
| Logout button            | Display/Click    | Displays the logout button and successfully logs the user out of their account with/ a message                      | Pass      |



The above tables were created using [AliOKeeffe's](https://github.com/AliOKeeffe/PP4_My_Meal_Planner/blob/main/TESTING.md) readme as an example


[Back to top](#table-of-contents)

## Bugs

### Fixed Bugs

There were of course several bugs big and small that I came across while constructing my site. These can be seen in the list below:

* An error with the data type being an integer unable to be converted to a datetimefield. This occurred while I was trying to modify my data model field for the release date. I later found out that there can be some issues that occur when trying to change a data field after data has already been entered, which meant that I first had to empty the database before making any necessary changes to my data model.

* Trying to write a custom class-based view so that both the Release data as well as the Article data would be displayed correctly on the homepage was a big challenge for me when building this site. 

* Adding crud functionality to my site was undoubtedly one of the most challenging aspects of building my project. As the codestar blog tutorial only covered an administrator being able to edit user comments as well as delete them, I had to find a way to allow a specific registered user to be able to both edit as well as delete their comment without altering anybody else's. 

* Including null=True to my review and article fields in my Comment data model ensured that the fields could be null meaning I don't have to provide data for those fields when posting comments on either the articles page or reviews page.

* I was having some issues with posting an image through the form I created in Django, as everything else was being posted successfully. I managed to, however, with some help from tutor support identify the problem which was the enctype="multipart/form-data" attribute. This is set to text by default, which I needed to change to successfully post an image.

## Unfixed Bugs

There are no unfixed bugs

[Back to top](#table-of-contents)