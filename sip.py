# SIP calculator function
def sip_calculator():
    P = float(input("Enter monthly investment amount (P): "))
    r = float(input("Enter annual rate of return (r in %): "))
    n = int(input("Enter the number of years (n): ")) * 12  # convert years to months
    monthly_rate = r / (12 * 100)
    future_value = P * ((1 + monthly_rate) ** n - 1) / monthly_rate * (1 + monthly_rate)
    total_amount = n*P
    print(f"Invested Amount :{total_amount:.2f}",)
    print(f"Total Earnings:{future_value-total_amount:.2f}",)
    print(f"Future Value of SIP: {future_value:.2f}\n")

# Lumpsum calculator function
def lumpsum_calculator():
    P = float(input("Enter lumpsum investment amount (P): "))
    r = float(input("Enter annual rate of return (r in %): "))
    n = int(input("Enter the number of years (n): "))
    total_amount = P * (1 + r / 100) ** n
    print(f"Future lumpsum amount: {total_amount:.2f}\n")

# Switch-case implementation using match-case (Python 3.10+)
def switch_case(value):
    match value:
        case 1:
            sip_calculator()
        case 2:
            lumpsum_calculator()
        case 3:
            print("Exiting the program...")
            exit()
        case _:
            print("Invalid choice! Please enter a valid number.")

# Main execution starts here
while True:
    print("INVESTMENT CALCULATOR")
    print("1. SIP CALCULATOR")
    print("2. LUMPSUM CALCULATOR")
    print("3. Exit")

    value = int(input("Enter your choice: "))
    switch_case(value)
