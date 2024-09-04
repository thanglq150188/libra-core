import asyncio
from typing import List
from libra.messages import OpenAIMessage
from libra.types import ChatCompletionChunk

# Assuming AsyncLibraAgent is imported from the appropriate module
from libra.agents.async_libra_agent import AsyncLibraAgent

async def simulate_user(agent: AsyncLibraAgent, user_id: int):
    question = f"tổng giám đốc của MB là ai thế ?"
    messages: List[OpenAIMessage] = [
        {"role": "user", "content": question}
    ]

    print(f"User {user_id} sending question: {question}")

    async for chunk in agent.astep(messages=messages):
        pass

    print(f"\nUser {user_id} finished receiving response.")

async def simulate_ccu(num_users: int = 10):
    agent = AsyncLibraAgent()
    tasks = [simulate_user(agent, i) for i in range(num_users)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(simulate_ccu(50))