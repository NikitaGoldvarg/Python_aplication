from fastapi import FastAPI, requests , APIRouter
from fastapi.responses import HTMLResponse
app = FastAPI()
router = APIRouter

@router.get("/{url}")
async def read_users( url):
    html = f'''
        <html>
            <body>
                <p>{url}.</p>
            </body>
        </html>
        '''
    return HTMLResponse(html)

app.include_router(router)