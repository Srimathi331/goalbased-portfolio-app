def calculate_expected_wealth(investment_amount, annual_return, years, monthly_investment=False):
    months = years * 12
    monthly_return = (1 + annual_return) ** (1/12) - 1
    
    if monthly_investment:
        # Future value of monthly investments over months
        future_value = investment_amount * ((1 + monthly_return) ** months - 1) / monthly_return
    else:
        # Future value of lump sum invested once
        future_value = investment_amount * (1 + monthly_return) ** months
    
    return future_value
