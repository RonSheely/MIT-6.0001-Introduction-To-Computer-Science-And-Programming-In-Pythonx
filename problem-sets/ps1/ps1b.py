G_PORTION_DOWN_PAYMENT = 0.25
G_ANNUAL_RETURN = 0.04


def months_to_save(annual_salary: int, portion_saved: float,
                   total_cost: int, semi_annual_raise: float) -> int:
    money_to_save = total_cost * G_PORTION_DOWN_PAYMENT
    current_savings = 0
    months_passed = 0
    while current_savings < money_to_save:
        months_passed += 1
        if months_passed % 6 == 0:
            # print(f"Raise given at month {months_passed}, current salary is {annual_salary}")
            annual_salary = annual_salary + round(annual_salary * semi_annual_raise)
            # print(f"New Salary is {annual_salary}")
        return_on_investments = round(current_savings * G_ANNUAL_RETURN / 12, 2)
        annual_salary_portion = round(annual_salary * portion_saved / 12, 2)
        current_savings += return_on_investments
        current_savings += annual_salary_portion
    return months_passed


input_annual_salary = int(input("Enter your annual salary: "))
input_portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
input_total_cost = int(input("Enter the cost of your dream home: "))
input_semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

number_of_months = months_to_save(input_annual_salary, input_portion_saved,
                                  input_total_cost, input_semi_annual_raise)

print(f"Number of months: {number_of_months}")
