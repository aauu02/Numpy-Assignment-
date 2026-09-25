import numpy as np

prices = np.array([199, 299, 399, 499, 599])

print("First price:", prices[0])
print("Last price:", prices[-1])



scores = np.array([
    [45, 60, 72, 80, 55],
    [50, 65, 70, 85, 60],
    [40, 58, 75, 78, 62]
])

result = scores[:, 1:4]

print("Scores for matches 2 to 4:")
print(result)




ratings = np.array([4.5, 3.8, 4.2, 2.9, 5.0, 3.5])

print("Last three ratings:", ratings[-3:])




numbers = np.arange(1, 21)

result = numbers[1::3]

print("Every 3rd number starting from the second element:", result)



prices = np.array([250, 650, 450, 800, 350, 1200, 499, 750])

result = prices[prices > 500]

print("Prices greater than 500:", result)



scores = np.array([210, 180, 195, 220, 205, 175])

indices = np.where(scores > 200)

print("Indices of scores above 200:", indices[0])