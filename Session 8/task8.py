import numpy as np

teams = np.array([
    "CSK", "MI", "RCB", "CSK", "KKR",
    "MI", "GT", "RCB", "GT", "PBKS"
])

unique_teams = np.unique(teams)

print("Unique teams:", unique_teams)


ratings = np.array([4.5, 4.2, np.nan, 3.8, np.nan, 4.7, 4.0])

missing_ratings = np.isnan(ratings)

print("Missing values:", missing_ratings)
print("Number of missing ratings:", np.sum(missing_ratings))



prices = np.array([50, 150, 450, 800, 1200, 2500, 999])

clipped_prices = np.clip(prices, 100, 1000)

print("Original prices:", prices)
print("Clipped prices:", clipped_prices)


views = np.array([
    1000, 2500, np.nan, 5000,
    np.inf, 3500, np.nan, np.inf
])

finite_values = views[np.isfinite(views)]
max_finite = np.max(finite_values)

views[np.isnan(views)] = 0
views[np.isinf(views)] = max_finite

print("Updated views:", views)




numbers = np.array([11, 24, 37, 42, 55, 68, 71, 80, 93, 100])

even_indices = np.where(numbers % 2 == 0)

print("Array:", numbers)
print("Indices of even numbers:", even_indices[0])
