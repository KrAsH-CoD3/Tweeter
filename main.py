import ffmpeg
from datetime import datetime
from selenium import webdriver
from typing import Optional, Dict
from os import path, remove, rename 
from time import sleep, perf_counter
from os import environ as env_variable
from selenium.webdriver.common.by import By
from art import tprint, set_default, text2art
from selenium.webdriver.common.keys import Keys
import contextlib, json, pyautogui, pytz, random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from python_whatsapp_bot import Whatsapp, Inline_list, List_item
from selenium.common.exceptions import TimeoutException, NoSuchElementException

NUMBER: str = env_variable.get("MY_NUMBER")  # Your WhatsApp Number e.g: 234xxxxxxxxxx
NUM_ID: str = env_variable.get("NUM_ID")  # Your Number ID
TOKEN: str =  env_variable.get("TOKEN")  # Token


set_default("fancy99")
# tprint("WhatsApp Status Viewer", 'rectangles')

timezone: str = "Africa/Lagos"  # Your timezone
statusUploaderName: str = "Jake" # As it is saved on your phone(Case Sensitive)
# statusUploaderName: str = input("Whose person status do you want to view? ") # As it is saved on your phone(Case Sensitive)
ppsXpath: str = f'//span[@title="{statusUploaderName}"]//..//..//..//preceding-sibling::\
    div[@class="_1AHcd"]//*[local-name()="svg" and @class="bx0vhl82 ma4rpf0l lhggkp7q"]'
ppXpath: str = f'//span[@title="{statusUploaderName}"]//..//..//..//preceding-sibling::\
    div[@class="_1AHcd"]//*[local-name()="svg" and @class="bx0vhl82 ma4rpf0l lhggkp7q"]//parent::div'
barsXpath: str = '//div[@class="g0rxnol2 qq0sjtgm jxacihee l7jjieqr egv1zj2i ppled2lx gj5xqxfh om6y7gxh"]'
barXpath: str =  '//div[@class="lhggkp7q qq0sjtgm tkdu00h0 ln8gz9je ppled2lx ss1fofi6 o7z9b2jg"]'
barVA_Xpath: str =  '//div[@class="lhggkp7q qq0sjtgm tkdu00h0 ln8gz9je ppled2lx ss1fofi6 o7z9b2jg velocity-animating"]'
pause_btn_xpath:str = '//span[@data-icon="status-media-controls-pause"]'
driverpath: str = "C:\\Users\\Administrator\\Documents\\WhatsApp Status Checker\\assest\\driver\\chromedriver.exe"
scrolled_viewed_person_xpath :str = f'//span[@title="{statusUploaderName}" and @class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 _11JPr"]'
tempStatusThumbnail: str = '//div[@class="t3g6t33p sxl192xd qnwaluaf g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb gfz4du6o r7fjleex lniyxyh2 qssinsw9 rx2toazg"]'
img_status_xpath: str = '//div[@class="g0rxnol2 ln8gz9je ppled2lx gfz4du6o r7fjleex"]//img'
video_status_xpath: str = '//div[@class="g0rxnol2 ln8gz9je ppled2lx gfz4du6o r7fjleex"]//video'
text_status_xpath: str = '//div[@data-testid="status-v3-text"]'
audio_status_xpath: str = '//audio[@class="ln8gz9je"]' #  '//div[@class="g0rxnol2 ggj6brxn"]'
oldMessage_status_xpath: str = '//div[contains(@class, "qfejxiq4 b6f1x6w7 m62443ks")]'
caption_xpath: str = '//div[@class="tvsr5v2h mz6luxmp clw8hvz5 p2tfx3a3 holukk2e cw3vfol9"]//span[@class="_11JPr" and @dir="auto" and @aria-label]'
read_more_caption_xpath: str = f'{caption_xpath}//following-sibling::strong'
emoji_xpath: str = f'{caption_xpath}//following-sibling::img'

prefs = {
    'download.default_directory': 'C:\\Users\\Administrator\\Downloads\\Tweeter_Uploads\\',
    'download.prompt_for_download': False,
}

