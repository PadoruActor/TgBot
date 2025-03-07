from aiogram import  F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import Keyboards  as kb
router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi!", reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Help:")

@router.message(F.text == "HomeWork")
async def homework(message:Message):
    await message.answer("Choose the course", reply_markup=kb.Homework)

@router.message(F.text == "Terms")
async def terms(message:Message):
    await message.answer("Choose the terms level", reply_markup=kb.Terms)

@router.callback_query(F.data == "bTerms")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer('Choose the term:', reply_markup= kb.bTerms)


@router.callback_query(F.data == "iTerms")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer('Choose the term:', reply_markup= kb.iTerms)



@router.callback_query(F.data == "PyDev")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer('PyDev HomeWork:')


@router.callback_query(F.data == "PyDev")
async def pydev(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer('PyDev HomeWork:')










