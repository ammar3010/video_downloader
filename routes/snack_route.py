from helper import get_driver
from selenium.webdriver.common.by import By
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model import URL
import time

router = APIRouter()

@router.get("/snackdown")
async def snack_download(request: URL):
    try:
        driver = get_driver()
        driver.get("https://getsnackvideo.com/")
        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, "input.form-control.input-lg").send_keys(request.url)

        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.input-lg").click()
        time.sleep(5)

        thumbnail = driver.find_element(By.CSS_SELECTOR, "div.img_thumb").find_element(By.TAG_NAME, "img").get_attribute("src")
        video = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.download_link.without_watermark").get_attribute("href")

        response = {
            "thumbnail": thumbnail,
            "video": video
        }

        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")