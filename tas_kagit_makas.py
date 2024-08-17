import random
print("Taş, kağıt, makas oyununa hoşgeldin!")
print("Bu oyunun amacı her turda 2 oyuncunun farklı figürler göstererek rakibini yenmeye çalışmasıdır.")
print("Kısaca kurallardan bahsedelim: Her turda taş, kağıt, makas hamlelerinden birini seçmelisin.")
print("Taş makasa, makas kağıda ve kağıt ise taşa üstünlük kurar.")
print("2 turu kazanan oyuncu oyunun galibi olur!")

def tas_kagit_makas_HATICESUDE_KORUCU():
    oyuncu_skor = 0
    bilgisayar_skor = 0
    hamleler = ["Taş", "Kağıt","Makas"]
    evet_hayır = ["Evet", "Hayır"]
    print("Oyun başladı!")

    while bilgisayar_skor < 2 and oyuncu_skor < 2:                
        oyuncu_hamlesi = input("Taş, Kağıt, Makas hamlelerinden birini seç: ")               
        bilgisayar_hamlesi = random.choice(hamleler)
        if oyuncu_hamlesi not in hamleler:
           print("Geçersiz hamle, tekrar dene!")
        else:    
            if bilgisayar_hamlesi == oyuncu_hamlesi:
                print(f"Bilgisayarın hamlesi: {bilgisayar_hamlesi}, tur berabere!")
                print(f"Bilgisayar: {bilgisayar_skor}")
                print(f"Oyuncu: {oyuncu_skor}")
                                      
            elif (bilgisayar_hamlesi == "Taş" and oyuncu_hamlesi == "Makas") or \
                 (bilgisayar_hamlesi == "Makas" and oyuncu_hamlesi == "Kağıt") or \
                 (bilgisayar_hamlesi == "Kağıt" and oyuncu_hamlesi == "Taş"):
                bilgisayar_skor += 1
                print(f"Bilgisayarın hamlesi: {bilgisayar_hamlesi}, bilgisayar turu kazandı!")
                print(f"Bilgisayar: {bilgisayar_skor}")
                print(f"Oyuncu: {oyuncu_skor}")
                               
            else:
                print(f"Bilgisayarın hamlesi: {bilgisayar_hamlesi}, turu kazandın!")
                oyuncu_skor += 1
                print(f"Bilgisayar: {bilgisayar_skor}")
                print(f"Oyuncu: {oyuncu_skor}")
                
    while oyuncu_skor == 2:
        bilgisayar_tekrar = random.choice(evet_hayır)
        tekrar = input("Tebrikler oyunu kazandın, tekrar oynamak ister misin?(Evet/Hayır): ")
        if tekrar not in evet_hayır:
            print("Geçersiz cevap, 'Evet' veya 'Hayır' gir!")
            continue
        else:
            if tekrar == "Evet" and bilgisayar_tekrar == "Hayır":
                print("Bilgisayar tekrar oynamak istemiyor, oyun bitti!")
                break
            elif tekrar == "Hayır" and bilgisayar_tekrar == "Evet":
                print("Oyuncu tekrar oynamak istemiyor, oyun bitti!")
                break
            elif tekrar == "Hayır" and bilgisayar_tekrar == "Hayır":
                print("Oyun bitti, teşekkürler!")
                break
            else:
                tas_kagit_makas_HATICESUDE_KORUCU()
                break

    while bilgisayar_skor == 2:
        bilgisayar_tekrar = random.choice(evet_hayır)
        tekrar = input("Bilgisayar oyunu kazandı, tekrar oynamak ister misin?(Evet/Hayır): ")
        if tekrar not in evet_hayır:
            print("Geçersiz cevap, 'Evet' veya 'Hayır' gir!")
            continue
        else:
            if tekrar == "Evet" and bilgisayar_tekrar == "Hayır":
                print("Bilgisayar tekrar oynamak istemiyor, oyun bitti!")
                break
            elif tekrar == "Hayır" and bilgisayar_tekrar == "Evet":
                print("Oyuncu tekrar oynamak istemiyor, oyun bitti!")
                break
            elif tekrar == "Hayır" and bilgisayar_tekrar == "Hayır":
                print("Oyun bitti, teşekkürler!")
                break
            else:
                tas_kagit_makas_HATICESUDE_KORUCU()
                break 

tas_kagit_makas_HATICESUDE_KORUCU()
