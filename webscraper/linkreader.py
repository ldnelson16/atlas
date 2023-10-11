import json
import time
import os

#selenium
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

#read in links json
file_path = "webscraper/data/atlasdict.json"
with open(file_path, 'r') as json_file:
  results = json.load(json_file)

#chrome options for wd
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")

#path to chromedriver
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

#create webdriver
driver = webdriver.Chrome(service=webdriver_service,options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://atlas.ai.umich.edu")
time.sleep(40) # time to get logged in with duo

for key in results:
  try:
    driver.get(results[key]["Link"])
    title=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[1]/h2").text
    results[key]["Class Title"]=title
    credits=float(driver.find_element(By.XPATH,'//*[@id="credits"]/p').text[9:])
    results[key]["Credits"]=credits
    mediangrade=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div/p[1]/span").text
    results[key]["Median Grade"] = mediangrade
    desire=int(driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[1]/div[1]/h5").text[:-1])
    results[key]["Desire to Take"] = desire
    understanding=int(driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[2]/div[1]/h5").text[:-1])
    results[key]["Understanding"] = understanding
    workload=int(driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/h5").text[:-1])
    results[key]["Workload"] = workload
    expectations=int(driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[4]/div[1]/h5").text[:-1])
    results[key]["Expectations"] = expectations
    interest=int(driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div[5]/div[1]/h5").text[:-1])
    results[key]["Increased Interest"] = interest
  except: 
    print("Couldn't find all values for",key)
    pass

driver.close()

file_path = "webscraper/data/atlasdict.json"
with open(file_path, 'w') as json_file:
    json.dump(results, json_file,indent=2)
print("Finished adding information from links.")
print("Data was stored in",file_path)
