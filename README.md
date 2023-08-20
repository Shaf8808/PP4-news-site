Tinymce - wysiwyg text editor

Summernote - wysiwyg text editor

Changing the login templates of Django Allauth (login, signup html files etc.) to improve UI and inherit styling of my own templates and css

Make sure to detail the ability for the site admin to post articles, reviews and releases through the website, as well as the ability to edit and delete them.

**3 types of Users:**

A user who is not authenticated and doesn't have an account

A user who IS authenticated and has a registered account on the site

A superuser (myself) who is the administrator (and builder) of the site with special privileges

**Testing**

An error with data type being an integear unable to be converted to a datetimefield

Trying to write a custom class based view so that both the Release data as well as the Article data would be displayed correctly on the homepage was a big challenge for me when building this site. 

Adding crud functionality to my site was undoubtedly one of the most challenging aspects of building my project. As the  codestar blog tutorial only covered an administrator being able to edit user comments as well as delete them, I had to find a way to allow a specific registered user to be able to both edit as well as delete their own comment without altering anybody else's. 


Including null=True to my review and article fields in my Comment data model ensured that the fields could be null meaning I don't have to provide data for those fields when posting comments on either the articles page or reviews page.


I was having some issues with posting an image through my form I created in Django, as everything else was being posted successfully. I managed to, however, with some help from tutor support identify the problem which was the enctype="multipart/form-data" attribute. This is set to text by default, which I needed to change in order to successfully post an image.


Credits

Review header text styling:
https://codepen.io/mireille1306/pen/BawdXzY

Review header text animation
https://www.sliderrevolution.com/resources/css-text-animation/

Mortal Kombat article:
https://www.ign.com/articles/mortal-kombat-1-pre-order-beta-johnny-cage-ps5-xbox

Images:

Texas Chainsaw Massacre:
https://images.app.goo.gl/vrbBbdUFDb5qFqJU6

Shadow Gambit the Cursed Crew:
https://images.app.goo.gl/6BiRYQNq6CMCq7jm7

Tutoring

Stack Overflow

Mentoring

CI Django Codestar blog walkthrough