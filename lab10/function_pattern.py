import psycopg2
from config import load_config

def get_names_by_phone(pattern):
    
    names = []
    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                cur.callproc('get_names_by_phone', (pattern,))
                
                # process the result set
                row = cur.fetchone()
                while row is not None:
                    names.append(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return names
pattern = input("pattern: ")
if __name__ == '__main__':
    names = get_names_by_phone('8777%')
    print(names)