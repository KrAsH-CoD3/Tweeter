# num = [1, 3, 4, 10, 22, 7, 5, 7, 8]
# print(num[3+1:])


import ffmpeg
from os import system
from time import time
from functools import wraps
from os import path, remove 
from os import environ as env_variable
from python_whatsapp_bot import Whatsapp, Inline_list, List_item

NUMBER: str = env_variable.get("MY_NUMBER")  # Your WhatsApp Number e.g: 234xxxxxxxxxx
NUM_ID: str = env_variable.get("NUM_ID")  # Your Number ID
TOKEN: str =  env_variable.get("TOKEN")  # Token
wa_bot = Whatsapp(number_id=NUM_ID, token=TOKEN)

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        wa_bot.send_message(NUMBER, f"{func.__name__} took {end_time - start_time} seconds to execute.", \
            reply_markup=Inline_list("Show list",list_items=[List_item("Nice one 👌"), List_item("Thanks ✨"), List_item("Great Job")]))
        return result
    return wrapper

@timeit
def normalProcessVideoFn(): system("ffmpeg -i part1.mp4 OUTPUT.mp4")

@timeit
def ffmpegProcessVideoFn():
    stream = ffmpeg.input("part1.mp4")
    # stream = ffmpeg.filter(stream, 'fps', fps=25, round='up')
    stream = ffmpeg.output(stream, "dummy.mp4")
    ffmpeg.run(stream)

for _ in range(5):
    if path.exists('OUTPUT.mp4'):
        remove('OUTPUT.mp4')
    if path.exists('dummy.mp4'):
        remove('dummy.mp4')

    normalProcessVideoFn()
    ffmpegProcessVideoFn()
