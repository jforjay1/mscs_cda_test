import math

n = int(input("Enter the number of entries to calculate mortgage: "))
name_arr, balance_arr, intrestrate_arr, curr_mp_arr, newpay_arr, cur_dur, new_dur, curr_int, new_int, savings, fees = [], [], [], [], [], [],[],[],[],[],[]

def duration(pay,intrestrate,balance):
    ii = intrestrate/1200
    dur = (math.log((pay/ii)/((pay/ii)-balance)))/(math.log(1+ii))
    return dur

for i in range(1,n+1):
    name = input("Enter the name of  %i borrower: " %i)                                
    balance = float(input("Enter the mortgage balance: $"))                      
    intrestrate = float(input("Enter intrest rate: "))                          
    curr_mp = float(input("Enter current montly payment: $"))                    
    ext_mp = float(input("Enter extra monthly payment: $"))
    print(" ")
    print(" ")                      
    name_arr.append(name)                                                       #Names of Borrower
    balance_arr.append(format(balance, '.2f'))                                        #Mortgage Balance of borrower
    intrestrate_arr.append(format(intrestrate, '.3f'))                                #Intrest rate
    curr_mp_arr.append(format(curr_mp, '.2f'))                                        #Current Payment
    newpay_arr.append(format(curr_mp+ext_mp, '.2f'))                                  #New monthly Payment
    obj = duration(curr_mp,intrestrate,balance)                                 #Current duration
    cd = round(obj)
    cur_dur.append(cd)
    obj = duration(curr_mp+ext_mp,intrestrate,balance)                          #New duration
    nd = round(obj)
    new_dur.append(nd)
    curr_int.append(format((curr_mp*cd)-balance,'.2f'))                              #Current Intrest
    new_int.append(format(((curr_mp+ext_mp)*nd)-balance,'.2f'))                      #New Intrest
    savings.append(format(((curr_mp*cd)-balance)-(((curr_mp+ext_mp)*nd)-balance),'.2f')) #Savings
    if nd<=(cd/2):
        fees.append("Extra Fees")
    else:
        fees.append("No Fees")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Name   | Mortgage Balance| Intrest Rate|               Current                    |                 New                              |    Savings    |    Fees   |")
print("                                       |   Payment   |   Duration  |    Intrest   |     Payment     |    Duration    |    Intrest    |")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
for i in range(0,n):
    print(name_arr[i],"     ", "$"+str(balance_arr[i]),"      ", str(intrestrate_arr[i])+"%","      ", "$"+str(curr_mp_arr[i]),"    ", 
    str(int(cur_dur[i]/12))+"yrs "+str(int(cur_dur[i]%12))+"mo      ","$"+str(curr_int[i]),"     ","$"+str(newpay_arr[i]),"      ",
    str(int(new_dur[i]/12))+"yrs ",str(int(new_dur[i]%12))+"mo      ", "$"+str(new_int[i]),"      ", "$"+str(savings[i]),"      ", fees[i])
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")