import numpy as np

# Likes on 7 Instagram posts
likes = np.array([120, 250, 180, 340, 500, 275, 410])

print("Likes:", likes)

print("ndim:", likes.ndim)
print("shape:", likes.shape)
print("size:", likes.size)
print("dtype:", likes.dtype)
print("itemsize:", likes.itemsize)
print("nbytes:", likes.nbytes)

# Daily step counts for 5 days
steps = np.array([
    [3000, 4500],
    [2500, 4000],
    [3500, 5000],
    [2000, 3800],
    [4000, 5500]
])

print("\nOriginal 2D array:")
print(steps)
print("Original shape:", steps.shape)

# Convert 2D array into 1D array
steps_1d = steps.reshape(-1)

print("\n1D array:")
print(steps_1d)
print("1D shape:", steps_1d.shape)

# Convert 1D array back to 2D with 5 rows and 2 columns
steps_2d = steps_1d.reshape(5, 2)

print("\nBack to 2D array:")
print(steps_2d)
print("2D shape:", steps_2d.shape)

# Prices of 12 Zomato food items
food_prices = np.array([
    150, 220, 180, 300,
    250, 175, 400, 320,
    275, 190, 350, 280
])

print("\nOriginal food prices:")
print(food_prices)
print("Original shape:", food_prices.shape)

# Reshape into a 3x4 array
food_2d = food_prices.reshape(3, 4)

print("\n3x4 food price array:")
print(food_2d)

# ravel() converts the array into 1D
ravel_prices = food_2d.ravel()

print("\nUsing ravel():")
print(ravel_prices)

# flatten() also converts the array into 1D
flatten_prices = food_2d.flatten()

print("\nUsing flatten():")
print(flatten_prices)

# resize() changes the shape of the array
resized_prices = np.resize(food_2d, (2, 6))

print("\nUsing resize():")
print(resized_prices)
print("Resized shape:", resized_prices.shape)

# Spotify playlist grid
playlist = np.array([
    [12, 8, 5],    # Playlist 1: Pop, Rock, Indie
    [7, 10, 6],    # Playlist 2: Pop, Rock, Indie
    [15, 4, 9]     # Playlist 3: Pop, Rock, Indie
])

print("\nOriginal Spotify playlist grid:")
print(playlist)

# Transpose using .T
transpose_t = playlist.T

print("\nTranspose using .T:")
print(transpose_t)

# Transpose using np.transpose()
transpose_function = np.transpose(playlist)

print("\nTranspose using np.transpose():")
print(transpose_function)

# Flipkart product ratings
ratings = np.array([
    4, 5, 3, 4, 2,
    5, 4, 5, 3, 4,
    2, 5, 4, 3, 5
])

print("\nOriginal ratings:")
print(ratings)
print("Original shape:", ratings.shape)

# Reshape 1D array into 3 rows and 5 columns
ratings_2d = ratings.reshape(3, 5)

print("\nRatings after reshape:")
print(ratings_2d)
print("Shape:", ratings_2d.shape)

# Convert the 2D array back to 1D
ratings_1d = ratings_2d.flatten()

print("\nRatings after flatten:")
print(ratings_1d)
print("Shape:", ratings_1d.shape)

# Use flatten() when you need an independent copy of the data.
# Use ravel() when you want a 1D view when possible and don't need a separate copy.
