import math

def pow(a, b):
    return math.pow(a, b)

def PV(FV, r, N):
    return FV / pow(1+r, N)

def FV(PV, r, N):
    return PV * pow(1+r, N)

def get_IRR(PV, FV, N):
    return pow((FV / PV), 1 / N)

def future_value_annuity_factor(r, N):
    return (pow(1+r, N) - 1) / r 

def present_value_annuity_factor(r, N):
    return (1 - pow(1+r, -N)) / r

def macaulay_duration(coupon, last_payment, years):
    pass



if __name__ == "__main__":
    # r = 0.09

    # result = 10000 * future_value_annuity_factor(0.09, 10)

    # result = FV(result, r, 1)


    # print(result)

    # result = 10000 * pow(1+r, 3) + 10000 * pow(1+r, 2) + 10000 * pow(1+r, 1) + 10000

    # print(result)

    print(get_IRR(100, 200, 5))

    print(PV(200, 0.15, 5))