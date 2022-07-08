from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

KEYWORD = "buy domain"

drivers = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
drivers.get("https://google.com")

search_bar = drivers.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = drivers.find_elements(By.CLASS_NAME, "g")

for index, search_result in enumerate(search_results):
    class_name = search_result.get_attribute("class")
    search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
    # if "Ww4FFb tF2Cxc" not in class_name:
    #     search_result.screenshot(f"screenshot/{KEYWORD}x{index}.png")
