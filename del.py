from pyrogram import Client
from pyrogram.sessions import StringSession

api_id = 23212132
api_hash = "1c17efa86bdef8f806ed70e81b473c20"
string = (
    "BQFiMGQAhf4JrlOx0d230td4NFd5nlerbkQkVEMJIpYR974l2sOL8883iFRY_ijV_taYcsF9D_y6GdxpFad90Wo6QjUPuqMfVvlvS3nckX_mwz0LtJ2hK2i1yAabE4WOD9QnFiT4hp4NfhqQrxpX4zlEziRdBwWft"
    "-O3WE4kWw-6uxiGSrUAVoqOJKUXOZEMwu8PNshf4MPiaPZuPywlkBLa4nexI1vjqtQwX0w48XZVX3eXIHPlREw-xfH3ojJk6Z8rkSWj7rmRL7LGckpTTu3NQiQYZ8aocMYQylxiwyyuf1WqGHgzcXS6PXyV4qzZlZBMxEZLIZk9PYDC_WMj2pqn-wD-TgAAAAHQsVyNAA"
)

app = Client(StringSession(string), api_id, api_hash)

async def delete_session():
    async with app:
        await app.log_out()
        print("✅ String session destroyed and logged out successfully.")

app.run(delete_session())
