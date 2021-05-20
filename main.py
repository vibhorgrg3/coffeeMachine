import data as d
import os
class coffeeMachine:
    money=0
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    # "water": 0,
    # "milk": 0,
    # "coffee": 0,
    }
    MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def printReport(machine):
    print(machine.money)
    print(machine.resources['water'])
    print(machine.resources['milk'])
    print(machine.resources['coffee'])

def checkResources(machine,ch):
    if(ch.lower() not in ['water','coffee','milk']):
        return
    waterReq=machine.MENU[ch.lower()]['ingredients']['water']
    milkReq=machine.MENU[ch.lower()]['ingredients']['milk']
    coffeeReq=machine.MENU[ch.lower()]['ingredients']['coffee']
    waterLeft=machine.resources['water']
    milkLeft=machine.resources['milk']
    coffeeLeft=machine.resources['coffee']
    if(waterReq<=waterLeft and milkReq<=milkLeft and coffeeReq<coffeeLeft):
        return True
    else:
        return False

def moneyInput(ch,machine):
    #will call check resources
    if(checkResources(machine,ch)==False):
        print("out of ingredients")
        printReport(machine)
        return False
    
    cost=machine.MENU[ch.lower()]['cost']
    quaters=int(input('Quaters: '))*0.25
    dimes=int(input('Dimes: '))*0.15
    nickle=int(input('nickles: '))*0.05
    pennies=int(input('pennies: '))*0.01
    total=quaters+dimes+nickle+pennies
    if(cost>total):
        print("Not Enough Money")
        return False
    else:
        machine.money=cost
        machine.resources['water']=machine.resources['water']-machine.MENU[ch.lower()]['ingredients']['water']
        machine.resources['milk']=machine.resources['milk']-machine.MENU[ch.lower()]['ingredients']['milk']
        machine.resources['coffee']=machine.resources['coffee']-machine.MENU[ch.lower()]['ingredients']['coffee']
        print("here, your change: ",total-cost)
        # os.system()la
        return True


def printMenu(machine):
    os.system('cls')
    ch=input("What do u want (espresso, cappuccino, latte): ")
    if(ch.lower()=='off'):
        return
    if(ch.lower()=='report'):
        printReport(machine)
        input("Press key to continue")
        printMenu(machine)
    # TODO check ch and call respective functiosn
    else:
        check=moneyInput(ch,machine)
        if(check):
            print("enjoy your coffee")
            printReport(machine)
            input("Hit a key to continue: ")
            printMenu(machine)


machine=coffeeMachine
printReport(machine)
printMenu(machine)