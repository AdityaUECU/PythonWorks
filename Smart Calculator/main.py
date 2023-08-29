import math
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--type", choices = ["diff", "annuity"])           
parser.add_argument("--principal")           
parser.add_argument("--payment")           
parser.add_argument("--periods")           
parser.add_argument("--interest")  

args = parser.parse_args()
enrty = [args.type, args.principal, args.payment, args.periods, args.interest]

if args.type == "":
    print("Incorrect parameters.")
  
if args.type == "diff":
    if args.principal and args.periods and args.interest:        
        li = float(args.interest)
        periods = int(args.periods)
        pl = int(args.principal)
        i = li/1200
        n = int(args.periods) 
        total =0
        for period in range(1, periods+1):
            mp = math.ceil((pl/n)+i*(pl-(pl*(period-1))/n))
            total += mp 
            print(f"Month {period}: payment is {mp}")
            
              
        totally = total-pl    
        print(f"Overpayment = {totally}")
    else:
        print("Incorrect parameters.")
        
if args.type == "annuity":
    if args.payment and args.periods and args.interest:
        li = float(args.interest)
        periods = int(args.periods)
        pl = int(args.payment)
        i = li/1200
        n = periods
        lp = pl/((i*(math.pow(1+i, n)))/(math.pow(1+i, n) - 1))
        print(f"Your loan principal = {lp}!")
        total = pl*n
        totally = total - lp
        print(f"Overpayment = {totally}")
        
    elif args.payment and args.principal and args.interest :
        li = float(args.interest)
        mp = int(args.payment)
        ap = int(args.principal)
        i = li/1200       
        ex = mp/(mp-i*ap)
        n = math.ceil(math.log(ex, 1+i))   
        # month = n%12
        year = math.floor(n/12)
        print(f"It will take {year} years to repay this loan!")
        month = year*12
        total = month*mp
        totally = total-ap
        print(f"Overpayment = {totally}")
    elif args.principal and args.periods and args.interest:
        li = float(args.interest)
        periods = int(args.periods)
        pl = int(args.principal)
        i = li/1200
        n = periods   
        mp = math.ceil(((i*(math.pow(1+i, n)))/(math.pow(1+i, n) - 1))*pl)
        print(f"Your annuity payment = {mp}!")
        # total = pl*n
        # totally = total - mp
        print(f"Overpayment = {mp}")       
    else:
        print("Incorrect parameters.")