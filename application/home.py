from fastapi import APIRouter

home = APIRouter()

@home.get("/", response_model=str)
async def homepage():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Logged In</title>
    </head>
    <body>
        <h1>You have logged in</h1>
        <p>Welcome to our website!</p>
    </body>
    </html>
    """
