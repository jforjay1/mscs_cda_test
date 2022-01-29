import math

n = int(input("Enter the number of entries to calculate mortgage: "))

dictx = []

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
    obj = duration(curr_mp,intrestrate,balance)                                 #Current duration
    curr_d = round(obj)
    obj = duration(curr_mp+ext_mp,intrestrate,balance)                          #New duration
    new_d = round(obj)   
    if new_d<=(curr_d/2):
        fees="Extra Fees"
    else:
        fees="No Fee"                   
    varx = [name,
                    format(balance, '.2f'),
                    format(intrestrate, '.3f'),
                    format(curr_mp, '.2f'),
                    curr_d,
                    format((curr_mp*curr_d)-balance, '.2f'),
                    format(curr_mp+ext_mp, '.2f'),
                    new_d,
                    format(((curr_mp+ext_mp)*new_d)-balance, '.2f'),
                    float(((curr_mp*curr_d)-balance)-(((curr_mp+ext_mp)*new_d)-balance)),
                    fees]
    dictx.append(varx)

dictx.sort(key = lambda x: x[9], reverse=True)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Name   | Mortgage Balance| Intrest Rate|               Current                    |                 New                              |    Savings    |    Fees   |")
print("                                       |   Payment   |   Duration  |    Intrest   |     Payment     |    Duration    |    Intrest    |")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
for i in range(0,n):
    print(dictx[i][0],"     ", "$"+dictx[i][1],"      ", dictx[i][2]+"%","      ", "$"+dictx[i][3],"    ",str(int((dictx[i][4])/12))+"yrs "
    +str(int((dictx[i][4])%12))+"mo      ","$"+dictx[i][5],"     ","$"+dictx[i][6],"      ",str(int((dictx[i][7])/12))+"yrs ",
    str(int((dictx[i][7])%12))+"mo      ", "$"+dictx[i][8],"      ", "$"+format(dictx[i][9], '.2f'),"      ", dictx[i][10])
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")