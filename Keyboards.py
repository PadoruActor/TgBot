from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
InlineKeyboardMarkup, InlineKeyboardButton,
InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard = [ [ KeyboardButton(text = 'HomeWork')],
                                        [KeyboardButton(text = 'Terms')]])

Homework = InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text = 'Python Developer', callback_data = "PyDev")],
                                [InlineKeyboardButton(text = 'Python Minecraft', callback_data="PyMine")]])
Terms = InlineKeyboardMarkup(inline_keyboard=
                                [[InlineKeyboardButton(text = 'Переменная', callback_data = "Variable")],
                                [InlineKeyboardButton(text = 'Функция', callback_data="Function")],
                                [InlineKeyboardButton(text = 'Массив', callback_data="Array")],
                                [InlineKeyboardButton(text = 'Условный оператор', callback_data="Operator")],
                                [InlineKeyboardButton(text = 'Аругмент', callback_data="Arguemnt")],
                                [InlineKeyboardButton(text = 'Цикл for ', callback_data="cicle")]
                                ])