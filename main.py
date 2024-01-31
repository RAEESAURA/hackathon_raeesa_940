import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Halo. Saya {bot.user}.')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'./{file_name}')
            await ctx.send(f'File telah disimpan di=./{file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)
            
            if hasil[0] == 'Organik\n' and hasil[1] >= 0.9:
                await ctx.send('Ini sampah organik. Sampah organik adalah sampah yang berasal dari bahan-bahan hayati. Sampah ini dapat didegradasi oleh mikroba atau memiliki sifat biodegradable. Sampah ini dengan mudah dapat terurai melalui proses alami. Kebanyakan sampah organik berasal dari sampah rumah tangga.')
            elif hasil[0] == 'Anorganik\n' and hasil[1] <= 0.9:
                await ctx.send('ini sampah anorganik. Sampah anorganik adalah sampah yang berasal dari bahan-bahan nonhayati, baik itu produk sintetis, maupun hasil dari proses teknologi pengolahan bahan tambang. Bentuk sampah ini bisa berupa logam, plastik, kertas, kaca, keramik, dan detergen. Kebanyakan sampah anorganik tidak dapat terurai oleh mikroorganisme secara keseluruhan. Sebagian sampah anorganik dapat terurai, namun dalam waktu yang sangat lama.')
            else:
                await ctx.send('Ini gambar apaan?')
    else:
        await ctx.send('Mana file yang dikirim?')

bot.run("MTEwMzk4MzA3NTE4MTk5ODE0MQ.GyvvKJ.L4rq0deCK22DVcLVQ-G10vQXUP3Ts-9zAOGSew")
