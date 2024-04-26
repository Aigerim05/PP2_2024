import psycopg2
from config import load_config

def get_names():

    sql = """
    SELECT first_name, phone_number
    FROM username
    INNER JOIN phone_number
    ON username.id = phone_number.id;"""

    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                print("The number of usernames: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_names()        