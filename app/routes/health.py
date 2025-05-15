from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/check")
async def health_check():
    return {"status": "healthy"}

@router.get("/square/{number}")
async def calculate_square(number: int):
    return {"number": number, "square": number ** 2}