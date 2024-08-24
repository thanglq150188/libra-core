from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import AsyncGenerator
import httpx
import asyncio
 
 
# Access environment variables
API_KEY = "dc0a9af7732c92a4d1e08cc5e8baf9adb282dfb6d0540c76e1b1cf52c7c72f28"
app = FastAPI()
 
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, you can restrict it to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
 
async def external_streaming_request(payload: dict) -> AsyncGenerator[str, None]:
    async with httpx.AsyncClient() as client:
        # Use the `httpx.AsyncClient.stream` method for streaming requests
        async with client.stream(
            'POST',
            url= "https://api.together.xyz/v1/chat/completions",  # API endpoint
            headers={'Authorization': f'Bearer {API_KEY}'},  # API key
            json=payload
        ) as response:
            async for chunk in response.aiter_raw():
                print(chunk)
                yield chunk.decode('utf-8')
 
@app.post("/v1/chat/completions")
async def stream_text(request: Request):
    payload = await request.json()
    # Validate the payload format if needed
    return StreamingResponse(external_streaming_request(payload), media_type="text/event-stream")
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)