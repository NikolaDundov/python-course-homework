def mortgage_payment(amount, yearly_rate, years):
    r = yearly_rate / 12 / 100
    return round(amount * r / (1 - (1 + r) ** - (years * 12)),2) 
print(mortgage_payment)