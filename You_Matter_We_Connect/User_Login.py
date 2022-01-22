import sqlite3


def create_connection(db_file):
   """ create a database connection to the SQLite database
   """
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except:
       print("Failed to open database")
   return None


def create_table(conn):
   cur = conn.cursor()
   cur.execute("DROP TABLE example")
   cur.execute("CREATE TABLE example (Email VARCHAR, Passwd TEXT, Major TEXT)")


def enter_dynamic_data(conn):
   email = raw_input("Email: ")
   passwd = raw_input("Passwd: ")
   major = raw_input("Major: ")
   cur = conn.cursor()
   cur.execute("INSERT INTO example(Email, Passwd, Major) VALUES (?, ?, ?)", (email, passwd, major))
   conn.commit()


def main():
   database = "account.db"

   # create a database connection

   conn = create_connection(database)

   create_table(conn) # should only be run once
   with conn:
       for i in range(3):
           # update_task(conn)
           enter_dynamic_data(conn)


if __name__ == '__main__':
   main()
