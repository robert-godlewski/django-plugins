# Summary
This is a list of custom made plugins that Robert Godlewski created to make developing in Django easier.

Plugins in current development:
* tag
* crm

Plugins to create later:
* blog
* store
* user - I think that this one exists but might need to add in some features

# tag
The tag app is really useful for SEO purposes and grouping content together.  It can be used for blogs, stores, crm, cms, etc.

In this app you are able to create, read, and destroy tags in the database.  No updating once it's made, it's made.

# crm
This is a client relation manager app to help keep track of several things.
* Todo list
* list of contacts
* email lists

Other packages might be needed:
* tag

## Todos:
1. Add in full CRUD functionality
2. Create tests
3. Create templates to see the data in views

## Tables
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

## Relational tables
Model Design for client_task: Many To Many
* client_id - int, foreign key to client
* task_id - int, foreign key to task
