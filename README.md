Lisa-graph Project
========
Project developed during the hackathon [hack4medAND](http://hack4med.homerproject.eu/andalusia/ "hack4med ") in Seville.

Users can upload CSVs files to Lisa-graph. The CSVs are converted in data base tables and then an user can make relations between database tables fields.

The objetive is to do a smarter use of datasets provided to HomerProject organizations.

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
