chrome_exe = "./chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from _datetime import datetime

# Setting up my driver
driver = webdriver.Chrome(chrome_exe)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=URL)
start = datetime.now()
start_min = start.time().minute
stop_min = 0

# Don't put in the def function when you're creating an update
cookie_press = driver.find_element_by_id("cookie")
find_element = driver.find_elements_by_css_selector("#store div")
value = [i.get_attribute("id") for i in find_element]


def check_buy_stuff(value):
    map = {}
    for i in value:
        click_items = driver.find_element_by_id(i)
        prices_get = click_items.find_element_by_tag_name("b")
        value_p = (prices_get.text)
        if len(value_p) > 0:
            prices = value_p.split(" - ")
            if "," in prices[1]:
                prices[1] = prices[1].replace(",", '')
            map[int(prices[1])] = click_items
    return map


start_sec = 0
while (stop_min - start_min != 3):
    start = datetime.now()
    stop_min = start.time().minute
    find_money_collected = driver.find_element_by_id("money")

    start_sec = start_sec + 1
    cookie_press.click()

    if start_sec == 6:
        buy_confirm = False
        map_shop = check_buy_stuff(value)
        while (buy_confirm == False):
            if len(map_shop) == 0:
                break
            money_wallet = int(find_money_collected.text)
            buy_item = max(map_shop)

            if buy_item < money_wallet:
                map_shop[buy_item].click()
                break
            else:
                map_shop.pop(buy_item)
                buy_confirm = False

        start_sec = 0

result = driver.find_element_by_xpath('//*[@id="cps"]')
print(result.text)

driver.quit()
