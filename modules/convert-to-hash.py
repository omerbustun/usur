# Use hashlib
import hashlib

# Open txt
with open('C:/Users/TAW/Documents/GitHub/AbiHacklendikGaliba/based_html/dedas_baseHTML.txt') as f:
    lines = f.readlines()
with open('C:/Users/TAW/Documents/GitHub/AbiHacklendikGaliba/based_html/dedas_baseHTML2.txt') as f:
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

dedas_html_hash = int(hashlib.sha1(stringver.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
dedas_changed_html_hash = int(hashlib.sha1(stringver2.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
print("Dedas html hash:         " + str(dedas_html_hash))
print("Dedas changed html hash: " + str(dedas_changed_html_hash))
