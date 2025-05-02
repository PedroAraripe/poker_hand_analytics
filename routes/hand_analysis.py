from fastapi import APIRouter, HTTPException, Query
from services.service_hand_analysis_synthethic import analyze_hand

router = APIRouter()

@router.get("/analysis/hand")
def get_poker_analysis(player_current_hand: str = Query(..., min_length=1)):
    try:
        return analyze_hand(player_current_hand)
    except KeyError:
        raise HTTPException(status_code=400, detail="Categoria de mão inválida")