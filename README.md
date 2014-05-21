Lisa-graph Project
========
Project developed during hackathon [hack4medAND](http://hack4med.homerproject.eu/andalusia/ "hack4med ")

Our tool enable relations between uploaded CSVs field files. 
We enable smarte use of datasets provided to HomerProject organizations.

![system diagram](https://dl.dropboxusercontent.com/u/3620266/hack4med.png "lisa-graph")

How to deploy it.
========

Dependencies.
*   pip 
*   mongodb

To install all:

3.  make initial


To install python modules and run the application:

    cd lisa_graph
    pip install -r requirement.txt
    source bin/activate
    service mongodb start #ubuntu call
    python manage.py runserver_plus
    
Now open in a web browse:
    http://localhost:8080
