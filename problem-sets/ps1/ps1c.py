G_PORTION_DOWN_PAYMENT = 0.25
G_ANNUAL_INVESTMENT_RETURN = 0.04
G_SEMI_ANNUAL_RAISE = 0.07
G_TIME_TILL_DOWNPAYMENT = 36
G_HOUSE_COST = 1000000


def months_to_save(annual_salary: int, portion_saved: float, total_cost: int) -> int:
    money_to_save = total_cost * G_PORTION_DOWN_PAYMENT
    current_savings = 0
    months_passed = 0
    while current_savings < money_to_save:
        months_passed += 1
        if months_passed % 6 == 0:
            # print(f"Raise given at month {months_passed}, current salary is {annual_salary}")
            annual_salary = annual_salary + round(annual_salary * G_SEMI_ANNUAL_RAISE)
            # print(f"New Salary is {annual_salary}")
        return_on_investments = round(current_savings * G_ANNUAL_INVESTMENT_RETURN / 12, 2)
        annual_salary_portion = round(annual_salary * portion_saved / 12, 2)
        current_savings += return_on_investments
        current_savings += annual_salary_portion
    return months_passed


def find_save_rate(annual_salary: int, total_house_cost: int, total_months: int):
    lo = 0.00
    hi = 1.00
    result = 0
    steps = 0
    while lo < hi:
        steps += 1
        mid = (lo + hi) / 2
        result = months_to_save(annual_salary, mid, total_house_cost)
        if result == total_months:
            return round(mid, 2), steps
        if result > total_months:
            lo = mid + 0.01
        else:
            hi = mid
    return "None Found", steps


input_salary = int(input("Enter the starting salary: "))

save_rate, steps_taken = find_save_rate(input_salary, G_HOUSE_COST, G_TIME_TILL_DOWNPAYMENT)

print(f"Best savings rate: {save_rate}")
print(f"Steps in bisection search taken: {steps_taken}")
