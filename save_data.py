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

# take job info
for n in range(3, 11, 2):
    for i in range(1, 14):
        job_info = browser.find_elements_by_css_selector("#bbs-table > div:nth-child({}) > div:nth-child({}) > div.divTableCell.col4 > a".format(n, i))
        if n == 9 and i >= 12:
            break
        for info in job_info:
            job_url = info.get_attribute('href')
            job_title = info.text
            print("title:", job_title, "link:", job_url)
