import screen as s
from time import sleep


h = s.Screen()
items = ["Dart Gun", "Water Bottle", "Paper", "Books"]

h.print_main(items)
sleep(5)

h.turn_in(items[1])
h.Clear()