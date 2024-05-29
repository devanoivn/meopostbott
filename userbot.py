from telethon import TelegramClient, events

api_id = '26167827'
api_hash = '56156da681f90d4fd030754e30024b29'

source_channel = -1002188392090  # Ganti dengan ID channel Anda
target_groups = [-1001512107471, -1002017144201, -1001305600099, -1001704887478, -1001206618963, -1001630737216, -1002037882706, -1001655590359, -1001965994500, -1002080290525, -1001977205543, -1001502298591, -1002115426574, -1001942497629, -1001518363166, -1002099000872, -1001561634565, -1001803649521, -1002108171068, -1001801158176, -1001553897176, -1001524934070, -1001742737823, -1001736428304, -1001633749647, -1001770048665, -1002006943988, -1001949785056, -1001620066848, -1001267977953, -1001827340445, -1002094087505, -1001690543893, -1002089403369, -1001884854496, -1001545068794, -1001517341344, -1001959085903, -1001935407874, -1001554343519, -1001610912474, -1001753719175, -1001636255192]  # Ganti dengan ID grup tujuan

async def forward_message(event):
    if event.chat_id == source_channel:
        for group_id in target_groups:
            await event.forward_to(group_id)

async def main():
    async with TelegramClient('userbot_session', api_id, api_hash) as client:
        client.add_event_handler(forward_message, events.NewMessage)

        await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
