print('!! Selamat datang di H+ GYM !!')
print('Silahkan pilih menu dibawah ini:')
print('1. Menambah data')
print('2. Menampilkan data')
print('3. Keluar')
pil = int(input('Silahkan masukkan pilihan yang Anda inginkan:'))
if pil==1:
    nama = input('Masukkan nama pelanggan :')
    jenis = input('Masukkan jenis member:')
    data = (nama, jenis)
    print('Data sudah berhasil ditambahkan')
elif pil==2:
    print('-'*20)
    print('Pelanggan        Member:')
    for i in data:
        print(i)
elif pil==3:
    print('Sistem Berhenti...')
else:
    print('error...')