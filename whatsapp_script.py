from selenium import webdriver
from time import sleep

import csv 
  
# csv file name 
filename = "Participation teams - WGD.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 

with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

#get the driver for individual browser
driver = webdriver.Chrome('/usr/bin/chromedriver')

#scan the QR code
print("Scan the QR code")
driver.get("https://web.whatsapp.com/")

#send message function
def Sendmsg():

    for i in range(0,10):


        #enter name of receiver
        #name = input("Enter the name of user or group : ")
        name=rows[i][1]
        #name="DU KE CONTACTS"
        #enter the message
        #msg = input("Enter the message : ")
        msg = "Hii "+ rows[i][1] +", Rishi here, Member of IITD dance club. This year we are going to organize Rendezvous  tentatively in the last week of March in online mode, and Kaleidoscope will be one of the Pronite in RDV. More details regarding the same will be announced soon. So we are contacting presidents of all the dance societies. So could you please share the contact details of the Current president of " + rows[i][3]
        #enter the count
        #count = int(input("Enter Number of count : "))
        count=1

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
            button.click()

#send image or video file function
def sendimgvid():
    #enter name of receiver
    name = input("Enter the name of user or group : ")
    #enter file path
    filepath = input("Enter the file path (Image,Video) : ")

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()

    imgvid_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    imgvid_box.send_keys(filepath)

    sleep(3)

    send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
    send_button.click()

#user input
print("Press 1 for sending multiple messages \nPress 2 to send an image or video \nPress  to exit")
n = int(input())
if (n == 1):
    Sendmsg()

elif(n == 2):
    sendimgvid()

elif(n==3):
    quit()