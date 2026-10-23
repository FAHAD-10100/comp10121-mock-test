answer = "y"
    while answer == "y":
  weight = float(input("Enter parcel weight in kg: ")) 
cost = weight * 2.50
       print ("Delivery cost: £", cost)
if weight < 2:
       print ("Light")
elif weight > 10:
       print ("Heavy")
else:
       print("standard")
  answer = input("Another parcel to calculate? y/n: ").lower()
