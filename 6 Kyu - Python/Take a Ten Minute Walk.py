def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        n, s, w, e = walk.count('n'), walk.count('s') * -1, walk.count('w') * -1, walk.count('e')
        result = ((n + s), (w + e))
        if result == (0,0):
            return True
        else:
            return False
