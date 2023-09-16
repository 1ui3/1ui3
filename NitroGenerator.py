# Import above your code ! (for interaction)
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)







# Main Code ! Generate Discord Nitro Link | @1ui3
@bot.tree.command(name="nitro", description="Generate Discord Nitro 🎉")
async def nitro(interaction:discord.Interaction):
    nitro_code = 'https://discord.gift/' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=16))
    await interaction.response.send_message(interaction.user.mention , nitro_code)
