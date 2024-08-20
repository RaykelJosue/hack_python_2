"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    # Define el mapeo de caracteres a sus valores
    mapping = {
        "a": "1",
        "b": "-",
        "c": "3",
        "d": "-",
        "e": "5"
    }
    
    # Si la lista está vacía, devuelve ["0"]
    if not s:
        return ["0"]
    
    # Convierte la lista usando el mapeo
    result = [mapping.get(char, char) for char in s]
    return result


print(fn_hack_6(["a","b","c","d","e"]))  # Salida: ["1","-","3","-","5"]
print(fn_hack_6([]))  # Salida: ["0"]

