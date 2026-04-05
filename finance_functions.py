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
    r = r / 12          # monthly rate
    n = n * 12          # convert years to months
    PV = C * (1 - (1 + r) ** (-n)) / r
    return PV

def calculate_emi(P, annual_rate, years):
    r = annual_rate / 12
    n = years * 12 
    if r == 0:
        return P / n
    EMI = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return EMI

