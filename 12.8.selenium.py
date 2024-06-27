from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://cn.bing.com/')

try:
    elem = browser.find_element('#est_switch')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
