
# Menerapkan Prinsip PBO | Objek Kelas // Class Object

class Decimal:

    def toBin(value):
        return bin(value)[2:]
    
    def toOctal(value):
        return oct(value)[2:]
    
    def toHex(value):
        return hex(value)[2:]

# Constructor dalam python

class Bilangan:

    def __init__(self, value):
        self.value = value

    def int2Bin(self):
        return bin(self.value)[2:]
        


print("Class Biasa: ", Decimal.toBin(20))

a = Bilangan(40)

print(f"Class + Constructor: {a.int2Bin()}")