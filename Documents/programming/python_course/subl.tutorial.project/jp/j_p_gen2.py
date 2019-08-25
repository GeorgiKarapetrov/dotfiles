def p(x, s=0):
    v =yield
    while True:
        if s+v<=x:
            s +=v
            v= yield True
        else:
            v=yield False

