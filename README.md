# My project - MongoDB – Flask application
An sqlite database is connected, cleaned up and written to MongoDB.


## Description
This code creates a Flask Application, connects to the sqlite database, cleans the company names, normalizes the
capitalization, and records them in the MongoDB database as a dictionary.

### Dependencies

* modules:  sqlite3, pandas, IPython.display, re, pymongo, flask

* SQLite database manipulation application: DB Browser (SQLite);
* An application for connecting to the MongoDB database: Compass

### Functions

* konektiranjesosqlite - connecting to db with sqlite (with connection and cursor)

* procistuvanje - Cleaning up the names of unwanted companies  characters, to be without their
legal entity, word decapitalization

*home - is executed in @app.route, where it reads from the sql database, calls the cleanup function, 
creates a Mongo database with this data in the form of a dictionary.