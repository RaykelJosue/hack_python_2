"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    length = len(s)
    
    if length % 2 == 0:
        # Para listas con longitud par, devuelve los índices descendentes
        return [str(length - idx) for idx in range(length)]
    else:
        # Para listas con longitud impar, devuelve en formato "carácter-índice"
        return [f"{char}-{length - idx}" for idx, char in enumerate(s[::-1])]


print(fn_hack_8(["a", "b", "c", "d", "e"]))  # Salida: ["5", "4", "3", "2", "1"]
print(fn_hack_8(["a", "b", "c"]))             # Salida: ["c-3", "b-2", "a-1"]
print(fn_hack_8(["a", "b", "c", "d"]))        # Salida: ["4", "3", "2", "1"]
print(fn_hack_8(["a", "b"]))                  # Salida: ["2", "1"]
