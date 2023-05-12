with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

def count_words(file):
    words = file.split()
    return len(words)

def character_count(file):
    file_string = file.lower()
    char_dict = {}
    for c in file_string:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

word_count = count_words(file_contents)
c_count = character_count(file_contents)
sorted_list = sorted(c_count.items(),key=lambda x:x[1], reverse=True)
sorted_dict = dict(sorted_list)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
print("")
for c in sorted_dict:
    if c.isalpha():
        print(f"The '{c}' character was found {c_count[c]} times")
print("--- End report ---")
