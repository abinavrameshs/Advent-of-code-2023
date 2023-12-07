# %%

# Python 3 code to demonstrate the 
# working of MD5 (string - hexadecimal)
 
import hashlib
 
# initializing string
str2hash = "pqrstuv1"
 
# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
# %%

def compute_md5_hash_hex(str_input):
    result = hashlib.md5(str_input.encode())
    return result.hexdigest()
# %%

puzzle_input = "yzbqklnj"
for i in range(10000000):
    input_str = puzzle_input + str(i) 
    out_hash=compute_md5_hash_hex(input_str)
    if out_hash.startswith("000000"):
        break 

print(i)
# %%
