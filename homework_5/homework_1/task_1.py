def fibonacci(n):
    Fm_1 = 1
    Fm_2 = 1
    m = 2
    if n == 1 or n == 2:
        Fm = Fm_1
    else:
        while m != n:
            Fm = Fm_1 + Fm_2
            m += 1
            Fm_1 = Fm_2
            Fm_2 = Fm
    return Fm
        
