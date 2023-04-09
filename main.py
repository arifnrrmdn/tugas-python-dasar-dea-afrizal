saldo_awal = 5000
deposit = int(input('berapa jumlah deposit: '))

saldo_total = saldo_awal + deposit
hutang = 50000

if saldo_total == hutang:
    saldo_akhir = saldo_total - hutang
    sisa_hutang = hutang - saldo_total
    print("Hutang lunas")
    if saldo_akhir <= 0:
        saldo_akhir = 0
    else:
        saldo_akhir = saldo_akhir
    print("Sisa saldo anda: " + str(saldo_akhir))
    if sisa_hutang <= 0:
        sisa_hutang = 0
    else:
        sisa_hutang = sisa_hutang
    print("Sisa hutang anda: " + str(sisa_hutang))
elif saldo_total >= hutang:
    saldo_akhir = saldo_total - hutang
    sisa_hutang = hutang - saldo_total
    print("Hutang Lunas")
    if saldo_akhir <= 0:
        saldo_akhir = 0
    else:
        saldo_akhir = saldo_akhir
    print("Sisa saldo anda: " + str(saldo_akhir))
    if sisa_hutang <= 0:
        sisa_hutang = 0
    else:
        sisa_hutang = sisa_hutang
    print("Sisa hutang anda: " + str(sisa_hutang))
else:
    saldo_akhir = saldo_total - hutang
    sisa_hutang = hutang - saldo_total
    print("Hutang tidak lunas")
    if saldo_akhir <= 0:
        saldo_akhir = 0
    else:
        saldo_akhir = saldo_akhir
    print("Sisa saldo anda: " + str(saldo_akhir))
    if sisa_hutang <= 0:
        sisa_hutang = 0
    else:
        sisa_hutang = sisa_hutang
    print("Sisa hutang anda: " + str(sisa_hutang))

