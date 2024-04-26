import psycopg2
from config import load_config

def add_user(first_name, phone_number):
    # read database configuration
    params = load_config()
    
    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                cur.execute('CALL add_new_user(%s,%s)', (first_name, phone_number))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

first_name = input('new user name: ')
phone_number = input('new phone number: ')

if __name__ == '__main__':
    add_user(first_name, phone_number)