import asyncio
import json
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


from bs4 import BeautifulSoup

result_ = {}
load_dotenv()
path_to_driver = os.getenv("DRIVER_PATH")


async def async_search(name, count):
    options = Options()
    options.add_argument("--headless")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55")
    caps = webdriver.DesiredCapabilities.EDGE
    s = Service(
        path_to_driver)
    driver = webdriver.Edge(
        service=s,
        options=options,
        capabilities=caps
    )
    driver.get("https://www.google.ru/search?q=nature&tbm=isch&ved=2ahUKEwiFpYO-iob-AhXQuCoKHYS-B1QQ2-cCegQIABAA&oq=nature&gs_lcp=CgNpbWcQAzIFCAAQgAQyCAgAEIAEELEDMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6BwgAEIoFEEM6BwgjEOoCECc6CwgAEIAEELEDEIMBOggIABCxAxCDAToKCAAQigUQsQMQQ1DeA1jqFGCTFWgBcAB4AIABfIgB6wSSAQM2LjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=VMYmZIWrBtDxqgGE_Z6gBQ&bih=746&biw=1536")
    url_images = []
    search_label = driver.find_element(By.TAG_NAME, 'input')
    search_label.click()
    search_label.clear()
    search_label.send_keys(name)
    press_search_but = driver.find_element(By.TAG_NAME, 'button')
    press_search_but.click()
    for i in range(1, count+1):
        image_block = driver.find_element(
            By.XPATH, f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{i}]/a[1]')
        image_block.click()
        await asyncio.sleep(1)
        soup = BeautifulSoup(driver.page_source, "lxml")
        img_urls = soup.find_all(
            'a', attrs={'aria-label': True, 'role': True, 'rel': True})
        for img_url in img_urls:
            img = img_url.find('img')
            try:
                if len(img['src']) < 400:
                    url_images.append(img['src'])
                    break
            except Exception as exc:
                pass
    result_[name] = url_images
    driver.close()


async def result(names, count):

    tasks = []
    for name in names:
        tasks.append(asyncio.create_task(async_search(name, count)))

    for task in tasks:
        await task

    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(result_, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    asyncio.run(result(['Максим', 'Денис', 'Гриша'], 5))
