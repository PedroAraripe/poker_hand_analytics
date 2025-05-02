from fastapi import FastAPI
from routes.hand_analysis import router as hand_analysis_router

app = FastAPI()

# Registra as rotas do módulo routes/hand_analysis.py
app.include_router(hand_analysis_router)