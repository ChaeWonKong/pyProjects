'''Naver Cafe Attendance Checking Program

This program will automatically write attendance post 
on Naver Cafe when executed.'''

from selenium import webdriver
import time

# Naver log-in page path
login_path = "https://nid.naver.com/nidlogin.login"

# chrome driver path
chrome_path = "/Users/ChaewonKong/Desktop/pyWeb/chromedriver"
driver = webdriver.Chrome(chrome_path)

# chanthomjs path
# phantom_path = "/Users/ChaewonKong/Desktop/pyWeb/phantomjs-2.1.1-macosx/bin/phantomjs"
# driver = webdriver.PhantomJS(phantom_path)

# Set limit time for webpage loading
# driver.implicitly_wait(sec) # set is a int variable

# Get log-in page from Naver.com
driver.get(login_path)

# Write id/password in form fields in log-in page
driver.find_element_by_name("id").send_keys("kong4616")
driver.find_element_by_name("pw").send_keys("2theo22@@")

# Press "Log in" button
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# Open attendance post page
driver.get("http://cafe.naver.com/AttendanceView.nhn?search.clubid=12730407&search.menuid=99")

# Use iframe
time.sleep(3)
driver.switch_to_frame(driver.find_element_by_id("cafe_main"))

# Write comment
driver.find_element_by_id("cmtinput").send_keys("출첵")

# Submit the written comment
driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a').click()


''' naver는 iframe 을 사용해 글을 남기나봄. iframe으로 frame 교체를 해야만 코멘트 필드에 내용 작성이 가능함'''