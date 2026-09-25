import numpy as np

my_likes = np.array([120, 150, 180, 200, 175, 220, 250])
friend_likes = np.array([100, 160, 170, 190, 185, 210, 230])

combined = np.add(my_likes, friend_likes)
difference = np.subtract(my_likes, friend_likes)

print("Combined likes:", combined)
print("Difference in likes:", difference)

import numpy as np

prices = np.array([250, 180, 320, 150, 200])

discounted_prices = np.multiply(prices, 0.9)
final_bill = np.sum(discounted_prices)

print("Discounted prices:", discounted_prices)
print("Final bill amount:", final_bill)

import numpy as np

steps = np.array([
    5000, 6500, 7200, 8000, 4500,
    9000, 7500, 6200, 6800, 8200,
    5500, 7000, 7600, 8100, 9300,
    6000, 6700, 7400, 8500, 5000,
    7200, 7800, 8800, 9500, 6900,
    7300, 8100, 8600, 9200, 10000
])

mean_steps = np.mean(steps)
median_steps = np.median(steps)
std_steps = np.std(steps)
max_steps = np.max(steps)

print("Average steps:", mean_steps)
print("Median steps:", median_steps)
print("Standard deviation:", std_steps)
print("Maximum steps:", max_steps)

import numpy as np

ratings = np.array([4.2, 3.7, 4.8, 2.9, 4.5, 3.3, 4.1, 3.9, 4.6, 2.7])

rounded = np.round(ratings)
floored = np.floor(ratings)
ceiled = np.ceil(ratings)

print("Original ratings:", ratings)
print("Rounded ratings:", rounded)
print("Floor ratings:", floored)
print("Ceil ratings:", ceiled)

import numpy as np

skips = np.array([
    1, 0, 1, 0, 0,
    1, 0, 1, 0, 0,
    1, 0, 0, 1, 0,
    0, 1, 0, 0, 1
])

skip_percentage = np.mean(skips) * 100
seventy_fifth_percentile = np.percentile(skips, 75)

print("Percentage of songs skipped:", skip_percentage)
print("75th percentile of skips:", seventy_fifth_percentile)

