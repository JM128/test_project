from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os

# 删除文件
try:
    os.remove("job_info.txt")
except FileNotFoundError:
    pass

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91?px=default&city=%E5%85%A8%E5%9B%BD")


# 获取招聘信息
def jobs():
    try:
        jobs_name = driver.find_elements_by_xpath("//div/a/h3")
        jobs_address = driver.find_elements_by_xpath("//span[@class='add']/em")
        jobs_money_require = driver.find_elements_by_xpath("//div[@class='p_bot']/div[@class='li_b_l']")
    except NoSuchElementException:
        driver.quit()
    else:
        return jobs_name, jobs_address, jobs_money_require

# 点击下一页
def next_page():
    try:
        next_page = driver.find_element_by_xpath("//span[@class='pager_next ']")
    except NoSuchElementException:
        driver.quit()
    ActionChains(driver).move_to_element(next_page).perform()
    sleep(2)
    next_page.click()

# 写文件
def writ_file(job_data):
    with open("job_info.txt", 'a')as f:
        data = job_data.encode("gbk","ignore").decode("gbk")
        f.write(data)
        f.write("\n")
        f.close()

# 主程序，循环翻页，获取每一条数据，并写到 job_info.txt 文件。
for page in range(30):
    jobs_name, jobs_address, jobs_money_require = jobs()
    for i in range(15):
        # 数据清洗：拆分，
        job_name = jobs_name[i].text  # 职位
        job_address = jobs_address[i].text.split("·")[0]  # 城市
        info = jobs_money_require[i].text.split(' ')
        job_money = info[0]     # 薪资
        job_exper = info[1]     # 经验
        job_edu = info[3]       # 学历

        job_data = job_name + ";" + job_address + ";" + job_money + ";" + job_exper + ";" + job_edu
        writ_file(job_data)
    next_page() # 下一页
    sleep(10)










#coding=utf-8

编码问题：

1、 读取的外部文件，抓取的web页面上的数据
2、 脚本文件本身的编码
3、 运行python的编码