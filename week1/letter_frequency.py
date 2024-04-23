def whats_in_my_word(my_word):
    empty_dict= {}
    # print(empty_dict.keys())
    # empty_dict['a'] = 1
    # print(empty_dict.keys())
    
    sum = 0
    print(empty_dict.keys())
    for i in my_word:
        print(i)
        if i not in empty_dict.keys():
            print(True)
            empty_dict[i]=sum+1
            # print(empty_dict)
            print(empty_dict.keys())
        else:
            print(False)
            empty_dict[i] = empty_dict[i] +1
    return empty_dict
            

cc = whats_in_my_word('waaaas')
print(cc)
  