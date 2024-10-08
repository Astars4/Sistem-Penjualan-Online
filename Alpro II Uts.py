class Seller:
    def __init__(self, name, shipping_cost):
        self.name = name
        self.shipping_cost = shipping_cost
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print(f"Produk dari {self.name}:")
        for product in self.products:
            product.show_product_info()

class Product:
    def __init__(self, id, name, price, merk, seller, category):
        self.id = id
        self.name = name
        self.price = price
        self.merk = merk
        self.seller = seller
        self.category = category

    def show_product_info(self):
        print(f"{self.name} ({self.category}) - Rp {self.price}")

class PhysicalProduct(Product):
    def __init__(self, id, name, price, merk, seller, category, weight):
        super().__init__(id, name, price, merk, seller, category)
        self.weight = weight

    def show_product_info(self):
        super().show_product_info()
        print(f"Weight: {self.weight} grams")

class User:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{self.name} menambahkan {product.name} ke keranjang.")

    def checkout(self):
        total_price = 0
        shipping_cost_per_seller = {}

        print(f"{self.name} melakukan checkout:")
        for product in self.cart:
            total_price += product.price

            if product.seller.name not in shipping_cost_per_seller:
                shipping_cost_per_seller[product.seller.name] = product.seller.shipping_cost
            print(f"- {product.name} dari {product.seller.name}: Rp {product.price}")

        total_shipping = sum(shipping_cost_per_seller.values())
        total = total_price + total_shipping

        print(f"Total harga: Rp {total_price}")
        print(f"Total ongkir: Rp {total_shipping}")
        print(f"Total keseluruhan: Rp {total}")
        return total

class Order:
    def __init__(self, user, total_price):
        self.user = user
        self.total_price = total_price

    def show_order_details(self):
        print(f"Pesanan untuk {self.user.name} dengan total Rp {self.total_price} telah dibuat.")

if __name__ == "__main__":
    seller1 = Seller("Toko Aringo computer", 12000)
    seller2 = Seller("Toko Buku Bagus", 15000)

    product1 = PhysicalProduct(1, "Nebula", 85000, "Gramedia", seller2, "Buku", 350)
    product2 = PhysicalProduct(2, "Printer Canon", 950000, "Canon", seller1, "Elektronik", 3000)
    product3 = PhysicalProduct(3, "Pc ASUS", 9020000, "ASUS", seller1, "Komputer", 15000)
    product4 = PhysicalProduct(4, "Kursi Gaming", 1975000, "Rexus", seller1, "Furniture", 20200)
    product5 = PhysicalProduct(5, "Pulpen", 3000, "Pilot", seller2, "Alat Tulis", 20)
    product6 = PhysicalProduct(6, "Kertas HVS A4", 25000, "SiDU", seller2, "Alat Tulis", 80)

    seller1.add_product(product2)
    seller1.add_product(product3)
    seller1.add_product(product4)
    seller2.add_product(product1)
    seller2.add_product(product5)
    seller2.add_product(product6)

    seller1.list_products()
    seller2.list_products()

    user1 = User("Nita")
    user2 = User("Arifin")

    user1.add_to_cart(product1)
    user1.add_to_cart(product2)
    user1.add_to_cart(product3)
    user2.add_to_cart(product4)
    user2.add_to_cart(product5)
    user2.add_to_cart(product6)

    totals_user1 = user1.checkout()
    totals_user2 = user2.checkout()

    order1 = Order(user1, totals_user1)
    order1.show_order_details()

    order2 = Order(user2, totals_user2)
    order2.show_order_details()