menu = {
    "Chicken Biryani": 150,
    "Chicken Fried Rice": 100,
    "Paneer Biryani": 200,
    "Pizza": 150,
    "Burger": 90,
    "Ice Cream": 60,
    "Cold Drinks": 40
}
def display_menu():
        
        print("--------RESTAURANT MENU--------")
        i=1 
        for key,value in menu.items():
            print(i,key,"-",value)
            i=i+1
sales=[]
customer_choice="yes"
while customer_choice=="yes":
    print("Welcome to the Restaurant!")
    
    display_menu() 
    food_items=list(menu.keys()) 
    choice="yes"
    total_cost=0
    order_details=[]
    while choice=="yes":
        while True:
            enter_your_choice=int(input("Enter your favourite food_item serial number:"))
            if 1<=enter_your_choice<=len(food_items):
                break
            else:
                print("Invalid Number!Please choose the number from 1 to 7") 
        selected_item=food_items[enter_your_choice-1]
        while True: 
            quantity=int(input("Enter the Quantity:"))
            if quantity>0:
                break 
            else:
                print("Please enter the positive Number")
        item_cost=menu[selected_item]*quantity
        total_cost=total_cost+item_cost
        food_orders={
            "Food_item":selected_item,
            "Quantity":quantity,
            "Item_cost":item_cost
        
            }
        order_details.append(food_orders)
        print("Your food_item is:",selected_item)
        print("Quantity:",quantity)
        print("Cost:",menu[selected_item])
        print("Total_cost:",item_cost)
    
        choice=input("Do you want to order the another food_item?(Yes/No):")    

    if 500<=total_cost<1500:
        discount=total_cost*10/100
    elif total_cost>=1500:
        discount=total_cost*15/100
    else:
        discount=0 
    net_amount=total_cost-discount 


    print("\n==========Restaurant-Bill==========")
    print("Food Item\tQuantity\tItem-total")
    for food_orders in order_details:
        print(food_orders["Food_item"], "\t", food_orders["Quantity"], "\t", food_orders["Item_cost"])
    print("------------------------------------") 
    print("Total_cost:",total_cost)
    print("The total cost with discount:",net_amount)                
    print("Discount:",discount)   
    print("------------------------------------")
    print("THANK YOU! VISIT AGAIN")
    sales.append(net_amount)
    customer_choice = input("Do you want to process another customer? (yes/no): ")

    
print("\n--------Daily Sales--------")
print("No-of-orders:",len(sales))
print("Total sales:",sum(sales))
print("==============================")



