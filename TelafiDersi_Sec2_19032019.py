#https://repl.it/languages/python3 ile olu�turuldu.

#string par�alama
kelime="Merhaba"
#��kt�: h
print(kelime[3])
#��kt�: Merh
print(kelime[:4])

#��kt�: haba
print(kelime[3:])
#��kt�: ha
print(kelime[3:5])
#Merhaba ��kt�: Mraa 
print(kelime[::2])
#Sadece sesli harfler
sesli="ae�io�u�" #string
sayac=0
print("Sesli Harfler:")
for i in kelime:
  if i in sesli:
    print(i)
    sayac+=1
print("Sesli harf say�s�:",sayac)
for i in range(0,len(kelime)):
  if kelime[i] in sesli:
    print(i+1,".=",kelime[i])

sozluk={"elma":"apple","muz":"banana","bar��":"peace","kuzey":"north","g�ney":"south","bilgisayar":"computer"}
#kelime=input("Kelimeyi girin..:")
#print(sozluk[kelime])
print(sozluk.items())
print(sozluk.keys())
print(sozluk.values())
#items elma,apple
#key elma
#values apple

#Listeyi s�ralama:
liste=[10,45,30,23,27,2]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)

#Oyun:
#Listemiz 6 tane rastgele say�dan olu�sun
#Say� aral��� 1-45 aras�nda
#Kullan�c�n�n ka� tane say�y� do�ru tahmin etti�ini yazd�ral�m
#Not: �retilen say�lar benzersiz olmal� (ara s�navlardan sonra ��z�lecek), bu say�lar s�ral� olmal�
liste=[]
tahmin=[]
import random
for i in range(1,7):
  liste.append(random.randint(1,15))
  tahmin.append(int(input("Tahmininiz:")))

liste.sort()
tahmin.sort()
#A'dan Z'ye do�ru s�ral� bir �ekilde yazd�r�l�yor...
print("Random say�lar:")
print(liste)
print("Tahminler:")
print(tahmin)
sayac=0
for i in tahmin:
  if i in liste:
    sayac+=1
print("Do�ru Tahmininiz:",sayac)

#Girilen say�n�n 2 ile 9 aras�ndaki rakamlara tam b�l�n�p b�l�nmedi�inin ��kt�s�n� veren program
#�r: 45
#2 b�l�nenemez
#3 b�l�n�r
#4 b�l�nemez
#5 b�l�n�r
#6 b�l�nemez
#7 b�l�nemez
#8 b�l�nemez
#9 b�l�n�r
sayi=int(input("Say�:"))
for i in range(2,10):
#i de�eri 2 ile 9 aras�ndaki say�lar� tutar
  if sayi%i==0:
    print(i," b�l�n�r")
  else:
    print(i," b�l�nemez")


#1 ile 50 aras�ndaki say�lardan tek olanlar� ekrana yazd�ral�m
for i in range(1,51):
  if i%2==1:
    print(i)

#random �retilen 10 say�dan (Random say� aral���:1-100) �ift olanlar� ekrana yazd�ral�m
import random
for i in range(10):
  say�=random.randint(1,100)
  if say�%2==0:
    print(say�)
#random �retilen 10 say�dan (Random say� aral���:1-100) tek olanlar� teksay�, �ift olanlar� �iftsay�, t�m say�lar� da say�lar listesinde tutup, ayr� ayr� ekrana yazd�ral�m
�iftsay�=[]
teksay�=[]
say�lar=[]
for i in range(10):
  say�=random.randint(1,100)
  say�lar.append(say�)
  if say�%2==0:
    �iftsay�.append(say�)
  else:
    teksay�.append(say�)
say�lar.sort()
print("T�m say�lar:")
print(say�lar)
teksay�.sort()
print("Tek say�lar:")
print(teksay�)
�iftsay�.sort()
print("�ift say�lar:")
print(�iftsay�)