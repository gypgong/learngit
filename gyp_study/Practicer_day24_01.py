# !/usr/bin/env python3
# -*- coding: utf-8 -*-



# offer_list=["Allen","Tom"]
# for i in range(len(offer_list)):
#     print("{}, you have passed our interview and will soon become a member of our company.".format(offer_list[i]))
# for j in range(len(offer_list)):
#     if offer_list[j]=="Tom":
#         offer_list[j]="Andy"
#     print("{}, welcom to join us!".format(offer_list[j]))



guest_list = ['Niuniu', 'Niu Ke Le']
for i in guest_list:
    print('%s, do you want to come to my celebration party?' % i)
print('\n')
guest_list.insert(0, 'GURR')
guest_list.insert(2, 'Niumei')
for j in guest_list:
    print('%s, thank you for coming to my celebration party!'% j)