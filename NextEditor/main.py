import re
from tkinter import *
from tkinter import filedialog
from tkinter import font
import os
import settings as stt
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

TextSize = 15

def main():
    window = Tk()
    window.geometry('640x605+360+270')
    window.title('NextEditor')

    fileMenu = Menu()
    window.config(menu = fileMenu)

    #Файл
    file_menu = Menu(fileMenu, tearoff=0)
    fileMenu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Open', command=lambda: open_file0())
    file_menu.add_command(label='Save', command=lambda: save_file())

    # темы
    theme_menu = Menu(fileMenu, tearoff=0)
    fileMenu.add_cascade(label='Themes', menu=theme_menu)
    theme_menu.add_command(label='Dark theme', command=lambda: change_themes('dark'))
    theme_menu.add_command(label='Light theme', command=lambda: change_themes('white'))
    theme_menu.add_command(label='Brown theme', command=lambda: change_themes('brown'))
    
    # Шрифты
    font_menu = Menu(fileMenu, tearoff=0)
    fileMenu.add_cascade(label='Fonts', menu=font_menu)
    font_menu.add_cascade(label='Arial', command=lambda: change_font('Arial'))
    font_menu.add_cascade(label='Courier', command=lambda: change_font('Courier'))
    font_menu.add_cascade(label='System', command=lambda: change_font('System'))
    
    # цвет шрифта
    color_txt_menu = Menu(fileMenu, tearoff=0)
    fileMenu.add_cascade(label='Text color', menu=color_txt_menu)
    color_txt_menu.add_command(label='black', command=lambda: change_color('black'))
    color_txt_menu.add_command(label='white', command=lambda: change_color('white'))
    color_txt_menu.add_command(label='brown', command=lambda: change_color('brown'))
    color_txt_menu.add_command(label='green', command=lambda: change_color('green'))
    color_txt_menu.add_command(label='lime', command=lambda: change_color('lime'))

    # экран
    screen_menu = Menu(fileMenu, tearoff=0)
    fileMenu.add_cascade(label='Screen', menu=screen_menu)
    screen_menu.add_command(label='fullscreen', command=lambda: change_fullscreen())

    fileMenu.add_radiobutton(label='Run Python File', command=lambda: excute())

    view_color = {
        'dark': {
            'textbg': '#1E1E1E', 'textfg': 'lime', 'cursore': 'white'
        },
        'white': {
            'textbg': 'white', 'textfg': 'black', 'cursore': 'black'
        },
        'brown': {
            'textbg': '#4D220E', 'textfg': '#876743', 'cursore': 'white'
        }
    }
    text_font = {
        'Arial': {
            'font': ('Arial', TextSize)
        },
        'Courier': {
            'font': ('Courier', TextSize)
        },
        'System': {
            'font': ('system', TextSize)
        }
    }

    text_color = {
        'black': {
            'textfg': 'black'
        },
        'white': {
            'textfg': 'white'
        },
        'brown': {
            'textfg': '#876743'
        },
        'green': {
            'textfg': 'green'
        },
        'lime': {
            'textfg': 'lime'
        }
    }

    text = Frame(window)
    text.pack(fill=BOTH, expand=1)

    text_fild = Text(text,
                    bg='#1E1E1E',
                    fg='lime',
                    padx = 10,
                    pady = 10,
                    insertbackground='white',
                    spacing3=5,
                    width=10,
                    font=('', TextSize))
    text_fild.pack(expand=1, fill=BOTH, side=LEFT)

    text_fild.insert('1.0', 'def main(): \n   print("Hello World")\nif __name__ == "__main__":\n    main()')

    scrool = Scrollbar(text, command=text_fild.yview)
    scrool.pack(side=LEFT, fill=Y)
    text_fild.config(yscrollcommand=scrool.set)

    def change_themes(themes):
        text_fild['bg'] = view_color[themes]['textbg']
        text_fild['fg'] = view_color[themes]['textfg']
        text_fild['insertbackground'] = view_color[themes]['cursore']
        
    def change_font(text_fonts):
        text_fild['font'] = text_font[text_fonts]['font']

    def change_color(text_colors):
        text_fild['fg'] = text_color[text_colors]['textfg']

    def open_file0():
        file_path = filedialog.askopenfilename(title='выбор Файла', filetypes=(('Text documents (*.txt)', '*.txt'),
        ('All files', '*.*')))
        if file_path:
            text_fild.delete('1.0', END)
            text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

    def save_file():
        file_path = filedialog.asksaveasfilename(filetypes=(('Text documents (*.txt)', '*.txt'),
        ('Files', '*.*')))
        f = open(file_path, 'w', encoding='utf-8')
        text = text_fild.get('1.0', END)
        f.write(text)
        f.close()

    def change_fullscreen():
        window.state("zoomed")

    def excute():
        with open('run.py', 'w', encoding='utf-8') as f:
            f.write(text_fild.get('1.0', END))

        os.system('start cmd /K "python run.py"')

    window.mainloop()

if __name__ == '__main__':
    main()
