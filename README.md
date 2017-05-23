# Dojo Space Allocator
---
[![Coverage Status](https://coveralls.io/repos/github/kevintumbo/Office-space-allocation--Kevin-21/badge.svg?branch=Development)](https://coveralls.io/github/kevintumbo/Office-space-allocation--Kevin-21?branch=Development)
### intro
This is a commandline application that allows you to add people to it and assigns them rooms automatically and reallocates them to various rooms as need arises. The project was developed using and runs on python 3.5 +.

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/Ycv5MPRhdK8/0.jpg)](http://www.youtube.com/watch?v=Ycv5MPRhdK8)

### Getting started
---
To get started you will need to have the following
* Python version 3.5 +
* Python virtialenv
* SQLite3

### Installing
---
Clone this repo by running:

    https://github.com/kevintumbo/Office-space-allocation--Kevin-21.git

Create a virtual environment
Install dependancies:

    $ pip install -r requirements.txt

Run the app in interactive mode by executing

    $ python app.py -i

### Usage
---
    create_room <room_type> <room_name>...
Creates rooms in the Dojo. Using this command, the user should be able to create as many rooms as possible by specifying multiple room names after the create_room command.


    add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either Y or N. The default value if it is not provided is N.

    print_room <room_name>
Prints  the names of all the people in room_name on the screen.

    print_allocations [-o=filename]
Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file. See Appendix 2A for format.

    print_unallocated [-o=filename]
Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the txt file provided.

    reallocate_person <person_identifier> <new_room_name>
Reallocate the person with person_identifier to new_room_name.

    load_people
Adds people to rooms from a txt file. See Appendix 1A for text input format.

    save_state [--db=sqlite_database]
Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.

    load_state <sqlite_database>
Loads data from a database into the application.

### Tests
---

    To run tests, run nosetests or nosetests --with-coverage

### Built With
---

* Python - A verstile programming language
* Sqlite3 - Database Management engine
* SqlAlchemy - ORM that gives application developers the full power and flexibility of SQL.
* Docopt - Python commandline arguement parser

### Authors
---

[Kevin Tumbo](https://github.com/kevintumbo)

### Acknowledgments
---
* Facilitator - Angela mugo
* Andela 21 participants consulted during development
