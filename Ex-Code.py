from ast import Pass
import datetime, os
from multiprocessing.connection import wait
from random import randint
# from telnetlib import EC
import pytz
from selenium import webdriver
from time import sleep, perf_counter
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, \
    NoSuchElementException, ElementClickInterceptedException, NoSuchWindowException, \
        StaleElementReferenceException as ser, InvalidSessionIdException as isi

driverpath = "C:\\Users\\Administrator\\Documents\\Boss\\assest\\driver\\chromedriver.exe"
# driverpath = "C:\\Users\\LmAo\\Documents\\AAA Testing\\Code\\python\\drivers\\chromedriver.exe"


# chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\AAAChromeData
keepRunningBrowser = f'chrome.exe --remote-debugging-port=9000 --user-data-dir=C:\BBBChromeData'
# os.system(keepRunningBrowser)

service = Service(executable_path=driverpath)
options = Options()
# options.headless = True  #  Chrome has already besen opened, headless cannot work
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument('user-data-dir=C:\\BBBChromeData')   # For Keep Bossing DIR
# options.add_argument('user-data-dir=C:\\AAAChromeData')   # For My dev debugging DIR
# options.add_argument('user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data')   # Uncomment this and...\
# options.add_argument('--profile-directory=Default')                                                       # comment this to use default
 
options.add_experimental_option("debuggerAddress", "localhost:9000") # Keep Bossing
bot = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(bot, 20, ignored_exceptions=(ser, isi))
action = ActionChains(bot)

#. bot.maximize_window()


def start_Bot():
    # os.system(keepRunningBrowser)
    bot.get("https://web.whatsapp.com"); sleep(30)
start_Bot()

timeZones = pytz.all_timezones # All Time zone
start = int(perf_counter())
refreshedMsg = "Refreshed Message."
statusUploaderName="No Name"
output_TimeStart = int(perf_counter())
counter = 1


def gmtTime():
    return datetime.datetime.now(pytz.timezone("Africa/Lagos")).strftime("%H : %M : %S")

def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return f"{hour}:{min}:{sec}"

def refreshTime(): # This refreshed both the page and time
    global start, elapstedTime
    elapstedTime = int(perf_counter()) - start
    bot.refresh()
    sleep(3)
    while True:
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="intro-text"]')))
            print("Sleeping 5 secs to allow the Status to load up")
            sleep(5)
            break
        except Exception as e:
            pass
    start = int(perf_counter())
    refreshedMsg = "\n ------- Refreshed and Start Time reset succesfully. --------\n"
    print(refreshedMsg)

def getMessage(message, statusUploaderName, refreshedMsg):
    # Check if no conversation is selected
    try:
        bot.find_element(By.XPATH, '//div[@data-testid="intro-text" and @class="_1y6Yk"]')
        search_field = bot.find_element(By.XPATH, '//div[@data-testid="chat-list-search"]')
        search_field.clear(); sleep(0.5)
        search_field.send_keys("+234 909 686 6925"); sleep(0.5) # Search MySelf
        bot.find_element(By.XPATH, '//span[@title="+234 909 686 6925"]').click(); sleep(0.5) # Click MySelf
        # print("Error")
        if statusUploaderName:
            bot.find_element(By.XPATH, '//p[@class="selectable-text copyable-text"]').send_keys(f'{message}\n' + Keys.ENTER) # Type and Send
            print(f"{counter}. {message}"); sleep(0.5)
        else:
            bot.find_element(By.XPATH, '//p[@class="selectable-text copyable-text"]').send_keys(f'{refreshedMsg}\n' + Keys.ENTER) # Type and Send
            sleep(0.5); # print(f"{refreshedMsg}")    
    except Exception as e: # Send message to myself
        search_field = bot.find_element(By.XPATH, '//div[@data-testid="chat-list-search"]')
        search_field.clear(); sleep(0.5)
        search_field.send_keys("+234 909 686 6925"); sleep(0.5) # Search MySelf
        bot.find_element(By.XPATH, '//span[@title="+234 909 686 6925"]').click(); sleep(0.5) # Click MySelf
        # print("Error")
        bot.find_element(By.XPATH, '//p[@class="selectable-text copyable-text"]').send_keys(f'{message}\n' + Keys.ENTER) # Type and Send
        print(f"{counter}. {message}"); sleep(0.5)

