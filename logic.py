# boolean
# and
# or
# in/not in

narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")

#################################

menu = ['osh','qazonkabob','shashlik','norin','somsa']
print("manti" not in menu)
print('manti' in menu)

###################################

menu = ['osh','qazonkabob','shashlik','norin','somsa']
orders = ["osh","somsa","manti", "shashlik", "sho'rva", "bifshteks"]

if orders:
    for order in orders:
        if order in menu:
          print(f"There is {order} in menu")
        else:
            print(f"There's not {order} in menu")
else: 
    print("There is no order yet")