service = Service(executable_path=driverpath)
options = Options()
options.add_argument("--no-sandbox")
# options.add_argument("--headless")
options.add_argument("--single-process")
options.add_experimental_option('prefs', prefs)
options.add_argument('--disable-dev-shm-usage')
options.add_argument(r'--profile-directory=Tweeter Profile')
options.add_argument(r'user-data-dir=C:\Tweeter Chrome Profile')
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
pyautogui.FAILSAFE = False
pyautogui.press('esc')

gmtTime: str = lambda tz: datetime.now(
    pytz.timezone(tz)).strftime("%H : %M : %S")

def open_WhatsApp():
    bot.get("https://web.whatsapp.com")

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


def scroll(personName) -> None:

    bot.find_element(By.XPATH, '//div[@title="Status"]').click()  # Enter Status Screen
    status_container_xpath: str = '//*[@class="g0rxnol2 ggj6brxn m0h2a7mj lb5m6g5c lzi2pvmc ag5g9lrv jhwejjuw ny7g4cd4"]'
    viewed_circle_xpath: str = f'//span[@title="{personName}"]//ancestor::div[@class="lhggkp7q ln8gz9je rx9719la"]\
                        //*[local-name()="circle" and @class="i2tfkqu4"]'

    vertical_ordinate: int = 0
    while True:
        status_container = bot.find_element(By.XPATH, status_container_xpath)
        vertical_ordinate += 1000#2500
        try: 
            bot.execute_script(
                "arguments[0].scrollTop = arguments[1]", status_container, vertical_ordinate)
            statusPoster = bot.find_element(By.XPATH, viewed_circle_xpath)
        except Exception: continue
        bot.execute_script('arguments[0].scrollIntoView();', statusPoster)
        break
    vertical_ordinate = 0


def checkStatusType(xpath) -> Optional[Dict[str, bool]]:
    global kill
    while kill != True:
        with contextlib.suppress(NoSuchElementException, TimeoutException):
            WebDriverWait(bot, .1).until(EC.presence_of_element_located((By.XPATH, xpath)))
            # bot.find_element(By.XPATH, xpath)
            if 'r7fjleex"]//img' in xpath:
                kill = True
                return {"imgStatusValue": True}
            elif 'r7fjleex"]//video' in xpath:
                kill = True
                return {"videoStatusValue": True}
            elif 'status-v3-text"]' in xpath:
                kill = True
                return {"txtStatusValue": True}
            elif 'ajgl1lbb"]' in xpath:
                kill = True
                return {"audioStatusValue": True}
            elif 'b6f1x6w7 m62443ks")]' in xpath:
                kill = True
                return {"old_messageValue": True}  # Returning this is very rare


