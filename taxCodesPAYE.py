
marriageAllowanceTransferor = False #Transfer part of your personal allowance to your spouse
marriageAllowanceTransferee = False #Receive part of your spouses personal allowance
personalAllowance = 11850 #2018/19 personal allowance
marriageAllowanceAmount = 1190 #Capped at £1190
allowableExpenses = 0
adjustmentForOverpaidTax = 0
taxableBenefits = 12707
adjustmentForUnderpaidTax = 0

#Adjust personal allowance for marriage allowance
if marriageAllowanceTransferor == True:
    personalAllowance = personalAllowance - marriageAllowanceAmount
elif marriageAllowanceTransferee:
    personalAllowance = personalAllowance + marriageAllowanceAmount

#Calculate total allowances
totalAllowances = personalAllowance + allowableExpenses + adjustmentForOverpaidTax

#Calculate total deductions
totalDeductions = taxableBenefits + adjustmentForUnderpaidTax

#Net total allowances and total deductions
net = totalAllowances - totalDeductions
print(net)

#Calculate PAYE code
numericCode = 0
if net > 0 and marriageAllowanceTransferee == False and marriageAllowanceTransferor == False: #If positive remove last digit and add the letter 'L' at the end
    numericCode = int((net - (net % 10))/10)
    print(f"Paye Code is: {str(numericCode)}L")
elif net > 0 and marriageAllowanceTransferee == True and marriageAllowanceTransferor == False: #If postive and received marriage allowance
    numericCode = int((net - (net % 10)) / 10)
    print(f"Paye Code is: {str(numericCode)}N")
elif net > 0 and marriageAllowanceTransferee == False and marriageAllowanceTransferor == True: #If postive and transfered marriage allowance
    numericCode = int((net - (net % 10)) / 10)
    print(f"Paye Code is: {str(numericCode)}M")
elif net < 0: #If negative remove last digit and minus 1 from this number, and place the letter 'K' at the beginning
    net = net * -1
    numericCode = int((net - (net % 10))/10 - 1)
    print(f"Paye Code is: K{str(numericCode)}")