from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pickle
import csv

file = open('example1.csv', 'w', newline='', encoding='utf-8')

writer = csv.writer(file)

writer.writerow(["Title", "Article"])

# driver = webdriver.Chrome(executable_path=r"C:\Users\rusha\Desktop\Factiva\chromedriver.exe")

# answer = driver.get("https://global-factiva-com.mutex.gmu.edu/sb/default.aspx?lnep=hp")

# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

# print(answer)

# You need to: from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("user-data-dir=selenium") 
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("https://global-factiva-com.mutex.gmu.edu/sb/default.aspx?lnep=hp")


chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://mutex.gmu.edu/login?URL=https://global.factiva.com/en/sess/login.asp?xsid=S003cbsYXmnNdmnNTamN9apN96s5DByWa3w3DB94cj0WErBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUEA") # Now you can see the cookies, the settings, extensions, etc., and the logins done in the previous session are present here. 
 

time.sleep(50)

number = 1

# for page in range(len(driver.page_source)):
#     print(driver.page_source[page])

# for page in range(len(driver.page_source)):
#     if driver.page_source[page] == "a" and driver.page_source[page+1] == "c" and driver.page_source[page+2] == "c":
#         print(driver.page_source[page+3:page+10])

# while True:
#     time.sleep(10)
#     actualTitle = driver.title
#     print(actualTitle)

# source = driver.page_source
# domain = 'accno'
# if domain in source:
#     # Cut off the string behind @gmail.com (the mail is now the last word in the string)
#     sub = source[source.find(domain) + len(domain):]
#     # Get the last space and get the substring that comes after it
#     mail = sub[:sub.rindex('>') + 1]
#     print(mail)

while True:

    main_window = driver.current_window_handle

    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        if "accession" in elem.get_attribute("href"):
            #print(elem.get_attribute("href"))
            url_text = "window.open(\'" + str(elem.get_attribute("href")) + "\', \'tab" + str(number) + "\');"
            driver.execute_script(url_text)
            driver.switch_to_window("tab" + str(number))
            title_of_this = driver.find_elements_by_class_name("enHeadline")
            title_of_article = ""
            paragraphs_of_article = ""
            try:
                title_of_article += title_of_this[0].text
            except:
                print("No this")    

            title_of_this = driver.find_elements_by_class_name("idHeadline")
            try:
                title_of_article += title_of_this[0].text

            except:
                print("No this")

            title_of_this = driver.find_elements_by_class_name("deHeadline")
            try:
                title_of_article += title_of_this[0].text

            except:
                print("No this")

            paragraphs = driver.find_elements_by_tag_name('p')
            for paragraph in paragraphs:
                paragraphs_of_article += paragraph.text

            #Writing here now
            writer.writerow([title_of_article, paragraphs_of_article])
            driver.close()
            driver.switch_to.window(main_window)
            time.sleep(4)
            number += 1

    driver.find_element_by_link_text("Next 100").click()
    time.sleep(10)

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if "accession" in elem.get_attribute("href"):
#         #print(elem.get_attribute("href"))
#         url_text = "window.open(\'" + str(elem.get_attribute("href")) + "\', \'tab" + str(number) + "\');"
#         driver.execute_script(url_text)
#         driver.switch_to_window("tab" + str(number))
#         title_of_this = driver.find_elements_by_class_name("enHeadline")
#         title_of_article = ""
#         paragraphs_of_article = ""
#         try:
#             title_of_article += title_of_this[0].text
#         except:
#             print("No this")    

#         title_of_this = driver.find_elements_by_class_name("idHeadline")
#         try:
#             title_of_article += title_of_this[0].text

#         except:
#             print("No this")

#         paragraphs = driver.find_elements_by_tag_name('p')
#         for paragraph in paragraphs:
#             paragraphs_of_article += paragraph.text

#         #Writing here now
#         writer.writerow([title_of_article, paragraphs_of_article])

#         driver.switch_to.window(main_window)
#         time.sleep(10)
#         number += 1

# driver.find_element_by_link_text("Next 100").click()
# time.sleep(10)

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if "accession" in elem.get_attribute("href"):
#         #print(elem.get_attribute("href"))
#         url_text = "window.open(\'" + str(elem.get_attribute("href")) + "\', \'tab" + str(number) + "\');"
#         driver.execute_script(url_text)
#         driver.switch_to_window("tab" + str(number))
#         title_of_this = driver.find_elements_by_class_name("enHeadline")
#         title_of_article = ""
#         paragraphs_of_article = ""
#         try:
#             title_of_article += title_of_this[0].text
#         except:
#             print("No this")    

#         title_of_this = driver.find_elements_by_class_name("idHeadline")
#         try:
#             title_of_article += title_of_this[0].text

#         except:
#             print("No this")

#         paragraphs = driver.find_elements_by_tag_name('p')
#         for paragraph in paragraphs:
#             paragraphs_of_article += paragraph.text

