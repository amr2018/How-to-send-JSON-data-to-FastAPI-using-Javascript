
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/signup')
def view_signup():
    return HTMLResponse(open('index.html', 'r').read())

@app.post('/api/signup')
async def signup(request : Request):
    data = await request.json()
    print(data['email'])
