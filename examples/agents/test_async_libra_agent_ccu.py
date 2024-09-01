import os
import asyncio
import sys
import time
from dotenv import load_dotenv
from libra.messages import OpenAIMessage
from libra.agents.async_libra_agent import AsyncLibraAgent  # Assuming this is the name of your file

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

async def process_stream(stream, user_id):
    full_response = ""
    token_count = 0
    async for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            print(f"User {user_id}: {content}", end="", flush=True)
            full_response += content
            token_count += len(content.split())  # Rough estimate of token count
    print(f"\n\nUser {user_id} Full response: {full_response}")
    return token_count

async def single_request(agent: AsyncLibraAgent, user_id: int):
    try:
        start_time = time.time()
        message: OpenAIMessage = {"role": "user", "content": f"các sếp lớn ở MB, ai lớn tuổi nhất"} # type: ignore
        stream = agent.astep(messages=[message])
        token_count = await process_stream(stream, user_id)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time, token_count
    except Exception as e:
        print(f"Error for user {user_id}: {str(e)}")
        return 0, 0

async def run_ccu_test(ccu: int = 100):
    agent = AsyncLibraAgent()
    start_time = time.time()
    tasks = [single_request(agent, i) for i in range(ccu)]
    results = await asyncio.gather(*tasks)
    end_time = time.time()

    total_time = end_time - start_time
    total_tokens = sum(result[1] for result in results)
    avg_tokens_per_second = total_tokens / total_time if total_time > 0 else 0
    avg_response_time = sum(result[0] for result in results) / len(results)

    print(f"\n\nCCU Test Results:")
    print(f"Number of users: {ccu}")
    print(f"Total test time: {total_time:.2f} seconds")
    print(f"Total tokens generated: {total_tokens}")
    print(f"Average response time: {avg_response_time:.2f} seconds")
    print(f"Average throughput: {avg_tokens_per_second:.2f} tokens/second")
    print(f"Requests per second: {ccu / total_time:.2f}")

if __name__ == "__main__":
    CCU = 100  # Concurrent Users
    asyncio.run(run_ccu_test(CCU))