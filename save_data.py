from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# use Firefox
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

# access JP canada
top_page = "https://www.jpcanada.com/"
browser.get(top_page)

# find jobpage url
click_jobpage = browser.find_element_by_css_selector("#bbs-area > div > div > div:nth-child(2) > div:nth-child(4) > a:nth-child(4)")
click_jobpage.click()

# load wait
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "bbs-title")))

# access jobpage
jobpage_element  = browser.find_element_by_css_selector("body > footer > ul > li:nth-child(1) > a")
jobpage_url = jobpage_element.get_attribute('href')
browser.get(jobpage_url)
