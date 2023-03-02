from connect import conn, cur
from Classes import Rooms

room_1 = Rooms(1, "Small place but fells dope",
                 25, "TV, wi-fi, air-conditioning, two-side bed", 2)
room_2 = Rooms(2, "Small place and smells weird",
                 18, "TV, air-conditioning, two-side bed", 2)
room_3 = Rooms(3, "Huge number and looks nice",
                 35, "TV, air-conditioning, king-size bed, free snacks", 3)
room_4 = Rooms(3, "Huge number and looks nice",
                 50, "TV, air-conditioning, 2 beds, breakfast", 4)

cur.execute("INSERT INTO guests VALUES (1, 'Maddy')")
cur.execute("INSERT INTO guests VALUES (2, 'John')")
cur.execute("INSERT INTO hosts VALUES (1, 'Julia')")
cur.execute("INSERT INTO hosts VALUES (2, 'Patrick')")

cur.execute("INSERT INTO rooms VALUES (1, 1, 1, :number, :review,\
            :price, :conditions, :amount_of_residents)",
            {"number": room_1.number, "review": room_1.reviews, "price": room_1.price,
             "conditions": room_1.conditions, "amount_of_residents": room_1.amount_of_residents})

cur.execute("INSERT INTO rooms VALUES (2, 1, 1, :number, :review,\
            :price, :conditions, :amount_of_residents)",
            {"number": room_2.number, "review": room_2.reviews, "price": room_2.price,
             "conditions": room_2.conditions, "amount_of_residents": room_2.amount_of_residents})

cur.execute("INSERT INTO rooms VALUES (3, 2, 2, :number, :review,\
            :price, :conditions, :amount_of_residents)",
            {"number": room_3.number, "review": room_3.reviews, "price": room_3.price,
             "conditions": room_3.conditions, "amount_of_residents": room_3.amount_of_residents})

cur.execute("INSERT INTO rooms VALUES (4, 2, 2, :number, :review,\
            :price, :conditions, :amount_of_residents)",
            {"number": room_4.number, "review": room_4.reviews, "price": room_4.price,
             "conditions": room_4.conditions, "amount_of_residents": room_4.amount_of_residents})

cur.execute("INSERT INTO reservation VALUES (1, 1, 1, 1, '24/02/22')")
cur.execute("INSERT INTO reservation VALUES (2, 1, 1, 2, '24/02/22')")
cur.execute("INSERT INTO reservation VALUES (3, 2, 2, 3, '24/02/22')")
cur.execute("INSERT INTO reservation VALUES (4, 1, 2, 4, '24/02/22')")

conn.commit()
conn.close()

