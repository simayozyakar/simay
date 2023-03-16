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
print("ÖĞRENCİ KAYIT SİSTEMİNE HOŞGELDİNİZ")
print("Kayıt Sisteminde Yapılabilecek İşlemler")
print("1-Öğrenci Ekleme")
print("2-Öğrenci Çıkarma")
print("3-Birden Fazla Öğrenci Ekleme")
print("4-Öğrenci Listesini Görüntüleme")
print("5-Öğrenci Numarası Gösterme")
print("Not:Yapacağınız İşlemler Bitince Çıkmak İçin 6'ya basınız.")
liste=[" "]
sayi=input("Yapacağınız işlemin numarasını giriniz: ")
if sayi==1:
  ad_soyad=input("Eklemek istediğiniz öğrencinin adı-soyadı: ")
  liste.append(ad_soyad)
  print(f"{ad_soyad} başarıyla listeye eklenmiştir.")
elif sayi==2:
  ad_soyad=input("Çıkarmak istediğiniz öğrencinin adı-soyadı: ")
  liste.remove(ad_soyad)
  print(f"{ad_soyad} başarıyla listeden çıkarılmıştır.")
elif sayi==3:
  ögrenci_sayisi=input("Eklemek istediğiniz öğrenci sayısını giriniz: ")
  i=0
  while i<ögrenci_sayisi:
    ad_soyad=input(f"Eklemek istediğiniz {i}. öğrencinin adı-soyadı: ")
    liste.append(ad_soyad)
  print("Öğrenciler başarıyla eklenmiştir.")
elif sayi==4:
  print(liste)
elif sayi==5:
  okul_numarasi=input("Numarasını istediğiniz öğrencinin adı-soyadı: ")
  if 
