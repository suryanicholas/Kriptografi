# Selama input yang diterima sesuai
# alias 'true', perulangan (while) akan terus berlanjut

# Disini defenisi 'true' terjadi hanya jika
# input yang diberikan adalah 'y'
# selain dari itu nilainya 'false'

while input("Masukkan nilai (y/n): ").lower() == 'y':
    print('Hello World')

# Operasi dibawah ini akan di eksekusi ketika
# input yang diterima tidak sesuai alias 'false'
print('Berhenti')