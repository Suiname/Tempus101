"""Carousel

Create a python (.py) file named carousel.py inside your folder. Inside this file solve the following problem: Create an array that represents people hopping off a carousel. The array will store the names of each person on the carousel. Loop through the carousel using a for loop. Every other cycle through the loop (odd), someone will hop off.
Any time a person hops off, print the name of the person who hops off. If no one is hopping off because it is an even cycle, print "still spinning..." Repeat until the carousel is empty.
"""

list_of_people = ["Hailey", "Jason", "Bri", "Kaanan", "Hunter", "Chris"]

for i in range(len(list_of_people)):
	if i % 2 == 0:
		print("still spinning...")
	else:
		print(list_of_people[i])