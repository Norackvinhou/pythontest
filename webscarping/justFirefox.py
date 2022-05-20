from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://google.com')
# elem = browser.find_element_by_css_selector('.super-title > a:nth-child(1)')
# elem.click()

#find div element
# elem = browser.find_elements_by_css_selector('div')
# print(len(elem))

search = browser.find_element_by_css_selector('.gLFyf')
# search.click()
search.send_keys('Khmer')
search.submit()

#syntax for closing browser
browser.quit()
