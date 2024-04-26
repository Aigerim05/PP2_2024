import psycopg2
from config import load_config


def delete(deleting_item, ans):
    # read database configuration
    params = load_config()
    
    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                cur.execute('CALL delete_user(%s,%s)', (deleting_item, ans))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

ans = input('press 1 if delete by name, press 0 if delete by phone_number: ')
deleting_item = input('deleting item: ')

if __name__ == '__main__':
    delete(deleting_item, ans)