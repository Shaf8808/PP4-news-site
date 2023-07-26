Tinymce - wysiwyg text editor

Summernote - wysiwyg text editor

Changing the login templates of Django Allauth (login, signup html files etc.) to improve UI and inherit styling of my own templates and css

Make sure to detail the ability for the site admin to post articles, reviews and releases through the website

Testing

An error with data type being an integear unable to be converted to a datetimefield

Trying to write a custom class based view so that both the Release data as well as the Article data would be displayed correctly on the homepage was a big challenge for me when building this site. 

Adding crud functionality to my site was undoubtedly one of the most challenging aspects of building my project. As the  codestar blog tutorial only covered an administrator being able to edit user comments as well as delete them, I had to find a way to allow a specific registered user to be able to both edit as well as delete their own comment without altering anybody else's. 


Including null=True to my review and article fields in my Comment data model ensured that the fields could be null meaning I don't have to provide data for those fields when posting comments on either the articles page or reviews page.

Credits

Tutoring

Stack Overflow

Mentoring

CI Django Codestar blog walkthrough