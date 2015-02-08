try:
    import math, winsound
except RuntimeError as err:
    print(err.args)

def beepity_beep():
    n = str(math.pi)
    n = ''.join(n.split('.'))
    print(n)

    # play a random sequence
    for c in n:
        t = int(c) * 100
        d = 400 - 5 * int(c)
        winsound.Beep(t, d)
        print(c, t, d)

beepity_beep()
