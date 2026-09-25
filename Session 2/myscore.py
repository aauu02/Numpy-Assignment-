import numpy as np

# Last 5 Zomato order ratings
my_scores = np.array([5, 4, 3, 5, 4])

print("My Zomato ratings:")
print(my_scores)

# Even numbers from 10 to 30
even_numbers = np.arange(10, 31, 2)

print("\nEven numbers from 10 to 30:")
print(even_numbers)

# 8 equally spaced values between 0 and 1

values = np.linspace(0, 1, 8)
print("\n8 equally spaced values:")
print(values)

# Flipkart-style Add to Cart counter
cart = np.zeros(10)

# Update the 3rd and 7th items
cart[2] = 1
cart[6] = 1

print("\nUpdated cart:")
print(cart)

# Generate random OTP codes
np.random.seed(42)

otp_codes = np.random.randint(1000, 10000, 6)

print("\nRandom OTP codes:")
print(otp_codes)
