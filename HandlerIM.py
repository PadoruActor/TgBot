from aiogram import  F, Router
from aiogram.types import  CallbackQuery
from aiogram.enums import ParseMode
router = Router()

@router.callback_query(F.data == "class1")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(' Класс  — это коллекция элементов, хранящая упорядоченный набор значений \n '
                                   ' Пример: \n'
                                   ' ```python\nmy_list = [1, 2, 3, "apple", 4.5]  # Список с элементами разных типов\n'
                                    'print(my_list[0])  # Вывод: 1 (первый элемент)\n'
                                    "print(my_list[3])  # Вывод: apple (четвертый элемент)```\n", parse_mode = ParseMode.MARKDOWN)
