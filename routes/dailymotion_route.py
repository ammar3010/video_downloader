from helper import get_driver
from selenium.webdriver.common.by import By
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model import URL
import time

router = APIRouter()

@router.get("/dmdown/")
async def dm_downloader(request: URL):
    try:
        driver = get_driver()
        driver.get("https://dmvideo.download/")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "input.form-control.form-control-lg.form-control-alternative").send_keys(request.url)
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-danger.g-recaptcha").click()
        time.sleep(5)
        video = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-sm.btn-danger.shadow").get_attribute("href")
        thumbnail = driver.find_element(By.CSS_SELECTOR, "img.img.img-fluid.mb-3").get_attribute("src")
        title = driver.find_element(By.CSS_SELECTOR, "h2.mb-3").text

        response = {
            "video": video,
            "thumbnail": thumbnail,
            "title": title
        }

        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")