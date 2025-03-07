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
                                   ' ```python\nmy_list = [1, 2, 3, "apple", 4.5]  # Список с элементами разных типов\n'
                                    'print(my_list[0])  # Вывод: 1 (первый элемент)\n'
                                    "print(my_list[3])  # Вывод: apple (четвертый элемент)```\n", parse_mode = ParseMode.MARKDOWN)


@router.callback_query(F.data == "Variable")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(' Переменная = именованная ячейка памяти, в которой хранятся данные \n'
                                    ' Пример: \n'
                                    ' ```python\na = 5 # переменная a = 5\n'
                                    'b = "juice" # переменная b = 7\n'
                                    'print(a)  # Вывод: 5 (a)\n'
                                    "print(b)  # Вывод: juice (b)```\n", parse_mode = ParseMode.MARKDOWN)


@router.callback_query(F.data == "Function")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer('Функция  = набор команд, который можно вызвать в любом месте программы.\n'
                                  'Функции могут принимать аргументы и возвращать значения \n'
                                   ' Пример: \n'
                                   ' ```python\ndef sum(a,b): # функция sum, a,b = аргументы\n'
                                    '    return a+b# Функция возвращает сумму аргументов\n'
                                    'c = sum(5,12)  #В переменную c записывается возвращаемое значение\n'
                                    "print(c) # Вывод = 17 (c = 5+12)```", parse_mode = ParseMode.MARKDOWN)


@router.callback_query(F.data == "Operator")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(' Условный оператор = команда, позволяющая выполнить некоторые действия при выполнении некоторых условий \n'
                                    ' Пример: \n'
                                    ' ```python\na = 5 # переменная a = 5\n'
                                    'if a == 6: # Проверка, равняется ли a 5\n'
                                    '   print(a)  # Команда не выполнится(a=5)\n'
                                    'elif a == 4:'
                                    '   print(a+1) # Команда, не выполнится (a=5)'
                                    'else:'
                                    '   print(a+5) # Вывод: 10 ( a= 5) ```\n', parse_mode = ParseMode.MARKDOWN)



@router.callback_query(F.data == "cicle")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(' Цикл = команда, позволяющая выполнить набор команд некоторое количество раз \n'
                                  'Есть циклы While {условие}, do , until {условие}, for{range}\n'
                                    ' Пример: \n'
                                    ' ```python\n a = [5,7,9,11] # массив a \n'
                                    'for i in a: # i проходится по элементам массива a \n '
                                    '   print(a[i])  # Вывод = 5,7,9,11\n'
                                    'for i in range (5): # цикл проходится по 0-1-2-3-4'
                                    '   print(i*2) # вывод: 0,2,4,6,8 (i*2)', parse_mode = ParseMode.MARKDOWN)










