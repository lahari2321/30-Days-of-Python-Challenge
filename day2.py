expenses = [
    ("Food", 250),
    ("Transport", 120),
    ("Shopping", 800),
    ("Food", 300),
    ("Bills", 1500),
    ("Transport", 100)

]

amount=[item[1] for item in expenses]
print("Total Expense:", sum(amount))
print("Highest Expense:", max(amount))
print("Lowest Expense:", min(amount))
print("Average Expense:", round(sum(amount)/len(amount), 2))


category_details={}

for item in expenses:
    category=item[0]
    amount=item[1]
    if category in category_details:
        category_details[category]+=amount
    else:
        category_details[category]=amount
print("\nCategory Summary:")
for category,total in category_details.items():
    print(f"{category} --> {total}")

