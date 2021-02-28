# Restaurant Management System
import time
from tkinter import *

def total():
    global screen4
    global name, largefries, burgermeal, chickenfillet, chickenmeal, icecream, drinks
    global largefriesPrice, burgermealPrice, chickenfilletPrice, chickenmealPrice, icecreamPrice, drinksPrice
    global largefriesFinalPrice, burgermealFinalPrice, chickenfilletFinalPrice, chickenmealFinalPrice, icecreamFinalPrice, drinksFinalPrice, itemPrice

    largefriesPrice = 5
    burgermealPrice = 12
    chickenfilletPrice = 4
    chickenmealPrice = 7
    icecreamPrice = 1
    drinksPrice = 5

    name = str(name1.get())
    largefries = int(largefriesEntry.get())
    burgermeal = int(burgermealEntry.get())
    chickenfillet = int(chickenfilletEntry.get())
    chickenmeal = int(chickenmealEntry.get())
    icecream = int(icecreamEntry.get())
    drinks = int(drinksEntry.get())

    largefriesFinalPrice = largefriesPrice * largefries
    burgermealFinalPrice = burgermealPrice * burgermeal
    chickenfilletFinalPrice = chickenfilletPrice * chickenfillet
    chickenmealFinalPrice = chickenmealPrice * chickenmeal
    icecreamFinalPrice = icecreamPrice * icecream
    drinksFinalPrice = drinksPrice * drinks

    itemPrice = largefriesFinalPrice + burgermealFinalPrice + chickenfilletFinalPrice + chickenmealFinalPrice + icecreamFinalPrice + drinksFinalPrice


    screen4 = Toplevel(screen)
    screen4.geometry("600x650")
    screen4.title("Total")
    Label(screen4, text="Bill", bg="gray", width="300", height="2",font=("Brush MT Script", 20)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text=f"Name : {name}", width="300", height="2",
          font=("Brush MT Script", 15)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text=f"Large Fries : AED {largefriesFinalPrice}", width="300", height="2", font=("Brush MT Script", 15)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text=f"Burger Meal : AED {burgermealFinalPrice}", width="300", height="2",
          font=("Brush MT Script", 15)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text=f"Chicken Fillet : AED {chickenfilletFinalPrice}", width="300", height="2",
          font=("Brush MT Script", 15)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text=f"Chicken Meal : AED {chickenmealFinalPrice}", width="300", height="2",
          font=("Brush MT Script", 15)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text=f"Ice Cream : AED {icecreamFinalPrice}", width="300", height="2",
          font=("Brush MT Script", 15)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text=f"Drinks : AED {drinksFinalPrice}", width="300", height="2",
          font=("Brush MT Script", 15)).pack()
    Label(screen4, text="-----------------------------------------------------------------------------------------------------------------------").pack()
    Label(screen4, text=f"Total : AED {itemPrice}", width="300", height="2",
          font=("Brush MT Script", 15)).pack()
    Label(screen4,
          text="-----------------------------------------------------------------------------------------------------------------------").pack()
    Button(screen4, text="OK", command=lambda: screen4.destroy(), width="15", height="2", font=("Brush MT Script", 15)).pack()



def reset():
    name1.delete(0, 'end')
    largefriesEntry.delete(0, 'end')
    burgermealEntry.delete(0, 'end')
    chickenfilletEntry.delete(0, 'end')
    chickenmealEntry.delete(0, 'end')
    icecreamEntry.delete(0, 'end')
    drinksEntry.delete(0, 'end')
    screen3.destroy()

def order2():
    global screen3
    global chickenmealEntry, icecreamEntry, drinksEntry
    screen3 = Toplevel(screen)
    screen3.geometry("550x550")
    screen3.title("Order")
    Label(screen3, text="Order", bg="gray", width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen3, text="Chicken Meal"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    chickenmealEntry = Entry(screen3)
    chickenmealEntry.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Ice Cream"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    icecreamEntry = Entry(screen3)
    icecreamEntry.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Drinks"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    drinksEntry = Entry(screen3)
    drinksEntry.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Total", command=total
           , width="15", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Reset", command=reset
           , width="15", height="2", font=("Brush MT Script", 13)).pack()


def order():
    global screen2
    global name1, largefriesEntry, burgermealEntry, chickenfilletEntry
    screen2 = Toplevel(screen)
    screen2.geometry("550x550")
    screen2.title("Order")
    Label(screen2, text="Order", bg="gray"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Name"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    name1 = Entry(screen2)
    name1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="(Enter The Number Of Things You Want Like Large Fries : 2").pack()
    Label(screen2, text="Large Fries"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    largefriesEntry = Entry(screen2)
    largefriesEntry.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Burger Meal"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    burgermealEntry = Entry(screen2)
    burgermealEntry.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Chicken Fillet"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    chickenfilletEntry = Entry(screen2)
    chickenfilletEntry.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Next", command=order2
          , width="15", height="2", font=("Brush MT Script", 13)).pack()


def menu():
    global screen5
    screen5 = Toplevel(screen)
    screen5.geometry("400x500")
    screen5.title("Menu")
    Label(screen5, text="Menu (Per Piece )", bg = "gray"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Large Fries : AED 5 "
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Burger Meal : AED 12 "
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Chicken Fillet : AED 4 "
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Chicken Meal : AED 7 "
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Ice Cream : AED 1 "
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Drinks : AED 5 "
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="OK", command=lambda: screen5.destroy(), width="15", height="2",
           font=("Brush MT Script", 13)).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x400")
    screen.title("Restaurant Management System")
    clock = time.asctime(time.localtime(time.time()))
    Label(screen, text="Restaurant Management System", bg="gray"
          , width="300", height="2", font=("Brush MT Script", 13)).pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text=f"Time : {clock}", width=300
          , height="2", font=("Brush MT Script", 13)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Create New Order", command=order, height="3"
           , width="20", font=("Brush MT Script", 13)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Menu",command = menu, height="3"
           , width="20", font=("Brush MT Script", 13)).pack()
    Label(screen, text="").pack()
    Button(screen, text="Quit",command=lambda: quit(), height="3"
           , width="20", font=("Brush MT Script", 13)).pack()

    screen.mainloop()

main_screen()

