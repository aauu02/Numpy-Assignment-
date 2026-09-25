import numpy as np

zomato = np.array([4.2, 4.5, 3.9, 4.7, 4.1])
swiggy = np.array([4.0, 4.3, 4.6, 3.8, 4.4])

combined = np.concatenate((zomato, swiggy))

print("Combined ratings:", combined)



post1 = np.array([100, 120, 150, 130, 160, 180, 200])
post2 = np.array([80,  90,  110, 125, 140, 155, 170])
post3 = np.array([60,  75,  95,  105, 120, 135, 150])

stacked = np.vstack((post1, post2, post3))

print("Weekly likes:")
print(stacked)


product_ids = np.array([
    101, 102, 103, 104, 105, 106,
    107, 108, 109, 110, 111, 112
])

parts = np.array_split(product_ids, 5)

for i, part in enumerate(parts):
    print("Part", i + 1, ":", part)
    print("Shape:", part.shape)




messages = np.array([
    [20, 25, 30, 18, 22, 28, 35],
    [10, 15, 12, 20, 18, 14, 16],
    [35, 40, 32, 38, 45, 42, 50]
])

new_user = np.array([8, 10, 7, 12, 9, 11, 13])

messages = np.insert(messages, 3, new_user, axis=0)

print("After adding new user:")
print(messages)

total_messages = np.sum(messages, axis=1)

least_user = np.argmin(total_messages)

messages = np.delete(messages, least_user, axis=0)

print("\nAfter removing user with least messages:")
print(messages)



views = np.array([100, 200, 300, 400])

view_array = views.view()
copy_array = views.copy()

view_array[0] = 999
copy_array[0] = 888

print("Original array:", views)
print("View array:", view_array)
print("Copy array:", copy_array)
