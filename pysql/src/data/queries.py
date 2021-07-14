import psycopg2
from config import config
from psycopg2.sql import Identifier
from psycopg2 import sql

def select_all(table):
    con = None
    cursor = con.cursor()
    SQL = f'SELECT * FROM {table};'
    cursor.execute(SQL)
    dataframe = cursor.fetchall()
    for data in dataframe:
        print(data)
    cursor.close()
    

def insert_data(table, name, storage, url, user):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = sql.SQL("INSERT INTO {} (picturename, bucketname, address, users) VALUES (%s, %s, %s, %s)").format(Identifier(table))
        data = (name, storage, url, user)
        cursor.execute(SQL, data)
        con.commit()
        count = cursor.rowcount
        print(count, f"Record inserted successfully into {table} table")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def column_names(table):
    con = None
    cursor = con.cursor()
    SQL = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}';"
    cursor.execute(SQL)
    dataframe = cursor.fetchall()
    for data in dataframe:
        print(data)
    cursor.close()

def update_table(table):
    con = None
    try:
        print("Table Before updating record ")
        cursor = con.cursor()
        sql_select_query = """select * from person where id = %s"""
        cursor.execute(sql_select_query, (3,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update person set name = %s where id = %s"""
        cursor.execute(sql_update_query, ("Johnny", 3))
        con.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from person where id = %s"""
        cursor.execute(sql_select_query, (3,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

def deleteData(table):
    con = None
    try:
        cursor = con.cursor()

        # Update single record now
        sql_delete_query = """Delete from person where id = %s"""
        cursor.execute(sql_delete_query, (10,))
        con.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

def create_tables():
    """ create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE picturedata (
            id SERIAL PRIMARY KEY,
            picturename VARCHAR(255) NOT NULL,
            bucketname VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            users INT NOT NULL
        );
        """
    con = None
    try:
        con = psycopg2.connect(**config())
        cur = con.cursor()
        cur.execute(command)
        cur.close()
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

#create_tables()
insert_data("picturedata", "glob", "eww", "argh", 9)

#con = None
#try:
#    con = psycopg2.connect(**config())
#    create_tables()
#except (Exception, psycopg2.DatabaseError) as error:
#    print(error)
#finally:
#    if con is not None:
#        con.close()