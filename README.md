###### **Backend is project online store**

Swagger on url: /swagger/, /swagger.json

RESTful API online store for the sale of phones

Install docker <https://docs.docker.com/engine/install/>_

**Install docker-compose:**

    pip install docker-compose

**Clone project:**

    cd /path/to/project

**How start?**

**Start the environment** (it will take a long time to build for the first time):

    make dev

**Stoped:**

    make stop

**How enter?**

    Open browser: 0.0.0.0:5000 <http://0.0.0.0:5000>_

**How test?**

    make test

**If there are problems with migrations?**

    make clean

**The rest of the commands can be found by running:**

    make

**Create super user**
    
    make sh
    python manage.py create_super_user

    login super@user.do
    pass 12312300
    

**Main modules project:**

BlogAPI


1. env files all settings

Apps
djangoBlogAPI - keep main module on project
users - keep module registration customer
blog_api - keep module CRUD blogs
core - auxiliary functions