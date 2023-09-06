# Calculate the compound interest for a given principal amount, interest rate, and time period
PA= int(input("Enter Principal amount: "))
rate= float(input("Enter Interest: "))
time= int(input("Enter no.of years: "))

Amount = PA *(pow((1+rate/100),time))
CI= Amount-PA
print("compound Interest is: ", CI)