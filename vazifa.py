from args import *
# def create_product_dict():
#     mahsulotlar = {}
#     while True:
#         mahsulot_nomi = input("Maxsulot nomini kiriting (yoki yakunlash uchun 'exit' deb yozing): ")
#         mahsulot_nomi = mahsulot_nomi.lower()
#         if mahsulot_nomi == 'exit':
#             break
#         mahsulot_narhi = float(input("Mahsulot narxini kiritinf: "))
#         mahsulotlar[mahsulot_nomi] = mahsulot_narhi
#     return mahsulotlar
# mahsulot_dict = create_product_dict()
# print(mahsulot_dict)
# # print("\nMahsulotlar ro'yxati:")
# # for mahsulot, narhi in mahsulot_dict.items():
# #     print(mahsulot + " " + str(narhi) + " So'm")
#
# # mahsulot_dict = {"olma": "1000", "nok": "1500", "banan": "2000"}
#
buyurtma = []
while True:
    mahsulot = input("maxsulot nomini kiriting (yoki yakunlash uchun 'exit' deb yozing): ")
    if mahsulot.lower() == "exit":
        break
    #mahsulot = mahsulot.lower()
    buyurtma.append(mahsulot)
print(buyurtma)
#
# # Mahsulotlarning omborda mavjudligini tekshirish
# for product in buyurtma:
#     if product in mahsulot_dict:
#         print(product, "bizning omborda " + str(mahsulot_dict[product]) + " So'mdan mavjud.")
#     else:
#         print(product, "bizning omborda mavjud emas.")

print(summa(1, 3))