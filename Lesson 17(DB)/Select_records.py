from connect import conn, cur


def sort_data():
    select_data = "SELECT reservation.id, guests.name " \
                  "FROM " \
                  "reservation INNER JOIN guests ON guests.id = reservation.guests_id"
    cur.execute(select_data)
    fetch = cur.fetchall()
    return fetch


print(sort_data())


def return_name_and_id():
    select = "SELECT COUNT(reservation.id), guests.name FROM reservation INNER JOIN guests ON " \
             "guests.id = reservation.guests_id WHERE guests.name = 'Maddy'"
    cur.execute(select)
    fetch = cur.fetchall()
    return fetch


print(return_name_and_id())