def autoViewStatus(
    statusTypeMsg: str = "", 
    statusUploaderName: str = statusUploaderName, 
    media_info: dict = {}
    ) -> Optional[Dict[str, str]]:
    
    global kill
    kill = False

    media_names: list = []

    def _backnforward():
            # Go backward and forward to get 'blob' in url
            bot.find_elements(By.XPATH, barsXpath)[viewed_status-1].click(); sleep(1)
            bot.find_elements(By.XPATH, barsXpath)[viewed_status].click(); sleep(1)

    def click_pause():
        try:
            WebDriverWait(bot, 2).until(EC.invisibility_of_element_located(
                (By.XPATH, '//button[@class="icon-media-disabled"]')))
            bot.find_element(By.XPATH, pause_btn_xpath).click()
        except (TimeoutException, NoSuchElementException): return

    open_WhatsApp()

    search_field = bot.find_element(By.XPATH, '//div[@data-testid="chat-list-search"]')
    search_field.send_keys(statusUploaderName)

    counter = 0
    while True:
        counter += 1
        # if counter > 1:     #  DEBUGGING PURPOSE
        #     ...             #  BREAKPOINT AT THE END ALREADY
        while True:
            try:
                wait.until(EC.invisibility_of_element_located(  # SEARCH BAR LOADING SVG ICON                
                    (By.XPATH, '//*[local-name()="svg" and @class="gdrnme8s hbnrezoj f8mos8ky tkmeqcnu b9fczbqn"]')))
                bot.find_element(By.XPATH, ppsXpath)  # Status Circle around profile picture                         
                sleep(7)  # Not advisable for whatsapp viewer project(slow)
                bot.find_element(By.XPATH, ppXpath).click()  # Click Profile Picture to view Status
                break
            except TimeoutException: continue
            except NoSuchElementException: 
                # return  # COMMENT THIS AND USE BELOW FOR SCROLL
                
                scroll(statusUploaderName)
                wait.until(EC.invisibility_of_element((By.XPATH, tempStatusThumbnail)))
                bot.find_element(By.XPATH, scrolled_viewed_person_xpath).click()
                break

        unviewed_status: int = len(bot.find_elements(By.XPATH, '//div[contains(@class, "mjomr7am")]')) + 1
        total_status: int = len(bot.find_elements(By.XPATH, barsXpath))
        block_line: str = "-"*38
        loop_range: list = range(1, unviewed_status+1)
        viewed_status: int = total_status - unviewed_status
        statusTypeMsg += f"{statusUploaderName}\nUnviewed Statues is/are {unviewed_status} out of {total_status}.\n"
        statusType_xpaths = [img_status_xpath, video_status_xpath, text_status_xpath, audio_status_xpath, oldMessage_status_xpath]
        for status_idx in loop_range:

            click_pause()  # Pause incase of 5secs img

            if status_idx == 1: tprint(statusTypeMsg[:-1])

            with ThreadPoolExecutor(5) as pool:
                tasks = [pool.submit(checkStatusType, specific_xpath) for specific_xpath in statusType_xpaths]
                
                for future in as_completed(tasks):
                    if all([future.done(), future.result() is not None]):
                        check_Status = future.result()
                kill = False

            try:
                if check_Status["imgStatusValue"]:
                    try: bot.find_element(By.XPATH, pause_btn_xpath).click()
                    except NoSuchElementException: ...  # ALREADY CLCIKED
                    tprint(f"{status_idx}. Status is an Image.")
                    statusTypeMsg += f"{status_idx}. Status is an Image.\n"
                    image_link: str = bot.find_elements(By.XPATH, img_status_xpath)[-1].get_attribute('src')
                    try:
                        read_more = bot.find_element(By.XPATH, read_more_caption_xpath)

                        read_more.click()
                        caption: str = bot.find_element(By.XPATH, caption_xpath).text
                    except NoSuchElementException:  # No ReadMore
                        try:
                            caption: str = bot.find_element(By.XPATH, caption_xpath).text
                        except NoSuchElementException:  # No caption
                            caption = None
                    finally: 
                        uid: str = image_link.split(".com/")[1]#.split('-')[0]
                        media_names.append(uid)
                        media_info[uid] = {"type": "image", "caption": caption}
                    if len(bot.window_handles) == 1:
                        bot.execute_script('window.open("");')
                    bot.switch_to.window(bot.window_handles[1])
                    bot.get(image_link)
                    image = bot.find_element(By.XPATH, "//img")
                    image_rect: dict = image.rect
                    tlw = -((image_rect["width"]/2)-10)
                    tlh = -((image_rect["height"]/2)-10)
                    action.move_to_element_with_offset(image, tlw, tlh).perform()
                    action.context_click().perform()
                    sleep(1)  # Very necessary (Sometimes down dont work)
                    pyautogui.press(['down', 'down', 'enter'])
                    sleep(5) #  Try implement auto wait
                    pyautogui.press('enter')
                    bot.switch_to.window(bot.window_handles[0])
            except KeyError:
                try:
                    if check_Status["videoStatusValue"]:
                        loading_icon: bool = True
                
                        while True:
                            with contextlib.suppress(TimeoutException):
                                try:
                                    bot.find_element(By.XPATH, barXpath)  # paused status
                                    style_value = bot.find_element(By.XPATH, barXpath).get_attribute("style")  # Starts @ 100 reduces to 0
                                    if style_value == '': continue
                                except NoSuchElementException:
                                    bot.find_element(By.XPATH, barVA_Xpath)  # playing status
                                    style_value = bot.find_element(By.XPATH, barVA_Xpath).get_attribute("style")  # Starts @ 100 reduces to 0
                                    if style_value == '': continue
                                finally:
                                    video_progress = style_value.split("(")[1].split(")")[0][1:-1]
                                    with contextlib.suppress(TimeoutException, NoSuchElementException):
                                        wait3secs.until(EC.invisibility_of_element_located(
                                            (By.XPATH, '//button[@class="icon-media-disabled"]')))
                                        loading_icon = False
                                    if all([(0 <= float(video_progress) <= 30), loading_icon, total_status == 1]): # The only Status
                                        bot.find_element(By.XPATH, '//span[@data-icon="x-viewer"]').click()
                                        scroll(statusUploaderName)
                                        bot.find_element(By.XPATH, scrolled_viewed_person_xpath).click()
                                    elif all([(0 <= float(video_progress) <= 30), loading_icon, total_status > 1]): # Not the only Status
                                        _backnforward()
                                    if all([(30 <= float(video_progress) <= 100), loading_icon]): continue
                                    try: bot.find_element(By.XPATH, pause_btn_xpath).click()
                                    except NoSuchElementException: ...
                                    tprint(f"{status_idx}. Status is a Video.")
                                    statusTypeMsg += f"{status_idx}. Status is a Video.\n"
                                    loading_icon = False
                                    break
                        if total_status == 1:
                            while True:
                                video_link: str = bot.find_element(By.XPATH, video_status_xpath).get_attribute('src')                                    
                                if "blob" not in video_link:
                                    bot.find_element(By.XPATH, '//span[@data-icon="x-viewer"]').click()
                                    scroll(statusUploaderName)
                                    bot.find_element(By.XPATH, scrolled_viewed_person_xpath).click()
                                    while True:
                                        with contextlib.suppress(TimeoutException):
                                            wait.until(EC.invisibility_of_element_located(
                                                (By.XPATH, '//button[@class="icon-media-disabled"]')))
                                            break
                                    try: bot.find_element(By.XPATH, pause_btn_xpath).click()
                                    except NoSuchElementException: ...
                                    # finally: break  # Already Clicked
                                else: break
                        else:
                            while True:
                                video_link: str = bot.find_element(By.XPATH, video_status_xpath).get_attribute('src')                                    
                                if "blob" not in video_link:
                                    _backnforward()
                                    continue
                                while True:
                                    with contextlib.suppress(TimeoutException):
                                        wait.until(EC.invisibility_of_element_located(
                                            (By.XPATH, '//button[@class="icon-media-disabled"]')))
                                        break
                                try: bot.find_element(By.XPATH, pause_btn_xpath).click()
                                except NoSuchElementException: ...
                                finally: break  # Already Clicked
                        try:
                            read_more = bot.find_element(By.XPATH, read_more_caption_xpath)
                            read_more.click()
                            caption: str = bot.find_element(By.XPATH, caption_xpath).text
                        except NoSuchElementException: 
                            try:
                                caption: str = bot.find_element(By.XPATH, caption_xpath).text
                            except NoSuchElementException:
                                caption = None
                        finally: 
                            uid: str = video_link.split(".com/")[1]#.split('-')[0]
                            media_names.append(uid)
                            media_info[uid] = {"type": "video", "caption": caption}
                            if len(bot.window_handles) == 1:
                                bot.execute_script('window.open("");')
                            bot.switch_to.window(bot.window_handles[1])
                            bot.get(video_link)
                            sleep(.5)
                            video = bot.find_element(By.XPATH, "//video")
                            video.click()
                            size = video.size
                            brw = (size["width"]/2)-0.5
                            brh = (size["height"]/2)-41
                            action.move_to_element_with_offset(video, brw, brh).click().perform()
                            action.send_keys(Keys.UP, Keys.UP, Keys.ENTER).perform()
                            bot.switch_to.window(bot.window_handles[0])
                except KeyError: 
                    try:
                        if check_Status["txtStatusValue"]:
                            try: bot.find_element(By.XPATH, pause_btn_xpath).click()
                            except NoSuchElementException: ...  # ALREADY CLCIKED
                            caption: str = bot.find_element(By.XPATH, text_status_xpath).text
                            uid: str = f'txt{random.randint(1, 99999):05}'
                            media_names.append(uid)
                            media_info[uid] = {"type": "text", "caption": caption}
                            tprint(f"{status_idx}. Status is a Text.")
                            statusTypeMsg += f"{status_idx}. Status is a Text.\n"
                    except KeyError:
                        try:
                            if check_Status["audioStatusValue"]:
                                tprint(f"{status_idx}. Status is an Audio.")
                                statusTypeMsg += f"{status_idx}. Status is an Audio.\n"
                                if total_status == 1:
                                    while True:
                                        wait.until(EC.presence_of_element_located((By.XPATH, audio_status_xpath)))
                                        audio_link: str = bot.find_element(By.XPATH, audio_status_xpath).get_attribute('src')                                    
                                        if "blob" not in audio_link:
                                            bot.find_element(By.XPATH, '//span[@data-icon="x-viewer"]').click()
                                            scroll(statusUploaderName)
                                            bot.find_element(By.XPATH, scrolled_viewed_person_xpath).click()
                                            while True:
                                                with contextlib.suppress(TimeoutException):
                                                    wait.until(EC.invisibility_of_element_located(
                                                        (By.XPATH, '//button[@class="icon-media-disabled"]')))
                                                    break
                                            try: bot.find_element(By.XPATH, pause_btn_xpath).click()
                                            except NoSuchElementException: ...
                                        else: break
                                else:
                                    while True:
                                        wait.until(EC.presence_of_element_located((By.XPATH, audio_status_xpath)))
                                        bot.find_element(By.XPATH, pause_btn_xpath).click()
                                        audio_link: str = bot.find_element(By.XPATH, audio_status_xpath).get_attribute('src')                                    
                                        if "blob" not in audio_link:
                                            _backnforward()
                                            continue
                                        while True:
                                            with contextlib.suppress(TimeoutException):
                                                wait.until(EC.invisibility_of_element_located(
                                                    (By.XPATH, '//button[@class="icon-media-disabled"]')))
                                                break
                                        try: bot.find_element(By.XPATH, pause_btn_xpath).click()
                                        except NoSuchElementException: ...
                                        finally: break  # Already Clicked
                                uid: str = audio_link.split(".com/")[1]#.split('-')[0]
                                media_names.append(uid)
                                media_info[uid] = {"type": "audio", "caption": None}
                                if len(bot.window_handles) == 1:
                                    bot.execute_script('window.open("");')
                                bot.switch_to.window(bot.window_handles[1])
                                bot.get(audio_link)
                                sleep(.5)
                                audio = bot.find_element(By.XPATH, "//video")
                                audio_rect = audio.rect
                                brw = (audio_rect["width"]/2)-10  # TEST AUDIO CLICK DOWNLOAD
                                brh = (audio_rect["height"]/2)-10
                                action.move_to_element_with_offset(video, brw, brh).click().perform()
                                action.send_keys(Keys.UP, Keys.ENTER).perform()
                                bot.switch_to.window(bot.window_handles[0])
                        except KeyError:
                            try: 
                                if check_Status["old_messageValue"]:
                                    tprint(f"{status_idx}. Status is an Old Whatsapp Version.")
                                    statusTypeMsg += f"{status_idx}. Status is an Old Whatsapp Version.\n"
                            except KeyError as e: 
                                tprint(f'Failed! -> {e}')
            finally:
                if status_idx != loop_range[-1]:
                    viewed_status += 1
                    check_Status = None

                    # Click Next Status
                    bot.find_elements(By.XPATH, barsXpath)[ 
                        viewed_status].click()
                else: # Exit status
                    with contextlib.suppress(Exception):
                        bot.switch_to.window(bot.window_handles[1]); bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    bot.find_element(By.XPATH, '//span[@data-icon="x-viewer"]').click()
                    tprint(block_line)

        # Send to Self
        # wa_bot.send_message(NUMBER, f"{statusTypeMsg}\n{statusUploaderName} at {gmtTime(timezone)}.", \
        #     reply_markup=Inline_list("Show list",list_items=[List_item("Nice one 👌"), List_item("Thanks ✨"), List_item("Great Job")]))
        statusTypeMsg: str = ""
        return media_info


