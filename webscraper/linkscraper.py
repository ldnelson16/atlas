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

#chrome options for wd
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

#path to chromedriver
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

#create webdriver
driver = webdriver.Chrome(service=webdriver_service,options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://atlas.ai.umich.edu")
time.sleep(40)
driver.get("https://atlas.ai.umich.edu/courses/")
flag=False
results = {}
j=1
missed = 0
hit = 0
while True:
  try: 
    driver.get("https://atlas.ai.umich.edu/courses/?page="+str(j))
    try: 
      el1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[1]/div/p")
      print("Got element")
      print(el1.text,type(el1.text))
      if "No Results. Try adjusting your selected" in el1.text:
        print("Ended")
        break
    except: 
      pass
    j+=1
    for i in range(1,33):
      try:
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/div["+str(i)+"]/a")
        href = element.get_attribute("href")
        print(href)
        print(element.text)
        results[element.text] = {"Link":href,"Class Title":None,"Cross-References":[],"Median Grade":None,"Credits":None,"Desire to Take":None,"Understanding":None,"Workload":None,"Expectations":None,"Increased Interest":None}
        hit+=1
        print(missed)
      except: 
        missed+=1
        print(missed,"in except")
  except: 
    pass

file_path = "webscraper/data/atlasdict.json"
with open(file_path, 'w') as json_file:
    json.dump(results, json_file,indent=2)
print("Finished scraping ATLAS for links, collected",hit,"links and missed",missed,"links.")
print("Data was stored in",file_path)
driver.close()

