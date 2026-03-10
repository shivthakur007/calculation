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
    pv_total = 0
    for t, cf in cashflows:
        pv = cf / (1 + rate) ** t
        pv_total += pv

    return pv_total
