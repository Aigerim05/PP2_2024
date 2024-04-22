import psycopg2
from config import load_config

def delete_data(first_name):

    
    sql = """DELETE FROM phonebook
                WHERE first_name = %s;"""
    

    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (first_name,))

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

first_name = input("first_name: ")


if __name__ == '__main__':

    delete_data(first_name)
