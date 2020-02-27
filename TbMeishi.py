import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pyquery import PyQuery as pq

browser = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
wait = WebDriverWait(browser,10)

def search():
    print('搜索')
    try:
        browser.get("https://www.taobao.com/")
        input = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#q'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input.send_keys('美食')
        submit.click()
        
    except TimeoutException:
        return search()
def main():
    search()
if __name__ == "__main__":
    main()