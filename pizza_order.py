Large = int(25)
Medium = int(20)
Small = int(15)
PL = int(3)
PS = int(2)
Cheese = int(1)

print("Please place your order")
pizza_size = None
while pizza_size not in {"L","M","S"}:
    pizza_size = input("Enter L for Large, M for Medium, S for small\n")

pepperoni = None
while pepperoni not in {"Y","y","N","n"}:
    pepperoni = input("Enter Y/y for pepperoni and N/n for no pepperoni\n")

Extra_cheese = None
while Extra_cheese not in {"Y","y","N","n"}:
    Extra_cheese = input("Enter Y/y for Extra Cheese and N/n for no cheese\n")

bill = 0;
if pizza_size == "L":
    if pepperoni in {"Y","y"}:
        if Extra_cheese in {"Y","y"}:
            bill = Large + PL + Cheese
        else:
            bill = Large + PL
    else:
        bill = Large
elif pizza_size == "M":
    if pepperoni in {"Y","y"}:
        if Extra_cheese in {"Y","y"}:
            bill = Medium + PL + Cheese
        else:
            bill = Medium + PL
    else:
        bill = Medium
else:
    if pepperoni in {"Y","y"}:
        if Extra_cheese in {"Y","y"}:
            bill = Small + PS + Cheese
        else:
            bill = Small + PS
    else:
        bill = Small

print("Your final Bill is " + str(bill))     


