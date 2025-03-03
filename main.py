from fastapi import FastAPI, requests , APIRouter
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
router = APIRouter()

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


@router.get("/")
async def home_page():
    html = f'''
        <html>
            <body>
                <p>"Home page"</p>
            </body>
        </html>
        '''
    return HTMLResponse(html)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1',  port=80)