#coing=utf-8

import csv   #导入csv库，可以读取csv文件
from selenium import webdriver
import unittest
from time import sleep
import time
import os
from HTMLTestRunner import HTMLTestRunner

dr=webdriver.Chrome()



class Logintest(unittest.TestCase):
    def test_login(self):
        '''登陆测试'''
        #定义测试方法，框架中测试方法以test_开头，底下引号中的中文会在报告中显示，利于清楚的知道测试目的
        #要读取的scv文件路径
        my_file='E:\\Automatic\\testparameters.csv'
        #csv.reader()读取csv文件，
        #Python3.X用open，Python2.X用file，'r'为读取
        #open(file,'r')中'r'为读取权限，w为写入，还有rb，wd等涉及到编码的读写属性
        data=csv.reader(open(my_file,'r'))
        #for循环将读取到的csv文件的内容一行行循环，这里定义了user变量(可自定义)
        #user[0]表示csv文件的第一列，user[1]表示第二列，user[N]表示第N列
        #for循环有个缺点，就是一旦遇到错误，循环就停止，所以用try，except保证循环执行完
        for user in data:
            dr.implicitly_wait(10)
            dr.get('http://172.16.168.205:9021/login.aspx')
            dr.maximize_window()
            #dr.find_element_by_id('userName').clear()
            sleep(2)
            dr.find_element_by_id('userName').send_keys(user[0])
            #dr.find_element_by_id('pwd').clear()
            dr.find_element_by_id('pwd').send_keys(user[1])
            dr.find_element_by_id('login-button').click()
            sleep(2)
            print ('\n'+'测试项：'+user[2])
            dr.get_screenshot_as_file(path+user[3]+".png")
            try:
                assert dr.find_element_by_id(user[4]).text
                try:
                    error_message = dr.find_element_by_id(user[4]).text
                    self.assertEqual(error_message,user[5])
                    print(u'提示信息正确！预期值与实际值一致:')
                    print('期望值：'+user[5])
                    print('实际值:'+error_message)
                except:
                    print (u'提示信息错误！预期值与实际值不符：')
                    print ('期望值：'+user[5])
                    print('实际值:'+error_message)
            except:
                #print (u'提示信息类型错误,请确认元素名称是否正确！')
                print('登录成功')
     
    def test_logout(self):
        '''登出测试'''
        dr.implicitly_wait(10)
        dr.get('http://172.16.168.205:9021/login.aspx')
        dr.maximize_window()
        dr.find_element_by_id('userName').send_keys('zjm')
        dr.find_element_by_id('pwd').send_keys('333')
        dr.find_element_by_id('login-button').click()
        sleep(5)
        dr.find_element_by_css_selector('#stage_wrapper > div.top_box > div.fr > div > span.xx_icon.fr').click()
        #dr.find_element_by_css_selector('#stage_wrapper > div.top_box > div.fr > div > span.xx_icon.fr > div > ul > li').click()
        dr.find_element_by_css_selector("li:contains('Log out')").click()	
        #dr.find_element_by_xpath('//*[@id="stage_wrapper"]/div[1]/div[2]/div/span[1]/div/ul/li').click()	
        sleep(10)		
        try:
            assert dr.find_element_by_id('login-button').text
            print('登出成功！')
            dr.get_screenshot_as_file(path+'logoutsuccess.png')
        except:
            print('登出失败！')
            dr.get_screenshot_as_file(path+'logoutsuccess.png')
        sleep(10)
		   
    #def tearDown(self):
        #dr.refresh()
       # print('测试结束')

'''class Publictest(unittest.TestCase):
    def setUp(self):
        dr.get(http://172.16.168.205:9021/login.aspx)
        dr.find_element_by_id('userName').send_keys('zjm')
        dr.find_element_by_id('pwd').send_keys('333')
        dr.find_element_by_id('login-button').click()
        sleep(5)

    def tearDown(self):
        dr.refresh()
'''
'''
class Logincm():
    def login(self):
        dr.get(http://172.16.168.205:9021/login.aspx)
        dr.find_element_by_id('userName').send_keys('zjm')
        dr.find_element_by_id('pwd').send_keys('333')
        dr.find_element_by_id('login-button').click()
        sleep(5)

class Upload(unittest.TestCase):
    def uploadclip(self):
'''
if __name__=='__main__':
    

    #定义脚本标题，加u为了防止中文乱码
    report_title = u'登陆模块测试报告'

    #定义脚本内容，加u为了防止中文乱码
    desc = u'登陆模块测试报告详情：'
    
    #定义date为日期，time为时间
    date=time.strftime("%Y%m%d")
    time=time.strftime("%Y%m%d%H%M%S")

    #定义path为文件路径，目录级别，可根据实际情况自定义修改
    path= 'E:/Automatic/'+ date +"/login/"+time+"/"


    #定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    report_path = path+"report.html"
    
    #判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    #定义一个测试容器
    testsuite = unittest.TestSuite()
    
    #将测试用例添加到容器
    #tests = [Logintest("test_login"),Logintest("test_logout")]添加多条测试
    #testsuite.addTest(tests)
    #testsuite.addTest(Logintest("test_login"))
    testsuite.addTest(Logintest("test_logout"))
    
    #将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
    os.system(report_path)
    #关闭report，脚本结束
    #report.close()
    #关闭浏览器
    dr.quit()