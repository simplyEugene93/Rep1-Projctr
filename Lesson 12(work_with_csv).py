import random
import csv
from  collections import Counter
# Create file with some content.
# Create second file and copy content of the first file to the second file in upper case.

with open("E:\PyCharmProjects\Python\PRJCTR_2.txt", "w") as file_1:
    with open("E:\PyCharmProjects\Python\PRJCTR.txt", "r") as file_2:
        for line in file_2:
            file_1.write(line.upper())

# 3. Write a program that will simulate user score in a game. Create a list with 5 player's names.
# After that simulate 100 games for each player. As a result of the game create a list with
# player's name and his score (0-1000 range). And save it to a CSV file.
# File should looks like this:

#  Player name, Score
#    Josh, 56
#    Luke, 784
#    Kate, 90
#    Mark, 125
#    Mary, 877
#    Josh, 345


list_of_players = ["Josh", "Luke", "Kate", "Mark", "Mary"]


def random_list(list_of_players):
    score_list = []

    for i in range(100):
        for item in list_of_players:
            game_score = (random.randint(0, 1000))
            value_1 = item, game_score
            score_list.append(value_1)

    fields = ["Player name", "Score"]

    with open("projtr(new).csv", "w", newline='') as file:

        rows = score_list
        csv_writer = csv.writer(file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


print(random_list(list_of_players))



# 4. Write a script that reads the data from previous CSV file and creates a new file
# called high_scores.csv where each row contains the player name and their highest score.
# Final score should sorted by descending of highest score


def highest_score():

    with open('projtr(new).csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)
        data = [tuple(row) for row in reader]
    return data


def sort_Tuple(tup):
    tup.sort(key=lambda x: x[1], reverse=True)
    return tup
tup = highest_score()


def best_result():
    best_result = []

    for i in sort_Tuple(tup):
        if i[0] not in best_result:
            best_result.append(i[0])
            best_result.append(i[1])
        else:
            continue
    return tuple(best_result)


def create_csv():
    fields = ["Player name", "Score"]
    with open("best_score.csv", "w", newline='') as file:

        it = iter(best_result())
        list_of_tuples = zip(it, it)
        rows = list_of_tuples
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(rows)


print(create_csv())
