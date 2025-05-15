import random

A = ['♠', '♣', '♥', '♦']
B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deste = []
for i in A:
    for j in B:
        deste.append(i+j)

oyuncular = {}
oyuncu_sira = ['oyuncu1', 'oyuncu2', 'oyuncu3', 'oyuncu4']  
for i in range(4):
    
    oyuncular.setdefault(oyuncu_sira[i], {}.fromkeys(A)) 

for oyuncu in oyuncular:
    
    for i in A:
        oyuncular[oyuncu][i] = []
    for i in range(13):
        kart = random.choice(deste)
        oyuncular[oyuncu][kart[0]].append(kart[1:])
        deste.remove(kart)

print("\nDAĞITILAN KARTLAR:")
for oyuncu in oyuncular:
    print(oyuncu + ":")
    for karttip in oyuncular[oyuncu]:
        oyuncular[oyuncu][karttip].sort(key=B.index)  
        print(karttip, oyuncular[oyuncu][karttip])

print("\nOYUN BAŞLADI...")  
oyun_skor = dict()
macaAtildi = False
sira = random.randrange(4)  


tahminler = {}
for oyuncu in oyuncular:
    tahmin = int(input(f"{oyuncu}, kaç el alacağını tahmin et: "))
    tahminler[oyuncu] = tahmin

for el in range(13):  
    print(str(el+1) + ". el:")
    oynayan = 0
    oynanan_kartlar = []  
    while oynayan < 4:
        oyuncu = oyuncu_sira[sira]
        if oynayan == 0:  
            while True:
                if macaAtildi:  
                    kart_tipi = random.choice(A)
                else:  
                    kart_tipi = random.choice(A[1:])
                if len(oyuncular[oyuncu_sira[sira]][kart_tipi]):  
                    break
            oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())  
           
        else:  
            if len(oyuncular[oyuncu][kart_tipi]):  
                oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())
            elif len(oyuncular[oyuncu]['♠']):  
                oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(0))
                macaAtildi = True  
            else:  
                kart_tipleri = A[1:].copy()  
                for tip in kart_tipleri:
                    if len(oyuncular[oyuncu][tip]):
                        oyuncu_kart = (oyuncu, tip, oyuncular[oyuncu][tip].pop(0))
                        break
        print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
        oynanan_kartlar.append(oyuncu_kart)
        oynayan += 1
        sira += 1
        if sira >= 4:
            sira -= 4
    
    en_buyuk = oynanan_kartlar[0]   
    for kart in oynanan_kartlar[1:]:
        if kart[1] == en_buyuk[1] and B.index(kart[2]) > B.index(en_buyuk[2]):
            en_buyuk = kart  
        elif en_buyuk[1] != '♠' and kart[1] == '♠':
            en_buyuk = kart 
    print("eli kazanan:", en_buyuk[0])
    sira = oyuncu_sira.index(en_buyuk[0])
    oyun_skor[en_buyuk[0]] = oyun_skor.setdefault(en_buyuk[0], 0) + 1
print("\n--- OYUN BİTTİ, PUANLAR HESAPLANIYOR ---")
for oyuncu in oyuncular:
    tahmin = tahminler[oyuncu]
    alinan_el = oyun_skor.get(oyuncu, 0)
    if tahmin == alinan_el:
        puan = 10 * tahmin
    elif tahmin < alinan_el:
        puan = (10 * tahmin) - ((alinan_el - tahmin) * 10)
    else:
        puan = (10 * tahmin) - ((tahmin - alinan_el) * 10)
    print(f"{oyuncu}: Tahmin: {tahmin}, Alınan El: {alinan_el}, Puan: {puan}")

