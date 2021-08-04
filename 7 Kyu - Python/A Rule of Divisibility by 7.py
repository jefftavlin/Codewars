def seven(m):
    # your code
    steps = 0
    while len(str(m)) > 2:
        start = int(str(m)[0:-1])
        end = int(str(m)[-1])
        m = start - (2 * end)
        steps +=1
    
    return (m, steps)
