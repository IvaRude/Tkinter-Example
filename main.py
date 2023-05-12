import os
import random
from datetime import datetime
from random import shuffle
from tkinter import *
from tkinter import ttk


def shuffle_lines_in_file(filepath: str):
    random.seed(datetime.now().__str__())
    with open(filepath, 'r') as file:
        lines = file.readlines()
    if lines[-1][-1] != '\n':
        lines[-1] += '\n'
    shuffle(lines)
    with open(filepath, 'w') as file:
        file.writelines(lines)


def get_filenames_in_dir(directory_path: str) -> list[str]:
    return os.listdir(directory_path)


def shuffle_lines_in_files_in_directory(directory_path: str):
    filenames = get_filenames_in_dir(directory_path)
    for filename in filenames:
        shuffle_lines_in_file(directory_path + '/' + filename)


def remove_quotes_from_path(path: str) -> str:
    if path[-1] in ['"', "'"]:
        path = path[:-1]
    if path[0] in ['"', "'"]:
        path = path[1:]
    return path


def run_button_click(root: Tk, label: ttk.Label, input_entry: ttk.Entry, run_btn: ttk.Button):
    directory_path = input_entry.get()
    directory_path = remove_quotes_from_path(directory_path)
    input_entry.destroy()
    run_btn.destroy()
    label.configure(text='Подождите завершения программы.')
    root.update()
    try:
        shuffle_lines_in_files_in_directory(directory_path)
        # asyncio.run(make_excel_file(url))
        label.configure(text=f'Программа завершила работу.')
    except Exception as ex:
        # logger.error(ex, exc_info=True)
        # logger.error(f'\n\nFINAL URL: {url}\n\n')
        label.configure(text='Произошла ошибка')


def main():
    root = Tk()
    root.geometry('600x150')
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    label = ttk.Label(frm, text='Введите путь до папки:')
    label.grid(column=0, row=0)
    input_entry = ttk.Entry(frm)
    input_entry.grid(column=1, row=0)
    run_btn = ttk.Button(frm, text='Запустить',
                         command=lambda: run_button_click(root, label, input_entry, run_btn))
    run_btn.grid(column=2, row=0)
    ttk.Button(frm, text='Выход', command=root.destroy).grid(column=2, row=1)
    root.mainloop()


if __name__ == '__main__':
    main()
