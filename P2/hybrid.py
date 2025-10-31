# Hybrid Calculator

while True:
    
    opt = input("\nMasukan operasi Aritmetika: ").strip()
    
    if opt.lower() == 'exit':
        print("Berhenti")
        break
    
    if opt:
        try:
            
            result = eval(opt)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Pembagian dengan angka 0 tidak bisa dilakukan.")
        except SyntaxError:
            print("Error: Kesalahan sintaksis!")
        except NameError:
            print("Error: Operasi tidak dikenali!")
        except Exception as e:
            print(f"Error: Terjadi kesalahan fatal: {e}")
    else:
        print("Error: Masukan tidak boleh kosong")