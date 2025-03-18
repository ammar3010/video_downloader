from helper import get_driver
from selenium.webdriver.common.by import By
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model import URL
import time

router = APIRouter()

@router.get("/twdown/")
async def tw_download(request: URL):
    try:
        driver = get_driver()
        driver.get("https://savetwitter.net/en")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "input.search__input").send_keys(request.url)

        driver.find_element(By.CSS_SELECTOR, "button.btn-red").click()
        time.sleep(10)
        url = driver.find_element(By.CSS_SELECTOR, "a.tw-button-dl.button.dl-success").get_attribute("href")

        return JSONResponse(content={"url": url}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")