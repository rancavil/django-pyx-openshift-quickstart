Django on Openshift 
-------------------

This is a repository helps you to install and run Django 1.7 on Openshift.

you can deploy django in three simple steps.

Step 1: Create a python application on Openshift.

     $ rhc app create djangoapp python-2.7
     
or

     $ rhc app create djangoapp python-3.3

Step 2: Add remote upstream.

     $ cd djangoapp
     $ git remote add upstream -m master git://github.com/rancavil/django-pyx-openshift-quickstart.git
     $ git pull -s recursive -X theirs upstream master


Step 3: Now push to deploy.

     $ git push

Finally, you must get the next output, with the user admin and the secret password.

     remote: Creating admin user
     remote: Do not  forget change the password!!!!
     remote: Keep the secret!!!!
     remote: Django application credentials:
     remote: 	user: admin
     remote: 	nG2YMkKjMtkR
     remote: Change it!!!

Go to:

     http://djangoapp-<yourdomain>.rhcloud.com


