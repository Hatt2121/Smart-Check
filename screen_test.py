import screen as s
from time import sleep


items = ["Dart Gun", "Water Bottle", "Paper", "Books"]
s.print_main(items)
sleep(5)

s.turn_in(items[1])
items.remove(items[1])
sleep(5)

s.turn_in(items[0])
sleep(5)