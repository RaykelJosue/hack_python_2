"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    # Definición del mapeo de caracteres a números
    mapping = {
        "a": "1",
        "b": 2,
        "c": "3",
        "d": 4,
        "e": "5"
    }
    
    result = []
    i = 0
    while i < len(s):
        item = s[i]
        if isinstance(item, str):
            result.append(mapping.get(item, item))
        else:
            result.append(item)
        i += 1
    
    return result

# Ejemplos de uso:
print(fn_hack_7(["a", "b", "c", "d", "e"]))  # Salida: ["1", 2, "3", 4, "5"]
print(fn_hack_7([0]))                        # Salida: [0]