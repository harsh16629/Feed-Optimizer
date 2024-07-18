import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
    #credentials for yt account
    username = "dummywummy10@gmail.com"
    password = "Lmfaook@69!"
    
    #search term given by user
    search_term = "carti"

    #opening youtube
    browser = uc.Chrome()
    browser.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253FthemeRefresh%253D1&ec=65620&hl=en&ifkv=AdF4I76vdWkVZquOHr7odzb5wZDR4Y7BayUAAQIVsIe5YxROaQCkwrNN7JycVeecZawMwH9vlaBmhg&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1073761228%3A1721146017292480&ddm=0')
    browser.maximize_window()

    #youtube sign-in
    browser.find_element(By.CSS_SELECTOR, '#identifierId').send_keys(username)
    browser.find_element(By.CSS_SELECTOR, '#identifierNext > div > button > span').click()
    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')))
    browser.find_element(By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys(password)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()
    
    #youtube searching
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.NAME, "search_query")))
    browser.find_element(By.NAME, "search_query").send_keys(search_term)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "search-icon-legacy"))).click()
    browser.find_element(By.ID, "search-icon-legacy").click()
    
    #collecting all the urls on the page
    anchor_links = browser.find_elements(By.TAG_NAME, 'a')
    all_links = []
    for anchor_link in anchor_links:
        all_links.append(anchor_link.get_attribute('href'))
    #fitering out bad links
    valid_links = []
    for link in all_links:
        if isinstance(link, str):
            valid_links.append(link)
    #collecting video links
    clickable_links = []
    for valid_link in valid_links:
        if '/watch?v=' in valid_link:
            clickable_links.append(valid_link)
    for url in range(10):
        browser.get(f"{url}")
        time.sleep(15)
    #going back to the yt homepage to check for resulting feed
    browser.find_element(By.CSS_SELECTOR, '#logo-icon > yt-icon-shape > icon-shape').click()