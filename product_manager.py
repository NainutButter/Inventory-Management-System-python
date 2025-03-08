from product import Product  # Ensure this import statement is correct

class ProductManager:
    """
    คลาสสำหรับจัดการสินค้า (เพิ่ม, ลบ, อัปเดตราคา, แสดงสินค้า)
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        if not product.product_id:
            print("❌ Error: Product ID cannot be empty!")
            return
        if product.product_id in self.products:
            print("❌ Error: Product ID already exists!")
        else:
            self.products[product.product_id] = product
            print("✅ Product added successfully!")

    def remove_product(self, product_id: str):
        product_id = product_id.strip()
        if not product_id:
            print("❌ Error: Product ID cannot be empty!")
            return
        if product_id in self.products:
            del self.products[product_id]
            print("✅ Product removed successfully!")
        else:
            print("❌ Error: Product not found!")

    def update_price(self, product_id: str, new_price: float):
        product_id = product_id.strip()
        if not product_id:
            print("❌ Error: Product ID cannot be empty!")
            return
        if product_id in self.products:
            self.products[product_id].price = max(new_price, 0.01)  # ป้องกันราคาติดลบ
            print("✅ Product price updated successfully!")
        else:
            print("❌ Error: Product not found!")

    def show_products(self):
        if self.products:
            print("\n📦 Product List:")
            for product in self.products.values():
                print(product)
        else:
            print("⚠️ No products available.")