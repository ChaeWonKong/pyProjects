'''NAVER CAFE Attendance Comment Posting Program

This program will automatically post attendance comment 
on designated NAVER CAFE once per everyday 6.a.m'''

from selenium import webdriver
import time

# Assign NAVER ID, PW to variables by getting inputs
user_id = input("Please enter your NAVER ID -->")
user_pw = input("Please enter your NAVER PASSWORD -->")


def post_everyday():
	'''Execute attendance_post function once per day'''


def attendance_post(id, pw):
	'''Post attendance comment automatically on given NAVER CAFE.'''

	try:
		# Set chrome webdriver path
		driver = webdriver.Chrome("/Users/ChaewonKong/Desktop/pyWeb/chromedriver")

		# Get naver log in page
		driver.get("https://nid.naver.com/nidlogin.login")

		# Post naver id and pw on id/pw form fields
		driver.find_element_by_name("id").send_keys(user_id)
		driver.find_element_by_name("pw").send_keys(user_pw)

		# Click log in button
		driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

		# Navigate to "Bud-ongsan's Budongsan Study" NAVER CAFE attendance comment board
		driver.get("http://cafe.naver.com/AttendanceView.nhn?search.clubid=12730407&search.menuid=99")

		# Change frame to iframe
		time.sleep(2)
		driver.switch_to_frame(driver.find_element_by_id("cafe_main"))

		# Write down attendance comment on comment form field
		driver.find_element_by_id("cmtinput").send_keys("출첵합니다~")

		# Post written comment
		driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a').click()

		# Sleep time for 2 sec and close chrome webdriver
		time.sleep(2)
		driver.close()

	except TaskUnableError as e:
		print(e) # Print error message if error

	else:
		# Print success message if all the tesks are completed
		print("Successfully Done!")


# Execute attendance_post function
attendance_post(user_id, user_pw)