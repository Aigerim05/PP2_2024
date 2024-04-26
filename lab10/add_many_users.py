import psycopg2
from config import load_config

def add_user(list_of_new_users):
    # read database configuration
    params = load_config()
    
    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                for user in list_of_new_users:
                    cur.execute('CALL add_new_user(%s,%s)', (user[0], user[1]))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    add_user([('Nina','87089053434'), ('Zak', '87053828686')])