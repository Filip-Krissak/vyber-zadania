import random
import tkinter
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()
padli = input("napis cisla rozdelene medzerou: ")
padli = [int(num) for num in padli.split()]

subor = open('zoznam.txt', 'r')
cisla = subor.read().split()
cisla = [num for num in cisla if int(num) not in padli]
cislo = random.choice(cisla)
print(cislo)
index = cisla.index(cislo)
cisla.remove(cislo)
canvas.create_text(250,250,fill='black',text=cislo,font=('Arial','350','bold'))

subor = open('zoznam.txt', 'w')
subor.write(' '.join(cisla))
subor.close()
canvas.mainloop()
