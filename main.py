from fastapi import FastAPI
from routes.hand_analysis import router as hand_analysis_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Defina aqui os domínios que podem acessar sua API
origins = [
    "http://localhost",
    "http://localhost:3000",  # frontend local
    "https://meusite.com",    # domínio em produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas do módulo routes/hand_analysis.py
app.include_router(hand_analysis_router)