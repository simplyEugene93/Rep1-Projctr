from connect import conn, cur


cur.execute("""CREATE TABLE guests (
             id INTEGER PRIMARY KEY,
             name text
             )""")

conn.commit()


cur.execute("""CREATE TABLE hosts (
              id INTEGER PRIMARY KEY,
              name text
              )""")

conn.commit()


cur.execute("""CREATE TABLE rooms (
            id INTEGER PRIMARY KEY, 
            guests_id INTEGER,
            hosts_id INTEGER, 
            number INTEGER, 
            reviews text, 
            price INTEGER, 
            room conditions text, 
            amount of residents INTEGER,
            FOREIGN KEY (guests_id)
                REFERENCES guests (id),
            FOREIGN KEY (hosts_id)
                REFERENCES hosts (id)
            
        )""")

conn.commit()


cur.execute("""CREATE TABLE reservation (
            id INTEGER PRIMARY KEY, 
            guests_id INTEGER, 
            hosts_id INTEGER, 
            room_number INTEGER, 
            data_of_reservation text, 
            FOREIGN KEY (guests_id)
                REFERENCES guests (id),
            FOREIGN KEY (hosts_id)
                REFERENCES hosts (id)
            
        )""")


conn.commit()
conn.close()