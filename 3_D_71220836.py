brand = input('Masukkan brand apa saja yang hendak dibeli (pisahkan dengan koma):').split(',')
brand1 = brand.split()[0]
brand2 = brand.split()[1]
brand3 = brand.split()[2]
brand4 = brand.split()[3]
while brand<5:
    harga1 = input(f'Berapa harga barang {brand1} ?:')
print(f'Harga {brand1}       Rp. {harga1} Diskon Rp. {diskon1}')
harga2 = input(f'Berapa harga barang {brand2} ?:')
print(f'Harga {brand2}       Rp. {harga2} Diskon Rp. {diskon2}')
harga3 = input(f'Berapa harga barang {brand3} ?:')
print(f'Harga {brand3}       Rp. {harga3} Diskon Rp. {diskon3}')
harga4 = input(f'Berapa harga barang {brand4} ?:')
print(f'Harga {brand4}       Rp. {harga4} Diskon Rp. {diskon4}')