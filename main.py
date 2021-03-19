import time
import csv
import sys
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException, WebDriverException, WebDriverException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0
names = []
option =""
max_name_length = 20
max_massege_length = 100
choise = 0


class Browser:  # Class name to control browser inteaction

    def __init__(self):
        pass

    def browser_details(self):
        self.inutName = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'  # message box link.

        self.button = '//*[@id="main"]/footer/div[1]/div[3]'  # send button link

        self.browser = webdriver.Chrome()
        self.browser.get('https://web.whatsapp.com/')

    def find(self,name):
        self.browser.implicitly_wait(20)
        self.browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(name)  #search bar link used to find names
        # time.sleep(4)
        self.browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)  # Enter button used to enter search results


class App(Browser):

    def single(self, messege, name, count):

        self.browser_details()

        while True:
            try:
                self.find(name)
                break

            except NoSuchElementException:
                print("Scan Qr code")
                time.sleep(5)

        for i in range(count):
            self.browser.find_element_by_xpath(self.inutName).send_keys(messege)
            time.sleep(1)
            self.browser.find_element_by_xpath(self.button).click()
            i += 1
        self.browser.quit()


class Multi(Browser):

    def double(self, names, massege):

        self.browser_details()
        for i in names:
            print(i)
            time.sleep(2)
            while True:
                try:
                    self.find(i)
                    break
                except NoSuchElementException:
                    print("Scan Qr code")
                    time.sleep(5)

            self.browser.find_element_by_xpath(self.inutName).send_keys(massege)
            time.sleep(1)
            self.browser.find_element_by_xpath(self.button).click()
            time.sleep(2)
        self.browser.quit()


class Auto_Reply():

    def reading_notification(self):
        try:
            while True:

                def noti1():
                    try:
                        browser.implicitly_wait(2000)
                        self.noti = browser.find_element_by_class_name('_31gEB').text # getting notification

                    except AttributeError:
                        #print(self.noti)
                        print("No notification for now")


                    except(WebDriverException, NoSuchWindowException):
                        quit()


                def noti2():
                    try:
                        browser.implicitly_wait(2000)
                        self.read_massege = browser.find_element_by_xpath('//span[@class="_31gEB"]/parent::*/parent::*/parent::*/parent::*/div/span/span').text  # findin notification massage


                    except (NoSuchWindowException,AttributeError):
                        print(" ")
                        quit()
                def noti3():
                    try:
                        browser.implicitly_wait(2000)
                        self.sender_name = browser.find_element_by_xpath('//span[@class="_31gEB"]/parent::*/parent::*/parent::*/parent::*/parent::*/div/div/span/span[1]').text  # Finding sender name
                    except AttributeError:
                        print("no massage")
                    except (NoSuchWindowException, WebDriverException):
                        quit()
                def noti4():
                    try:
                        browser.implicitly_wait(2000)
                        browser.find_element_by_xpath('//span[@class="_31gEB"]/parent::*/parent::*/parent::*/parent::*').click()   # opening noitification
                    except NoSuchWindowException:
                        quit()
                # calling all threads
                try:
                    thread1 = threading.Thread(target=noti1)
                    thread2 = threading.Thread(target=noti2)
                    thread3 = threading.Thread(target=noti3)
                    thread4 = threading.Thread(target=noti4)
                    thread1.start()
                    thread2.start()
                    thread3.start()
                    thread4.start()

                    thread1.join()
                    thread2.join()
                    thread3.join()
                    thread4.join()
                    time.sleep(5)
                except AttributeError:
                    pass


                #return noti,read_massege,sender_name
                break
        except (NoSuchElementException, WebDriverException):
            print("Watting")
            pass
        except AttributeError:
            print("Help")
        #except ElementClickInterceptedException:
           # pass

    def reply(self):
        while True:
            self.reading_notification()
            try:
                if (len(self.noti) != 0):

                    print("Objective found")
                    # reply = "Hi dada"
                    if (self.read_massege == "Ki holo"):
                        reply = "nothing"
                    elif (self.read_massege == "Hi"):
                        reply = "Hellow there i am a bot"
                    else:
                        reply= "all the best"
                    browser.implicitly_wait(2000)
                    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(reply) # massege box
                    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
                    #time.sleep(3)
                    #browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.TAB)
                    time.sleep(5)
                    browser.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[3]').click() # backgroung clicking button
                    print(f"Sender Massage: {self.read_massege}")
                    print(f"Sender Name: {self.sender_name}")
                    print("\n")
                    time.sleep(60)
                    print("nessage sent")
                else:
                    print("No massege for now")

            except AttributeError:
                print("No Objective found")
                break
            except NoSuchWindowException:
                exit()

            except WebDriverException:
                print("I am here")
                quit()


class Error:
    pass



while True:
    try:
        while (choise < 1) or (choise > 3):
            choise = int(input("Enter yor choice? "))
        break
    except ValueError:
        print("Enter number between 1, 2, 3")


if choise == 1:
    while True:
        messege = input("Enter your messege: ")
        if (messege == "") or (len(messege) > max_massege_length):
            print("Enter messege")
            print("\n")
        else:
            break

    while True:
        name = input("Enter contact name: ")
        if (name == "") or (len(name) > max_name_length):
            print("Enter Correct user name")
            print("\n")
        else:
            break

    while True:
        try:
            while (count < 1) or (count > 500):
                count = int(input('Enter the count : '))
            break
        except ValueError:
            print("Enter correct number")
            print("\n")
    send = App()
    send.single(messege, name, count)

elif choise == 2:
    with open('name.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            names = row
            print(row)
    while True:
        massege = input("Enter your messege: ")
        if (massege == "") or (len(massege) > max_massege_length):
            print("Enter messege")
            print("\n")
        else:
            break
    print(names)
    new_multi = Multi()
    new_multi.double(names,massege)

elif choise == 3:
    browser = webdriver.Chrome()
    browser.get('https://web.whatsapp.com/')
    wait = WebDriverWait(browser, 600)
    browser.implicitly_wait(2000)
    new_reply = Auto_Reply()
    new_reply.reply()





