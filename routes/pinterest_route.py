from helper import get_driver
from selenium.webdriver.common.by import By
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model import URL
import time

router = APIRouter()

@router.get("/pindown/")
async def pin_download(request: URL):
    try:
        driver = get_driver()
        driver.get("https://www.savepin.app")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "input.input.url-input").send_keys(request.url)
        driver.find_element(By.CSS_SELECTOR, "button.button.button-go").click()
        title = driver.find_element(By.CSS_SELECTOR, "div.table-container").find_element(By.TAG_NAME, "h1").text
        video_elements = driver.find_elements(By.CSS_SELECTOR, "a.button.is-success.is-small")
        video = video_elements[0].get_attribute("href")
        thumbnail = video_elements[1].get_attribute("href")

        response = {
            "title": title,
            "video": video,
            "thumbnail": thumbnail
        }

        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")