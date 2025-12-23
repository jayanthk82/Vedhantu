import motor.motor_asyncio # type: ignore

MONGO_DETAILS = "mongodb://admin:password123@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.vendhanthuDB

note_collection = database.get_collection('notes')