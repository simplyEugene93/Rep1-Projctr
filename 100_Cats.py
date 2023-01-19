list_of_100_cats = [i for i in range(1,101)]
second_round = [i for i in range(1, 101) if i % 2 == 0]
third_round = [i for i in range(1, 101) if i % 3 == 0]
minus_2st_round = [x for x in list_of_100_cats if x not in second_round]
minus_3st_round = [x for x in minus_2st_round if x not in third_round]
print(f"The cats that still have hats are {minus_3st_round}")
