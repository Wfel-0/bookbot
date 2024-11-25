def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

        print(f"--- Begin report of {path} ---")
        print(f"{count_words(file_contents)} words found in the document")
        final_dic = dic_sort(dic_to_list_of_dics(count_chars(file_contents)))
        for i in final_dic:
            print(f"The '{i["name"]}' character was found {i["nums"]} times")

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    dic = {}
    lowerd_text = text.lower()
    for i in lowerd_text:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i] + 1
    
    return dic

def dic_to_list_of_dics(dic):
    list = []
    for i in dic:
        names = {}
        names["name"] = i
        names["nums"] = dic[i]
        list.append(names)
    return list

def sort_on(dic):
    return dic["nums"]

def dic_sort(dic):
    dic.sort(reverse=True, key=sort_on)
    new_dic = []
    for i in dic:
        if i["name"].isalpha():
            new_dic.append(i)
    
    return new_dic




main()