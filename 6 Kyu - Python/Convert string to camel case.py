def to_camel_case(text):
    #your code here
    text = text.replace('-',' ').replace('_',' ')
    text = [c for c in text]
    
    if len(text) == 0:
        return ''
    else:
        for i in range(1, len(text)):
            if text[i-1] == ' ':
                text[i] = text[i].title()
    return ''.join(text).replace(' ','')
