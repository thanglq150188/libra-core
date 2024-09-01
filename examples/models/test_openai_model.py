import os
import asyncio
import sys
from openai import AsyncOpenAI
from dotenv import load_dotenv
from libra.models import OpenAIModel
from libra.types import ModelLabel

load_dotenv(override=True)

def set_event_loop_policy():
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    else:
        print(f"Unsupported platform: {sys.platform}")
        sys.exit(1)

set_event_loop_policy()

model = OpenAIModel(
    model_label=ModelLabel.GPT_4o_mini,
    model_config_dict={
        "temperature": 0.0,
        "stream": True
    }
)

async def main() -> None:
    stream = await model.run_async(messages=[
        {
            "role": "user",
            "content": "tại sao tôi lại phải chịu nỗi đau nèi",
        }
    ])

    async for chunk in stream: # type: ignore
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()  # Add a newline at the end

if __name__ == "__main__":
    asyncio.run(main())