from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import requests
import time

#--------------------------------------------------------------------
print('*******************[조아라 노블레스 다운로더]*******************')
print('(본 프로그램을 사용함으로 인한 모든 책임은 사용자에게 있습니다.)\n\n')
time.sleep(1)
ID = input("아이디를 입력하세요 : ")
PW = input("비밀번호를 입력하세요 : ")
NOVEL_1PAGE = input("다운할 소설의 [1화 모바일버전 URL]을 입력하세요 (조아라 모바일 : https://m.joara.com) : ")
NOVEL_END = int(input("[마지막 화수]를 입력해 주세요 (자연수만 가능합니다) : "))
NOVEL_NAME = input("저장할 텍스트 파일 제목을 입력해주세요 : ")

#-----------------------------------페이지 이동---------------------------------

driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = 'https://m.joara.com'
driver.get(url)
action = ActionChains(driver)

time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div/header/div/div[1]/a[1]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[1]/div[3]/a/span[1]").click()
time.sleep(3)
driver.find_element_by_name("userId").send_keys(ID)
time.sleep(3)
driver.find_element_by_name("passwd").send_keys(PW)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div/div/div/button[1]").click()
time.sleep(3)
driver.get(NOVEL_1PAGE)
time.sleep(3)
driver.find_element_by_css_selector('.checkmark').click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[1]/a/img").click()
time.sleep(3)


#---------------------------------크롤링-----------------------------------

NOVEL_PAGE = 0

while NOVEL_PAGE < NOVEL_END:

    NOVEL_PAGE = NOVEL_PAGE +1

    f = open(f"{NOVEL_NAME} 1~{NOVEL_END}.txt", 'a', encoding='UTF8')
    f.write(f"\n\n***[{NOVEL_PAGE}/{NOVEL_END}화]***\n\n\n")
    time.sleep(0.5)

    webpage = driver.page_source #현재페이지
    soup = BeautifulSoup(webpage, "html.parser")
    f = open(f"{NOVEL_NAME} 1~{NOVEL_END}.txt", 'a', encoding='UTF8')
    for anchor in soup.select(".text-wrap"):
        data = (anchor.get_text())
        f.write(data)
    f.close()
    time.sleep(0.5)

    driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/a[2]/div").click()
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[3]/button[2]").click()
    time.sleep(0.5)

#---------------------------------완료-----------------------------------
print('\n\n***[다운로드가 완료되었습니다.]***')

