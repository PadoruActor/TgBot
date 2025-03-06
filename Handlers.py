from aiogram import  F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
import Keyboards  as kb
router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi!", reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Help:")

@router.message(F.text == "HomeWork")
async def pythondev(message:Message):
    await message.answer("Choose the course", reply_markup=kb.Homework)



@router.message(F.text == "Terms")
async def pythondev(message:Message):
    await message.answer("Choose the term", reply_markup=kb.Terms)


@router.callback_query(F.data == "PyDev")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer('PyDev HomeWork:')


@router.callback_query(F.data == "PyDev")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer('PyDev HomeWork:')

@router.callback_query(F.data == "Array")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(' Массив  — это коллекция элементов, хранящая упорядоченный набор значений \n '
                                   ' Пример: \n'
                                   ' ```python my_list = [1, 2, 3, "apple", 4.5]  # Список с элементами разных типов\n'
                                    'print(my_list[0])  # Вывод: 1 (первый элемент)\n'
                                    "print(my_list[3])  # Вывод: apple (четвертый элемент)```\n", parse_mode = ParseMode.MARKDOWN)


@router.callback_query(F.data == "Variable")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(' Переменная = именованная ячейка памяти, в которой хранятся данные \n'
                                   ' Пример: \n'
                                   ' ```python a = 5 # переменная a = 5\n'
                                   '  b = "juice" # переменная b = 7\n'
                                    'print(a)  # Вывод: 5 (a)\n'
                                    "print(b)  # Вывод: juice (b)```\n", parse_mode = ParseMode.MARKDOWN)


@router.callback_query(F.data == "Function")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(' Переменная = именованная ячейка памяти, в которой хранятся данные \n'
                                   ' Пример: \n'
                                   ' ```python a = 5 # переменная a = 5\n'
                                   '  b = "juice" # переменная b = 7\n'
                                    'print(a)  # Вывод: 5 (a)\n'
                                    "print(b)  # Вывод: juice (b)```\n", parse_mode = ParseMode.MARKDOWN)







