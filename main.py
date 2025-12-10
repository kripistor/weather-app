from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import requests

app = FastAPI()


REQUESTS = Counter('app_requests_total', 'Total requests to /weather endpoint')

@app.get("/weather")
def get_weather():
    REQUESTS.inc()  
    latitude = 55.7558
    longitude = 37.6176

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    response = requests.get(url)
    data = response.json()

    return {
        "temperature": data["current_weather"]["temperature"],
    }

@app.get("/")
def root():
    return {"message": "Weather API running"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
