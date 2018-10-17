from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import os
import csv

class LoginCase(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		print("start testing")
		self.dr = webdriver.Chrome()
		self.dr.get("https://www.baidu.com")

	def test_login_success(self):
		#Arange
		username = 'ZJM128'
		password = 'pass2word'
		#Action
		self.by_id('user_login').send_keys(username)
		self.by_id('user_pass').send_keys(password)
		self.by_id('wp-submit').click()
		#Assert
		self.assertTrue('wp-admin' in self.dr.current_url)
		login_name = self.by_css('#wp-admin-bar-my-account.ab-item')
		self.assertTrue(username in login_name)

	def test_login_failed(self):

		testfile = "E:\\MyPython\\testdata.csv"
		data = csv.reader(open(testfile,'r'))

		for user in data:
			self.by_id('user_login').send_keys(user[0])
			self.by_id('user_pass').send_keys(user[1])
			self.by_id('wp-submit').click()

			try:
				assert self.dr.by_id('login_error').text
				error_msg = self.dr.by_id('login_error').text
				self.assertEqual(error_msg,user[2])
				print(error_msg)
			except:
				print(u"用户名和密码不能为空")


	def by_id(self,the_id):
		return self.dr.find_element_by_id(the_id)

	def by_css(self,css):
		return self.dr.find_element_by_css_selector(css)

	def by_name(self,name):
		return self.dr.find_element_by_name(name)

	def by_xpath(self,path):
		return self.dr.find_element_by_xpath(path)


	def tearDown(self):
		print("end every testcase")
		self.dr.quit()


if __name__ = 'main':
	#unittest.main()
	testsuite = unittest.TestSuite()
	testsuite.addTest(LoginCase("test_login_success"))

	date = time.strftime(%Y%m%d)
	time = time.strftime(%Y%m%d-%H-%M-%S)

	path = "E:/MyPython/report/"+date+'/'+time+'/'
	report_path = path +"report.html"

	if not os.path.exists(path):
		os.makedirs(path)
	else:
		pass

	with open(report_path,'wb') as report:
		runner = HTMLTestRunner(stream=report,
			title=u'WordPress登录测试报告',
			description=u'测试用例详细描述')
		runner.run(testsuite)
