
print("\n Q2 Mutable vs Immutable")

#Tuple 

tuple = (4, 5, 6)
print("Original tuple:", tuple)
try:
    tuple[1] = 7
except TypeError as e:
    print("Error when trying to modify tuple:", e)

#List 

list = [4, 5, 6]
print("Original list:", list)
list[1] = 77
print("Modified list:", list)


#Dictionary

dictionary = {"name": "layba", "age": 21}
print("Original dictionary:", dictionary)
dictionary["age"] = 24
print("Modified dictionary:", dictionary)

#Tuple with Lists

tuple_with_lists = ([1, 2, 3], [4, 5, 6])
print("Original tuple with lists:", tuple_with_lists)
tuple_with_lists[0][2] = 10
print("Modified tuple with lists:", tuple_with_lists)


print("\nQ3 User Information Dictionary")


def get_name():
    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()
    return name


def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 < age < 100:
                return age
            else:
                print("Age must be positive and less than 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_email():
    while True:
        email = input("Enter your email: ").strip()
        if "@" in email and "." in email and not (email.startswith("@") or email.endswith(".")):
            return email
        else:
            print("Invalid email format. Try again.")


def get_fav_number():
    while True:
        try:
            fav_num = int(input("Enter your favorite number (1-100): "))
            if 1 <= fav_num <= 100:
                return fav_num
            else:
                print("Favorite number must be between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")



user_info = {
    "name": get_name(),
    "age": get_age(),
    "email": get_email(),
    "favorite_number": get_fav_number()
}


print(f"\nWelcome {user_info['name']}! Your account has been registered with email {user_info['email']}.")


print("\nQ4 Cinema Ticketing System")

def calculate_ticket_price(age, is_student, is_weekend):
    
    if age < 0 or age > 120:
        raise ValueError("Invalid age entered!")

    
    if age < 12:
        price = 5
    elif 13 <= age <= 17:
        price = 8
    elif 18 <= age <= 59:
        price = 12
    else:  
        price = 6

    
    if is_student and age > 12:
        price *= 0.8   

    
    if is_weekend:
        price += 2

    return round(price, 2)



customers = []
total_revenue = 0


while True:
    try:
        num_customers = int(input("Enter number of customers: "))
        if num_customers > 0:
            break
        else:
            print("Number of customers must be greater than 0.")
    except ValueError:
        print("Invalid input. Enter a number.")


for i in range(1, num_customers + 1):
    print(f"\n--- Customer {i} ---")
    
   
    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Invalid input. Enter a number.")
    
    
    student_input = input("Is the customer a student? (yes/no): ").strip().lower()
    is_student = (student_input == "yes")

    
    weekend_input = input("Is it a weekend show? (yes/no): ").strip().lower()
    is_weekend = (weekend_input == "yes")

    
    try:
        ticket_price = calculate_ticket_price(age, is_student, is_weekend)
    except ValueError as e:
        print("Error:", e)
        continue

    
    customers.append({
        "customer_id": i,
        "age": age,
        "is_student": is_student,
        "is_weekend": is_weekend,
        "ticket_price": ticket_price
    })

    total_revenue += ticket_price



if len(customers) >= 4:
    print("\nGroup discount applied (10% off total bill).")
    total_revenue *= 0.9



print("\n Ticket Details ")
for cust in customers:
    print(f"Customer {cust['customer_id']} | Age: {cust['age']} | "
          f"Student: {cust['is_student']} | Weekend: {cust['is_weekend']} | "
          f"Ticket Price: ${cust['ticket_price']}")

print(f"\nTotal Revenue: ${round(total_revenue, 2)}")


if customers:
    highest = max(customers, key=lambda x: x['ticket_price'])
    lowest = min(customers, key=lambda x: x['ticket_price'])

    print(f"Highest Paying Customer: Customer {highest['customer_id']} -> ${highest['ticket_price']}")
    print(f"Lowest Paying Customer: Customer {lowest['customer_id']} -> ${lowest['ticket_price']}")


print("\n Q5  Weather Alert System")

def weather_alert(temp_celsius, condition):
    
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    temp_kelvin = temp_celsius + 273.15

    if temp_celsius < 0 and condition.lower() == "snowy":
        alert = "Heavy snow alert! Stay indoors."
    elif temp_celsius > 35 and condition.lower() == "sunny":
        alert = "Heatwave warning! Stay hydrated."
    elif condition.lower() == "rainy" and temp_celsius < 15:
        alert = "Cold rain alert! Wear warm clothes."
    else:
        alert = "Normal weather conditions."

    return f"{alert}\nTemperature: {temp_celsius}°C, {temp_fahrenheit:.2f}°F, {temp_kelvin:.2f}K"



temp_celsius = float(input("Enter the temperature in Celsius: "))
condition = input("Enter the weather condition: ")
result = weather_alert(temp_celsius, condition)
print("\nWeather Alert System Output:")
print(result)




print("\n Q6 Sales Analytics")
import statistics

def analyze_sales(sales_list):
    
    highest = max(sales_list)
    lowest = min(sales_list)
    median = statistics.median(sales_list)
    return highest, lowest, median


while True:
    try:
        sales_input = input("Enter daily sales ( 5 values): ").split()
        sales_list = [float(x) for x in sales_input] 
        
        if len(sales_list) < 5:
            print("Please enter at least 5 values.")
            continue 
        
        
        highest, lowest, median = analyze_sales(sales_list)
        
        
        print("\n Sales Summary ")
        print(f"Highest sales day: {highest}")
        print(f"Lowest sales day: {lowest}")
        print(f"Median sales: {median}")
        break 
    
    except ValueError:
        print(" Invalid input. Please enter numeric values only.")



print("\n Q7 Inventory Management")
def update_inventory(inventory_dict, item, quantity):
    if item not in inventory_dict:
        print(f"{item} is not available in inventory.")
        return inventory_dict
    
    
    if quantity < 0:
        if inventory_dict[item] + quantity < 0:  
            print(f"Not enough stock for {item}")
        else:
            inventory_dict[item] += quantity
    else:
        inventory_dict[item] += quantity 
    
    return inventory_dict



inventory = {
    "Monitor": 10,
    "Phone": 15,
    "Airpods": 8,
    "Speakers": 12,
    "Laptop": 20
}

print("Initial Inventory:", inventory)


for i in range(3):
    item = input("Enter the item you want to buy: ")
    qty = int(input(f"Enter quantity of {item}: "))
    inventory = update_inventory(inventory, item, -qty)


print("\nUpdated Inventory:", inventory)


most_stocked = max(inventory, key=inventory.get)
least_stocked = min(inventory, key=inventory.get)

print(f"Most stocked product: {most_stocked} ({inventory[most_stocked]} left)")
print(f"Least stocked product: {least_stocked} ({inventory[least_stocked]} left)")
