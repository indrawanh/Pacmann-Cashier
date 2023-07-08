import tabulate as tabualate

class Transaction:
    def __init__(self):

        self.items = []

    def add_item(self, item):

        self.items.append(item)
        print(f"{item} telah berhasil ditambahkan ke keranjang")
        self.show_items()

    def update_item_name(self, name1, name2):

        for item in self.items:
            if item[0] == name1:
                item[0] = name2

        print(f"Produk diubah! {name1} menjadi {name2}")
        self.show_items()

    def update_item_qty(self, name, qty):

        for item in self.items:
            if item[0] == name:
                item[1] = qty

        print(f"Jumlah produk diubah! menjadi {qty} buah! ")
        self.show_items()

    def update_item_price(self, name, price):

        for item in self.items:
            if item[0] == name:
                item[2] = price

        print(f"Keranjang telah diupdate! {name} menjadi Rp. {price} ")
        self.show_items()

    def delete_item(self, name):

        for item in self.items:
            if item[0] == name:
                self.items.remove(item)

        print(f"{name} telah berhasil dihapus dari keranjang!")       
        self.show_items()

    def reset_transaction(self):
 
        self.items = []

        print(f"Isi keranjang telah dikosongkan!")
        self.show_items()

    def check_order(self):

        if (len(self.items) == 0):
            print("Keranjang belanja Anda kosong!")
        else:
            print("Pesanan dalam Keranjang sudah benar!")
            self.show_items()

    def show_items(self):
        
        print("*" * 50)
        print("Item\t\tQty\tPrice\tTotal Price")
        print("=" * 50)
        for item in self.items:
            total_price = item[1] * item[2]
            print("{}\t\t{}\t{}\t\t{}".format(item[0], item[1], item[2], total_price))
        print("=" * 50)

    def total_price(self):

        total = 0
        for item in self.items:
            total += item[1] * item[2]
        if total > 500000:
            discount = total * 0.1
            print(f'Total belanja sebesar Rp. {total} ')
            print(f'Selamat anda mendapatkan diskon sebesar Rp. {discount}')
            print(f'Total belanja setelah mendapat diskon sebesar Rp. {total - discount}')
        elif total > 300000:
            discount = total * 0.08
            print(f'Total belanja sebesar Rp. {total} ')
            print(f'Selamat anda mendapatkan diskon sebesar Rp. {discount}')
            print(f'Total belanja setelah mendapat diskon sebesar Rp. {total - discount}')
        elif total > 200000:
            discount = total * 0.05
            print(f'Total belanja sebesar Rp. {total} ')
            print(f'Selamat anda mendapatkan diskon sebesar Rp. {discount}')
            print(f'Total belanja setelah mendapat diskon sebesar Rp. {total - discount}')
        else:
            discount = 0
            print(f'Total belanja sebesar Rp. {total}')
            print(f'Maaf anda belum mendapatkan diskon :( Yuk masukkan barang lagi ke keranjang!')
        