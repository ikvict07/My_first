from tkinter import *
from tkinter import ttk
import random

ROOT_HEIGHT = 650
ROOT_WIDTH = 1200
# настройка окна
root = Tk()
root.title('Первые тесты')
root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}')
root.config(bg='cyan')

counter = 3


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
        regenerate_btn.grid(row=1, column=4)


def write_to(data_to_write):
    # TODO сделать чтоб записывалось в список собранных комбинаций
    def renew_dont_touch():
        global dont_touch_list
        for i in dont_touch_list:
            i.set(True)
    def renew_regenerate_btn():
        global counter
        counter = 3
        regenerate_btn = Button(root, text=f'Перебросить {counter}', command=lambda: recreate(dont_touch_list))
        regenerate_btn.grid(row=1, column=4)
    renew_dont_touch()
    renew_regenerate_btn()
    global data
    global canvas
    data = generate_data()
    canvas.delete('all')





user_1_stats = StringVar()
user_1_stats.set(f'''
1: {0}              some_comb: {0}
2: {0}              some_comb: {0}
3: {0}              some_comb: {0}
4: {0}              some_comb: {0}
5: {0}              some_comb: {0}
6: {0}              some_comb: {0}
''')
user_2_stats = StringVar()
user_2_stats.set(f'''
1: {0}              some_comb: {0}
2: {0}              some_comb: {0}
3: {0}              some_comb: {0}
4: {0}              some_comb: {0}
5: {0}              some_comb: {0}
6: {0}              some_comb: {0}
''')

user_1_stats_label = Label(root, textvariable=user_1_stats, anchor='nw')
user_1_stats_label.grid(row=0, column=0, sticky='wens', padx=5, pady=5, columnspan=2)

number_of_user = Label(root, text=f'Player №{1}', bg='cyan')
number_of_user.grid(row=0, column=2, sticky='wens', padx=15, pady=15)

user_2_stats_label = Label(root, textvariable=user_2_stats, anchor='nw')
user_2_stats_label.grid(row=0, column=3, sticky='wens', padx=5, pady=5, columnspan=2)

write_to_btn = Button(root, text='Записать в: ', command=lambda: write_to(data))
write_to_btn.grid(row=1, column=0)

combination_to_write = StringVar()
combination_to_write_combox = ttk.Combobox(root, textvariable=combination_to_write, values=['street', 'flash'])
combination_to_write_combox.grid(row=1, column=1)

which_dont_touch = Label(root, text='Какие оставлять?')
which_dont_touch.grid(row=1, column=2)

generate_btn = Button(root, text='Генерировать', command=lambda: draw_data(data))
generate_btn.grid(row=1, column=3)

regenerate_btn = Button(root, text=f'Перебросить {counter}', command=lambda: recreate(dont_touch_list))
regenerate_btn.grid(row=1, column=4)

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

dont_touch_1_check_button.grid(row=2, column=0)
dont_touch_2_check_button.grid(row=2, column=1)
dont_touch_3_check_button.grid(row=2, column=2)
dont_touch_4_check_button.grid(row=2, column=3)
dont_touch_5_check_button.grid(row=2, column=4)

canvas = Canvas(root, height=ROOT_HEIGHT * 20 / 35, width=ROOT_WIDTH - 20, bg='white')
canvas.grid(row=3, column=0, padx=10, pady=10, columnspan=5)

root.mainloop()
