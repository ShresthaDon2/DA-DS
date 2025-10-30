import json 

def load_products():
    products = []
    try:
        file = open("product.txt","r")
        try:
            content = file.read().strip().split("\n")
            for line in content:
                if line:
                    products.append(json.loads(line))
        except json.JSONDecodeError as e :
            print(f"Error decoding Json: {e}")
        finally:
            file.close()
    except FileNotFoundError:
        print("No product file found!!")
    except Exception as e:
        print(f"Error reading file: {e}")
    return products

def save_product(product):
    try:
        file = open("product.txt", "a")
        try:
            file.write(json.dumps(product) + "\n")
        finally:
            file.close()
    except Exception as e:
        print(f"Error writing to file: {e}")

def overwrite_products(products):
    
    try:
        file = open("product.txt", "w")
        try:
            for p in products:
                file.write(json.dumps(p) + "\n")
        finally:
            file.close()
    except Exception as e:
        print(f"Error overwriting file: {e}")

def view_products():
    products = load_products()
    if not products:
        print("No products found.")
    else:
        print("---Product List--")
        for p in products:
            print(f"ID: {p['id']} | Name: {p['name']} | Price: {p['price']} | Qty: {p['quantity']}")
        print("-------------\n")

def add_products():
    products = load_products()
    try: 
        pid = 1 if not products else max(p["id"] for p in products) + 1
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price: "))
        qty = int(input("Enter product quantity: "))
    except ValueError:
        print("Invalid number entered!")
        return
    except Exception as e :
        print(f"Error: {e}")
        return
    product = {"id": pid,"name": name, "price": price,"quantity":qty}
    save_product(product)
    print(f"Product '{name}' added successfully!")
    
def remove_product():
    products = load_products()
    try : 
        pid = int(input("Enter product ID to remove: "))
    except ValueError:
        print("Invalid ID.")
        return
    
    for p in products:
        if p["id"]== pid:
            products.remove(p)
            overwrite_products(products)
            print(f"Product ID {pid} removed.")
            break
    else:
        print("Product not found!")
        
def search_product():
    products = load_products()
    term = input("Enter product name to search: ").lower()
    found = [p for p in products if term in p["name"].lower()]
    if found:
        for p in found:
            print(f"ID: {p['id']} | Name: {p['name']} | Price: {p['price']} | Qty: {p['quantity']}")
    else:
        print("No matching products found.")
        
def main():
    while True:
        print("----E-Commerce Menu---")
        print("1. Add add_products")
        print("2. View add_products")
        print("3. Remove Product")
        print("4. Search Product")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_products()
        elif choice == "2":
            view_products()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            search_product()
        elif choice == "5":
            print("Exiting....")
            break
        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    main()
        
        