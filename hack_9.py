"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(input_dict):
    # Diccionario para almacenar el resultado final
    output_dict = {}
    
    # Itera sobre cada par clave-valor en el diccionario de entrada
    for idx, (key, value) in enumerate(input_dict.items()):
        # Procesa solo el primer par clave-valor
        if idx == 0:
            # Transforma la clave a formato capitalizado
            modified_key = key[0].upper() + key[1:]
            
            # Transforma el valor a formato capitalizado y elimina la letra 'k'
            modified_value = value[0].upper() + value[1:].replace('k', '')
            
            # Asigna la clave y el valor transformados al diccionario de salida
            output_dict[modified_key] = modified_value
    
    return output_dict


print(fn_hack_9({"foo": "fookziman", "bar": "barziman"}))  # Output: {"Foo": "Fooziman"}

