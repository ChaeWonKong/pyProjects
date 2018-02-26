'''Naver Cafe Attendance Checking Program

This program will automatically write attendance post 
on Naver Cafe when executed.'''

from selenium import webdriver
import time

# 네이버 아이디 및 비밀번호 변수 할당
user_id = "" # 네이버 아이디 입력
user_pw = "" # 네이버 비밀번호 입력


try:
	# 크롬 드라이버 경로 지정
	driver = webdriver.Chrome("/Users/ChaewonKong/Desktop/pyWeb/chromedriver")

	# 네이버 로그인 화면 Get Request
	driver.get("https://nid.naver.com/nidlogin.login")

	# 네이버 로그인화면에 아이디 및 비밀번호 입력
	driver.find_element_by_name("id").send_keys(user_id)
	driver.find_element_by_name("pw").send_keys(user_pw)

	# 로그인 버튼 클릭
	driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

	# 네이버의 '붇옹산의 부동산스터디' 카페 출석부 페이지 열기
	driver.get("http://cafe.naver.com/AttendanceView.nhn?search.clubid=12730407&search.menuid=99")

	# iframe으로 프레임 변경
	time.sleep(2)
	driver.switch_to_frame(driver.find_element_by_id("cafe_main"))

	# 폼 필드에 "출첵합니다~" 코멘트 작성
	driver.find_element_by_id("cmtinput").send_keys("출첵합니다~")

	# 작성된 출석 코멘트 Post
	driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a').click()

	# 2초간 타임슬립 후 크롬 드라이버 및 셀레니움 종료
	time.sleep(2)
	driver.close()

except TaskUnableError as e:
	print(e) # 오류시 오류 메세지 출력

else:
	# 완료시 완료 메시지 출력
	print("Successfully Done!")