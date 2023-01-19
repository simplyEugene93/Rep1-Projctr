### Practice

"""**You have 100 cats.**

One day you decide to arrange all your cats in a giant circle. Initially,
none of your cats have any hats on. You walk around the circle 100 times,
always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat,
you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
1. The first round, you stop at every cat, placing a hat on each one.
2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.

Optional: Make function that can calculate hat with any amount of rounds and cats.

Here you should write an algorithm, after that, try to make pseudo code.
Only after that start to work. Code is simple here, but you might struggle with algorithm.
Therefore don`t try to write a code from the first attempt.

list_of_100_cats = [i for i in range(1,101)]
second_round = [i for i in range(1, 101) if i % 2 == 0]
third_round = [i for i in range(1, 101) if i % 3 == 0]
minus_2st_round = [x for x in list_of_100_cats if x not in second_round]
minus_3st_round = [x for x in minus_2st_round if x not in third_round]
print(f"The cats that still have hats are {minus_3st_round}")
