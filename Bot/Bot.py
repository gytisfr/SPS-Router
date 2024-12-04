import discord, requests, json, io
from discord.ext import commands

from Imager import main as getImages

myid = 301014178703998987 #Creator's ID

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command("help")
tree = client.tree

class Colours:
    class Brand:
        darkBlue = 0x005A9D
        lightBlue = 0x3399D5
        yellow = 0xE8D568
        white = 0xFFFFFF
        #change
    class Logs:
        red = 0xe96c6c #very bad
        orange = 0xd18f5d #bad
        yellow = 0xe5e07a #eh
        purple = 0xa18ad1 #neutral
        green = 0x6bc96b #good

@client.event
async def on_ready():
    print(f"SPS Router now online with {round(client.latency * 1000)}ms ping.")

@tree.command(name="route", description="Create a route")
async def route(interaction : discord.Interaction):
    class CyrusHouses(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.values = []

        @discord.ui.select(placeholder="Select", min_values=0, max_values=15, options=[
            discord.SelectOption(label="1 Cyrus Acres, Milton", value=1, description=None, emoji=None, default=False),
            discord.SelectOption(label="2 Cyrus Acres, Milton", value=2, description=None, emoji=None, default=False),
            discord.SelectOption(label="3 Cyrus Acres, Milton", value=3, description=None, emoji=None, default=False),
            discord.SelectOption(label="4 Cyrus Acres, Milton", value=4, description=None, emoji=None, default=False),
            discord.SelectOption(label="5 Cyrus Acres, Milton", value=5, description=None, emoji=None, default=False),
            discord.SelectOption(label="6 Cyrus Acres, Milton", value=6, description=None, emoji=None, default=False),
            discord.SelectOption(label="7 Cyrus Acres, Milton", value=7, description=None, emoji=None, default=False),
            discord.SelectOption(label="8 Cyrus Acres, Milton", value=8, description=None, emoji=None, default=False),
            discord.SelectOption(label="9 Cyrus Acres, Milton", value=9, description=None, emoji=None, default=False),
            discord.SelectOption(label="10 Cyrus Acres, Milton", value=10, description=None, emoji=None, default=False),
            discord.SelectOption(label="11 Cyrus Acres, Milton", value=11, description=None, emoji=None, default=False),
            discord.SelectOption(label="12 Cyrus Acres, Milton", value=12, description=None, emoji=None, default=False),
            discord.SelectOption(label="13 Cyrus Acres, Milton", value=13, description=None, emoji=None, default=False),
            discord.SelectOption(label="14 Cyrus Acres, Milton", value=14, description=None, emoji=None, default=False),
            discord.SelectOption(label="15 Cyrus Acres, Milton", value=15, description=None, emoji=None, default=False),
            discord.SelectOption(label="None", value=0, description=None, emoji=None, default=False)
        ], disabled=False, row=None)
        async def select_callback(self, interaction, select):
            self.values = select.values
            self.stop()
    
    #@discord.ui.button(style=discord.ButtonStyle.green, label="Submit", emoji="✖")

    class OaklandHouses(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.values = []
        
        @discord.ui.select(placeholder="Select", min_values=0, max_values=15, options=[
            discord.SelectOption(label="950 Dana St, Oakland", value=950, description=None, emoji=None, default=False),
            discord.SelectOption(label="975 Alma Way, Oakland", value=975, description=None, emoji=None, default=False),
            discord.SelectOption(label="1000 Alma Way, Oakland", value=1000, description=None, emoji=None, default=False),
            discord.SelectOption(label="1025 Menlo St, Oakland", value=1025, description=None, emoji=None, default=False),
            discord.SelectOption(label="1050 Menlo St, Oakland", value=1050, description=None, emoji=None, default=False),
            discord.SelectOption(label="1075 Menlo St, Oakland", value=1075, description=None, emoji=None, default=False),
            discord.SelectOption(label="1100 Menlo St, Oakland", value=1100, description=None, emoji=None, default=False),
            discord.SelectOption(label="1125 Menlo St, Oakland", value=1125, description=None, emoji=None, default=False),
            discord.SelectOption(label="1150 Menlo St, Oakland", value=1150, description=None, emoji=None, default=False),
            discord.SelectOption(label="1175 Menlo St, Oakland", value=1175, description=None, emoji=None, default=False),
            discord.SelectOption(label="1200 Menlo St, Oakland", value=1200, description=None, emoji=None, default=False),
            discord.SelectOption(label="1225 Menlo St, Oakland", value=1225, description=None, emoji=None, default=False),
            discord.SelectOption(label="1250 Rodgers Rd, Oakland", value=1250, description=None, emoji=None, default=False),
            discord.SelectOption(label="1275 Rodgers Rd, Oakland", value=1275, description=None, emoji=None, default=False),
            discord.SelectOption(label="1300 Rodgers Rd, Oakland", value=1300, description=None, emoji=None, default=False),
            discord.SelectOption(label="1325 Rodgers Rd, Oakland", value=1325, description=None, emoji=None, default=False),
            discord.SelectOption(label="1350 Rodgers Rd, Oakland", value=1350, description=None, emoji=None, default=False),
            discord.SelectOption(label="1375 Rodgers Rd, Oakland", value=1375, description=None, emoji=None, default=False),
            discord.SelectOption(label="1400 Belgrade Rd, Oakland", value=1400, description=None, emoji=None, default=False),
            discord.SelectOption(label="1425 Belgrade Rd, Oakland", value=1425, description=None, emoji=None, default=False),
            discord.SelectOption(label="1450 Belgrade Rd, Oakland", value=1450, description=None, emoji=None, default=False),
            discord.SelectOption(label="1475 Belgrade Rd, Oakland", value=1475, description=None, emoji=None, default=False),
            discord.SelectOption(label="1500 Belgrade Rd, Oakland", value=1500, description=None, emoji=None, default=False),
            discord.SelectOption(label="1525 Belgrade Rd, Oakland", value=1525, description=None, emoji=None, default=False),
            discord.SelectOption(label="None", value=0, description=None, emoji=None, default=False)
        ], disabled=False, row=None)
        async def select_callback(self, interaction, select):
            self.values = select.values
            self.stop()

    class OaklandHouses2(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.values = []
        
        @discord.ui.select(placeholder="Select", min_values=0, max_values=7, options=[
            discord.SelectOption(label="1550 Belgrade Rd, Oakland", value=1550, description=None, emoji=None, default=False),
            discord.SelectOption(label="1575 Belgrade Rd, Oakland", value=1575, description=None, emoji=None, default=False),
            discord.SelectOption(label="1600 Belgrade Rd, Oakland", value=1600, description=None, emoji=None, default=False),
            discord.SelectOption(label="1625 Belgrade Rd, Oakland", value=1625, description=None, emoji=None, default=False),
            discord.SelectOption(label="1650 Belgrade Rd, Oakland", value=1650, description=None, emoji=None, default=False),
            discord.SelectOption(label="1675 Belgrade Rd, Oakland", value=1675, description=None, emoji=None, default=False),
            discord.SelectOption(label="1700 Belgrade Rd, Oakland", value=1700, description=None, emoji=None, default=False),
            discord.SelectOption(label="None", value=0, description=None, emoji=None, default=False)
        ], disabled=False, row=None)
        async def select_callback(self, interaction, select):
            self.values = select.values
            self.stop()

    class PalmerHouses(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.values = []
        
        @discord.ui.select(placeholder="Select", min_values=0, max_values=15, options=[
            discord.SelectOption(label="1A Altee Rd, Palmer", value="RA1", description=None, emoji=None, default=False),
            discord.SelectOption(label="2A Altee Rd, Palmer", value="RA2", description=None, emoji=None, default=False),
            discord.SelectOption(label="3A Altee Rd, Palmer", value="RA3", description=None, emoji=None, default=False),
            discord.SelectOption(label="4A Altee Rd, Palmer", value="RA4", description=None, emoji=None, default=False),
            discord.SelectOption(label="5A Altee Rd, Palmer", value="RA5", description=None, emoji=None, default=False),
            discord.SelectOption(label="6A Altee Rd, Palmer", value="RA6", description=None, emoji=None, default=False),
            discord.SelectOption(label="1B Altee Rd, Palmer", value="RB1", description=None, emoji=None, default=False),
            discord.SelectOption(label="2B Altee Rd, Palmer", value="RB2", description=None, emoji=None, default=False),
            discord.SelectOption(label="3B Altee Rd, Palmer", value="RB3", description=None, emoji=None, default=False),
            discord.SelectOption(label="4B Altee Rd, Palmer", value="RB4", description=None, emoji=None, default=False),
            discord.SelectOption(label="5B Altee Rd, Palmer", value="RB5", description=None, emoji=None, default=False),
            discord.SelectOption(label="6B Altee Rd, Palmer", value="RB6", description=None, emoji=None, default=False),
            discord.SelectOption(label="1A Palm View, Palmer", value="SA1", description=None, emoji=None, default=False),
            discord.SelectOption(label="2A Palm View, Palmer", value="SA2", description=None, emoji=None, default=False),
            discord.SelectOption(label="1B Palm View, Palmer", value="SB1", description=None, emoji=None, default=False),
            discord.SelectOption(label="2B Palm View, Palmer", value="SB2", description=None, emoji=None, default=False),
            discord.SelectOption(label="None", value=0, description=None, emoji=None, default=False)
        ], disabled=False, row=None)
        async def select_callback(self, interaction, select):
            self.values = select.values
            self.stop()

    class SterlingHouses(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.values = []
        
        @discord.ui.select(placeholder="Select", min_values=0, max_values=15, options=[
            discord.SelectOption(label="3200 Majellan Way, Sterling Heights", value=3200, description=None, emoji=None, default=False),
            discord.SelectOption(label="3250 Majellan Way, Sterling Heights", value=3250, description=None, emoji=None, default=False),
            discord.SelectOption(label="3300 Majellan Way, Sterling Heights", value=3300, description=None, emoji=None, default=False),
            discord.SelectOption(label="3350 Majellan Way, Sterling Heights", value=3350, description=None, emoji=None, default=False),
            discord.SelectOption(label="3400 Majellan Way, Sterling Heights", value=3400, description=None, emoji=None, default=False),
            discord.SelectOption(label="3450 Majellan Way, Sterling Heights", value=3450, description=None, emoji=None, default=False),
            discord.SelectOption(label="3500 Majellan Way, Sterling Heights", value=3500, description=None, emoji=None, default=False),
            discord.SelectOption(label="3550 Majellan Way, Sterling Heights", value=3550, description=None, emoji=None, default=False),
            discord.SelectOption(label="3600 Majellan Way, Sterling Heights", value=3600, description=None, emoji=None, default=False),
            discord.SelectOption(label="3650 Majellan Way, Sterling Heights", value=3650, description=None, emoji=None, default=False),
            discord.SelectOption(label="3700 Majellan Way, Sterling Heights", value=3700, description=None, emoji=None, default=False),
            discord.SelectOption(label="3750 Majellan Way, Sterling Heights", value=3750, description=None, emoji=None, default=False),
            discord.SelectOption(label="3800 Majellan Way, Sterling Heights", value=3800, description=None, emoji=None, default=False),
            discord.SelectOption(label="3850 Majellan Way, Sterling Heights", value=3850, description=None, emoji=None, default=False),
            discord.SelectOption(label="3900 Majellan Way, Sterling Heights", value=3900, description=None, emoji=None, default=False),
            discord.SelectOption(label="3950 Majellan Way, Sterling Heights", value=3950, description=None, emoji=None, default=False),
            discord.SelectOption(label="4000 Majellan Way, Sterling Heights", value=4000, description=None, emoji=None, default=False),
            discord.SelectOption(label="4050 Majellan Way, Sterling Heights", value=4050, description=None, emoji=None, default=False),
            discord.SelectOption(label="4100 Majellan Way, Sterling Heights", value=4100, description=None, emoji=None, default=False),
            discord.SelectOption(label="4150 Majellan Way, Sterling Heights", value=4150, description=None, emoji=None, default=False),
            discord.SelectOption(label="4200 Majellan Way, Sterling Heights", value=4200, description=None, emoji=None, default=False),
            discord.SelectOption(label="4250 Majellan Way, Sterling Heights", value=4250, description=None, emoji=None, default=False),
            discord.SelectOption(label="4300 Majellan Way, Sterling Heights", value=4300, description=None, emoji=None, default=False),
            discord.SelectOption(label="4350 Majellan Way, Sterling Heights", value=4350, description=None, emoji=None, default=False),
            discord.SelectOption(label="None", value=0, description=None, emoji=None, default=False)
        ], disabled=False, row=None)
        async def select_callback(self, interaction, select):
            self.values = select.values
            self.stop()

    class SterlingHouses2(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.values = []
        
        @discord.ui.select(placeholder="Select", min_values=0, max_values=7, options=[
            discord.SelectOption(label="4400 Majellan Way, Sterling Heights", value=4400, description=None, emoji=None, default=False),
            discord.SelectOption(label="4450 Majellan Way, Sterling Heights", value=4450, description=None, emoji=None, default=False),
            discord.SelectOption(label="4500 Majellan Way, Sterling Heights", value=4500, description=None, emoji=None, default=False),
            discord.SelectOption(label="4550 Majellan Way, Sterling Heights", value=4550, description=None, emoji=None, default=False),
            discord.SelectOption(label="4600 Majellan Way, Sterling Heights", value=4600, description=None, emoji=None, default=False),
            discord.SelectOption(label="4650 Majellan Way, Sterling Heights", value=4650, description=None, emoji=None, default=False),
            discord.SelectOption(label="4700 Cypress St, Sterling Heights", value=4700, description=None, emoji=None, default=False),
            discord.SelectOption(label="None", value=0, description=None, emoji=None, default=False)
        ], disabled=False, row=None)
        async def select_callback(self, interaction, select):
            self.values = select.values
            self.stop()
    
    #CyrusHouses, OaklandHouses, OaklandHouses2, PalmerHouses, SterlingHouses, SterlingHouses2
    #declare views
    cyrusHousesView = CyrusHouses()
    oaklandHousesView = OaklandHouses()
    oaklandHouses2View = OaklandHouses2()
    palmerHousesView = PalmerHouses()
    sterlingHousesView = SterlingHouses()
    sterlingHouses2View = SterlingHouses2()

    #get addresses
    await interaction.response.send_message(embed=discord.Embed(title="Cyrus", colour=0x8A7761, description="Select below all of the houses you are delivering to in **Cyrus Acres**").set_image(url="https://i.ibb.co/sRFhSrB/Cyrus.png"), view=cyrusHousesView, ephemeral=True)
    await cyrusHousesView.wait()

    await interaction.edit_original_response(embed=discord.Embed(title="Oakland (1/2)", colour=0x8A7761, description="Select below all of the houses you are delivering to in **Oakland Park**").set_image(url="https://i.ibb.co/qkHscTc/Oakland.png"), view=oaklandHousesView)
    await oaklandHousesView.wait()

    await interaction.edit_original_response(embed=discord.Embed(title="Oakland (2/2)", colour=0x8A7761, description="Select below all of the houses you are delivering to in **Oakland Park**").set_image(url="https://i.ibb.co/qkHscTc/Oakland.png"), view=oaklandHouses2View)
    await oaklandHouses2View.wait()

    await interaction.edit_original_response(embed=discord.Embed(title="Palmer", colour=0x8A7761, description="Select below all of the houses you are delivering to in **Palmer**").set_image(url="https://i.ibb.co/7Ky8Pjq/Palmer.png"), view=palmerHousesView)
    await palmerHousesView.wait()

    await interaction.edit_original_response(embed=discord.Embed(title="Sterling (1/2)", colour=0x8A7761, description="Select below all of the houses you are delivering to in **Sterling Heights**").set_image(url="https://i.ibb.co/YPCK9Qg/Sterling.png"), view=sterlingHousesView)
    await sterlingHousesView.wait()

    await interaction.edit_original_response(embed=discord.Embed(title="Sterling (2/2)", colour=0x8A7761, description="Select below all of the houses you are delivering to in **Sterling Heights**").set_image(url="https://i.ibb.co/YPCK9Qg/Sterling.png"), view=sterlingHouses2View)
    await sterlingHouses2View.wait()

    #
    locations = [int(el) for el in cyrusHousesView.values] + [int(el) for el in oaklandHousesView.values] + [int(el) for el in oaklandHouses2View.values] + palmerHousesView.values + [int(el) for el in sterlingHousesView.values] + [int(el) for el in sterlingHouses2View.values]
    await interaction.edit_original_response(embed=discord.Embed(title="Loading", colour=0x8A7761, description="We're processing your deliveries and creating your routes..."))
    
    images = await getImages(locations)
    paths = []

    for image in images:
        img_path: PIL.Image = images[image]
        img_path = io.BytesIO()
        images[image].save(img_path, format="PNG")
        img_path.seek(0)
        img = discord.File(img_path, f"{image}.png")
        paths.append(img)

    await interaction.edit_original_response(attachments=paths, embeds=[discord.Embed(title=el, colour=0x8A7761, description=None).set_image(url=f"attachment://{el}.png") for el in images], view=None)

@client.command()
@commands.check(lambda ctx : ctx.author.id == myid)
async def connect(ctx):
    await tree.sync()

client.run("MTIwMjI5MTc2MDg5OTAzOTIzMg.GixumW.YLSEL4HwDHczlSnF8fRWH8Y2sUiFeey2vrXaAg")
#https://discord.com/api/oauth2/authorize?client_id=1202291760899039232&permissions=8&scope=bot