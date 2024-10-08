# datas : ((1,"one"), (2, "two"), (3, "three"))
def get_data(datas):
    num = ()
    words = ()
    for t in datas:
        num = num + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    
    min_nums = min(num)
    max_nums = max(num)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

(min_val, max_val, unique_val) = get_data(
    ((1,"one"), (2, "two"), (3, "three"))
    )

print(min_val)