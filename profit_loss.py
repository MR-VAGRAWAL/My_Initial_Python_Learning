buying_price = eval(input("Enter the purchase price : \n"))
selling_price = eval(input("Enter the selling price : \n"))
if buying_price > selling_price :
    print(f"Loss of Rs{buying_price - selling_price}")
elif selling_price > buying_price :
    print(f"Profit of Rs{selling_price - buying_price}")
else:
    print("No Profit No Loss")