import sys
from product_manager import ProductManager  # Ensure this import statement is correct
from product import Product  # Ensure this import statement is correct

def get_valid_float(prompt: str) -> float:
    """
    รับค่า float ที่ถูกต้องจากผู้ใช้
    """
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:
                return value
            print("❌ Error: Value must be greater than 0!")
        except ValueError:
            print("❌ Error: Please enter a valid number!")


def get_non_empty_input(prompt: str) -> str:
    """
    รับค่า string ที่ไม่ว่างเปล่าจากผู้ใช้
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❌ Error: Input cannot be empty!")


def main():
    manager = ProductManager()

    while True:
        try:
            print("\n📌 Product Management System")
            print("1️⃣ Add Product")
            print("2️⃣ Remove Product")
            print("3️⃣ Update Product Price")
            print("4️⃣ Show Products")
            print("5️⃣ Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                product_id = get_non_empty_input("Enter Product ID: ")
                name = get_non_empty_input("Enter Product Name: ")
                price = get_valid_float("Enter Product Price: ")
                manager.add_product(Product(product_id, name, price))
            elif choice == "2":
                product_id = get_non_empty_input("Enter Product ID to Remove: ")
                manager.remove_product(product_id)
            elif choice == "3":
                product_id = get_non_empty_input("Enter Product ID to Update: ")
                new_price = get_valid_float("Enter New Price: ")
                manager.update_price(product_id, new_price)
            elif choice == "4":
                manager.show_products()
            elif choice == "5":
                print("👋 Exiting... Have a nice day!")
                sys.exit(0)
            else:
                print("❌ Invalid choice! Please try again.")
        except KeyboardInterrupt:
            print("\n🚨 Program interrupted. Exiting safely...")
            sys.exit(0)
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    main()
