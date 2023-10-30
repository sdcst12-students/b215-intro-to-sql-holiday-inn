## SDSS Computing Studies Python Assignment
### Assignment #xx <Title> (Total Marks xx)

Objectives:
* Define a table in a database
* Define a record in a table
* Determine the relation between a record and a row
* Connect a python file to a database
* Read data from a database using Python


Writing your data/variables to a file is a quick way of putting data in non-volatile storage, but it is not very efficient.  Think about how many people play an MMORPG - if everyone's data was constantly being written/read from file every time that a player entered or left the game, that would be a lot of disk reading/writing and it would be very slow.  The same would happen with websites that store user or game data.  Not very efficient.

SQL Databases (Structured Query Languages) have become the standard for storing data in a way that is scalable (works for large numbers) as well as fast, although it's like learning a new language in many ways.  We will be looking at SQL databases to see how we can create new data sets (called tables), read from them, search them, update existing entries or add new entries.

We will be using a basic version that connects to a file based database using SQLite3.  Complete documentation is available at https://www.tutorialspoint.com/sqlite/sqlite_python.htm, but you may have more success starting with simple code snippets or tutorials


Assignment:

Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.

