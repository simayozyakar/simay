#Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

#Bu öğrenci kayıt sistemine;

#Aldığı isim soy isim ile listeye öğrenci ekleyen
#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
#Listeye birden fazla öğrenci eklemeyi mümkün kılan
#Listedeki tüm öğrencileri tek tek ekrana yazdıran
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
#fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

#Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir
liste=["simay","bahar","ece"]
def ogrenci_ekleme():
  ad_soyad=input("Eklemek istediğiniz öğrencinin adı-soyadı: ")
  liste.append(ad_soyad)
  print(f"{ad_soyad} başarıyla listeye eklenmiştir.")
def ogrenci_cikarma():
  ad_soyad=input("Çıkarmak istediğiniz öğrencinin adı-soyadı: ")
  liste.remove(ad_soyad)
  print(f"{ad_soyad} başarıyla listeden çıkarılmıştır.")
def ogrencileri_ekleme():
  ögrenci_sayisi=int(input("Eklemek istediğiniz öğrenci sayısını giriniz: "))
  i=0
  while i<ögrenci_sayisi:
    ad_soyad=input(f"Eklemek istediğiniz {i+1}. öğrencinin adı-soyadı: ")
    liste.append(ad_soyad)
    i=i+1
  print("Öğrenciler başarıyla eklenmiştir.")
def liste_goruntuleme():
  print(liste)
def numara_gosterme():
  ad_soyad=input("Numarasını istediğiniz öğrencinin adı-soyadı: ")
  if (ad_soyad in liste):
    numara= liste.index(ad_soyad)
    print(f"Öğrencinin numarası: {numara}")
  else:
    print("Öğrenci listede bulunmamaktadır.")
print("ÖĞRENCİ KAYIT SİSTEMİNE HOŞGELDİNİZ")
print("Kayıt Sisteminde Yapılabilecek İşlemler")
print("1-Öğrenci Ekleme")
print("2-Öğrenci Çıkarma")
print("3-Birden Fazla Öğrenci Ekleme")
print("4-Öğrenci Listesini Görüntüleme")
print("5-Öğrenci Numarası Gösterme")
sayi=int(input("Yapacağınız işlemin numarasını giriniz: "))
while sayi<6:
  if sayi==1:
    ogrenci_ekleme()
  elif sayi==2:
    ogrenci_cikarma()
  elif sayi==3:
    ogrencileri_ekleme()
  elif sayi==4:
    liste_goruntuleme()
  elif sayi==5:
    numara_gosterme()
else:
  print("Girdiğiniz numara hatalı. Tekrar giriniz.")
