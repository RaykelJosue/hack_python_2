"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    transformed_list = []

    segments = [result[i:i+3] for i in range(0, len(result), 3)]

    for segment in segments:
        if len(segment) == 3:
            new_segment = f"{segment[0]}{segment[1].upper()}{segment[2]}"
            transformed_list.append(new_segment)
        else:
            transformed_list.append(segment)
    
    final_result = "".join(transformed_list)
    return final_result

if __name__ == "__main__":
    test_string = "fooziman"
    print(fn_hack_1(test_string))