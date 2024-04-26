import psycopg2
from config import load_config

def update_data(first_name, phone_number, ans, id):

    sql_phone_number = """ UPDATE phone_number
                SET phone_number = %s
                WHERE id = %s"""
    
    sql_username = """ UPDATE username
                SET first_name = %s
                WHERE id = %s"""

    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                if ans == '1':
                    cur.execute(sql_username, (first_name, id))

                if ans == '2':
                    cur.execute(sql_phone_number, (phone_number, id))

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

ans = input("Enter 1 if set new name and enter 2 if set new phone: ")
phone_number = None
first_name = None
if __name__ == '__main__':
    if ans == '1':
        new_name = input("new name: ")
        id = input("id: ")
        update_data(new_name, phone_number, ans, id)

    if ans == '2':
        new_phone = input("new phone: ")
        id = input("id: ")
        update_data(first_name, new_phone, ans, id)