# Self-Service Cashier System
Self-Service Cashier System sederhana dengan menggunakan bahasa pemrograman python
## Background Problem
Andi merupakan seorang pemiliki supermarket besar di salah satu kota di Indonesia. Andi berencana melakukan perbaikan proses bisnis
dengan cara membuat kasir self-service di supermarket miliknya yang dapat digunakan pelanggan untuk 
memasukkan item, jumlah item, harga item dan fitur lainnya hingga ke tahap pembayaran.

## Feature Requirements
1 Membuat ID transaksi customer dengan membuat objek baru 

2 Membuat fungsi untuk `add_item()` dengan parameter `nama_item`, `jumlah_item`, `harga_item`

3 Membuat fungsi untuk `update_item_name`, `update_item_quantity`, `update_item_price` berdasarkan `nama_item`

4 Membuat fungsi untuk `delete_item` untuk menghapus salah satu item berdasarkan  `nama_item`

5 Membuat fungsi untuk `reset_transaction` untuk menghapus semua transaksi

6 Membuat fungsi untuk `check_order` untuk mengecek detail item yang telah diinput

7 membuat fungsi untuk menghitung `total_price` untuk mengetahui detail pembayaran, dengan ketentuan diskon :
  - Jika total belanja di atas Rp.200.000 maka akan mendapatkan diskon 5%
  - Jika total belanja di atas Rp.300.000 maka akan mendapatkan diskon 8%
  - Jika total belanja di atas Rp.500.000 maka akan mendapatkan diskon 10%
    
## Alur Program / Flowchart
![New Flowchart](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/0883d45f-b97e-4160-8d4e-dc244f881637)

## Test Case
1 Membuat ID transaksi customer dengan membuat objek baru 

![Pacmann_Project_Python_Menu Utama](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/9006f1ef-8ffa-4555-8efc-7cd87e7aa7bf)


2 Membuat fungsi untuk `add_item()` dengan parameter `nama_item`, `jumlah_item`, `harga_item`
![Pacmann_Project_Python_add item_2](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/2a742f29-eee5-41b6-bed5-ac321a8cfb12)



3 Membuat fungsi untuk `update_item_name`, `update_item_quantity`, `update_item_price` berdasarkan `nama_item`

`nama_item`, 
![Pacmann_Project_Python_update item_2](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/18113a52-a8d5-4b7e-bd80-55ceb9878bf2)

`jumlah_item`
![Pacmann_Project_Python_update jumlah](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/8ef1607d-1cd1-4202-b30c-df2ccdceff9d)

`harga_item`
![Pacmann_Project_Python_update harga](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/b1ce529a-4db5-4b1d-947c-059648d4433c)

4 Membuat fungsi untuk `delete_item` untuk menghapus salah satu item berdasarkan  `nama_item`
![Pacmann_Project_Python_hapus item](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/283859a3-4a90-4d63-9254-759bcaa8fe3f)

5 Membuat fungsi untuk `reset_transaction` untuk menghapus semua transaksi
![Pacmann_Project_Python_reset item](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/a3eda489-8a34-498f-a49b-a346356b84c1)


6 Membuat fungsi untuk `check_order` untuk mengecek detail item yang telah diinput
![Pacmann_Project_Python_cek kerangjang_isi](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/ff252055-1f10-4ba5-bb5d-ce674443d1a7)

Bila keranjang kosong
![Pacmann_Project_Python_cek kerangjang_kosong](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/96e463d3-55b3-4882-8369-e5014c3addbb)

7 membuat fungsi untuk menghitung `total_price` untuk mengetahui detail pembayaran, dengan ketentuan diskon
![Pacmann_Project_Python_total_diskon](https://github.com/indrawanh/Pacmann-Cashier/assets/68576233/e3001c3c-e107-4553-9cff-52b88534c016)


## Conclusion
Project cashier dengan python memudahkan dalam mengelola proses transaksi pembelian barang di supermarket Andi. Dalam project ini menggunakan class Transaction dengan berbagai methods di dalamnya. Method-method tersebut digunakan untuk mengelola data transaksi yang masuk seperti:
-menambahkan item, harga item dan jumlah item, 
-mengubah data produk
-melakukan pengecekan keranjang
-menghapus produk di keranjang
-mereset daftar belanja 
-melakukan pembayaran serta menghitung diskon yang didapat.

## Future Work
1.  Kedepannya program ini dapat menambahkan fitur yang lebih lengkap seperti kode barang atau katalog dan paket diskon untuk meningkatkan kepuasan pembeli dan penjualan
2.  Perbaikan visual program untuk memudahkan user 

## Video
Penjelasan dalam bentuk video dapat dilihat pada link berikut
https://www.youtube.com/channel/UCwFUL7-Lyae8YMiBTMFEM6w




