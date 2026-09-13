transactions = {
    "Aman": [500, 1200, 300, 15000, 700],
    "Riya": [200, 300, 450, 600],
    "Karan": [10000, 50, 80, 12000],
    "Simran": [400, 500, 600, 700]
}

highest_spending = 0
top_spender = ""
global_suspicious_count = 0

for customer, amounts in transactions.items():
    total_spent = 0
    suspicious_count = 0
    
    for amount in amounts:
        total_spent += amount
        if amount > 10000:
            suspicious_count += 1
            global_suspicious_count += 1
            
    if suspicious_count >= 2 or (suspicious_count == 1 and total_spent > 20000):
        print(f"{customer} High Risk")
    else:
        print(f"{customer} Low Risk")
        
    print(f"  Total amount spent: ₹{total_spent}")
    print(f"  Suspicious transactions: {suspicious_count}")
    
    if total_spent > highest_spending:
        highest_spending = total_spent
        top_spender = customer

print(f"Customer with highest total spending: {top_spender} (₹{highest_spending})")
print(f"Total number of suspicious transactions across all customers: {global_suspicious_count}")