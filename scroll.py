import pytz
import contextlib
from datetime import datetime
from selenium import webdriver
from time import sleep, perf_counter
from os import environ as env_variable
from selenium.webdriver.common.by import By
from art import tprint, set_default, text2art
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from python_whatsapp_bot import Whatsapp, Inline_list, List_item
from selenium.common.exceptions import TimeoutException, NoSuchElementException

NUMBER: str = env_variable.get("MY_NUMBER")  # Your WhatsApp Number e.g: 234xxxxxxxxxx
NUM_ID: str = env_variable.get("NUM_ID")  # Your Number ID
TOKEN: str =  env_variable.get("TOKEN")  # Token

set_default("fancy99")
tprint("WhatsApp Status Viewer", 'rectangles')

timezone: str = "Africa/Lagos"  # Your timezone
statusUploaderName: str = "Ijk" # As it is saved on your phone(Case Sensitive)
ppsXpath: str = f'//span[@title="{statusUploaderName}"]//..//..//..//preceding-sibling::\
    div[@class="_1AHcd"]//*[local-name()="svg" and @class="bx0vhl82 ma4rpf0l lhggkp7q"]'
ppXpath: str = f'//span[@title="{statusUploaderName}"]//..//..//..//preceding-sibling::\
    div[@class="_1AHcd"]//*[local-name()="svg" and @class="bx0vhl82 ma4rpf0l lhggkp7q"]//parent::div'
barsXpath: str = '//div[@class="g0rxnol2 qq0sjtgm jxacihee l7jjieqr egv1zj2i ppled2lx gj5xqxfh om6y7gxh"]'
barXpath: str =  '//div[@class="lhggkp7q qq0sjtgm tkdu00h0 ln8gz9je ppled2lx ss1fofi6 o7z9b2jg"]'
barVA_Xpath: str =  '//div[@class="lhggkp7q qq0sjtgm tkdu00h0 ln8gz9je ppled2lx ss1fofi6 o7z9b2jg velocity-animating"]'
driverpath: str = "C:\\Users\\Administrator\\Documents\\WhatsApp Status Checker\\assest\\driver\\chromedriver.exe"
img_status_xpath: str = '//div[@class="g0rxnol2 ln8gz9je ppled2lx gfz4du6o r7fjleex"]//img'
video_status_xpath: str = '//div[@class="g0rxnol2 ln8gz9je ppled2lx gfz4du6o r7fjleex"]//video'
text_status_xpath: str = '//div[@data-testid="status-v3-text"]'
audio_status_xpath: str = '//div[@class="g0rxnol2 ggj6brxn"]'

