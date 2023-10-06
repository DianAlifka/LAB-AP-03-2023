def angka_terbesar(daftar_angka):
    angka_terbesar = daftar_angka[0]
    for angka in daftar_angka:
        if angka > angka_terbesar:
            angka_terbesar = angka
    return angka_terbesar

daftar_angka = [5, 2, 8, 3, 1, 4]
print(angka_terbesar(daftar_angka))  # Output: 8
