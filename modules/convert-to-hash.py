# Use hashlib
import hashlib

# Open txt
with open('C:/usur/base_html/baseHTML.txt') as f:
    lines = f.readlines()
with open('C:/usur/base_html/baseHTML2.txt') as f:
    lines2 = f.readlines()
# Convert txt list to String
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele   
    return str1 
# Convert Txt list to string
stringver = listToString(lines)
stringver2 = listToString(lines2)

html_hash = int(hashlib.sha1(stringver.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
changed_html_hash = int(hashlib.sha1(stringver2.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
print("html hash:         " + str(html_hash))
print("changed html hash: " + str(changed_html_hash))
