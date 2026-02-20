class burger: #defines custom burger
	def __init__(self, bun, patty, number_of_patties, cheese, pickles, tomato, onion, sauce):
		self.bun = bun #string
		self.patty = patty #string
		self.number_of_patties = number_of_patties #int
		self.cheese = cheese #int
		self.pickles = pickles #int
		self.tomato = tomato #int
		self.onion = onion #int
		self.sauce = sauce #string

big_tasty = burger("big", "big", 1, 2, 2, 2, 2, "with a smoke tinge") #creates big tasty with its own characteristics
double_cheeseburger = burger("common", "common", 2, 2, 2, 1, 1, "ketchup") #another variable with the class of burger
print(big_tasty.sauce)
print(double_cheeseburger.cheese)