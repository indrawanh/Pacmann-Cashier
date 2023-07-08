from cobatransaksi import Transaction
import random as random
import datetime as dt

customer_name = input("Masukkan nama Anda: ").capitalize()
txn_id = random.randint(000000, 9999999)
date = dt.date.today().strftime('%d-%m-%Y')

print(f"Tanggal:  {date}")
print(f"Selamat datang {customer_name}!")
print(f"ID transaksi :  {txn_id}")

txn_123 = Transaction()

while True:
    print("Selamat datang di Supermarket Andi!\n"
          "Pilih menu 1 untuk memasukkan barang ke keranjang belanja!")
    print("1 - Tambah Produk")
    print("2 - Update Nama Produk")
    print("3 - Update Jumlah Produk")
    print("4 - Update Harga Produk")
    print("5 - Hapus Produk")
    print("6 - Kosongkan Keranjang")
    print("7 - Cek Keranjang")
    print("8 - Selesai")

    menu = input("Pilih menu: ")

    if menu == '1' :
        add = True
        while add:
            try:
                item_nama = str(input("Masukkan nama item: "))
                item_jumlah= int(input(f"Masukkan jumlah {item_nama}: "))
                item_harga= int(input(f"Masukkan harga {item_nama} Rp."))
            
            except ValueError:
                print("Input jumlah item dan harga item salah!\n"
                      "Input berupa angka ya ^^")
                item_nama = input("Masukkan nama item: ")
                item_jumlah= int(input(f"Masukkan jumlah {item_nama}: "))
                item_harga= int(input(f"Masukkan harga {item_nama} Rp."))

            txn_123.add_item([item_nama, item_jumlah, item_harga])

            add_new_item = input("Tambah item baru ke kerangjang? Ya(y) atau Tidak (n)")
            if add_new_item.lower() == 'y':
                pass
            elif add_new_item.lower () == "n" :
                print("Menuju menu utama")
                break
            else:
                print("Input harus berupa y atau n ")
                print("Menuju menu utama")
                break
            
    elif menu == '2' :
         item_nama_lama = input("Masukkan nama item yang akan diganti: ")
         item_nama_baru = input(f"Masukkan nama baru untuk {item_nama}: ")
         txn_123.update_item_name(item_nama_lama, item_nama_baru)
    
    elif menu == '3' :
        try :
             item_nama = input("Masukkan nama item: ")
             item_jumlah_baru = int(input(f'Masukkan jumlah baru untuk {item_nama}: '))

        except ValueError:
            print("Jumlah item baru harus diisi dengan angka ya!")
            item_nama = input("Masukkan nama item: ")
            item_jumlah_baru = int(input(f'Masukkan jumlah baru untuk {item_nama}: '))
            txn_123.update_item_qty(item_nama, item_jumlah_baru)

    elif menu == '4' :
        try :
             item_nama = input("Masukkan nama item: ")
             item_harga_baru = int(input(f'Masukkan harga baru untuk {item_nama}: '))

        except ValueError:
            print("Harga item baru harus diisi dengan angka ya!")
            item_nama = input("Masukkan nama item: ")
            item_harga_baru = int(input(f'Masukkan harga baru untuk {item_nama}: '))
        
        txn_123.update_item_price(item_nama, item_harga_baru)

    elif menu == '5' :
        item_nama = input("Masukkan nama item yang akan dihapus dari keranjang!")
        txn_123.delete_item(item_nama)
    
    elif menu == '6' :
        print("Semua item akan dikeluarkan dari keranjang!")
        txn_123.reset_transaction()

    elif menu == '7' :
        print("Keranjang akan diperiksa!")
        txn_123.check_order()

    elif menu == '8' :
        break

txn_123.check_order()

total = txn_123.total_price()
print(f"Terimakasih {customer_name} telah berbelanja di Supermarket Andi^^")       