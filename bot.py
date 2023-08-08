import logging
import os
from aiogram import Bot, Dispatcher, executor, types

#from config import TOKEN

logging.basicConfig (level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message): 
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    text = f"Приветствую,{user_fullname}.Пиши свое ФИО, я помогу!"

    logging.info(f'{user_fullname=}{user_id} sent message: {message.text}')
    await message.reply(text)


#моя часть

@dp.message_handler()
async def translite_fio(message: types.Message):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name
    fio_totrans =message.text

    logging.info(f'{user_fullname=}{user_id} sent message: {message.text}')

    translit_dict = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 
    'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 
    'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 
    'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
}

    def transliterate(text1):
        return ''.join(translit_dict.get(c, c) for c in text1).upper()
    output_text = transliterate(fio_totrans)

    await bot.send_message(user_id,output_text)

if __name__== '__main__':
    executor.start_polling(dp)











