'''Naver Cafe Attendance Checking Program

This program will automatically write attendance post 
on Naver Cafe when executed.'''

from selenium import webdriver

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

# Open attendance post page of Jaegebal cafe
driver.get("http://cafe.naver.com/AttendanceView.nhn?search.clubid=12730407&search.menuid=99")
driver.find_element_by_tag_name('textarea').send_keys("출첵합니다~")

# <textarea id="cmtinput" name="attendancePost.content" cols="" rows="" class="reply-write m-tcol-c"></textarea>

#cmtinput
#//*[@id="cmtinput"]

'''네이버 로그인 하고 카페 들어가서 출석 게시판까지 이동 성공했으나, 댓글을 적는 폼 필드의 name, id를 찾지 못함'''


# 버튼 xpath= '//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a'
