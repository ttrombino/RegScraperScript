from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.message import EmailMessage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = #enter user
    msg['from'] = user
    password = #enter password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def access_reg(course, dis, driver): #login to webreg, enroll in course/disc

    driver.get("https://www.reg.uci.edu/cgi-bin/webreg-redirect.sh")

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ucinetid"))
        )
    except:
        email_alert("!", "Program Crash in 1", phone_number)
        driver.quit()

    net_id = driver.find_element_by_id("ucinetid")
    net_id.send_keys("") #your uci net id
    psw = driver.find_element_by_name("password")
    psw.send_keys("") #your uci net id password
    psw.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/center[1]/table/tbody/tr/td/form[1]/input[4]"))
        )
    except:
        email_alert("!", "Program Crash in 2", phone_number)
        driver.quit()

    enroll_menu = driver.find_element_by_xpath("/html/body/center[1]/table/tbody/tr/td/form[1]/input[4]")
    enroll_menu.click()

    time.sleep(1)

    add_button = driver.find_element_by_id("add")
    add_button.click()

    cc = driver.find_element_by_name("courseCode")
    cc.send_keys(course)

    send_button = driver.find_element_by_xpath("/html/body/center[1]/form[2]/table/tbody/tr[1]/td/input[3]")
    send_button.click()

    time.sleep(1)

    add_button = driver.find_element_by_id("add")
    add_button.click()
    driver.save_screenshot("scrn1.png")

    cc = driver.find_element_by_name("courseCode")
    cc.send_keys(dis)

    send_button = driver.find_element_by_xpath("/html/body/center[1]/form[2]/table/tbody/tr[1]/td/input[3]")
    send_button.click()

    time.sleep(2)
    driver.save_screenshot("scrn2.png")
    logout_button = driver.find_element_by_xpath("/html/body/center[1]/form[1]/input[4]")
    logout_button.click()

    email_alert("!", "Enroll attempt made", phone_number)
    #raised
    driver.quit()

if __name__ == "__main__":
    phone_number = "" #enter phone number email i.e. 4444@vtext.com
    PATH = "Desktop/chromedriver/chromedriver"
    driver = webdriver.Chrome(PATH)

    #access_reg("34240", "34241", driver)

    driver.get("https://www.reg.uci.edu/perl/WebSoc")

    course = driver.find_element_by_name("CourseCodes")
    course.send_keys("34240, 34241, 34242, 34250, 34251, 34252")
    course.send_keys(Keys.RETURN)
    counter = 0
    email_alert("!", "Start", phone_number)

    try:
        while True:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/table/tbody/tr[9]/td[10]"))
                )
            except:
                email_alert("!", "Program Crash in 3", phone_number)
                driver.quit()

            enrolled_S = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[9]/td[10]").text
            enrolled_S_dis1 = driver.find_element_by_xpath("//html/body/div[4]/table/tbody/tr[10]/td[10]").text
            enrolled_S_dis2 = driver.find_element_by_xpath("//html/body/div[4]/table/tbody/tr[11]/td[10]").text
            req1 = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[9]/td[12]").text

            enrolled_M = driver.find_element_by_xpath("//html/body/div[4]/table/tbody/tr[12]/td[10]").text
            enrolled_M_dis1 = driver.find_element_by_xpath("//html/body/div[4]/table/tbody/tr[13]/td[10]").text
            enrolled_M_dis2 = driver.find_element_by_xpath("//html/body/div[4]/table/tbody/tr[14]/td[10]").text
            req2 = driver.find_element_by_xpath("//html/body/div[4]/table/tbody/tr[12]/td[12]").text

            if enrolled_S != "180":
                if enrolled_S_dis1 != "90":
                    dis = enrolled_S_dis1
                    access_reg("34240", "34241", driver)

                else:
                    dis = enrolled_S_dis2
                    access_reg("34240", "34242", driver)

                alrt = enrolled_S + " enrolled in 34240\n" + enrolled_S_dis1 + " in 34241 " + enrolled_S_dis2 + " in 34242"
                email_alert("!", alrt, phone_number)
                break

            if enrolled_M != "180":
                alrt = enrolled_S + " enrolled in 34250\n" + enrolled_S_dis1 + " in 34251 " + enrolled_S_dis2 + " in 34252"
                email_alert("!", alrt, phone_number)


            driver.refresh()
            time.sleep(2)

    finally:
        email_alert("!", "Program Crash", phone_number)
        driver.quit()




