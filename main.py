from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# temp vars, these are based on user inputs
marital_status = False
head_of_household = False
age = 19
income = 20000
federal_witholdings = 0
state_witholdings = 0


# Initiate the driver
# This chrome driver is compatible with windows and chrome version 107
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.hrblock.com/tax-calculator/')  # visits hrblock's dynamic tax calculator

driver.implicitly_wait(1)  # wait 1 second for page to load before clicking between each new page

# All finds are done on xpath, the full HTML path to an element
# Step 1: Press "Calculate Refund" button
driver.find_element(By.XPATH, "/html/body/main/div/section[1]/div/div/div[1]/div/div[2]/a").click()

driver.implicitly_wait(1)

# Step 2: Select marital status
if not marital_status:  # single
    driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                                  "div[2]/div/div/div/lib-marital-status/div[1]/ul/li[1]/label").click()
else:  # married
    driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                                  "div[2]/div/div/div/lib-marital-status/div[1]/ul/li[2]/label").click()

# Step 3: Press "Next" button -> head of household question
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/lib-marital-status/div[2]/div/div/a").click()

driver.implicitly_wait(1)

# Step 4: Select head of household status
if head_of_household:
    driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                                  "div[2]/div/div/div/app-head-of-household/div[1]/ul/li[1]/label").click()
else:
    driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                                  "div[2]/div/div/div/app-head-of-household/div[1]/ul/li[2]/label").click()

# Step 5: Press "Next" button -> age question
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-head-of-household/div[2]/div/div/button[1]").click()

driver.implicitly_wait(1)

# Step 6: Input age
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-tp-age/div[1]/div[2]/input").send_keys(age)

# Step 7: Press "Next" button -> W-2s
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-tp-age/div[2]/div/div/button[1]").click()

driver.implicitly_wait(1)

# Step 8: Press "No" for W-2's since plan.me won't take W-2 data
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-w2-status/div[1]/ul/li[2]/label").click()

# Step 9: Press "Next" button -> wages question
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-w2-status/div[2]/div/div/button[1]").click()

driver.implicitly_wait(1)

# Step 10: Input income
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-tp-wages/div[1]/div[2]/input").send_keys(income)

# Step 11: Press "Next" button -> witholdings question
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-tp-wages/div[2]/div/div/button[1]").click()

driver.implicitly_wait(1)

# Step 12: Input federal witholdings
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/div[2]/"
                              "div/div/div/app-tp-emp-fed-state-withheld/div[1]/div[2]/input").send_keys(federal_witholdings)

# Step 13: Input state witholdings
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/div[2]/"
                              "div/div/div/app-tp-emp-fed-state-withheld/div[1]/div[3]/input").send_keys(state_witholdings)

# Step 14: Press "Next" button -> receive estimated tax results
driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/form/div/"
                              "div[2]/div/div/div/app-tp-emp-fed-state-withheld/div[2]/div/div/button[1]").click()

# Step 15: Fetch estimated tax owed
estimated_tax = driver.find_element(By.XPATH, "/html/body/main/div/tax-calculator/div/div/div/section/app-wrapper/"
                                              "form/div/div[2]/div/div/div/app-estimation/div[1]/div/h1[2]").text

print(estimated_tax)
