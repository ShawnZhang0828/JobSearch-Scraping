from selenium import webdriver
import time


def googleExtractor(url):
    driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
    driver.get(url)

    time.sleep(1)  # Allow 1 seconds for the web page to open
    scroll_pause_time = 0.2     # pause 0.2 seconds between scroll actions
    screen_height = driver.execute_script('''return document.getElementsByClassName("zxU94d gws-plugins-horizon-jobs__tl-lvc")[0].clientHeight;''')   # get the screen height of the element
    scroll_counter = 1

    while True:
        # scroll one screen height each time
        driver.execute_script(f'''document.getElementsByClassName("zxU94d gws-plugins-horizon-jobs__tl-lvc")[0].scroll(0, {screen_height}*{scroll_counter});''')  
        scroll_counter += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script('''return document.getElementsByClassName("zxU94d gws-plugins-horizon-jobs__tl-lvc")[0].scrollHeight;''')  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * scroll_counter > scroll_height:
            break

    return driver.page_source


def indeedExtractor(url):
    driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
    driver.get(url)

    return driver.page_source

def linkedinExtractor(url):
    driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
    driver.get(url)

    time.sleep(1)
    scroll_pause_time = 0.5
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script(f"window.scrollTo(0, {screen_height}*{i});")
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break 
    return driver.page_source
