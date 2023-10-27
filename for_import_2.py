from math import sqrt
def main(a,b,c):
    p = ((a * b) + c) / 4

    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return area