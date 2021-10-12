import random
import numpy as np

number_of_cards = 60
number_of_simulations = 10000


def have_all_been_collected(arr):
    for i in arr:
        if i == 0:
            return False
    return True


iterations_required = []
for _ in range(number_of_simulations):
    count_cards = [0] * number_of_cards
    iterations = 0
    while not have_all_been_collected(count_cards):
        new_card = random.randint(0, number_of_cards - 1)
        count_cards[new_card] += 1
        iterations += 1
    iterations_required.append(iterations)
# Prints the average number of cards required
print(
    f"Minimum: {np.min(iterations_required)}, Maximum: {np.max(iterations_required)}, Average: {np.average(iterations_required)}"
)
