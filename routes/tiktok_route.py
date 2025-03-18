from helper import get_driver
from selenium.webdriver.common.by import By
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model import URL
import time

router = APIRouter()

@router.get("/ttkdown/")
async def ttk_download(request: URL):
    try:
        driver = get_driver()
        driver.get("https://tmate.cc/")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(request.url)
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-success").click()
        time.sleep(8)

        video_nowatermark = driver.find_elements(By.CSS_SELECTOR, "a.abutton.is-success.is-fullwidth")[0].get_attribute("href")
        video_watermark = driver.find_elements(By.CSS_SELECTOR, "a.abutton.is-success.is-fullwidth")[2].get_attribute("href")
        thumbnail = driver.find_element(By.CSS_SELECTOR, "div.downtmate-left.left").find_element(By.TAG_NAME, "img").get_attribute("src")
        title = driver.find_element(By.CSS_SELECTOR, "a.hover-underline").text

        response = {
            "video_nowatermark": video_nowatermark,
            "video_watermark": video_watermark,
            "thumbnail": thumbnail,
            "title": title
        }

        return JSONResponse(content=response, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")