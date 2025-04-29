def get_delete():
    delete = input("Kimni mehmonxonadan ketmoqchi? ").title()
    if delete.title() in mehmonlar:
        print(f"{delete} ro'yxatdan uchirildi.")
        uy = mehmonlar[delete]['son']
        mehmonlar.pop(delete)
        tekshir.remove(uy)
    else:
        print(f"{delete} ismli mehmon topilmadi.")


def get_add():
    ism = input("Ism: ")
    while True:
        son = int(input("Xona raqamini kiriting: "))
        if son not in tekshir:
            break
        else:
            print("Bu xona band boshqa xona tanlang")
    tekshir.append(son)
    while True:
        tur = input("""Xona turini quyidagi belgilar orqali tanlang:
    e - ekanom
    s - standart
    l - lyuks\n""")
        if tur == 'e':
            tur = "ekanom"
            break
        elif tur == 's':
            tur = "standart"
            break
        elif tur == 'l':
            tur = "lyuks"
            break
        else:
            print("Bu turdagi xonamiz mavjud emas, boshqatdan tanlang")
    mehmonlar[ism] = {
        'son': son,
        'tur': tur
    }
    print(f"{ism.title()} ro'yxatga qo'shildi.")


def get_print():
    if mehmonlar:
        print("\nIsmi                   Xonasi                  Xona turi")
        for key, value in mehmonlar.items():
            print(f"{key.title():<23}{value['son']:<24}{value['tur']:<15}")
    else:
        print("Hozirda ro'yxat bo'sh.")


def get_name():
    print("""Optimuss mehmonxonasiga xush kelibsiz!
 Buyruqni tanlang:
1 - mehmon qo'shish
2 - mehmonni ruyxatdan chiqarish
3 - mehmonlar ruyxati

0 - dasturdan chiqish""")


get_name()
mehmonlar = {}
tekshir = []
while True:
    try:
        n = int(input())
        if n == 0:
            print("Dastur tugadi.")
            break
        elif n == 1:
            get_add()
        elif n == 2:
            get_delete()
        elif n == 3:
            get_print()
        get_name()
    except ValueError:
        print("Faqat berilgan sonlardan tanlang")
