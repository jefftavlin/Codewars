def solution(s):
    s = [s for s in s]
    final = []
    
    for i in range(len(s)):
        if i % 2 == 0:
            final.append(s[i])
        else:
            final.append(s[i])
            final.append('_')
    
    final = [pair for pair in ''.join(final).split('_') if pair != '']
    final = [pair if len(pair) == 2 else pair + '_' for pair in final]
    return final
