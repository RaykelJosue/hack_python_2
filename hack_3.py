"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 

"""

def fn_hack_3(input_str):
    output_str = input_str
    vowels = ["a", "e", "i", "o", "u"]
    replacements = ["@", "3", "¡", "0", "v"]
    transformed_chars = []
    counter = 0
    
    for char in output_str:
        if char in vowels:
            idx = vowels.index(char)
            transformed_chars.append(replacements[idx])
        else:
            if counter == 0 or counter == len(output_str) - 1:
                transformed_chars.append(char.upper())
            else:
                transformed_chars.append(char)
        counter += 1
    
    output_str = "".join(transformed_chars)
    return output_str

print(fn_hack_3('fooziman')) 
print(fn_hack_3('barziman'))  
print(fn_hack_3('3q'))
print(fn_hack_3('qu'))
print(fn_hack_3('qux'))