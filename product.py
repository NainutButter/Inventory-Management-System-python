class Product:
    """
    คลาสสำหรับเก็บข้อมูลสินค้า
    """
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id.strip()
        self.name = name.strip()
        self.price = max(price, 0.01)  # ป้องกันราคาเป็น 0 หรือติดลบ

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price:.2f} THB"