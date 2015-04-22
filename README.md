Django on Openshift 
-------------------

Quickstart and Document in progress, this will be a quickstart to deploy django 1.7 on Openshift.

This is a repository helps you to install and run Django on Openshift.

Create a python application on Openshift.

     $ rhc app create djangoapp python-2.7

Add this upstream repo.

     $ cd djangoapp
     $ git remote add upstream -m master git://github.com/rancavil/django-openshift-test.git
     $ git pull -s recursive -X theirs upstream master


Now push the repo.

    $ git push
