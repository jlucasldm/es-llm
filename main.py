from blood import Blood
import asyncio


async def main():
    blood = Blood(model="gpt-4o-mini", max_tokens=5000, temperature=0)
    await blood.process_questions()


if __name__ == "__main__":
    asyncio.run(main())
