import os, sys, io, re, threading
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.alert import Alert
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
UpperDir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

class RailAutoTest(QThread,threading.Thread):
    add_al = pyqtSignal(int)
    add_al_2 = pyqtSignal(int)
    add_al_3 = pyqtSignal(int)
    sleepsig = pyqtSignal(int)

    #초기화 실행(webdriver 설정)
    def __init__(self):
        super().__init__()
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI (User-agent)
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path = os.path.join(UpperDir,'chromedriver'))
        self.driver.implicitly_wait(5)

    # 페이지 접속후 로그인
    def SrtRailAuto(self,SrtID,SrtPW):
        try:
            self.driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
            self.add_al.emit(13)
            self.driver.find_element_by_id('srchDvNm01').send_keys(SrtID)
            self.add_al.emit(15)
            self.driver.find_element_by_id('hmpgPwdCphd01').send_keys(SrtPW)
            self.add_al.emit(15)
            self.driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[1]/div[1]/div[1]/input').click()
            self.driver.implicitly_wait(4)
            self.add_al.emit(37)
            sleep(0.4)
            if self.driver.current_url != 'https://etk.srail.co.kr/main.do':
                self.driver.quit()
                self.add_al.emit(20)
                yield False
            self.add_al.emit(20)
            RailStartplace,RailArriveplace,TripDate = yield True
            TripDatematch = TripDate.replace('-','')
            k = "a[onclick*='"+str(TripDatematch)+"']"
            self.driver.find_element_by_id('dptRsStnCdNm').clear()
            self.driver.find_element_by_id('dptRsStnCdNm').send_keys(RailStartplace)
            self.add_al_2.emit(12)
            self.driver.find_element_by_id('arvRsStnCdNm').clear()
            self.driver.find_element_by_id('arvRsStnCdNm').send_keys(RailArriveplace)
            self.add_al_2.emit(11)
            self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[3]/input[2]').click()
            self.driver.implicitly_wait(2)
            self.add_al_2.emit(9)
            self.driver.switch_to_frame(self.driver.find_element_by_id('_LAYER_BODY_'))
            self.driver.find_element_by_css_selector(k).click()
            self.driver.switch_to_default_content()
            self.add_al_2.emit(17)
            self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[5]/a/em').click()
            self.driver.implicitly_wait(4)
            self.add_al_2.emit(24)
            sleep(0.4)
            #if self.driver.current_url != 'https://etk.srail.co.kr/main.do':
                #self.driver.get_screenshot_as_file('1.png')
            sendlist = []
            while True:
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                trlist = soup.select('form#result-form > fieldset > table > tbody > tr')  # [tr,tr,tr,....]
                for tdl in trlist:
                    text = '[출발] '+tdl.select('td')[3].text+ ' [도착] '+tdl.select('td')[4].text+' [소요시간 - '+tdl.select('td')[10].text+']'
                    sendlist.append(text)
                inputlist = soup.select("#result-form > fieldset > div.navigation > input")
                nextlist=[]
                for e in inputlist:
                    nextlist.append(e.attrs['value'])
                if '다음' in nextlist:
                    clicknext = self.driver.find_element_by_css_selector("#result-form > fieldset > div.navigation > input[value='다음']")
                    self.driver.execute_script("arguments[0].click();", clicknext)
                    self.driver.implicitly_wait(4)
                    sleep(0.3)
                else:
                    break
            self.add_al_2.emit(27)
            index = yield sendlist
            ##
            while True:
                hindex = index
                select = Select(self.driver.find_element_by_css_selector("#search-form > fieldset > div.select > dl.hide > dd > select.date.checkForm"))
                select.select_by_visible_text('00')
                self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/div[2]/input').click()
                self.driver.implicitly_wait(4)
                self.add_al_3.emit(12)
                sleep(0.3)
                if index >= 10:
                    k = index // 10
                    for o in range(k):
                        clicknext = self.driver.find_element_by_css_selector("#result-form > fieldset > div.navigation > input[value='다음']")
                        self.driver.execute_script("arguments[0].click();", clicknext)
                        self.driver.implicitly_wait(4)
                        sleep(0.5)
                        index -= 10
                index += 1
                t = "#result-form > fieldset > table > tbody > tr:nth-child("+str(index)+") > td:nth-child(7) > a.button.button-02"
                self.add_al_3.emit(13)

                Currentpage = self.driver.current_url
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                sleep(0.2)
                self.add_al_3.emit(23)
                t2 = soup.select("#result-form > fieldset > table > tbody > tr")[index-1]
                self.add_al_3.emit(13)
                if '예약하기' in t2.select("td")[6].find_all(text='예약하기'):
                    self.driver.find_element_by_css_selector(t).click()
                    sleep(0.5)
                else:
                    sleep(0.3)
                self.add_al_3.emit(16)
                if self.driver.current_url != Currentpage:
                    self.driver.quit()
                    for i in range(3):
                        self.add_al_3.emit(7)
                        sleep(0.1)
                    index = hindex
                    self.add_al_3.emit(2)
                    yield True
                else:
                    for i in range(3):
                        self.add_al_3.emit(7)
                        sleep(0.1)
                    index = hindex
                    self.add_al_3.emit(2)
                    self.sleepsig.emit(1)
                    yield False

        except Exception as ex: # 에러 종류
            print('에러가 발생 했습니다', ex)
            self.driver.quit()
            yield False

    def KorailAuto(self,SrtID,SrtPW):
        try:
            sendlist = []
            forw = re.compile('[가-힣]+')
            aft = re.compile('[^가-힣]+')
            zeroback = re.compile('0\d')
            self.driver.get('https://www.letskorail.com/korail/com/login.do')
            self.add_al.emit(13)
            self.driver.find_element_by_id('txtMember').send_keys(SrtID)
            self.add_al.emit(15)
            self.driver.find_element_by_id('txtPwd').send_keys(SrtPW)
            self.add_al.emit(15)
            self.driver.find_element_by_xpath('//*[@id="loginDisplay1"]/ul/li[3]/a/img').click()
            self.driver.implicitly_wait(4)
            self.add_al.emit(37)
            sleep(0.3)
            if self.driver.current_url != 'http://www.letskorail.com/index.jsp':
                self.driver.quit()
                self.add_al.emit(20)
                yield False
            self.add_al.emit(20)
            RailStartplace,RailArriveplace,TripDate = yield True
            self.driver.get('http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')
            self.driver.implicitly_wait(3)
            self.add_al_2.emit(27)
            sleep(0.4)
            self.driver.find_element_by_id('start').clear()
            self.driver.find_element_by_id('start').send_keys(RailStartplace)
            self.add_al_2.emit(9)
            self.driver.find_element_by_id('get').clear()
            self.driver.find_element_by_id('get').send_keys(RailArriveplace)
            self.add_al_2.emit(9)
            TripDatelist = TripDate.split('-')
            if zeroback.match(TripDatelist[1]) is not None:
                TripDatelist[1] = TripDatelist[1][1:2]
            if zeroback.match(TripDatelist[2]) is not None:
                TripDatelist[2] = TripDatelist[2][1:2]
            select = Select(self.driver.find_element_by_id('s_year'))
            select.select_by_visible_text(TripDatelist[0])
            select = Select(self.driver.find_element_by_id('s_month'))
            select.select_by_visible_text(TripDatelist[1])
            select = Select(self.driver.find_element_by_id('s_day'))
            select.select_by_visible_text(TripDatelist[2])
            self.add_al_2.emit(9)
            self.driver.find_element_by_xpath('//*[@id="center"]/form/div/p/a/img').click()
            self.driver.implicitly_wait(3)
            self.add_al_2.emit(20)
            sleep(0.4)
            if self.driver.current_url == 'http://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do':
                self.driver.find_element_by_xpath('//*[@id="chkNotSee"]').click()
                self.driver.implicitly_wait(5)
                sleep(0.4)
            while True:
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                trlist = soup.select('table#tableResult > tbody > tr')  # [tr,tr,tr,....]
                for tdl in trlist:
                    t1 = forw.findall(tdl.select('td')[2].text.strip())[0]
                    t2 = forw.findall(tdl.select('td')[3].text.strip())[0]
                    t11 = aft.findall(tdl.select('td')[2].text.strip())[0]
                    t22 = aft.findall(tdl.select('td')[3].text.strip())[0]
                    text = '[출발] '+t1+' - '+str(t11)+' [도착] '+t2+' - '+str(t22)+' [소요시간 - '+str(tdl.select('td')[13].text.strip())+']'
                    sendlist.append(text)
                imglist = soup.select("#divResult > table.btn > tbody > tr > td > a > img")
                nextlist=[]
                for e in imglist:
                    nextlist.append(e.attrs['alt'])
                if '다음' in nextlist:
                    self.driver.find_element_by_css_selector("table.btn > tbody > tr > td > a > img[alt='다음']").click()
                    self.driver.implicitly_wait(4)
                    sleep(0.3)
                else:
                    break
            self.add_al_2.emit(26)
            index = yield sendlist
            ##
            while True:
                hindex = index
                self.driver.find_element_by_xpath('//*[@id="center"]/div[3]/p/a/img').click()
                self.driver.implicitly_wait(4)
                self.add_al_3.emit(9)
                sleep(0.3)
                if index >= 10:
                    k = index // 10
                    self.driver.find_element_by_css_selector("#divResult > table.btn > tbody > tr > td > a > img").click()
                    self.driver.implicitly_wait(4)
                    sleep(0.5)
                    index -= 10
                    k -= 1
                    for o in range(k):
                        self.driver.find_element_by_css_selector("#divResult > table.btn > tbody > tr > td > a:nth-child(2) > img").click()
                        self.driver.implicitly_wait(4)
                        sleep(0.5)
                        index -= 10
                index += 1
                tindex = index * 2 - 1
                t = "#tableResult > tbody > tr:nth-child("+str(tindex)+") > td:nth-child(6) > a:nth-child(1) > img"
                self.add_al_3.emit(16)
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.add_al_3.emit(18)
                t2 = soup.select("#tableResult > tbody > tr")[index-1]
                self.add_al_3.emit(16)
                if t2.select("td")[5].find_all(alt='예약하기'):   #[].attrs['alt']
                    self.driver.find_element_by_css_selector(t).click()
                    sleep(0.5)
                    if Alert(self.driver).text:
                        Alert(self.driver).accept()
                    self.driver.quit()
                    for i in range(5):
                        self.add_al_3.emit(7)
                        sleep(0.1)
                    yield True
                else:
                    index = hindex
                    for i in range(5):
                        self.add_al_3.emit(7)
                        sleep(0.1)
                    self.sleepsig.emit(1)
                    yield False

        except Exception as ex: # 에러 종류
            print('에러가 발생 했습니다', ex)
            self.driver.quit()
            yield False
    # 소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit()  #Seleninum 전체 프로그램 종료
