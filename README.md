# papersplease
Web application to handle conference papers collection

## Deployment

 * Dependencies:
    * python 2 / 3
    * Django >= 1.7
    * psycopg2, only if you use postgresql database

 * Copy the file local\_settings.py.example to local\_settings.py and
   change the default configuration. You should change the SECRET\_KEY and
   configure the database.

 * Run the database migrations:
```
python manage.py migrate
```

 * Create an admin user:
```
python manage.py createsuperuser
```

 * Deploy it in your web server: https://docs.djangoproject.com/en/1.7/howto/deployment/


## How it works

I will explain how to use this web application from the point of view of
the administrator, because the paper author that should upload the file
only can do that and it's not dificult. We'll assume here that the base
path is http://localhost:8000.

First of all, you should login in the admin interface with the superuser
that you created before:

 * http://localhost:8000/admin/

Then you will view all models. You can create more users if you want to
give access. You only need to set as staff and give permissions on paper,
attachment, author and conference models to be able to manage papers.

### Adding a paper to the database

 * http://localhost:8000/admin/papers/paper/add/

You should set a title for the paper, a conference and a list of authors.
You can create from here conferences and authors, clicking in the green
plus, a popup window will be opened and you can add the information here.

### Sending emails to authors

 * http://localhost:8000/admin/papers/paper/

To send an email to authors with a link to upload a paper, you should go to
the list of papers, then select all the papers you want to email, you can
filter using the right filter column or searching by keywords, and to
select all filtered avoiding pagination, you can click on the link that
appears in the top.

Then you can select the action "Send email" from the list of actions and
click in the "Go" button.

An email with a random unique url will be sent to all authors. This url
will only work one time, once the file was uploaded this url won't work
again.

Sendind the email again will create a new url, so previous ones won't work
anymore.

### Downloading papers

 * http://localhost:8000/admin/papers/paper/

To download the papers uploaded you only need to select the papers to
download and then select the action "Download" and click "Go", a tar.gz
file will be downloaded with all attachments.

You can also download individual papers from the detailed view:

 * http://localhost:8000/admin/papers/paper/1/

In the bottom there's the list of paper files attached to this paper, and
you can add, delete or change. There's also a link to the current file.