def runCode():
    global counter, output_TimeStart
    title = "Agba"
    other_person = "NNaijaTwitterSavage"
    #  NaijaTwitterSavage, Agba, Tweet Savage, Freebiestech, XD Gaming, Naija, Kazmpire , Texy, All Football
    #  Crypto Base, Emmyzee Yello, Bot Tv, Zurkzz
    # bot.execute_script('arguments[0].scrollIntoView();', agba)
    try: 
        statusPage = bot.find_element(By.XPATH, '//span[@data-icon="status-v3-unread"]')
        statusPage.click(); sleep(1)  # Click to enter list of Status screen and sleep 1 sec
        
        if statusPage: Pass
        else: counter -= 1
    except ser as e: 
        bot.quit()
        print("Stale Error\nRelauching...")
        sleep(1)
        start_Bot()
    except NoSuchElementException as e: 
        try:
            agba = bot.find_element(By.XPATH, f'//span[@title="{title}"]') 
            other_p = bot.find_element(By.XPATH, f'//span[@title="{other_person}"]')
            if agba: agba.click()
            elif other_p: other_p.click()
            sleep(2)
            statusUploaderName = bot.find_element(By.XPATH, '//div[@class="_1tRGW"]').get_attribute('innerText')
            sleep(5)
            message = f"{statusUploaderName} at {gmtTime()}"
            # Click back to list of Status screen
            bot.find_element(By.XPATH, '//span[@data-testid="back"]').click(); sleep(0.5)
            # Click back to the Main screen
            bot.find_element(By.XPATH, '//span[@data-testid="x-viewer"]').click(); sleep(0.5)
            getMessage(message, statusUploaderName, refreshedMsg)
            counter += 1
        except NoSuchElementException as e: # print(e)
            output_TimeEnd = int(perf_counter()) - output_TimeStart
            # print(output_TimeEnd)
            if 7 <= output_TimeEnd <= 2000: 
                print(f"{counter}. ECI - NSE || sleeping..." ); # sleep(3)
                output_TimeStart = int(perf_counter())
                counter += 1
        except ElementClickInterceptedException as e: # print(e) 
            output_TimeEnd = int(perf_counter()) - output_TimeStart
            # print(output_TimeEnd)
            if 7 <= output_TimeEnd <= 2000: 
                print(f"{counter}. ECI - ECI || sleeping..."); # sleep(3)
                output_TimeStart = int(perf_counter())
                counter += 1
        except NoSuchWindowException as e: 
            try: bot.quit(); start_Bot()
            except Exception as e: sleep(1); start_Bot()
        except WebDriverException as e: 
            try: bot.quit(); start_Bot()
            except Exception as e: sleep(1); start_Bot()
        except Exception as e: # print(e)
            output_TimeEnd = int(perf_counter()) - output_TimeStart
            # print(output_TimeEnd)
            if 7 <= output_TimeEnd <= 2000: 
                print(f"{counter}. ECI - GE || sleeping..."); # sleep(3)
                output_TimeStart = int(perf_counter())
                counter += 1
            
        tempElapstedTime = int(perf_counter()) - start
        # print(tempElapstedTime)
        if 900 <= tempElapstedTime <= 1800: # Check if it between 25 to 30 mins (1800)
            print(f"Refreshed at => {convert(tempElapstedTime)}")
            try:
                refreshTime()
                wait.until(EC.alert_is_present())
                bot.switch_to.alert.accept()
            except: pass
    except ElementClickInterceptedException as e: 
        try:
            try:
                agba = bot.find_element(By.XPATH, f'//span[@title="{title}"]')
                circle_xpath = f'//span[@title="{title}"]//ancestor::div[@class="lhggkp7q ln8gz9je rx9719la"]\
                    //*[local-name()="circle" and @class="j9ny8kmf"]'
                circle_attr = bot.find_element(By.XPATH, circle_xpath).get_attribute("stroke-dasharray").split(" ")
                unviewed_circle = circle_attr.count(circle_attr[0])
                agba.click()                
            except NoSuchElementException as e: # print(e)
                other = bot.find_element(By.XPATH, f'//span[@title="{other_person}"]') 
                other.click()
            except ElementClickInterceptedException as e: # print(e) 
                other = bot.find_element(By.XPATH, f'//span[@title="{other_person}"]')
                other.click() 
            except : print(f"It all an Exception Right?") # \n{e}
                # other = bot.find_element(By.XPATH, f'//span[@title="{other_person}"]') 
            finally: 
                sleep(6)
                statusUploaderName = bot.find_element(By.XPATH, '//div[@class="_1tRGW"]').get_attribute('innerText')
                #sleep(2)
                global imgStatus, videoStatus, txtStatusOnly, txtLinkBanImg, txtLinkNoBan, txtLinkBanNoImg
                try: imgStatus = bot.find_element(By.XPATH, '//div[@class="_26Q83"]//img'); print("Image Status.")
                except: 
                    try: videoStatus = bot.find_element(By.XPATH, '//div[@class="_26Q83"]//video'); print("Video Status.")
                    except:
                        try: txtStatusOnly = bot.find_element(By.XPATH, '//div[@class="_3KpnX _4WvQQ _2fG2M"]'); print("Text Only Status.")
                        except:
                            try: txtLinkBanImg = bot.find_element(By.XPATH, '//div[@class="_3KpnX _2uTr8 _2fG2M _1Kiur _11vA6"]'); print("Text, Link and Banner Image Status.")
                            except:
                                try: txtLinkNoBan = bot.find_element(By.XPATH, '//div[@class="_3KpnX _2uTr8 _2fG2M"]'); print("Text, Link (No Banner) Status.")
                                except:
                                    try: txtLinkBanNoImg = bot.find_element(By.XPATH, '//div[@class="_3KpnX i-2rU _2fG2M _1Kiur _11vA6"]'); print("Text, Link, Banner (No Image) Status")
                                    except: pass

                    
                # playPauseBtn = bot.find_element(By.XPATH, '//div[@class="lyrceosr bx7g2weo i94gqilv bmot90v7 lxozqee9"]')
                # playPauseBtn.click(); #sleep(6)
                bars = bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')
                # //div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3f8oh _2gskD"] 
                # for idx, _ in enumerate(bars): #print(_)
                #     bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')[randStat].click()
                #     print(f"{idx}. Clicked. Status {randStat}")
                #     sleep(1)
                # print(f"Done with the For loop\nGotten Status bars, which are {len(bars)}.")

                # for idx, bar in enumerate(bars):
                #     randStat = randint(0, len(bars)-1)
                #     print(f"Entered {idx+1} time(s)")
                #     sleep(1)
                #     print("Slept for 1 sec, moving on...")
                #     if imgStatus: 
                #         bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')[randStat].click()
                #         print(f"clicked Image bar {idx+1}"); sleep(1.5)
                #     elif videoStatus:
                #         bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')[randStat].click()
                #         print(f"clicked Video bar {idx+1}"); sleep(1.5)
                #     elif txtStatusOnly:
                #         bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')[randStat].click()
                #         print(f"clicked TextStatus bar {idx+1}"); sleep(1.5)
                #     elif txtLinkBanImg:
                #         bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')[randStat].click()
                #         print(f"clicked Text_Link_Ban_Img bar {idx+1}"); sleep(1.5)
                #     elif txtLinkNoBan:
                #         bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')[randStat].click()
                #         print(f"clicked Text_Link_NoBan bar {idx+1}"); sleep(1.5)
                #     elif txtLinkBanNoImg:
                #         bot.find_elements(By.XPATH, '//div[@class="_3b17O"]//child::div[@class="sZBni"]//child::div[@class="_3CRhO"]')[randStat].click()
                #         print(f"clicked Text_Link_Ban_NoImg bar {idx+1}"); sleep(1.5)
                #     else: print("--------------What on heaven could the status be then???--------------".upper())


                # print(type(bars))
                # sleep(1)
                # for bar in bars:
                #     try:
                #         viewing = bot.find_element(By.XPATH, '//div[@class="_3f8oh _2gskD"]')
                #         val = len(bars) - bar
                #         print(val)
                #     except: pass
                # body = bot.find_element(By.XPATH, '//body[@class="web dark"]')
                # action.click_and_hold(on_element=body).perform()
                # sleep(4)
                message = f"{statusUploaderName} at {gmtTime()}"
                # Click back to list of Status screen
                # bot.find_element(By.XPATH, '//span[@data-testid="back"]').click(); sleep(0.5)
                # Click back to the Main screen
                bot.find_element(By.XPATH, '//span[@data-testid="x-viewer"]').click(); sleep(0.5)
                getMessage(message, statusUploaderName, refreshedMsg)
                counter += 1
        except NoSuchElementException as e:  
            # print(e)
            output_TimeEnd = int(perf_counter()) - output_TimeStart
            # print(output_TimeEnd)
            if 7 <= output_TimeEnd <= 2000: 
                print(f"{counter}. ECI - NSE || sleeping..." ); # sleep(3)
                output_TimeStart = int(perf_counter())
                counter += 1
        except ElementClickInterceptedException as e: 
            # print(e) 
            output_TimeEnd = int(perf_counter()) - output_TimeStart
            # print(output_TimeEnd)
            if 7 <= output_TimeEnd <= 2000: 
                print(f"{counter}. ECI - ECI || sleeping..."); # sleep(3)
                output_TimeStart = int(perf_counter())
                counter += 1
        except isi as e: print(f"ISI occured but movement...")
        except NoSuchWindowException as e: 
            try: bot.quit(); start_Bot()
            except Exception as e: sleep(1); start_Bot()
        except WebDriverException as ex: 
            print(f"WDE || {ex}")

            # try: bot.quit(); start_Bot()
            # except Exception as e: sleep(1); start_Bot()
        except Exception as e: 
            print(f"GE || {e}")
            output_TimeEnd = int(perf_counter()) - output_TimeStart
            # print(output_TimeEnd)
            if 7 <= output_TimeEnd <= 2000: # Outputting error if after 7 secs
                print(f"{counter}. ECI - GE || sleeping..."); # sleep(3)
                output_TimeStart = int(perf_counter())
                counter += 1
            
        tempElapstedTime = int(perf_counter()) - start
        # 900 = 15 mins, 1500 was before
        if 900 <= tempElapstedTime <= 1800: # Check if it between 25 to 30 mins (1800)
            print(f"Refreshed at => {convert(tempElapstedTime)}")
            try:
                refreshTime()
                wait.until(EC.alert_is_present())
                bot.switch_to.alert.accept()
            except: pass



while True:
    try:
        try: bot.quit()
        except: os.system(keepRunningBrowser)
        finally: runCode() 
    except NoSuchElementException as ee:
        print(f"NoSuchElement Exception.\n{ee}")
    except TimeoutException as eee:
        print(f"Timeout Exception.\n{eee}")
    except NoSuchWindowException as e: 
        try: bot.quit(); start_Bot()
        except Exception as e: sleep(1); start_Bot()
    except WebDriverException as e: 
        try: bot.quit(); start_Bot()
        except Exception as e: sleep(1); start_Bot()
    except Exception as e:
        print(f"While Exception\n{e}")
        try:
            runCode()
            # The whatsapp StartUp Text
            bot.find_element(By.XPATH, '//p[@class="selectable-text copyable-text"]')
            # print("hello")
        except NoSuchElementException as ee2: print(f"NSE Exception EE2")
        except Exception as e1:
            try: # This is done for the main program, incase error occured
                message = f"{counter}. Whatsapp Not Found.\n{e1}"
                print(message)
                getMessage(message, statusUploaderName, refreshedMsg)
            except Exception as e2: 
                print(f"Exception E2 {e2}")
                Pass # This is for the first try block where it wait for the displayed Whatsapp Text    
    