#         #Writing here now
#         writer.writerow([title_of_article, paragraphs_of_article])

#         driver.switch_to.window(main_window)
#         time.sleep(10)
#         number += 1

# driver.find_element_by_link_text("Next 100").click()
# time.sleep(10)

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if "accession" in elem.get_attribute("href"):
#         #print(elem.get_attribute("href"))
#         url_text = "window.open(\'" + str(elem.get_attribute("href")) + "\', \'tab" + str(number) + "\');"
#         driver.execute_script(url_text)
#         driver.switch_to_window("tab" + str(number))
#         title_of_this = driver.find_elements_by_class_name("enHeadline")
#         title_of_article = ""
#         paragraphs_of_article = ""
#         try:
#             title_of_article += title_of_this[0].text
#         except:
#             print("No this")    

#         title_of_this = driver.find_elements_by_class_name("idHeadline")
#         try:
#             title_of_article += title_of_this[0].text

#         except:
#             print("No this")

#         paragraphs = driver.find_elements_by_tag_name('p')
#         for paragraph in paragraphs:
#             paragraphs_of_article += paragraph.text

#         #Writing here now
#         writer.writerow([title_of_article, paragraphs_of_article])

#         driver.switch_to.window(main_window)
#         time.sleep(10)
#         number += 1

# driver.find_element_by_link_text("Next 100").click()

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if "accession" in elem.get_attribute("href"):
#         #print(elem.get_attribute("href"))
#         url_text = "window.open(\'" + str(elem.get_attribute("href")) + "\', \'tab" + str(number) + "\');"
#         driver.execute_script(url_text)
#         driver.switch_to_window("tab" + str(number))
#         title_of_this = driver.find_elements_by_class_name("enHeadline")
#         title_of_article = ""
#         paragraphs_of_article = ""
#         try:
#             title_of_article += title_of_this[0].text
#         except:
#             print("No this")    

#         title_of_this = driver.find_elements_by_class_name("idHeadline")
#         try:
#             title_of_article += title_of_this[0].text

#         except:
#             print("No this")

#         paragraphs = driver.find_elements_by_tag_name('p')
#         for paragraph in paragraphs:
#             paragraphs_of_article += paragraph.text

#         #Writing here now
#         writer.writerow([title_of_article, paragraphs_of_article])

#         driver.switch_to.window(main_window)
#         time.sleep(10)
#         number += 1

# driver.find_element_by_link_text("Next 100").click()

# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if "accession" in elem.get_attribute("href"):
#         #print(elem.get_attribute("href"))
#         url_text = "window.open(\'" + str(elem.get_attribute("href")) + "\', \'tab" + str(number) + "\');"
#         driver.execute_script(url_text)
#         driver.switch_to_window("tab" + str(number))
#         title_of_this = driver.find_elements_by_class_name("enHeadline")
#         title_of_article = ""
#         paragraphs_of_article = ""
#         try:
#             title_of_article += title_of_this[0].text
#         except:
#             print("No this")    

#         title_of_this = driver.find_elements_by_class_name("idHeadline")
#         try:
#             title_of_article += title_of_this[0].text

#         except:
#             print("No this")

#         paragraphs = driver.find_elements_by_tag_name('p')
#         for paragraph in paragraphs:
#             paragraphs_of_article += paragraph.text

#         #Writing here now
#         writer.writerow([title_of_article, paragraphs_of_article])

#         driver.switch_to.window(main_window)
#         time.sleep(10)
#         number += 1

# driver.find_element_by_link_text("Next 100").click()
# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     if "accession" in elem.get_attribute("href"):
#         #print(elem.get_attribute("href"))
#         url_text = "window.open(\'" + str(elem.get_attribute("href")) + "\', \'tab" + str(number) + "\');"
#         driver.execute_script(url_text)
#         driver.switch_to_window("tab" + str(number))
#         title_of_this = driver.find_elements_by_class_name("enHeadline")
#         title_of_article = ""
#         paragraphs_of_article = ""
#         try:
#             title_of_article += title_of_this[0].text
#         except:
#             print("No this")    

#         title_of_this = driver.find_elements_by_class_name("idHeadline")
#         try:
#             title_of_article += title_of_this[0].text

#         except:
#             print("No this")

#         paragraphs = driver.find_elements_by_tag_name('p')
#         for paragraph in paragraphs:
#             paragraphs_of_article += paragraph.text

#         #Writing here now
#         writer.writerow([title_of_article, paragraphs_of_article])

#         driver.switch_to.window(main_window)
#         time.sleep(10)
#         number += 1

#driver.find_element_by_link_text("Next 100").click()
#browser.execute_script("window.open('about:blank', 'tab2');") 

#base_url = 'https://global-factiva-com.mutex.gmu.edu/du/article.aspx/?'

#all_accession_numbers = []

#https://global-factiva-com.mutex.gmu.edu/du/article.aspx/?accessionno=SUNDTI0020210321eh3l0009z&fcpil=en&napc=S&sa_from=&cat=a

