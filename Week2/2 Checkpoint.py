import math

num_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

num_box = math.ceil(num_items/items_per_box)

print(f"For these {num_items} items and packing {items_per_box} per box, you'll need {num_box:.0f} box(es).")