service = Service(executable_path=driverpath)
options = Options()
prefs = {'download.default_directory': '/Tweeter_Files/'}
options.add_experimental_option('prefs', prefs)
options.add_argument("--disable-gpu")
options.add_argument("--no-first-run")
options.add_argument('--disable-dev-shm-usage')
options.add_argument(r'--profile-directory=BoT Profile')
options.add_argument(r'user-data-dir=C:\BoT Chrome Profile')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option(
    "excludeSwitches", ["enable-automation", 'enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')


bot = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(bot, 60)
wait3secs = WebDriverWait(bot, 3)
action = ActionChains(bot)
# bot.set_window_position(676, 0)
bot.set_window_size(300, 733)
bot.set_window_position(870, 0)
wa_bot = Whatsapp(number_id=NUM_ID, token=TOKEN)

bot.get("https://web.whatsapp.com")

gmtTime: str = lambda tz: datetime.now(
    pytz.timezone(tz)).strftime("%H : %M : %S")

try:
    print(text2art("\nLogging in..."), "💿")
    login_count: int = 1
    while True:
        try:
            bot.find_element(By.XPATH, '//div[@data-testid="chat-list-search"]')
            break
        except NoSuchElementException:  # Log in page (Scan QRCode)
            with contextlib.suppress(TimeoutException):
                wait3secs.until(EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="_3AjBo"]')))  # WhatsApp list login instructions
                if login_count == 1:
                    print(text2art("Please scan the QRCODE to log in"), "🔑")
                    login_count += 1
                wait3secs.until(EC.invisibility_of_element(
                    (By.XPATH, '//div[@class="_3AjBo"]')))  # WhatsApp list login instructions
                wait3secs.until(EC.visibility_of_element_located(
                    (By.XPATH, '//div[@class="_1dEQH _26aja"]'))) # WhatsApp: Text
                wait3secs.until(EC.invisibility_of_element(
                    (By.XPATH, '//div[@class="_2dfCc"]')))  # Loading your chat
                break
    print(text2art("Logged in successfully."), "✌")
    tprint(f'Logged in at {gmtTime(timezone)}\n')
except TimeoutException:
    wa_bot.send_message(NUMBER, 'Took too long to login.', reply_markup=Inline_list("Show list", \
        list_items=[List_item("Nice one 👌"), List_item("Thanks ✨"), List_item("Great Job 🤞")]))
    bot.quit()

sleep(3)
while True:
    with contextlib.suppress(Exception):  # Loading messages (I Guess)
        wait3secs.until(EC.invisibility_of_element((By.XPATH, '//div[@class="_2z7gr"]')))
        break


def getMedia() -> None:

    bot.find_element(By.XPATH, '//div[@title="Status"]').click()  # Enter Status Screen
    status_container_xpath: str = '//*[@class="g0rxnol2 ggj6brxn m0h2a7mj lb5m6g5c lzi2pvmc ag5g9lrv jhwejjuw ny7g4cd4"]'
    viewed_circle_xpath: str = '//span[@title="Ijk"]//ancestor::div[@class="lhggkp7q ln8gz9je rx9719la"]\
                        //*[local-name()="circle" and @class="i2tfkqu4"]'

    vertical_ordinate: int = 0
    while True:
        status_container = bot.find_element(By.XPATH, status_container_xpath)
        vertical_ordinate += 2500
        try: 
            bot.execute_script(
                "arguments[0].scrollTop = arguments[1]", status_container, vertical_ordinate)
            danny = bot.find_element(By.XPATH, viewed_circle_xpath)
        except Exception: continue
        bot.execute_script('arguments[0].scrollIntoView();', danny)
        circle_attr = bot.find_element(By.XPATH, viewed_circle_xpath).get_attribute("stroke-dasharray").split(" ")
        init_viewed_circle = circle_attr.count(circle_attr[0])
        # while True:
        #     with contextlib.suppress(Exception):
        #         WebDriverWait(bot, 1).until(EC.invisibility_of_element((By.XPATH, viewed_circle_xpath)))
        #         while True:
        #             try:
        #                 WebDriverWait(bot, 1).until(EC.visibility_of_element_located((By.XPATH, viewed_circle_xpath)))
        #                 print("Sleeping 3 Sec"); sleep(3)
        #                 viewed_circle = circle_attr.count(circle_attr[0])
        #             except Exception: 
        #                 continue
        #             # break

        #             if viewed_circle > init_viewed_circle:
        #                 difference = viewed_circle - init_viewed_circle
        #                 sleep(1)
        #                 danny.click()
        #                 sleep(1)
        #                 new_status_bars = bot.find_elements(By.XPATH, barsXpath)[init_viewed_circle + 1:]
        #                 for new_status_bar in new_status_bars:
        #                     new_status_bar.click()

                    
        #             try: 
        #                 bot.execute_script(
        #                     "arguments[0].scrollTop = arguments[1]", status_container, vertical_ordinate)
        #                 danny = bot.find_element(By.XPATH, '//span[@title="Ijk" and @class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 _11JPr"]')
        #             except Exception: continue
        #             # sleep(5)
        #             danny.click()
        #             sleep(1)
        #             while True:
        #                 with contextlib.suppress(Exception):
        #                     wait3secs.until(EC.visibility_of_element_located((By.XPATH, status_container_xpath)))
        #                     vertical_ordinate = 0
        #                     break
    
    input("QUIT: ")
    # break
getMedia()

# <circle cx="52" cy="52" r="50" fill="none" stroke-linecap="round" class="j9ny8kmf" stroke-dashoffset="387.69908169872417" stroke-dasharray="68.53981633974483 10 68.53981633974483 10 68.53981633974483 10 68.53981633974483 10" stroke-width="4"></circle>

# bot.execute_script("window.open('');")
# tabs = bot.window_handles()

