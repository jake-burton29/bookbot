def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    words = count_words(file_contents)
    char_dict = count_char(file_contents)
    print('--- Begin report of books/frankenstein.txt ---')
    print (f"{len(words)} words found in the document \n")
    report(char_dict)
    print('--- End report ---')

def count_words(file_contents):
    words = file_contents.split()
    return words
   
def count_char(file_contents):
    count = {}
    string = file_contents.lower()
    for char in string:
        if char in count and char.isalpha():
            count[char] += 1
        else:
            count.update({char: 1})
    return count
    
def sort_on(dict): 
    return dict["num"]

def report(dict):
    my_list = []
    for d in dict:
        if d.isalpha():
            my_list.append({"char":d,"num": dict[d]})
    my_list.sort(reverse=True, key=sort_on)
    for i in my_list:
        print(f"The '{i.get('char')}' character was found {i.get('num')} times")

main()