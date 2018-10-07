from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def is_exist(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def hover(driver,element):
    ActionChains(driver).move_to_element(element).perform()


#STEP 1
print("step 1")

#go to amazon
browser = webdriver.Chrome()
browser.implicitly_wait(20)

base_url = "https://www.amazon.com/"
browser.get(base_url)
browser.maximize_window()
current_url=browser.current_url
time.sleep(2)
        
#assert current page is homepage

if base_url==current_url:
    print("görüntülenen sayfa ",current_url)
else:
    print("istenilen sayfada değilsiniz")
    
time.sleep(2)


#STEP 2
print("step 2")

#login
account_list = browser.find_element_by_xpath('//*[@id="nav-link-accountList"]')

hover(browser,account_list)

sign_in = None
while not sign_in:
    try:
        sign_in = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-flyout-ya-signin"]/a')))
    except NoSuchElementException:
        time.sleep(4)

hover(browser,sign_in)
time.sleep(3)
sign_in.click()

email = browser.find_element_by_name("email")
email.send_keys("") # you have to write email address for amazon account
time.sleep(2)
continue_button = browser.find_element_by_id("continue")
continue_button.click()

password = browser.find_element_by_name("password")
password.send_keys("") # you have to write password for amazon
time.sleep(3)

remember=browser.find_element_by_name("rememberMe")
remember.click()

sign_in_submit = browser.find_element_by_id("signInSubmit")
sign_in_submit.click()


#step 2.5 vertification code page 
if is_exist('//*[@id="continue"]')==False:
    print("devam edilebilir")
else:
    print("email e doğrulama kodu gönderiliyor")
    send_code=browser.find_element_by_xpath('//*[@id="continue"]')
    send_code.click()
    time.sleep(3)
    
    main_window=browser.window_handles[0]
    
    browser.execute_script("window.open('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=12&ct=1446228061&rver=6.4.6456.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fmail.live.com%2Fdefault.aspx&lc=1055&id=64855&mkt=tr-tr&cbcxt=mai', 'new_window')")

    tab_window=browser.window_handles[1]
    
    browser.switch_to_window(tab_window)

#enter email
    email_textbox=browser.find_element_by_name("loginfmt")
    email_textbox.click()
    email_textbox.send_keys("") # you have to write email address for microsoft account
    time.sleep(2)
    email_textbox.send_keys(Keys.ENTER)
#enter password
    password_textbox=browser.find_element_by_name("passwd")
    password_textbox.send_keys("") # you have to write password
    time.sleep(2)
#login to my account
    login_email = None
    while not login_email:
        try:
            login_email = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]')))
        except NoSuchElementException:
            time.sleep(4)

    login_email.click()
#find the vertification code
    numbers = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="x_verificationMsg"]/p[2]')))
    codes=numbers.text
    print(codes)

#switch to amazon page
    time.sleep(2)
    browser.switch_to_window(main_window)
    time.sleep(2)

#enter the vertification number
    verify=browser.find_element_by_xpath('//*[@id="cvf-page-content"]/div/div/div[1]/form/div[2]/input')
    verify.send_keys(codes)
    time.sleep(3)
    verify.send_keys(Keys.ENTER)   

    
#STEP 3
print("step 3")

#search samsung
input_element = browser.find_element_by_id("twotabsearchtextbox")
input_element.send_keys("samsung")
input_element.submit()
#input_element.clear()


#STEP 4
print("step 4")

#verify that results are found
if is_exist('//*[@id="noResultsTitle"]'):
    print("ilgili sonuç bulunamadı")
else:
    print("ilgili sonuçlar bulundu")
time.sleep(2)


#STEP 5
print("step 5")

#go to 2nd page
page2=browser.find_element_by_css_selector('#pagn > span:nth-child(3) > a')
page2.click()

print("2. arama sayfasındasınız", browser.current_url)
time.sleep(2)


#STEP 6
print("step 6")

#select 3rd product from 2nd page
product3=browser.find_element_by_xpath('//*[@id="result_18"]/div/div/div/div[2]/div[1]/div[1]/a')
time.sleep(3)
product3.click()
time.sleep(2)

#click dropdown
dropdown = None
while not dropdown:
    try:
        dropdown = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wishListDropDown"]')))
    except NoSuchElementException:
        time.sleep(7)

dropdown.click()
time.sleep(4)

#add to wish
add_to_wishlist = None
while not add_to_wishlist:
    try:
        add_to_wishlist = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="atwl-dd-ul"]/li[2]')))
    except NoSuchElementException:
        time.sleep(7)

hover(browser,add_to_wishlist)
time.sleep(4)
add_to_wishlist.click()
time.sleep(2)

browser.get(base_url)

time.sleep(3)


#STEP 7
print("step 7")

#hover over accountlist
account_list = browser.find_element_by_xpath('//*[@id="nav-link-accountList"]')
hover(browser,account_list) 

time.sleep(3)

wishlist_private = None
while not wishlist_private:
    try:
        wishlist_private = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-flyout-wl-items"]/div/a[3]')))
    except NoSuchElementException:
        time.sleep(4)

hover(browser,wishlist_private)

time.sleep(5)
wishlist_private.click()


#STEP 8
print("step 8")
time.sleep(4)

#check if it is added to wishlist (note:be more spesific)
if is_exist('//*[@id="no-items-section"]'):
    print("listeye eklenemedi...")
else:
    print("listeye eklendi...")


#STEP 9
print("step 9")

#delete it from wishlist
wishdelete=browser.find_element_by_css_selector('#a-autoid-7 > span > input')
wishdelete.click()
time.sleep(2)


#STEP 10
print("step 10")

#check if it is deleted (note:be more spesific)
browser.refresh()
time.sleep(2)
if is_exist('//*[@id="no-items-section"]'):
    print("listeden silindi")
else:
    print("listeden silinemedi")

time.sleep(5)
browser.quit()



    



