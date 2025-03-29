


from fastapi import APIRouter

router = APIRouter()


@router.get("/deploy")
async def deploy():
    return {"message": "Deployed"}