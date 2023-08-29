def preprocess_pattern(pattern):
table = {}
pattern_len = len(pattern)
for i in range(pattern_len - 1): 
table[pattern[i]] = pattern_len - i - 1
return table
def horspool_search(text, pattern): 
text_len = len(text)
pattern_len = len(pattern)
table = preprocess_pattern(pattern)
i = pattern_len - 1 
while i < text_len:
k = 0
while k < pattern_len and pattern[pattern_len - 1 - k] == text[i - k]: 
k += 1
if k == pattern_len:
print("Pattern found at index:", i - pattern_len + 1) 
i += table.get(text[i], pattern_len)
def main():
text = input("Enter the text: ")
pattern = input("Enter the pattern to search for: ")
horspool_search(text, pattern)
if name == " main ": 
main()