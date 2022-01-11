import math

n = int(input("Enter the number of entries to calculate mortgage: "))
name_arr, balance_arr, intrestrate_arr, curr_mp_arr, newpay_arr, cur_dur, new_dur, curr_int, new_int, savings, fees = [], [], [], [], [], [],[],[],[],[],[]

def duration(pay,intrestrate,balance):
    ii = intrestrate/1200
    dur = (math.log((pay/ii)/((pay/ii)-balance)))/(math.log(1+ii))
    return dur

for i in range(1,n+1):
    name = input("Enter the name of  %i borrower: " %i)                                
    balance = float(input("Enter the mortgage balance: "))                      
    intrestrate = float(input("Enter intrest rate: "))                          
    curr_mp = float(input("Enter current montly payment: "))                    
    ext_mp = float(input("Enter extra monthly payment: "))                      
    name_arr.append(name)                                                       #Names of Borrower
    balance_arr.append(round(balance,2))                                        #Mortgage Balance of borrower
    intrestrate_arr.append(round(intrestrate,2))                                #Intrest rate
    curr_mp_arr.append(round(curr_mp,2))                                        #Current Payment
    newpay_arr.append(round(curr_mp+ext_mp,2))                                  #New monthly Payment
    obj = duration(curr_mp,intrestrate,balance)                                 #Current duration
    cd = round(obj)
    cur_dur.append(cd)
    obj = duration(curr_mp+ext_mp,intrestrate,balance)                          #New duration
    nd = round(obj)
    new_dur.append(nd)
    curr_int.append(round((curr_mp*cd)-balance,2))                              #Current Intrest
    new_int.append(round(((curr_mp+ext_mp)*nd)-balance,2))                      #New Intrest
    savings.append(round(((curr_mp*cd)-balance)-(((curr_mp+ext_mp)*nd)-balance),2)) #Savings
    if nd<=(cd/2):
        fees.append("Extra Fees")
    else:
        fees.append("No Fees")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Name   | Mortgage Balance| Intrest Rate|               Current                    |                 New                              |    Savings    |    Fees   |")
print("                                       |   Payment   |   Duration  |    Intrest   |     Payment     |    Duration    |    Intrest    |")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
for i in range(0,n):
    print(name_arr[i],"        ", balance_arr[i],"        ", intrestrate_arr[i],"%    $", curr_mp_arr[i],"    ", int(cur_dur[i]/12),"Yrs ",int(cur_dur[i]%12),"Mo    $", curr_int[i],"     $", 
                            newpay_arr[i],"       ",int(new_dur[i]/12),"Yrs ",int(new_dur[i]%12),"Mo     $", new_int[i],"      $", savings[i],"      ", fees[i])
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")