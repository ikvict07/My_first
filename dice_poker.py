from tkinter import *
from tkinter import ttk
import random

counter_for_user = 0


class User:
    def __init__(self, num):
        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixs = 0
        self.set_comb = 0
        self.four_of_a_kind = 0
        self.full_house = 0
        self.short_street = 0
        self.long_street = 0
        self.poker = 0
        self.chance = 0
        self.total_score = 0
        self.num = num
user1 = User(1)
user2 = User(2)

users_list = [user1,user2]
curent_user = users_list[counter_for_user%2]


def ones(data: [int]):
    global for_info
    if a := data.count(1) > 0:
        return (data.count(1)*1)
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Единицы')


def twos(data: [int]):
    global for_info
    if a := data.count(2) > 0:
        return (data.count(2)*2)
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Двойки')


def threes(data):
    global for_info
    if a := data.count(3) > 0:
        return (data.count(3)*3)
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Тройки')


def fours(data):
    global for_info
    if a := data.count(4) > 0:
        return (data.count(4) * 4)
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Четверки')


def fives(data):
    global for_info
    if a := data.count(5) > 0:
        return (data.count(5)*5)
    else:
        for_info.set('Ошибка! Вы не можете\n'
                     ' записать эту комбинацию в\n'
                     ' Пятерки')


def sixs(data):
    global for_info
    if a := data.count(6) > 0:
        return (data.count(6)*6)
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
                     ' Покер')


def chance(data):
    return sum(data)


ROOT_HEIGHT = 650
ROOT_WIDTH = 1200
# настройка окна
root = Tk()
root.title('Первые тесты')
root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}')
root.config(bg='cyan')

counter = 3
for_info = StringVar()


def draw_data(data):
    spacing = 10
    side = 224

    x1 = 0

    for i in range(5):
        x0 = x1 + spacing
        y0 = (ROOT_HEIGHT * 20 / 35) / 2 - side / 2
        x1 = x0 + side
        y1 = y0 + side
        canvas.create_rectangle(x0, y0, x1, y1, fill='gray')
        canvas.create_text(x0 + 115, y1 - 110, text=data[i], font=['Times New Romans', '150'])


# root.grid_rowconfigure(minsize=50, index=0)
for i in range(5):
    root.grid_columnconfigure(minsize=240, index=i)


def generate_data():
    return [random.randint(1, 6) for _ in range(5)]


data = generate_data()


def regenerate_data(data, dont_touch: [bool]):
    for n, v in enumerate(dont_touch):
        if v.get():
            data[n] = random.randint(1, 6)


def recreate(dont_touch):
    global counter
    if counter > 0:
        global data

        regenerate_data(data, dont_touch)
        draw_data(data)
        counter -= 1
        regenerate_btn = Button(root, text=f'Перебросить {counter}', command=lambda: recreate(dont_touch_list))
        regenerate_btn.grid(row=2, column=4)


def switch_to_next_user():
    global users_list
    global curent_user
    global counter_for_user
    curent_user = users_list[counter_for_user%2]

def write_to(data_to_write, comb):
    dict_comb_name = {
        'Единицы': ones, 'Двойки': twos, 'Тройки': threes,
        'Четверки': fours, 'Пятерки': fives,
        'Шестерки': sixs, 'Сет': set_comb, 'Каре': four_of_a_kind,
        'Фулл Хаус': full_house,
        'Короткий Стрит': short_street,
        'Длинный Стрит': long_street, 'Покер': poker,
        'Шанс(Любая)': chance
    }

    def renew_dont_touch():
        global dont_touch_list
        for i in dont_touch_list:
            i.set(True)

    def renew_regenerate_btn():
        global counter
        global regenerate_btn
        regenerate_btn.destroy()
        counter = 3
        regenerate_btn = Button(root, text=f'Перебросить {counter}', command=lambda: recreate(dont_touch_list))
        regenerate_btn.grid(row=2, column=4)

    if isinstance(dict_comb_name[comb.get()](data_to_write), int):
        score = dict_comb_name[comb.get()](data_to_write)
        renew_dont_touch()
        renew_regenerate_btn()
        global data
        global canvas
        data = generate_data()
        canvas.delete('all')
        for_info.set('')


        global curent_user
        match comb.get():
            case 'Единицы':
                curent_user.ones = dict_comb_name[comb.get()](data_to_write)
            case 'Двойки':
                curent_user.twos = dict_comb_name[comb.get()](data_to_write)
            case 'Тройки':
                curent_user.threes = dict_comb_name[comb.get()](data_to_write)
            case 'Четверки':
                curent_user.fours =dict_comb_name[comb.get()](data_to_write)
            case 'Пятерки':
                curent_user.fives = dict_comb_name[comb.get()](data_to_write)
            case 'Шестерки':
                curent_user.sixs =dict_comb_name[comb.get()](data_to_write)
            case 'Сет':
                curent_user.set_comb = dict_comb_name[comb.get()](data_to_write)
            case 'Каре':
                curent_user.four_of_a_kind = dict_comb_name[comb.get()](data_to_write)
            case 'Фулл Хаус':
                curent_user.full_house = dict_comb_name[comb.get()](data_to_write)
            case 'Короткий Стрит':
                curent_user.short_street = dict_comb_name[comb.get()](data_to_write)
            case 'Длинный Стрит':
                curent_user.long_street = dict_comb_name[comb.get()](data_to_write)
            case 'Покер':
                curent_user.poker = dict_comb_name[comb.get()](data_to_write)
            case 'Шанс(Любая)':
                curent_user.chance = dict_comb_name[comb.get()](data_to_write)
        match curent_user.num:
            case 1:
                user_1_stats.set(f'''
1: {user1.ones}              Set: {user1.set_comb}
2: {user1.twos}              Caree: {user1.four_of_a_kind}
3: {user1.threes}              Full House: {user1.full_house}
4: {user1.fours}              Short Street: {user1.short_street}
5: {user1.fives}              Long Street: {user1.long_street}
6: {user1.sixs}              Poker: {user1.poker}
                         Chance: {user1.chance}
''')
            case 2:
                user_2_stats.set(f'''
1: {user2.ones}              Set: {user2.set_comb}
2: {user2.twos}              Caree: {user2.four_of_a_kind}
3: {user2.threes}              Full House: {user2.full_house}
4: {user2.fours}              Short Street: {user2.short_street}
5: {user2.fives}              Long Street: {user2.long_street}
6: {user2.sixs}              Poker: {user2.poker}
                        Chance: {user2.chance}
''')



        global counter_for_user
        counter_for_user += 1
        switch_to_next_user()
        global number_of_user_var
        number_of_user_var.set(f'Сейчас очередь\n Игрока №{curent_user.num} ')
    else:
        dict_comb_name[comb.get()](data_to_write)


