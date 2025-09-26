from fastapi import APIRouter

# NOTE: tag
router = APIRouter(prefix="/items")


@router.get("")
async def get_items():
    return "An item"
