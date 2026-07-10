import mpmath
from mpmath import zeta, findroot, mp, re, im

mp.dps = 50

def zsinh(x, t=0.5):
    z = x * 1j
    sinus = (zeta(t + z) - zeta(t - z)) / 2
    return im(sinus)

def zcosh(x, t=0.5):
    z = x * 1j
    cosine = (zeta(t + z) + zeta(t - z)) / 2
    return re(cosine)

def find_roots_for_t(func, t, num_roots=20, step=0.091):
    roots = []
    x1 = 0
    y1 = func(x1, t)
    x = step  
    while True:
        y2 = func(x, t)
        if y1 * y2 < 0:
            try:
                r = findroot(lambda s: func(s, t), (x-step, x), method='bisect')
                if not roots or abs(r - roots[-1]) > 1e-8:
                    roots.append(r)
            except:
                pass
        x1 = x
        y1 = y2
        x += step
        if len(roots) >= num_roots:
            break
    return roots

iteration = 20
zsinh_zeros = find_roots_for_t(zsinh, 0.49999, iteration)
zcosh_zeros = find_roots_for_t(zcosh, 0.49999, iteration)

for i in range(iteration):
    print(zsinh_zeros[i])
    print(zcosh_zeros[i])
