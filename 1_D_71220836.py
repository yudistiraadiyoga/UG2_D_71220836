print('='*15,' MAKANAN ','='*15)
hargatelur = 7000
hargaleleterbang = 10000
hargaEsCoklat = 5000
hargaEsDoger= 13000
print(f'1. Telur Bakar           : Rp {hargatelur}')
print(f'2. Lele Terbang Mas Bhe  : Rp {hargaleleterbang}')
print(f'3. Es Coklat Lempu       : Rp {hargaEsCoklat}')
print(f'4. Es Doger Langensari   : Rp {hargaEsDoger}')
print('')
print('='*15,' PESENAN ','='*15)
jumlahtelurbakar  = int(input('Telur Bakar        :'))
jumlahleleterbang = int(input('Lele Terbang       :'))
jumlahEsCoklat    = int(input('EsCoklat           :'))
jumlahEsDoger     = int(input('EsDoger            :'))
print('')
print('='*15,' TOTAL ','='*15)
totaltelur          = hargatelur*jumlahtelurbakar
totalleleterbang    = hargaleleterbang*jumlahleleterbang
totalEsCoklat       = hargaEsCoklat*jumlahEsCoklat
totalEsDoger        = hargaEsDoger*jumlahEsDoger
totalsemua          = totaltelur+totalleleterbang+totalEsCoklat+totalEsDoger
print(f'TOTAL TELUR BAKAR x {jumlahtelurbakar}              : Rp {totaltelur}')
print(f'TOTAL LELE TERBANG x {jumlahleleterbang}            : Rp {totalleleterbang}')
print(f'TOTAL ES COKLAT x {jumlahEsCoklat}                  : Rp {totalEsCoklat}')
print(f'TOTAL ES DOGER x {jumlahEsDoger}                    : Rp {totalEsDoger}')
print(f'Jumlah total biaya yang harus dibayar adalah Rp {totalsemua}')