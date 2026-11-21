# Run from the tools/ folder: python3 gen_sample_data.py  (writes ../sample_data/)
import random, datetime as dt, csv, io, json
random.seed(42)
rows=[]  # (date, narration, ref, debit, credit)
def d(y,m,day): return dt.date(y,m,day)
def add(date, narr, debit=0, credit=0):
    rows.append([date, narr, debit, credit])
def ref(): return str(random.randint(600000000000, 699999999999))
months=[(2026,8,31),(2026,9,30),(2026,10,31)]
food=[('SWIGGY','swiggy@icici'),('ZOMATO','zomato@hdfcbank')]
groc=[('BLINKIT','blinkit.payu@hdfcbank'),('ZEPTO','zeptonow@ybl'),('BIGBASKET','bigbasket@icici')]
cabs=[('UBER INDIA','uber.rides@axisbank'),('OLA','olacabs@ybl'),('RAPIDO','rapido@ybl')]
dine=[('TOIT BREWPUB','toitbrew@ybl'),('THIRD WAVE COFFEE','thirdwave@icici'),('MTR RESTAURANT','mtr1924@okaxis'),('SRI LAKSHMI TIFFINS','srilakshmitiffins@okicici'),('MEGHANA FOODS','meghanafoods@ybl')]
shop=[('AMAZON PAY','amazon@apl'),('MYNTRA','myntra@icici'),('FLIPKART','flipkart@axisbank'),('DECATHLON','decathlonin@hdfcbank')]
for (y,m,last) in months:
    mn=dt.date(y,m,1).strftime('%b').upper()
    add(d(y,m,1), f"NEFT CR-CITI0000001-ACME TECHNOLOGIES PVT LTD-SALARY {mn}{str(y)[2:]}-CITIN{y}{m:02d}01{random.randint(10000,99999)}", credit=85000)
    add(d(y,m,2), f"UPI-CULTFIT-cultfit.payu@hdfcbank-HDFC0000499-{ref()}-CULTPASS ELITE", debit=1599)
    add(d(y,m,3), f"UPI-RAMESH KUMAR-rameshk@okhdfcbank-HDFC0001234-{ref()}-PAYMENT FROM PHONE", debit=22000)
    add(d(y,m,5), "ACH D- ICCL-MF SIP-HDFC00000012345678", debit=5000)
    add(d(y,m,7), "POS 512345XXXXXX5678 NETFLIX.COM", debit=649)
    add(d(y,m,10), f"BIL/BPAY/{random.randint(100000,999999)}/BESCOM ELECTRICITY", debit=random.choice([1180,1340,1520]))
    add(d(y,m,12), "POS 512345XXXXXX5678 SPOTIFY INDIA", debit=119)
    add(d(y,m,15), f"UPI-AMAZON PRIME VIDEO-amazonprime@apl-UTIB0000100-{ref()}-PRIME MONTHLY", debit=299)
    add(d(y,m,16), f"UPI-JIOHOTSTAR-jiohotstar@icici-ICIC0000104-{ref()}-SUBSCRIPTION", debit=299)
    add(d(y,m,18), f"UPI-ACT FIBERNET-actfibernet@axisbank-UTIB0000034-{ref()}-BROADBAND", debit=1050)
    add(d(y,m,20), f"BIL/BPAY/{random.randint(100000,999999)}/AIRTEL POSTPAID", debit=599)
    add(d(y,m,random.randint(8,12)), f"NWD-512345XXXXXX5678-ATM KORAMANGALA 5TH BLOCK", debit=2000)
    add(d(y,m,random.randint(4,6)), f"UPI-NAMMA METRO-bmrcl@sbi-SBIN0000813-{ref()}-CARD RECHARGE", debit=500)
    add(d(y,m,25), f"UPI-DMART AVENUE-dmart@ybl-YESB0000001-{ref()}-GROCERY", debit=random.choice([2380,2615,2890]))
    for _ in range(random.randint(10,13)):
        n,v=random.choice(food); add(d(y,m,random.randint(1,last)), f"UPI-{n}-{v}-ICIC0DC0099-{ref()}-ORDER", debit=random.choice([248,312,365,410,455,520,589,640]))
    for _ in range(random.randint(6,8)):
        n,v=random.choice(groc); add(d(y,m,random.randint(1,last)), f"UPI-{n}-{v}-HDFC0000001-{ref()}-ORDER", debit=random.choice([286,412,535,698,845,1120,1385]))
    for _ in range(random.randint(9,12)):
        n,v=random.choice(cabs); add(d(y,m,random.randint(1,last)), f"UPI-{n}-{v}-UTIB0000001-{ref()}-RIDE", debit=random.choice([118,156,198,236,289,342,415]))
    for _ in range(random.randint(4,5)):
        n,v=random.choice(dine); add(d(y,m,random.randint(1,last)), f"UPI-{n}-{v}-ICIC0000001-{ref()}-PAYMENT", debit=random.choice([280,420,650,980,1450,2350]))
    for _ in range(random.randint(2,3)):
        n,v=random.choice(shop); add(d(y,m,random.randint(1,last)), f"UPI-{n}-{v}-UTIB0000002-{ref()}-ORDER", debit=random.choice([649,899,1299,1899,2499,3499]))
    add(d(y,m,random.randint(13,22)), f"UPI-APOLLO PHARMACY-apollopharmacy@icici-ICIC0000221-{ref()}-MEDICINES", debit=random.choice([385,520,740]))
    add(d(y,m,random.randint(21,27)), f"IMPS-{ref()}-ANKIT SHARMA-SBIN0001234-SPLIT DINNER", debit=random.choice([850,1200,1600]))
