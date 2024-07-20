size=input("what pizza size you want ?:")
bill=0
if size=="s" or size=="S":
    bill=100
    print("small_size pizz is 100rs")
elif size=="m" or size=="M":
    bill=200
    print("medium_size pizza is 200rs")
elif size=="l" or size=="L":
    bill=300
    print("large_size pizza is 300rs")
pepperoni=input("Do you want pepperoni..?:")
if pepperoni=="yes":
    if size=="s" or size=="S":
        bill=bill+30
        print(f"your total bill is {bill}")
    else:
        bill=bill+50
        print(f"your total bill is {bill}")
else:
    print("Thank you")
extra_cheese=input("Do you want extra_cheese..?")
if extra_cheese=="yes":
    bill=bill+20
    print(f"your total bill is {bill}")
else:
    print("Thank you")
print("Thank you for ordering pizza.. Have a good day")