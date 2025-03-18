from helper import get_driver
from selenium.webdriver.common.by import By
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model import URL
import time

router = APIRouter()

@router.get("/fbdown/")
async def fb_downloader(request: URL):
    try:
        driver = get_driver()
        driver.get("https://snapsave.app/")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "input.input.input-url").send_keys(request.url)
        driver.find_element(By.CSS_SELECTOR, "button.button.is-download").click()
        time.sleep(5)
        video = driver.find_element(By.CSS_SELECTOR, "a.button.is-success.is-small").get_attribute("href")
        thumbnail = driver.find_element(By.CSS_SELECTOR, "p.image.is-64x64").find_element(By.TAG_NAME, "img").get_attribute("src")
        
        response = {
            "video": video,
            "thumbnail": thumbnail
        }

        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")