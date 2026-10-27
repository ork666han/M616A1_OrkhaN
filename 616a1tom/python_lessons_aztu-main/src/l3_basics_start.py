# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

# print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı 
# name=input()
# print("menim adim", name)
# age=int (input())
# age=age + 1
# print("menim yasim", age)
# print(age <50)
# print(age > 100)

# rsrp_list = [-91.5 , -108.1 , -86.2 , -103.3 , -97.4]
# print(rsrp_list [0])
# print(rsrp_list [1])
# print(rsrp_list [-1])
# print(len(rsrp_list))

# index = int(input())
# print(rsrp_list[index])

# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)

print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu

# TODO: cell, rsrp, drops

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»

print("=== Kərpic 4 ===")   # Müqayisə → True / False

# TODO: rsrp < -105, ==

print("=== Kərpic 5 ===")   # Siyahı (list)
rsrp_list = [-91.5, -108.1, -86.2, -103.3, -97.4]
index = int(input("Please enter an index: ")) #a = 666 
print(rsrp_list[index]) 
# print(rsrp_list[0]) # birinci element — indeks 0-dan başlayır
# print(rsrp_list[1]) # ikinci element
# print(rsrp_list[-1]) # sonuncu element
# print(len(rsrp_list)) # elementlərin sayı
# avg = sum(rsrp_list) / len(rsrp_list)
# print(round(avg, 1)) # orta qiymət
# TODO: rsrp_list, indeks, len, orta

print("=== Kərpic 6 ===")   # Lüğət (dict)
row = {"cell_id": "BAK-0207", "region": "Yasamal", "rsrp_dbm": -108.1}
print(row["region"])
print(row["rsrp_dbm"])
print(row)
row["band"] = "LTE800"
row["region"]="Nesimi"
print(row)

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
for v in rsrp_list:
    v = v * int(input())
    print(v)

  

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