# one-offs
add(d(2026,9,13), f"UPI-MAKEMYTRIP-mmt@icici-ICIC0000331-{ref()}-HOTEL COORG", debit=8400)
add(d(2026,9,12), f"UPI-IRCTC-irctc@sbi-SBIN0000691-{ref()}-TICKET", debit=1250)
add(d(2026,10,24), f"UPI-MYNTRA-myntra@icici-UTIB0000002-{ref()}-DIWALI SALE", debit=4999)
add(d(2026,10,19), f"UPI-URBAN COMPANY-urbancompany@ybl-YESB0000004-{ref()}-HOME CLEANING", debit=1899)
add(d(2026,8,22), f"UPI-BOOKMYSHOW-bookmyshow@icici-ICIC0000071-{ref()}-MOVIE", debit=640)
add(d(2026,10,11), f"UPI-GOPAL PROVISION STORE-gopalstores@okaxis-UTIB0000111-{ref()}-PAYMENT", debit=730)
rows.sort(key=lambda r:(r[0], -r[3]))
bal=140000
out=io.StringIO()
out.write('HDFC BANK Ltd.\n"Statement of account"\n"Account No :XXXXXXXX1234   Priya S, Koramangala, Bengaluru"\n"Statement From : 01/08/2026  To : 31/10/2026"\n\n')
w=csv.writer(out)
w.writerow(['Date','Narration','Chq./Ref.No.','Value Dt','Withdrawal Amt.','Deposit Amt.','Closing Balance'])
def fmt(x): return f"{x:,.2f}" if x else ""
for date,narr,deb,cre in rows:
    bal=bal-deb+cre
    ds=date.strftime('%d/%m/%y')
    w.writerow([ds,narr,'0000'+str(random.randint(100000000,999999999)),ds,fmt(deb),fmt(cre),fmt(bal)])
out.write('\n"**Computer generated statement - does not require signature**"\n')
open('../sample_data/hdfc_statement_aug-oct_2026.csv','w').write(out.getvalue())
print(len(rows),'csv rows; closing balance',bal)

# SMS for November 1-20
sms=[]
def sms_upi_debit(day, amt, vpa, name):
    sms.append(f"Rs.{amt:.2f} debited from A/c XX1234 on {day:02d}-11-26 to VPA {vpa} ({name}). UPI Ref no {ref()}. Not you? Call 18002586161 - HDFC Bank")
