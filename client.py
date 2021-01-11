import discord


class TaskClient(discord.Client):
    async def on_ready(self):
        print(f"Logged as {self.user}")
