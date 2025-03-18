from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.dailymotion_route import router as dm_route
from routes.instagram_route import router as ig_route
from routes.pinterest_route import router as pin_route
from routes.snack_route import router as snack_route
from routes.tiktok_route import router as tk_route
from routes.twitter_route import router as tw_route
from routes.facebook_route import router as fb_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dm_route)
app.include_router(ig_route)
app.include_router(pin_route)
app.include_router(snack_route)
app.include_router(tk_route)
app.include_router(tw_route)
app.include_router(fb_route)