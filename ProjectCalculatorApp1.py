# Omnicalculator.com
# Needed to import math to use the sqrt() (square root) function 
import math

# Defining functions for each calculator:

# Pixels Per Inch Calculator
def PPImain():
    DiagScreen=input('Diagonal Screen Size: ')
    HoriPix=input('Horizontal Pixels: ')
    VertPix=input('Vertical Pixels: ')

    fDiagScreen=float(DiagScreen)
    fVertPix=float(VertPix)
    fHoriPix=float(HoriPix)
    PPI=(math.sqrt(fVertPix**2+fHoriPix**2))/fDiagScreen
    print('Pixels Per Inch:', PPI)

# Markup Calculator
def MUmain():
    Cost=input('Item Cost: ')
    Markup=input('Markup Percent: ')
    
    fCost=float(Cost)
    fMarkup=float(Markup)
    
    revenue=fCost+fCost*(fMarkup/100)
    profit=fCost*(fMarkup/100)
    
    print('Revenue:', revenue)
    print('Profit:', profit)

# Cat Years to Human Years Calculator
def Catmain():
    CatYears=input('Years: ')
    CatMonths=input('Months: ')
    
    iCatYears=int(CatYears)
    iCatMonths=int(CatMonths)
    
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
    length=input('Length (m):' )
    width=input('Width (m):' )
    wastefactor=input('Waste Factor (%):' )
    rollprice=input('Roll Price per sqft ($):' )
    
    flength=float(length)
    fwidth=float(width)
    fwastefactor=float(wastefactor)
    wastefactorpercent=fwastefactor/100
    frollprice=float(rollprice)
    
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
    length=input('Length (ft):' )
    width=input('Width (ft):' )
    depth=input('Depth (ft):' )
    density=input('Density of sand being used (lb/cu ft):' )
    priceperlb=input('Price of Sand (per lb):' )
    
    flength=float(length)
    fwidth=float(width)
    fdepth=float(depth)
    fdensity=float(density)
    fpriceperlb=float(priceperlb)
    
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
    cperday=input('Cigarettes smoked each day: ')
    packsize=input('Pack size: ')
    packcost=input('Pack cost: ')
    yearsleft=input('How long you wont smoke (years): ')
    
    fcperday=float(cperday)
    fpacksize=float(packsize)
    fpackcost=float(packcost)
    fyearsleft=float(yearsleft)
    
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

    


    
  
    