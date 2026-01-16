mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-3]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 
print(mevalar[-1])

narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)

mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
print(mevalar)

#.insert() metodi
# Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz. .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:


cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
print(cars)

# .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. Agar ro'yxatning ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
del hayvonlar[0]
hayvonlar.insert(0, "dog")
print(hayvonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)