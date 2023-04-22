from fastapi import APIRouter, Response
import requests

router = APIRouter()

@router.get("/logo")
async def get_logo():
    # Fetch the SVG logo from a URL
    response = requests.get("https://firebasestorage.googleapis.com/v0/b/fir-test-92d5e.appspot.com/o/Logo.svg?alt=media&token=4fd9b64e-01b5-4e3f-a41e-7eb4134265f7")
    logo_svg = response.content
    
    # Return the SVG with appropriate headers
    return Response(content=logo_svg, media_type="image/svg+xml")