print('küpün hacmini ogrenmek isterseniz k ya,silindirin hacmini ogrenmek isterseniz s ye basın')
seçim=input("seçiminiz: ")
if(seçim=='k'):
    k=int(input("kenar uzunlugu giriniz:"))
    print('küpün hacmi :',k**3)
    print("Gamze kara 18220023 yönetim bilişim sistemleri 1.sınıf 2.öğretim")
else:
    r=int(input("çap uzunluğunu giriniz:"))
    h=int(input("yüksekliği giriniz:"))
    print('silindirin hacmi',3*(r**2)*h)
    print("Gamze kara 18220023 yönetim bilişim sistemleri 1.sınıf 2.öğretim")
