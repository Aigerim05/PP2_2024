import psycopg2
from config import load_config
import csv

def insert_data(first_name, phone_number):
    """ Insert a new vendor into the vendors table """

    sql_username = """INSERT INTO username(first_name)
             VALUES(%s)"""
    sql_phone_number = """INSERT INTO phone_number(phone_number)
             VALUES(%s)"""
    
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement

                cur.execute(sql_username, (first_name,))
                cur.execute(sql_phone_number, (phone_number,))

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    


ans = input("Press 1 if console, press 2 if csv: ")

if ans == '1' and __name__ == '__main__':
    first_name = input("First Name: ")
    phone_number = input("Phone Number: ")
    insert_data(first_name, phone_number)

if ans == '2' and __name__ == '__main__':
    with open('data.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            insert_data(line[0], line[1])

