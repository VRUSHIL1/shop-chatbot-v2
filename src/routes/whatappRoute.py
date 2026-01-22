from fastapi import APIRouter,Request
from controllers.whatappController import handle_whatsapp_webhook

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    return await handle_whatsapp_webhook(request)
