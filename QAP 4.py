# Program for , By Lucas Keats, 11/29/23.
while True:

 from datetime import datetime

 # Default values
 next_policy_number = 1944
 basic_premium = 869.00
 discount_for_additional_cars = 0.25
 cost_of_extra_liability_coverage = 130.00
 cost_of_glass_coverage = 86.00
 cost_for_loaner_car_coverage = 58.00
 hst_rate = 0.15
 processing_fee_monthly_payments = 39.99

 # Lists to store previous claims
 claim_dates = []
 claim_amounts = []

 def format_values(value):
    # Placeholder for FormatValues library or custom formatting function
    pass

 def get_customer_information():
    print()
    first_name = input("Enter customer's first name: ").title()
    last_name = input("Enter customer's last name: ").title()
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ").title()
    province_list = ['ON', 'BC', 'AB', 'QC', 'NL', 'SK', 'NS', 'NB', 'MB', 'PE']  # Add other provinces as needed
    province = input("Enter customer's province (ON, BC, AB, QC, NL, SK, NS, NB, MB, PE): ").upper()
    while province not in province_list:
        province = input("Invalid province. Enter customer's province (ON, BC, AB, QC, NL, SK, NS, NB, MB, PE): ").upper()
    
    postal_code = input("Enter customer's postal code: ")
    phone_number = input("Enter customer's phone number: ")

    num_cars = int(input("Enter the number of cars being insured: "))

    extra_liability_option = input("Do you want extra liability coverage? (Y/N): ").upper()
    glass_coverage_option = input("Do you want glass coverage? (Y/N): ").upper()
    loaner_car_option = input("Do you want loaner car coverage? (Y/N): ").upper()

    payment_options = ['FULL', 'MONTHLY', 'DOWN PAY']
    payment_method = input("Select payment method (Full/Monthly/Down Pay): ").upper()
    while payment_method not in payment_options:
        payment_method = input("Invalid payment method. Select payment method (Full/Monthly/Down Pay): ").upper()

    down_payment = 0.0
    if payment_method == 'DOWN PAY':
        down_payment = float(input("Enter the amount of the down payment: "))

    return {
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'city': city,
        'province': province,
        'postal_code': postal_code,
        'phone_number': phone_number,
        'num_cars': num_cars,
        'extra_liability_option': extra_liability_option,
        'glass_coverage_option': glass_coverage_option,
        'loaner_car_option': loaner_car_option,
        'payment_method': payment_method,
        'down_payment': down_payment
    }

 def calculate_premium_and_costs(num_cars, extra_liability_option, glass_coverage_option, loaner_car_option):
    total_premium = basic_premium + (num_cars - 1) * (basic_premium * discount_for_additional_cars)

    extra_costs = 0.0
    if extra_liability_option == 'Y':
        extra_costs += num_cars * cost_of_extra_liability_coverage
    if glass_coverage_option == 'Y':
        extra_costs += num_cars * cost_of_glass_coverage
    if loaner_car_option == 'Y':
        extra_costs += num_cars * cost_for_loaner_car_coverage

    total_premium += extra_costs
    hst = total_premium * hst_rate
    total_cost = total_premium + hst

    return total_premium, extra_costs, hst, total_cost

 def calculate_monthly_payment(total_cost, down_payment=0.0):
    if down_payment > 0:
        remaining_balance = total_cost - down_payment
    else:
        remaining_balance = total_cost

    monthly_payment = (remaining_balance + processing_fee_monthly_payments) / 8
    return monthly_payment

 def display_receipt(customer_info, total_premium, extra_costs, hst, total_cost):
    print("\n----- Receipt -----\n")
    print(f"Policy Number: {next_policy_number}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"\nCustomer Information:")
    print(f"Name: {customer_info['first_name']} {customer_info['last_name']}")
    print(f"Address: {customer_info['address']}, {customer_info['city']}, {customer_info['province']} {customer_info['postal_code']}")
    print(f"Phone Number: {customer_info['phone_number']}")
    print(f"\nInsurance Information:")
    print(f"Number of Cars: {customer_info['num_cars']}")
    print(f"Extra Liability Coverage: {customer_info['extra_liability_option']}")
    print(f"Glass Coverage: {customer_info['glass_coverage_option']}")
    print(f"Loaner Car Coverage: {customer_info['loaner_car_option']}")
    print(f"\nPayment Information:")
    print(f"Payment Method: {customer_info['payment_method']}")
    if customer_info['payment_method'] == 'DOWN PAY':
        print(f"Down Payment: ${customer_info['down_payment']:.2f}")
    print(f"\nPremium and Costs:")
    print(f"Basic Premium: ${basic_premium:.2f}")
    print(f"Additional Cars Discount: ${extra_costs:.2f}")
    print(f"Extra Liability Coverage Cost: ${extra_costs:.2f}")
    print(f"Glass Coverage Cost: ${extra_costs:.2f}")
    print(f"Loaner Car Coverage Cost: ${extra_costs:.2f}")
    print(f"Total Premium: ${total_premium:.2f}")
    print(f"HST (15%): ${hst:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

 def enter_previous_claims():
    print()
    num_claims = int(input("Enter the number of previous claims: "))
    for i in range(1, num_claims + 1):
        claim_date = input(f"Enter claim {i} date (YYYY-MM-DD): ")
        claim_amount = float(input(f"Enter claim {i} amount: $"))
        claim_dates.append(claim_date)
        claim_amounts.append(claim_amount)

 def display_previous_claims():
    print("\nPrevious Claims:")
    print("Claim #   Claim Date   Amount")
    print("---------------------------------")
    for i in range(len(claim_dates)):
        print(f"{i + 1}. {claim_dates[i]}    ${claim_amounts[i]:,.2f}")

 # Main program
 customer_info = get_customer_information()
 total_premium, extra_costs, hst, total_cost = calculate_premium_and_costs(
    customer_info['num_cars'],
    customer_info['extra_liability_option'],
    customer_info['glass_coverage_option'],
    customer_info['loaner_car_option']
)
 monthly_payment = calculate_monthly_payment(total_cost, customer_info['down_payment'])

 display_receipt(customer_info, total_premium, extra_costs, hst, total_cost)

 enter_previous_claims()
 display_previous_claims()

 user_input = input("Do you want to continue? (yes/no): ")
 if user_input.lower() != 'yes':
        break