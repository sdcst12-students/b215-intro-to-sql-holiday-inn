#!python

"""
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
"""
import sqlite3
from datetime import date
class database:
    def __init__(self):
        file = "mqt.db"
        conec = sqlite3.connect(file)
        cursor = conec.cursor()
        query = """
        create table if not exists customers (
            id integer primary key autoincrement,
            petname tinytext,
            species tinytext,
            breed tinytext,
            name tinytext,
            phonenum integer,
            email tinytext,
            balance int,
            firstdate date);"""
        print("Welcome to pet store database")
        data = ["ID","Pet Name","Pet Species", "Pet Breed", "Owner Name","Phone Number","Email","Balance Owed","First Date of Visit"]
        while True:
            
            inp = input("\nWhat would you like to do???:  -->").strip()
            if inp == "add":
                pname = input("Enter pet name: ")
                species = input("Enter pet species: ")
                breed = input("Enter pet breed: ")
                rname = input("Enter your name: ")
                while True:
                    try:
                        pnum = int(input("Enter phone number: "))
                        break
                    except:print("Enter valid input");pass

                email = input("Enter email: ")
                balance = 0
                fdate = date.today()
                print("Account created")
                query = f"""insert into customers (petname,species,breed,name,phonenum,email,balance,firstdate) values ('{pname}','{species}','{breed}','{rname}',{pnum},"{email}",{balance},"{fdate}");"""
                cursor.execute(query)
                conec.commit()
            elif inp == "getwid":
                while True:
                    try:
                        sinput = int(input("enter id: "))
                        break
                    except: print("invalid input");pass
                query = f"select * from customers where id = {sinput}"
                cursor.execute(query)
                result = cursor.fetchall()
                for i in range(len(result[0])):
                    print(f"{data[i]}: {result[0][i]}")
            elif inp == "getwemail":
                while True:
                    try:
                        sinput = input("enter email: ").strip()
                        break
                    except: print("invalid input");pass  
                query = f"select * from customers where email = '{sinput}'"
                cursor.execute(query)
                result = cursor.fetchall()
                for i in range(len(result[0])):
                    print(f"{data[i]}: {result[0][i]}")
            elif inp == "getwphonenumber":
                while True:
                    try:
                        sinput = int(input("enter phone number: ").strip())
                        break
                    except: print("invalid input");pass
                query = f"select * from customers where phonenum = {sinput}"
                cursor.execute(query)
                result = cursor.fetchall()
                for i in range(len(result[0])):
                    print(f"{data[i]}: {result[0][i]}")
            elif inp == "exit":break 
            elif inp == "printall":
                query = f"select id from customers"
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
            else:print("enter valid input(add, getwid, getwemail, getwphonenumber,exit)")
database()