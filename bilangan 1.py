try:
    decimal = int(input("Masukkan nilai desimal: "))

    # Konversi ke biner
    binary = bin(decimal)[2:].zfill(8)

    # Konversi ke oktal
    octal = oct(decimal)[2:].zfill(8)

    # Konversi ke heksadesimal
    hexadecimal = hex(decimal)[2:].zfill(8)

    print("Nilai dalam format Biner:", binary)
    print("Nilai dalam format Oktal:", octal)
    print("Nilai dalam format Heksadesimal:", hexadecimal)

except ValueError:
    print("Masukan tidak valid. Harap masukkan nilai desimal yang benar.")