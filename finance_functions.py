def simple_interest(p, r, t):
    return (p * r * t) / 100

def present_value(fv, r , n):
    r = r/100
    return fv/(1+r)**n

def compound_value(pv, r, n):
    r = r/100
    return pv*(1+r)**n

def compound_interest(pv, r, n):
    fv = compound_value(pv, r, n)
    return fv - pv

def pv_cashflows(cashflows, rate):
    rate = rate / 100
    pv_total = sum(
        row["Cashflow"] / (1 + rate) ** row["Period"]
        for _, row in cashflows.iterrows()
    )
    return pv_total

def present_value_annuity(C, r, n):
    if r == 0:
        return C * n
    return C * (1 - (1 + r) ** (-n)) / r
    
def calculate_emi(P, annual_rate, years):
    r = annual_rate / 100 / 12   # monthly rate
    n = years * 12               # months

    if r == 0:
        return P / n

    EMI = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return EMI

def calculate_irr_df(price, cashflows):
    low = -90      # -90% (because your function expects %)
    high = 200     # 200%
    tolerance = 0.0001
    while high - low > tolerance:
        mid = (low + high) / 2
        pv = pv_cashflows(cashflows, mid)
        if pv > price:
            low = mid
        else:
            high = mid
    return mid