def processVideos(**media_info):
    base_path: str = r"C:\Users\Administrator\Downloads\Tweeter_Uploads"
    idx: int = 1
    for key, value in media_info.items():
        if value['type'] == 'video':
            if path.exists(fr'{base_path}\video{idx}.mp4'):
                remove(fr'{base_path}\video{idx}.mp4')
            rename(f'{base_path}\{key}.mp4', fr'{base_path}\video{idx}.mp4')
            stream = ffmpeg.input(fr'{base_path}\video{idx}.mp4')
            stream = ffmpeg.output(stream, f'{base_path}\{key}.mp4')
            ffmpeg.run(stream)
            idx += 1
    return media_info


def uploadToTwitter(**media_info):
    add_photo_xpath: str = '//div[@aria-label="Add photos or video"]'
    uploaded_percentage: str = "//div[contains(@class, 'r-15zivkp r-bcqeeo r-qvutc0')]"
    tweet_textarea: str = '//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]'
    
    compose_tweet_url: str = "https://twitter.com/compose/tweet"
    bot.get(compose_tweet_url)
    try:
        WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.XPATH, add_photo_xpath)))
    except TimeoutException:
        with open(r'C:\Users\Administrator\Downloads\TestTweet.cookies.json') as cookiejson:
            cookies = json.loads(cookiejson.read())
        for cookie in cookies: bot.add_cookie(cookie)
        bot.refresh()
        WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.XPATH, add_photo_xpath)))
    
    def extension():
        if value['type'] == 'image': return '.jpg'
        elif value['type'] == 'video': return '.mp4'
        elif value['type'] == 'audio': return '.ogg'

    for idx, (key, value) in enumerate(media_info.items(), 1):
        if all([value['caption'] != '', value['caption'] != None]):
            bot.find_elements(By.XPATH, tweet_textarea)[-1].send_keys(value['caption'])
        if value['type'] != 'text':  # Add Media if no text
            bot.find_element(By.XPATH, add_photo_xpath).click(); sleep(3)
            pyautogui.write(f'"{key}{extension()}"')
            pyautogui.press('enter'); sleep(3)
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if value['type'] == 'video':
                while True:
                    with contextlib.suppress(AssertionError):
                        # if len(bot.find_elements(By.XPATH, uploaded_percentage)) == idx:
                        upload_status = bot.find_elements(By.XPATH, uploaded_percentage)[-1].text
                        assert upload_status == "Uploaded (100%)"
                        break
        bot.find_element(By.XPATH, '//div[@aria-label="Add Tweet"]').click()
        sleep(2)
        if idx == len(media_info):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            bot.find_elements(By.XPATH, '//div[@aria-label="Remove Tweet"]')[-1].click()
            sleep(2)
            bot.find_element(By.XPATH, '//div[@data-testid="tweetButton"]').click()
            wait.until(EC.url_changes(compose_tweet_url))
            assert compose_tweet_url != 'https://twitter.com/home'


if __name__ == "__main__":
    status_captions: Optional[Dict] = autoViewStatus()
    status_captions: Optional[Dict] = processVideos(**status_captions)
    # status_captions = {
    #     'processedVideo': {'type': 'video', 'caption': None},
    #     'processedVideo - Copy': {'type': 'video', 'caption': None},

        # '149d5777-ba16-48fa-8abd-a0886feba294': {'type': 'video', 'caption': None},
        # 'cb365106-1c9e-43c4-a4a0-ec23872e0453': {'type': 'video', 'caption': None},
        # 'richee': {'type': 'video', 'caption': None},
    # }

    uploadToTwitter(**status_captions)
    wa_bot.send_message(NUMBER, f"Successfully Uploaded to Twitter at {gmtTime(timezone)}.", \
        reply_markup=Inline_list("Show list",list_items=[List_item("Nice one 👌"), List_item("Thanks ✨"), List_item("Great Job")]))
        