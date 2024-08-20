"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vowels = {"a", "e", "i", "o", "u"}
    filtered_chars = [char for char in result if char.lower() not in vowels]

    final_result = "".join(filtered_chars)
    return final_result

if __name__ == "__main__":
    test_string = "fooziman"
    print(fn_hack_2(test_string))