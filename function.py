# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu aleykum, hurmatli {ism.title()}!")


# print(salom_ber.__doc__)
#
# salom_ber('hasan')
# salom_ber('mansur')


# def toliq_ism(ism, familiya):
#     """Foydalanuvchini ism familiyasini chiqaruvchi funksiya"""
#
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
#
#
# print(toliq_ism.__doc__)
#
# toliq_ism('olim', 'hakimov')


# def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")
#
#
# yosh_hisobla(tugilgan_yil=2001, joriy_yil=2023)

# def toliq_ism_yasa(ism, familiya):
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
#
#
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakimov', 'olim')
#
# print(f"{talaba1} \n{talaba2}")

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
#
#
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakimov', 'olim', 'abrorovich')
#
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rangi,
#             'korobka': korobka,
#             'yil': yili,
#             'narh': narhi}
#     return avto
#
#
# print("Saytimizdagi avtolar ro'yxatini shakllantiriamiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi:")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print(avtolar)


# avto1 = avto_info('GM', 'Malibu', 'Qora', 'avtomat', 2018)
# avto2 = avto_info('Gm', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Nomalum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min+= 1
#     return sonlar
#
# print(oraliq(1,14))
# print(oraliq(10,21))

# 24.10.2023
# Mavzu: Funksiyaga ro'yxat uzatish

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = baho
#     return baholar
#
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning
# birinchi harfini katta harfga o'zgartiruvchi funksiya yozing.

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)


# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#     return matnlar
#
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)


talabalar = ['jamshid', 'asad', 'masur', 'temur']


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = int(input(f"Talaba {ism.title()}ning bahosini kiriting: "))
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar)
print(baholar)
print(talabalar)
