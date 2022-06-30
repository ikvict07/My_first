def second_index(text: str, symbol: str) -> [int, None]:
    ans = []
    for (index, word) in enumerate(text):
        if word == symbol:
            ans.append(index)
    try:
        return ans
    except:
        return None
'''
Список всех индексов символа в тексте
'''
