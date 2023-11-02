print("Welcome to the tip calculator.")
sum = float(input("what was the total bill ? $"))
tip = int(input("what percentage tip would you like to give ? 10,12, or 15 ?"))
n = int(input("how many people to split the bill ?"))
s = sum + (tip/100)*sum
m = s/n
f = "{:.2f}".format(m)
print(f"Each person should pay: ${f}")