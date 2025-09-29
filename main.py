from sympy import *  #Что это такое (Ответ: это импорт всех методов/классов из библиотеки sympy) 5/5
k, T, C, L = symbols('k T C L')
#1
C_ost = 100000
Am_lst = []
C_ost_lst = []
for i in range(5):
  Am = (C-L)/T
  C_ost -= Am.subs({C:100000, T:5, L:0})
  Am_lst.append(round(Am.subs({C:100000, T:5, L:0}),2))
  C_ost_lst.append(round(C_ost,2))
print('Am_lst', Am_lst)
print('C_ost_lst', C_ost_lst)
# # из блока выше убрана вторая решетка

#2
Aj = 0
C_ost = 100000
Am_lst2 = []
C_ost_lst2 = []
for i in range(5):
  Am = k/T *(C-Aj) #Что такое k
  C_ost -= Am.subs({C:100000, T:5, L:0, k:2})
  Am_lst2.append(round(Am.subs({C:100000, T:5, L:0, k:2}),2))
  Aj += Am
  C_ost_lst2.append(round(C_ost,2))
print('Am_lst2', Am_lst2)
print('C_ost_lst2', C_ost_lst2)

#tableview container
import pandas as pd
Y= range(1,6)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst2, Am_lst2))
tFrame = pd.DataFrame(table1, columns=['Y', 'C_ost', 'Am'])
tFrame2 = pd.DataFrame(table2, columns=['Y', 'C_ost2', 'Am2'])
print(tFrame)
print(tFrame2)

#visual conainer

from matplotlib import pyplot as plt
fig, ax = plt.subplots(3) #Почему subplots(3) а обращения к ax: [0], [1], [2] 🤡 (Ответ: потому что 3 графика) 4/5 (да, потому что 3 графика, но в python индексы начинаются с 0)

ax[0].plot(Y, tFrame2['C_ost2'], label='Am2')
ax[0].plot(Y, tFrame['C_ost'], label='Am')
ax[1].bar(Y, tFrame['Am'], label='Am')
ax[1].bar(Y, tFrame2['Am2'], label='Am2')

vals1 = Am_lst
vals2 = Am_lst2
labels = list(range(1,6))
explode = [0.1, 0.1, 0.1, 0.1, 0.1]
ax[2].pie(vals2, labels=labels, autopct= '%1.1f%%', explode=explode)
ax[2].axis('equal')

plt.show()