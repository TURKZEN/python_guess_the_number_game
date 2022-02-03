import random
import os 
os.system("cls" if os.name=="nt" else "clear")
rastgele_sayi = random.randint(0,1000)
hamle = 0
print(
"""
░█▀▀░█▀█░█░█░▀█▀░░░▀█▀░█▀█░█░█░█▄█░▀█▀░█▀█░░░█▀█░█░█░█░█░█▀█░█░█
░▀▀█░█▀█░░█░░░█░░░░░█░░█▀█░█▀█░█░█░░█░░█░█░░░█░█░░█░░█░█░█░█░█░█
░▀▀▀░▀░▀░░▀░░▀▀▀░░░░▀░░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀
"""
)
while True:
    tahmin = int(input("Tahmininizi Giriniz : "))
    if tahmin > rastgele_sayi:
        print("Daha küçük bir sayı !")
        hamle+=1
    elif tahmin < rastgele_sayi:
        print("Daha büyük bir sayı !")
        hamle+=1
    else:
        os.system("cls" if os.name=="nt" else "clear")
        print(
        """
            

            ██   ██  █████  ███████  █████  ███    ██ ██████  ██ ███    ██ 
            ██  ██  ██   ██    ███  ██   ██ ████   ██ ██   ██ ██ ████   ██ 
            █████   ███████   ███   ███████ ██ ██  ██ ██   ██ ██ ██ ██  ██ 
            ██  ██  ██   ██  ███    ██   ██ ██  ██ ██ ██   ██ ██ ██  ██ ██ 
            ██   ██ ██   ██ ███████ ██   ██ ██   ████ ██████  ██ ██   ████ 
                                                                           


            {}.Tahminde doğru sayıyı buldun







        """
        .format(hamle))

        break

