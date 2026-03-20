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
