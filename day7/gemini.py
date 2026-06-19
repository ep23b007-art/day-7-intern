import asyncio
from app.integrations.gemini import GeminiClient

async def main():
    gemini = GeminiClient()

    trip_query = """
    I am planning a 3-day caravan trip from Hyderabad with 4 friends.
    Suggest a fun and budget-friendly TravelKeet style itinerary.
    """

    reply = await gemini.generate_reply(trip_query)

    print("Gemini Reply:")
    print(reply)

if __name__ == "__main__":
    asyncio.run(main())
    