sms.append(f"Update! INR 85,000.00 deposited in HDFC Bank A/c XX1234 on 01-NOV-26 for NEFT Cr-CITI0000001-ACME TECHNOLOGIES PVT LTD-SALARY NOV26.Avl bal INR 1,31,204.50. Cheque deposits subject to clearing")
sms_upi_debit(2,1599,'cultfit.payu@hdfcbank','CULTFIT')
sms.append(f"Sent Rs.22000.00 From HDFC Bank A/C *1234 To RAMESH KUMAR On 03/11/26 Ref {ref()} Not You? Call 18002586161/SMS BLOCK UPI to 7308080808")
sms.append("Your A/c XX1234 has been debited by Rs.5,000.00 on 05-Nov-26 towards ACH D- ICCL-MF SIP. Avl Bal Rs.1,02,384.12")
sms.append("INR 799.00 spent on HDFC Bank Debit Card XX5678 at NETFLIX.COM on 2026-11-07:09:14:22. Avl Bal: INR 98,912.40. Not you? Call 18002586161")
sms.append("Your OTP for transaction of Rs.1,299.00 at MYNTRA is 482913. Valid for 5 mins. Do not share this OTP with anyone - HDFC Bank")
sms.append("Get a pre-approved Personal Loan of up to Rs.5,00,000 at attractive rates! Click hdfcbk.io/xyz to apply. T&C apply")
sms.append("INR 119.00 spent on HDFC Bank Debit Card XX5678 at SPOTIFY INDIA on 2026-11-12:07:01:10. Avl Bal: INR 84,201.11.")
sms_upi_debit(15,299,'amazonprime@apl','AMAZON PRIME VIDEO')
sms_upi_debit(16,299,'jiohotstar@icici','JIOHOTSTAR')
sms_upi_debit(18,1050,'actfibernet@axisbank','ACT FIBERNET')
sms.append(f"Rs.2000.00 withdrawn at ATM KORAMANGALA 5TH BLOCK from A/c XX1234 on 09-11-26. Avl Bal Rs.92,113.40")
sms.append(f"Rs.1,410.00 paid via BBPS for BESCOM ELECTRICITY from A/c XX1234 on 10-11-26. Ref {ref()}")
sms_upi_debit(5,500,'bmrcl@sbi','NAMMA METRO')
# food delivery overspend in Nov
fd=[(1,412),(2,589),(3,365),(4,640),(6,455),(7,520),(8,589),(9,640),(11,410),(12,365),(13,589),(14,455),(16,640),(17,520),(19,589),(20,410)]
for day,amt in fd:
    n,v=random.choice(food); sms_upi_debit(day,amt,v,n)
for day,amt in [(4,845),(9,535),(12,1120),(17,698)]:
    n,v=random.choice(groc); sms_upi_debit(day,amt,v,n)
for day,amt in [(3,236),(6,198),(10,342),(13,156),(15,289),(18,415)]:
    n,v=random.choice(cabs); sms_upi_debit(day,amt,v,n)
for day,amt in [(8,2350),(14,980)]:
    n,v=random.choice(dine); sms_upi_debit(day,amt,v,n)
sms_upi_debit(8,3499,'myntra@icici','MYNTRA')
sms_upi_debit(19,1899,'amazon@apl','AMAZON PAY')
# messy formats that need AI extraction
sms.append("Txn of INR 1,250 done via UPI on 14 Nov at SRI LAKSHMI TIFFINS frm a/c ending 1234. Ref 512398712. -Kotak")
sms.append("Dear Customer, your a/c no. XX1234 is debited for Rs 2,750 on 17Nov26 trf to DECATHLON SPORTS INDIA. If not done by you, report immediately.")
open('../sample_data/bank_sms_nov_2026.txt','w').write('\n'.join(sms)+'\n')
print(len(sms),'sms')
