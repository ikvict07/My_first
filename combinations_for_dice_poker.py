def ones(data: [int]):
    global for_info
    if a:=data.count(1) > 0:
        return a * 1
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Единицы')
def twos(data: [int]):
    global for_info
    if a := data.count(2) > 0:
        return a * 2
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Двойки')
def threes(data):
    global for_info
    if a := data.count(3) > 0:
        return a * 3
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Тройки')
def fours(data):
    global for_info
    if a := data.count(4) > 0:
        return a * 4
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Четверки')
def fives(data):
    global for_info
    if a := data.count(5) > 0:
        return a * 5
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Пятерки')
def sixs(data):
    global for_info
    if a := data.count(6) > 0:
        return a * 6
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Шестерки')
def set_comb(data):
    for i in data:
        if data.count(i) == 3:
            return sum(data)
    global for_info
    for_info.set('Ошибка! Вы не можете\n'
                 ' записать эту комбинацию в\n'
                 ' Cет')
def four_of_a_kind(data):
    for i in data:
        if data.count(i) == 4:
            return sum(data)
    global for_info
    for_info.set('Ошибка! Вы не можете\n'
                 ' записать эту комбинацию в\n'
                 ' Каре')
def full_house(data):
    global for_info
    if len(set(data)) == 2:
        return 25
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Фулл Хаус')
def short_street(data):
    global for_info
    if data == sorted(data):
        match sum(data[:-1]):
            case 10:
                return 30
            case 14:
                return 30
            case 18:
                return 30
        match sum(data[1:]):
            case 10:
                return 30
            case 14:
                return 30
            case 18:
                return 30
    for_info.set('Ошибка! Вы не можете\n'
                 ' записать эту комбинацию в\n'
                 ' Короткий Стрит')

def long_street(data):
    global for_info
    if data == sorted(data):
        match sum(data):
            case 15:
                return 40
            case 20:
                return 40
    for_info.set('Ошибка! Вы не можете\n'
                 ' записать эту комбинацию в\n'
                 ' Длинный Стрит')

def poker(data):
    global for_info
    if len(set(data)) == 1:
        return 50
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Фулл Хаус')

def chance(data):
    return sum(data)