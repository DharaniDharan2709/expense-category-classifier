import pandas as pd
import random

print("Spinning up the 10-Category Data Factory...")

# ==========================================
# THE VOCABULARY DICTIONARIES
# ==========================================
food = ["starbucks", "mcdonalds", "subway", "kroger", "whole foods", "pizza hut", "taco bell", "local bakery", "wendys", "chipotle"]
transport = ["uber", "lyft", "shell gas", "chevron", "metro", "bus pass", "amtrak", "delta airlines", "exxonmobil", "public transit"]
utilities = ["electric bill", "water bill", "apartment rent", "internet broadband", "verizon", "trash collection", "att mobile", "sewer bill"]
entertainment = ["netflix", "spotify", "hulu", "cinema", "playstation", "xbox", "concert ticket", "disney plus", "hbo max", "steam games"]
shopping = ["amazon", "walmart", "target", "nike", "best buy", "apple store", "ikea", "ebay", "home depot", "macys"]

# --- THE 5 NEW CATEGORIES ---
health = ["cvs pharmacy", "walgreens", "urgent care", "hospital copay", "dentist office", "advil medicine", "prescription refill", "eye doctor", "quest diagnostics", "first aid kit"]
education = ["university tuition", "college textbook", "udemy course", "coursera subscription", "school supplies", "student loan payment", "khan academy donation", "notebooks and pens"]
personal_care = ["haircut salon", "barber shop", "sephora cosmetics", "ulta beauty", "day spa", "manicure pedicure", "skincare products", "shampoo and soap"]
pets = ["petco", "petsmart", "chewy online", "veterinary clinic", "dog food bag", "cat litter", "pet grooming", "flea medication", "dog walker"]
travel = ["marriott hotel", "airbnb booking", "expedia flight", "hertz car rental", "luggage bag", "resort fee", "uber to resort", "vacation cruise"]

data = []

# Generate exactly 1,000 transactions for EACH of the 10 categories (10,000 total rows)
for _ in range(1000):
    data.append({"Description": f"{random.choice(food)} {random.choice(['order', 'payment', 'purchase', ''])}", "Category": "Food"})
    data.append({"Description": f"{random.choice(transport)} {random.choice(['ride', 'ticket', 'station', ''])}", "Category": "Transport"})
    data.append({"Description": f"{random.choice(utilities)} {random.choice(['monthly', 'fee', 'payment', ''])}", "Category": "Utilities"})
    data.append({"Description": f"{random.choice(entertainment)} {random.choice(['subscription', 'membership', 'premium', ''])}", "Category": "Entertainment"})
    data.append({"Description": f"{random.choice(shopping)} {random.choice(['online', 'store', 'checkout', ''])}", "Category": "Shopping"})
    
    data.append({"Description": f"{random.choice(health)} {random.choice(['bill', 'clinic', 'health', ''])}", "Category": "Health"})
    data.append({"Description": f"{random.choice(education)} {random.choice(['fee', 'online', 'store', ''])}", "Category": "Education"})
    data.append({"Description": f"{random.choice(personal_care)} {random.choice(['appointment', 'store', 'routine', ''])}", "Category": "Personal Care"})
    data.append({"Description": f"{random.choice(pets)} {random.choice(['supplies', 'store', 'visit', ''])}", "Category": "Pets"})
    data.append({"Description": f"{random.choice(travel)} {random.choice(['reservation', 'booking', 'trip', ''])}", "Category": "Travel"})

# Clean up extra spaces
for row in data:
    row["Description"] = row["Description"].strip()

# Save the dataset and shuffle the rows so they are mixed up
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True) 
df.to_csv("expenses.csv", index=False)

print("Success! A new 'expenses.csv' file with 10 Categories and 10,000 rows has been created.")