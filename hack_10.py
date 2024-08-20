"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(input_list):
    result_list = []
    
    # Iniciar el contador para las claves y valores
    key_counter = 1
    value_counter = 2
    
    # Procesar cada diccionario en la lista de entrada
    for dic in input_list:
        new_dic = {}
        for key in dic:
            new_dic[str(key_counter)] = str(value_counter)
            key_counter += 2
            value_counter += 2
        result_list.append(new_dic)
    
    return result_list

print(fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]))  # Salida: [{"1":"2"},{"3":"4"},{"5":"6"}]
