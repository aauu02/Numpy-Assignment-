import numpy as np

# Likes on last 7 Instagram posts
likes = np.array([120, 250, 180, 340, 500, 275, 410])

# Comments on last 7 Instagram posts
comments = np.array([15, 30, 20, 45, 60, 25, 40])

# Calculate engagement for each post
engagement = likes + comments

# Calculate average engagement per post
average_engagement = np.mean(engagement)

print("Engagement per post:", engagement)
print("Average engagement per post:", average_engagement)

# Zomato food prices
prices = np.array([250, 400, 180, 350, 500])

# Discounts in rupees
discounts = np.array([50, 80, 30, 70, 100])

# Calculate final prices using element-wise subtraction
final_prices = prices - discounts

print("\nOriginal prices:", prices)
print("Discounts:", discounts)
print("Final prices:", final_prices)

# IPL team scores for 5 matches
scores = np.array([175, 195, 182, 160, 210])

# Check which scores are greater than 180
high_scores = scores > 180

print("\nIPL scores:", scores)
print("Scores greater than 180:", high_scores)

# Paytm payment status
paytm = np.array([1, 0, 1, 0, 0, 1])

# PhonePe payment status
phonepe = np.array([0, 1, 1, 0, 1, 0])

# Check whether either Paytm or PhonePe was used
either_app = np.logical_or(paytm, phonepe)

print("\nPaytm:", paytm)
print("PhonePe:", phonepe)
print("Paid by either app:", either_app)

# Steps walked each day for one week
weekly_steps = np.array([4500, 6200, 5800, 7000, 5100, 8000, 6500])

# Add 500 bonus steps to every day using broadcasting
bonus_steps = 500
updated_steps = weekly_steps + bonus_steps

# Calculate total steps for the week
total_steps = np.sum(updated_steps)

print("\nOriginal weekly steps:", weekly_steps)
print("Steps after 500-step bonus:", updated_steps)
print("Total steps for the week:", total_steps)
