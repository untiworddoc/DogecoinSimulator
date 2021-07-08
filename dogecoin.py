#Made by Khiem. Designed for the TI-Nspire. 
#Use font size 9 (Menu -> 1. Actions -> 6. Settings) 
#Press Ctrl-R to run.

from random import *
from time import *

#initial values
balance=100
amt=win=0
rent=1000
rdays=8
loop=day=0
a=2
b=1
price1=price2=0
money=cost=0
dayspent=daysold=0
t=localtime()
dayhigh=0
name=" "
taxp=0
tax=0

#menu
def menu():
  global balance
  global amt
  global win
  global rent
  global rdays
  global day
  global price1
  global price2
  global money
  global cost
  global daysold
  global dayspent
  global taxp
  global tax
  global dif
  amt=win=0
  rdays=15
  price1=price2=day=0
  money=cost=0
  daysold=dayspent=0
  tax=taxp=0
  balance=100
  t=localtime()
  print("============{:02}/{:02}/{:02}======={:02}:{:02}============".format(t[0],t[1],t[2],t[3],t[4]))
  print("                                 ===============")
  print("                                 Dogecoin Simulator")
  print("                                 ===============")
  print("                                 ===High scores===")
  print("=Name:",name)
  print("====Number of days:",dayhigh)
  print("                                   ====Rules====")
  print("Buy low, sell high. Don't run out of money.")
  print("Rent doubles and taxes increase by 4% every week.")
  print("Get to $1 septillion to win and keep going.")
  print("==============")
  input("Type 1 to play: ")
  print("==============")
  print(" ")
  print(" ")
  print("==============")
  print("Select difficulty:")
  print("==============")
  print("Starting balance: $100, Tax increase: 2% per week")
  print("==============")
  print("=Easy=               Rent=$500    Tax Start/Limit=0/20% ")
  print("=Normal=           Rent=$750    Tax Start/Limit=2/20%")
  print("=Hard=               Rent=$1000  Tax Start/Limit=8/40%")
  print("=Impossible=     Rent=$2000  Tax Start/Limit=16/60%")
  print("==============")
  dif=int(input("1 (Easy), 2 (Normal), 3 (Hard), 4 (Impossible): "))
  print("==============")
#Difficulty settings 
  if dif==1: rent=500; taxp=0
  elif dif==2: rent=750; taxp=0.02
  elif dif==3: rent=1000; taxp=0.08
  elif dif==4: rent=2000; taxp=0.16
  else: rent=750; taxp=0.02
  print("Game started.",dif,"selected")

#Shortens numbers
def short(numvar):
  if numvar<1*10**6:
    return "{:.4f}".format(numvar)
  elif 1*10**6<=numvar<1*10**9:
    mil=numvar/10**6
    return "{:.4f} million".format(mil)
  elif 1*10**9<=numvar<1*10**12:
    bil=numvar/10**9
    return "{:.4f} billion".format(bil)
  elif 1*10**12<=numvar<1*10**15:
    tril=numvar/10**12
    return "{:.4f} trillion".format(tril)
  elif 1*10**15<=numvar<1*10**18:
    quad=numvar/10**15
    return "{:.4f} quadrillion".format(quad)
  elif 1*10**18<=numvar<1*10**21:
    quin=numvar/10**18
    return "{:.4f} quintillion".format(quin)
  elif 1*10**21<=numvar<1*10**24:
    sext=numvar/10**21
    return "{:.4f} sextillion".format(sext)
  elif 1*10**24<=numvar<1*10**27:
    sept=numvar/10**24
    return "{:.4f} septillion".format(sept)
  elif 1*10**27<=numvar<1*10**30:
    oct=numvar/10**27
    return "{:.4f} octillion".format(oct)

#program starts here
menu()

#Loops everyday
while loop==0:
  t=localtime()
  a=1/a                                       #alternates variable (to find price diff)
  rdays=rdays-1
  day=day+1
  if a<b: price1=round(uniform(0.01,1),4)
  else: price2=round(uniform(0.01,1),4)
#Millionaire
  if balance>=1*10**24 and win==0:
    print("==============")
    print("You win!")
    print("You became a septillionaire in",day,"days")
    print("==============")
    cont=int(input("Continue playing? 1 (Yes) or 0 (No): "))
    if cont==1: win=1
    else: menu(); continue


#Main GUI
#Pay day
  if rdays==0:
    balance=balance-rent
    tax=balance*taxp
    balance=balance-tax
    print(" ")
    print("============{:02}/{:02}/{:02}======={:02}:{:02}============".format(t[0],t[1],t[2],t[3],t[4]))
    print("                                       ===DAY",str(day)+"===")
    print("Rent and taxes are due! ${} deducted from balance.".format(short(rent+tax)))
    if a>b:
      change24a=price2-price1
      if change24a>0:
        print("====Price of dogecoin is: ${:.4f}⫽(▲{:.4f})".format(price2,change24a))
      elif change24a<0:
        print("====Price of dogecoin is: ${:.4f}⫽(▼{:.4f})".format(price2,-change24a))
      elif change24a==0:
        print("====Price of dogecoin is: ${:.4f}⫽(•{:.4f})".format(price2,change24a))
    else:
      change24b=price1-price2
      if change24b>0:
        print("====Price of dogecoin is: ${:.4f}⫽(▲{:.4f})".format(price1,change24b))
      elif change24b<0:
        print("====Price of dogecoin is: ${:.4f}⫽(▼{:.4f})".format(price1,-change24b))
      elif change24b==0:
        print("====Price of dogecoin is: ${:.4f}⫽(•{:.4f})".format(price1,change24b))
    print("==You have ",short(amt),"dogecoins")
    print("==Your balance is: $"+short(balance))
    print("Spent (Day",str(dayspent)+"): $"+short(cost))
    print("Sold (Day",str(daysold)+"): $"+short(money))
    print("Rent pay (Due): - $"+short(rent))
    print("Tax (Due): {:.1f}%".format(taxp*100),"(${})".format(short(tax)))
    print("===========")
    rdays=8
    rent=rent*2
    if taxp<=18 and dif==1 or 2: taxp=taxp+0.02
    elif taxp<=38 and dif==3: taxp=taxp+0.02
    elif taxp<=58 and dif==4: taxp=taxp+0.02

