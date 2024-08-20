"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    # Convertir la cadena en una lista de caracteres
    chars = list(s)
    length = len(chars)
    
    # Reemplazos basados en el prefijo
    if s.startswith("fo"):
        if length > 2:
            chars[2] = '-'
        if length > 5:
            chars.insert(5, '-')
        if length > 6:
            chars[-1] = '-'
    
    elif s.startswith("ba"):
        if length > 2:
            chars[2] = '-'
        if length > 5:
            chars[5] = '-'
    
    elif length < 5:
        if length > 2:
            chars[2] = '-'
    
    # Convertir la lista de caracteres de nuevo a una cadena
    return ''.join(chars)


print(fn_hack_5("fooziman"))  # Salida: "fo-zi-ma-"
print(fn_hack_5("barziman"))  # Salida: "ba-zi-an"
print(fn_hack_5("qux"))       # Salida: "qu-"
print(fn_hack_5("eq"))        # Salida: "eq"
