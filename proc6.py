#Печёнкина Анастасия 15.09.2026 в 19:08
def DigitCountSum(K):
    C = 0
    S = 0
    for i in str(K):
        C += 1
        S += int(i)
    return C, S

print(DigitCountSum(123))