#Normal day
  elif rdays!=0:
    tax=balance*taxp
    print("  ")
    print("============{:02}/{:02}/{:02}======={:02}:{:02}============".format(t[0],t[1],t[2],t[3],t[4]))
    print("                                       ===DAY",str(day)+"===")
    print("                         Rent and taxes due in",rdays,"days")
    if a<b:
      change24b=price1-price2
      if change24b>0:
        print("====Price of dogecoin is: ${:.4f}⫽(▲{:.4f})".format(price1,change24b))
      elif change24b<0:
        print("====Price of dogecoin is: ${:.4f}⫽(▼{:.4f})".format(price1,-change24b))
      elif change24b==0:
        print("====Price of dogecoin is: ${:.4f}⫽(•{:.4f})".format(price1,change24b))
    else:
      change24a=price2-price1
      if change24a>0:
        print("====Price of dogecoin is: ${:.4f}⫽(▲{:.4f})".format(price2,change24a))
      elif change24a<0:
        print("====Price of dogecoin is: ${:.4f}⫽(▼{:.4f})".format(price2,-change24a))
      elif change24a==0:
        print("====Price of dogecoin is: ${:.4f}⫽(•{:.4f})".format(price2,change24a))
    print("==You have ",short(amt),"dogecoins")
    print("==Your balance is: $"+short(balance))
    print("Spent (Day",str(dayspent)+"): $"+short(cost))
    print("Sold (Day",str(daysold)+"): $"+short(money))
    print("Rent pay ("+str(rdays),"days left): - $"+short(rent))
    print("Tax ({} days left): {:.1f}%".format(rdays,taxp*100),"(${})".format(short(tax)))
    print("===========")

#ran out of money
  if balance<0:
    print("You ran out of money. GAME OVER.")
    print("===========")
    print("You went through",day-1,"days without being in debt")
    if day-1>dayhigh:
      dayhigh=day-1
      print("New record!")
      name=input("Enter your name: ")
      menu()
      continue
    else: sleep(2); menu(); continue

#Buy menu 
  while loop==0:
    try: choice=int(input("Would you like to 1 (buy), 2 (sell) or 3 (skip)?: "))
    except ValueError: continue
#Buy
    if choice==1:
      if a<b:
        afford=balance/price1
        print("You can buy maximum:",afford,"dogecoins")
        try:
          buy=float(input("How much do you want to buy? Buy all (-1): "))
        except ValueError:
          continue
        if buy==-1: buy=afford-0.001
        cost=buy*price1
        bpreview=balance-cost
        if cost>balance:
          print("Can't buy. Not enough money.")
          continue
        print("==Cost: ${}".format(cost))
        print("==Balance after: ${}".format(bpreview))
        try: confirm=int(input("Confirm? 1 (yes) or 0 (no): "))
        except ValueError: continue
        if confirm==1:
          amt=amt+buy
          balance=balance-cost
          dayspent=day
          break
        else: continue
      else:
        afford=balance/price2
        print("You can buy maximum:",afford,"dogecoins")
        try: buy=float(input("How much do you want to buy? Buy all (-1): "))
        except ValueError: continue
        if buy==-1:
          buy=afford-0.0000000000001
        cost=buy*price2
        bpreview=balance-cost
        if cost>balance:
          print("Can't buy. Not enough money.")
          continue
        print("==Cost: ${}".format(cost))
        print("==Balance after: ${}".format(bpreview))
        try:
          confirm=int(input("Confirm? 1 (yes) or 0 (no): "))
        except ValueError:
          continue
        if confirm==1:
          amt=amt+buy
          balance=balance-cost
          dayspent=day
          break
        else:
          continue

#Sell
    elif choice==2:
      if amt==0:
        print("Can't sell. No dogecoins.")
        continue
      elif amt>0:
        try:
          print("You have total:",amt,"dogecoins")
          sell=float(input("How much do you want to sell? Sell all (-1): "))
        except ValueError:
          continue
        if sell==-1:
          sell=amt
        if sell>amt:
          print("You don't have that many dogecoins")
          continue
        elif a<b:
          money=sell*price1
          bpreview=balance+money
          print("==Receive: ${}".format(money))
          print("==Balance after: ${}".format(bpreview))
          try:
            confirm=int(input("Confirm? 1 (yes) or 0 (no): "))
          except ValueError:
            continue
          if confirm==1:
            balance=balance+money
            amt=amt-sell
            daysold=day
            break
          else:
            continue
        else:
          money=sell*price2
          bpreview=balance+money
          print("==Receive: ${}".format(money))
          print("==Balance after: ${}".format(bpreview))
          try:
            confirm=int(input("Confirm? 1 (yes) or 0 (no): "))
          except ValueError:
            continue
          if confirm==1:
            balance=balance+money
            amt=amt-sell
            daysold=day
            break
          else:
            continue

#Skip day
    elif choice==3: break
    else: continue
