from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
InlineKeyboardMarkup, InlineKeyboardButton,
InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard = [ [ KeyboardButton(text = 'HomeWork')],
                                        [KeyboardButton(text = 'Terms')]])

Terms = InlineKeyboardMarkup(inline_keyboard=
                             [[InlineKeyboardButton(text = 'Basic Terms',callback_data= "bTerms")],
                              [InlineKeyboardButton(text = 'Intermediate Terms', callback_data= 'iTerms')]])


Homework = InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text = 'Python Developer', callback_data = "PyDev")],
                                [InlineKeyboardButton(text = 'Python Minecraft', callback_data="PyMine")]])

bTerms = InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text = 'Переменная', callback_data = "Variable")],
                                [InlineKeyboardButton(text = 'Функция', callback_data="Function")],
                                [InlineKeyboardButton(text = 'Массив', callback_data="Array")],
                                [InlineKeyboardButton(text = 'Условный оператор', callback_data="Operator")],
                                [InlineKeyboardButton(text = 'Pass', callback_data="Operator")],
                                [InlineKeyboardButton(text = 'Глобальные переменные', callback_data="Operator")],
                                 [InlineKeyboardButton(text = 'Цикл for ', callback_data="cicle")]
                                ])

iTerms = InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text = 'Класс', callback_data = "class1")],
                                [InlineKeyboardButton(text = 'Полиморфизм', callback_data="Polymorphosis")],
                                [InlineKeyboardButton(text = 'Наследование', callback_data="Array")],
                                [InlineKeyboardButton(text = 'Словарь', callback_data="Collection")],
                                [InlineKeyboardButton(text = 'Форматированные строки', callback_data="cicle")],
                                [InlineKeyboardButton(text = 'Кортеж', callback_data="Collection")],
                                [InlineKeyboardButton(text = 'Исключения', callback_data="Collection")],
                                [InlineKeyboardButton(text = 'Множество ', callback_data="cicle")]
                                ])