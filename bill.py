bill = float(input("Enter shopping bill: "))
if bill >= 5000:
    discount = bill *0.10
    final = bill - discount
    print("10% discount applied! Final amount: ", final)
else:
        print("No discount. Final amount: ",bill)