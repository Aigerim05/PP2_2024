import psycopg2
from config import load_config


def get_names(limit_num, offset_num):
    """ Get parts provided by a vendor specified by the vendor_id """
    parts = []
    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                cur.callproc('get_part_of_names', (limit_num, offset_num))
                
                # process the result set
                row = cur.fetchone()
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts
    
limit_num = input("limit_num: ")
offset_num = input("offset_num (starts from 0): ")

if __name__ == '__main__':
    parts = get_names(limit_num, offset_num)
    print(parts)