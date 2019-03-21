# Omnicalculator.com
# Needed to import math to use the sqrt() (square root) function 
import math

# Defining functions for each calculator:

# Pixels Per Inch Calculator
def PPImain():
    while True:
        try:
            DiagScreen=input('Diagonal Screen Size: ')
            fDiagScreen=float(DiagScreen)
            break
        except:
            print("Enter a number")
    while True:
        try:
            HoriPix=input('Horizontal Pixels: ')
            fHoriPix=float(HoriPix)
            break
        except:
            print("Enter a number")
    while True:
        try:
            VertPix=input('Vertical Pixels: ')
            fVertPix=float(VertPix)
            break
        except:
            print("Enter a number")
    PPI=(math.sqrt(fVertPix**2+fHoriPix**2))/fDiagScreen
    print('Pixels Per Inch:', PPI)
# Markup Calculator
def MUmain():
    while True:
        try:
            Cost=input('Item Cost: ')
            fCost=float(Cost)
            break
        except:
            print("Enter a number")
    while True:
        try: 
            Markup=input('Markup Percent: ')
            fMarkup=float(Markup)
            break
        except:
            print("Enter a number")
    revenue=fCost+fCost*(fMarkup/100)
    profit=fCost*(fMarkup/100)
    print('Revenue:', revenue)
    print('Profit:', profit)
# Cat Years to Human Years Calculator
def Catmain():
    while True:
        try:
            CatYears=input('Years: ')
            iCatYears = int(CatYears)
            break
        except:
            print("Enter a number")
    while True:
        try:
            CatMonths=input('Months: ')
            iCatMonths=int(CatMonths)
            break
        except: 
            print("Enter a number")
    HumanYears=iCatYears*7
    HumanMonths=iCatMonths*7
    if HumanMonths >= 12:
        HumanYearsNew=HumanMonths//12
        HumanYears=HumanYears+HumanYearsNew        
        HumanMonthsRmd=HumanMonths%12
        HumanMonths=0+HumanMonthsRmd
        print('Human Years:', HumanYears)
        print('Human Months:', HumanMonths)
    else:
        print('Human Years:', HumanYears)
        print('Human Months:', HumanMonths)
# Sod Calculator 
def Sodmain():
    print('Field Parameters' )
    while True:
        try:
            length=input('Length (m):' )
            flength=float(length)
            break
        except: 
            print("Enter a number")
    while True:
        try:
            width=input('Width (m):' )
            fwidth=float(width)
            break
        except:
            print("Enter a number")
    while True:
        try:
            wastefactor=input('Waste Factor (%):' )
            fwastefactor=float(wastefactor)
            break
        except:
            print("Enter a number")
    while True:
        try:
            rollprice=input('Roll Price per sqft ($):' )
            frollprice=float(rollprice)
            break
        except:
            print("Enter a number")
    wastefactorpercent=fwastefactor/100
    landarea=flength*fwidth
    sodarea=landarea*(1+wastefactorpercent)
    totalcost=sodarea*frollprice
    totalrolls=sodarea/(1.5*6)
    print('Results:')
    print('Land Area:', landarea)
    print('Rolls Needed:', totalrolls)
    print('Total Cost: $',totalcost)
# Sand Calculator 
def Sandmain():
    print('Calculate Volume of Sand needed:')
    while True:
        try: 
            length=input('Length (ft):' )
            flength=float(length)
            break
        except:
            print("Enter a number")
    while True:
        try:
            width=input('Width (ft):' )
            fwidth=float(width)
            break
        except:
            print("Enter a number")
    while True: 
        try:
            depth=input('Depth (ft):' )
            fdepth=float(depth)
            break
        except:
            print("Enter a number")
    while True:
        try:
            density=input('Density of sand being used (lb/cu ft):' )
            fdensity=float(density)
            break
        except:
            print("Enter a number")
    while True:
        try:
            priceperlb=input('Price of Sand (per lb):' )
            fpriceperlb=float(priceperlb)
            break
        except:
            print("Enter a number")  
    area=flength*fwidth
    volume=area*fdepth
    totalweightsand=fdensity*volume
    totalcost=fpriceperlb*totalweightsand
    print('Results:')
    print('Area that needs sanding:', area,'sqft')
    print('Volume of Sand needed:', volume,'cu ft')
    print('Total weight of Sand Needed:', totalweightsand,'lbs')
    print('Total Cost of Sand Needed: $',totalcost)
# Quit Cigarettes and Save Calculator:
def Cigmain():
    print('Calculate how much you save by quitting today: ')
    while True:
        try:
            cperday=input('Cigarettes smoked each day: ')
            fcperday=float(cperday)
            break
        except:
            print("Enter a number")
    while True:
        try:
            packsize=input('Pack size: ')
            fpacksize=float(packsize)
            break
        except:
            print("Enter a number")
    while True:
        try:
            packcost=input('Pack cost: ')
            fpackcost=float(packcost)
            break
        except:
            print("Enter a number")
    while True:
        try:
            yearsleft=input('How long you wont smoke (years): ')
            fyearsleft=float(yearsleft)
            break
        except:
            print("Enter a number")
    cperyear=fcperday*365
    icperyear=int(cperyear)
    pperyear=icperyear/fpacksize
    spentperyear=fpackcost*pperyear
    cnotperyear=cperyear*fyearsleft
    moneytobesaved=(cnotperyear/fpacksize)*fpackcost
    print('')
    print('Results:')
    print('')
    print('Packs smoked per year:', pperyear)
    print('Money spent per year: $',spentperyear)
    print('')
    print('If you quit smoking today...:')
    print('')
    print('Cigarettes not smoked:', cnotperyear)
    print('Money savings: $',moneytobesaved) 
#Program Code:
while True:
    print()
    print('1: Cat Years to Human Years')
    print('2: Markup Calculator')
    print('3: Pixels Per Inch')
    print('4: Sod Calculator')
    print('5: Sand Calculator')
    print('6: Quit Smoking and Save Calculator:')
    print('')
    print('0: Done')
    ChooseCalc=input('Which Calculator do you want to use? ')
# Runs a function depending on the user's input
    if ChooseCalc == '3':
        print('')
        print('*Pixels Per Inch Calculator*')
        PPImain()
    elif ChooseCalc == '2':
        print('')
        print('*Markup Calculator*')
        MUmain()
    elif ChooseCalc == '1':
        print('')
        print('*Cat Years to Human Years*')
        Catmain()
    elif ChooseCalc == '4':
        print('')
        print('*Sod Calculator*')
        Sodmain()
    elif ChooseCalc == '5':
        print('')
        print('*Sand Calculator*')
        Sandmain()
    elif ChooseCalc == '6':
        print('')
        print('*Quit Smoking and Save Calculator*')
        Cigmain()
    elif ChooseCalc == '0':
        break
    else:
        print('Choose Valid Option')