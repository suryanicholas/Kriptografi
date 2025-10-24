# Konversi dengan Logic Manual

class Decimal:

    def toBin(val: int):
        if(val == 0):
            return 0
        
        a = ""
        while val > 0:
            b = val % 2 # Modulus
            a = str(b) + a # 

            val //= 2
        
        return a
    
print("Hasil: ", Decimal.toBin(5))