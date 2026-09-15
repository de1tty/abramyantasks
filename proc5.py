#Печёнкина Анастасия 15.09.2026 в 18:48


def RectPS(x1,x2,y1,y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    P = 2 * (x + y)
    S = x * y
    return P, S

print(RectPS(21,34,12,22))