import psycopg2
from config import load_config

def update_data(first_name, phone_number, ans):

    sql1 = """ UPDATE phonebook
                SET first_name = %s
                WHERE phone_number = %s"""
    
    sql2 = """ UPDATE phonebook
                SET  phone_number = %s
                WHERE first_name = %s"""

    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                if ans == '1':
                    cur.execute(sql1, (first_name, phone_number))

                if ans == '2':
                    cur.execute(sql2, (phone_number, first_name))

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

ans = input("Enter 1 if set new name and enter 2 if set new phone: ")

if __name__ == '__main__':
    if ans == '1':
        new_name = input("new name: ")
        old_phone = input("to what phone number: ")
        update_data(new_name, old_phone, ans)

    if ans == '2':
        new_phone = input("new phone: ")
        old_name = input("to what first_name: ")
        update_data(old_name, new_phone, ans)