user_1_stats = StringVar()
user_1_stats.set(f'''
1: {user1.ones}              Set: {user1.set_comb}
2: {user1.twos}              Caree: {user1.four_of_a_kind}
3: {user1.threes}              Full House: {user1.full_house}
4: {user1.fours}              Short Street: {user1.short_street}
5: {user1.fives}              Long Street: {user1.long_street}
6: {user1.sixs}              Poker: {user1.poker}
                         Chance: {user1.chance}
''')
user_2_stats = StringVar()
user_2_stats.set(f'''
1: {user2.ones}              Set: {user2.set_comb}
2: {user2.twos}              Caree: {user2.four_of_a_kind}
3: {user2.threes}              Full House: {user2.full_house}
4: {user2.fours}              Short Street: {user2.short_street}
5: {user2.fives}              Long Street: {user2.long_street}
6: {user2.sixs}              Poker: {user2.poker}
                         Chance: {user2.chance}
''')

user_1_stats_label = Label(root, textvariable=user_1_stats, anchor='nw', justify=LEFT)
user_1_stats_label.grid(row=0, column=0, sticky='wens', padx=5, pady=5, columnspan=2, rowspan=2)

number_of_user_var = StringVar()
number_of_user_var.set(f'Сейчас очередь\n Игрока №{curent_user.num} ')
number_of_user = Label(root, textvariable=number_of_user_var, bg='cyan')
number_of_user.grid(row=0, column=2, sticky='wens', padx=15, pady=15)

user_2_stats_label = Label(root, textvariable=user_2_stats, anchor='nw', justify=LEFT)
user_2_stats_label.grid(row=0, column=3, sticky='wens', padx=5, pady=5, columnspan=2, rowspan=2)

label_for_info = Label(root, textvariable=for_info, bg='cyan')
label_for_info.grid(row=1, column=2, sticky='ns')
# for_info.set('Ошибка! Вы не можете\n'
#              ' записать эту комбинацию в\n'
#              ' {}')


write_to_btn = Button(root, text='Записать в: ', command=lambda: write_to(data, combination_to_write))
write_to_btn.grid(row=2, column=0)

combination_to_write = StringVar()
combination_to_write_combox = ttk.Combobox(root, textvariable=combination_to_write,
                                           values=['Единицы', 'Двойки', 'Тройки',
                                                   'Четверки', 'Пятерки',
                                                   'Шестерки', 'Сет', 'Каре',
                                                   'Фулл Хаус',
                                                   'Короткий Стрит',
                                                   'Длинный Стрит', 'Покер',
                                                   'Шанс(Любая)'])
combination_to_write_combox.grid(row=2, column=1)

which_dont_touch = Label(root, text='Какие оставлять?')
which_dont_touch.grid(row=2, column=2)

generate_btn = Button(root, text='Генерировать', command=lambda: draw_data(data))
generate_btn.grid(row=2, column=3)

regenerate_btn = Button(root, text=f'Перебросить {counter}', command=lambda: recreate(dont_touch_list))
regenerate_btn.grid(row=2, column=4)

dont_touch_1 = BooleanVar()
dont_touch_2 = BooleanVar()
dont_touch_3 = BooleanVar()
dont_touch_4 = BooleanVar()
dont_touch_5 = BooleanVar()

dont_touch_list = [dont_touch_1, dont_touch_2, dont_touch_3, dont_touch_4, dont_touch_5]
for i in dont_touch_list:
    i.set(True)

dont_touch_1_check_button = Checkbutton(root, variable=dont_touch_1, offvalue=True, onvalue=False)
dont_touch_2_check_button = Checkbutton(root, variable=dont_touch_2, offvalue=True, onvalue=False)
dont_touch_3_check_button = Checkbutton(root, variable=dont_touch_3, offvalue=True, onvalue=False)
dont_touch_4_check_button = Checkbutton(root, variable=dont_touch_4, offvalue=True, onvalue=False)
dont_touch_5_check_button = Checkbutton(root, variable=dont_touch_5, offvalue=True, onvalue=False)

dont_touch_1_check_button.grid(row=3, column=0)
dont_touch_2_check_button.grid(row=3, column=1)
dont_touch_3_check_button.grid(row=3, column=2)
dont_touch_4_check_button.grid(row=3, column=3)
dont_touch_5_check_button.grid(row=3, column=4)

canvas = Canvas(root, height=ROOT_HEIGHT * 20 / 35, width=ROOT_WIDTH - 20, bg='white')
canvas.grid(row=4, column=0, padx=10, pady=10, columnspan=5)

root.mainloop()
