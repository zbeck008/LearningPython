from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Zack\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys(
    "5610")
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div[1]/div/span/a/div/img").click()
if driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/h1/span"):
    print("Casio watch found correctly")
    driver.close()
else:
    print("Casio watch not found!")
    driver.save_screenshot("C:\\Users\\Zack\\Desktop\\casiowatchtest.png")
    driver.close()
