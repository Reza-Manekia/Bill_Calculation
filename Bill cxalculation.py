#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[6]:





# # ASSIGMENT QUESTION: (BILL CACULATION)
# 

# In[11]:


def electricity(monthly_units):
    charges = 0
    if(monthly_units == 0 & monthly_units <= 100):
        charges = 9.43*monthly_units
        return charges
    elif(monthly_units > 100 & monthly_units <= 200):
        charges = 10.29*monthly_units
        return charges
    elif(monthly_units > 200 & monthly_units <= 300):
        charges = 12.43*monthly_units
        return charges
    elif(monthly_units > 300 & monthly_units <= 400):
        charges = 14.43*monthly_units
        return charges
    elif(monthly_units > 400 & monthly_units <= 500):
        charges = 16.43*monthly_units
        return charges
    elif(monthly_units > 500 & monthly_units <= 600):
        charges = 18.43*monthly_units
        return charges
    elif(monthly_units > 600 & monthly_units <= 700):
        charges = 20.43*monthly_units
        return charges
    elif(monthly_units > 700):
        charges = 22.43*monthly_units
        return charges
    else:
        print("invalid syntax")
        
def electricity_duty():
    charges = electricity(monthly_units) 
    duty = charges*0.015
    return duty
    
def TV_fees(Tv):
    Pay = Tv*35
    return Pay

def Fuel(monthly_units):
    charges = monthly_units*3.7
    return charges
    
def Income_Tax():
    cost = electricity(monthly_units) 
    duty = electricity_duty()
    TV = TV_fees(Tv)
    fuel = Fuel(monthly_units)
    charges = cost+duty+TV+fuel 
    if(charges >= 25000):
        Tax = charges*0.075
    else:
        Tax = 0
    return Tax

def main_bill():      #  main function
    charges = electricity(monthly_units) 
    print("Your variable charges cost of " + str(monthly_units) + " units are: " + str(charges))
    duty = electricity_duty()
    print("Your electricity duty cost of " + str(monthly_units) + " units are: " + str(duty))
    TV = TV_fees(Tv) 
    print("Your variable charges cost for " + str(Tv) + " Television of " + str(monthly_units) + " units are: " + str(TV))
    fuel = Fuel(monthly_units)
    print("Your fuel cost of " + str(monthly_units) + " units are: " + str(fuel))
    tax = Income_Tax()
    print("Your sales tax cost of " + str(monthly_units) + " units are: " + str(tax))
    Total = charges + duty + TV + fuel + tax
    print("Your total monthly bill including all our costing is: " + str(Total))
    
monthly_units = int(input("Units: "))
Tv = int(input("Enter No of televisions you have: "))
main_bill()


# In[ ]:





# In[ ]:





# In[ ]:




