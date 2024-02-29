# Summary
This is the direct repository Robert Godlewski uses to develop Django plugins to make the process easier to develop Django web applications.

Packages are not directly included here on the repository.

Plugins in current development:
* tag - version 0.1 - Need to package
* crm

Plugins to create later:
* blog
* store
* registration

templates/admin directory in the myplugins directory now has the html for the admin and base html look.

# Plugin Descriptions
## tag plugin
The package is called django-tags.

The tag app is really useful for SEO purposes and grouping content together.  It can be used for blogs, stores, crm, cms, etc.

In this app you are able to create, read, and destroy tags in the database.  No updating once it's made, it's made.

External Repo

## crm plugin
This is a client relation manager app to help keep track of several things.
* Todo list
* list of contacts
* email lists

Other packages might be needed:
* tag

External Repo

### Todos:
1. Add in everything else for Task variables to be edited
2. Edit the form to edit some of the other variables
3. Create tests for Task variables to see if they work
4. Fix bugs for Tasks
5. Add in full CRUD for the other Models

### Tables
Model Design for client:
* f_name - str
* l_name - str
* email - email, special str
* user_id - int, foreign key to users

Model Design for task:
* title - str
* description - str or None
* priority - choices, special str or None
* is_recurring - bool
* reminder_dates - date, special str or None
* reminder_time - time, special str
* due_date - datetime, special str or None
* is_done - bool
* user_id - int, foreign key to users

### Relational tables
Model Design for client_task: Many To Many
* client_id - int, foreign key to client
* task_id - int, foreign key to task

# References
## Tools used
* [Python Markdown](https://pypi.org/project/Markdown/)
* [Django](https://www.djangoproject.com/)

## References from django
* https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
* https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
* https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
* https://forum.djangoproject.com/t/adding-extra-fields-to-a-register-form/14922
* https://forum.djangoproject.com/t/save-a-model-with-foreign-key-at-the-same-time/17401/5
* https://docs.djangoproject.com/en/4.1/intro/tutorial03/#removing-hardcoded-urls-in-templates
* https://docs.djangoproject.com/en/5.0/topics/auth/default/#changing-passwords
* https://docs.djangoproject.com/en/5.0/topics/auth/default/#built-in-auth-views
* https://docs.djangoproject.com/en/5.0/topics/auth/default/#built-in-auth-forms

## References from stackoverflow
* https://stackoverflow.com/questions/16906515/how-can-i-get-the-username-of-the-logged-in-user-in-django
* https://stackoverflow.com/questions/68087796/saving-username-to-model-in-django
* https://stackoverflow.com/questions/26558422/django-and-time-zone
* https://stackoverflow.com/questions/12030187/how-do-i-get-the-current-date-and-current-time-only-respectively-in-django
* https://stackoverflow.com/questions/15307623/cant-compare-naive-and-aware-datetime-now-challenge-datetime-end
* https://stackoverflow.com/questions/10306389/python-pass-tzinfo-to-naive-datetime-without-pytz
* https://stackoverflow.com/questions/10048216/compare-date-and-datetime-in-django
* https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django
* https://stackoverflow.com/questions/60518086/django-external-url-link

## Other References
* https://medium.com/@zackliutju/building-react-and-django-web-application-and-deploy-it-on-google-cloud-545f06eb5521
* https://justdjango.com/blog/build-a-blog-with-django
* https://realpython.com/python-django-blog/
* https://learndjango.com/tutorials/django-login-and-logout-tutorial
* https://learndjango.com/tutorials/django-slug-tutorial
* https://ordinarycoders.com/blog/article/django-user-register-login-logout
* https://www.digitalocean.com/community/tutorial_series/django-development
* https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893
* https://www.javatpoint.com/django-crud-application
* https://www.w3schools.com/tags/att_input_type_datetime-local.asp
* https://java2blog.com/check-if-date-is-greater-than-today-python/
* https://groups.google.com/g/google-appengine/c/F63ZswcKrX4?pli=1
* https://pypi.org/project/pytz/
* https://learndjango.com/tutorials/django-markdown-tutorial
* https://www.youtube.com/watch?v=W5PyXUTjwS4
* https://www.youtube.com/watch?v=I8TRkEcw9Mg

# For developing the site locally
## Django
This site is developed using pipenv as it's virtual environment so best to use these commands when using these commands after installing python:

1. Create virtual environment: % pip3 install pipenv
2. Activate the virtual environment: % pipenv shell
3. Using pipenv to install the packages locally: % pipenv install
4. When you want to test the live site do: % python3 myplugins/manage.py runserver
5. When you are done using with the updates of the program deactivate your pipenv session by doing: % exit
