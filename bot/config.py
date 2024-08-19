import os

from pydrive2.auth import GoogleAuth
from bot.helpers.cookies import get_cookies
currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)


class TG_CONFIG:
    api_id = 23080322
    dburl = "mongodb+srv://hello:hello@cluster0.vc2htx0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    api_hash = "b3611c291bf82d917637d61e4a136535"
    stringhi = "BQD6zg0AiiffNu7bpwJSeCweXvrM9EJm2cZxnx4lsfLuBGVacl7F_1ZtBPo5wHlN1sh-B60LKRvZ4k-UQFKsem9D4cMiVdFSpW86y4S93Kt9WPwRkKK8j5T6LY1Cry40t9p6ilNhMQZkRSJYAGogL_L0uIt1khEDARc_QgWtyrLtWA5YjSNDyja_vRIJT_luclVOxsK_bERZj3VLuBO0NyjJ0E7pPk5X6s7PehAvfiSP9FSkhl34ghLpaP0imNvyOteNJH7XACqE0VyMzdoL9lfg0pdLFRjQD7G694h0Y2KeMAgYBhtoGwS30I0U_MtDuxc0q5U3Y2ApeSiqcPdyloi_dZIJzwAAAABHP54rAA"
    UPSTREAM_REPO = "https://github.com/webserver5/testout4gb"
    UPSTREAM_BRANCH = "Aryan"
    bot_token = "7315218183:AAEggyhdPrn_a0fzC0jBx5c9XXQJMFj8do8"
    owner_id = 7011929837
    #DEVS or #OWNERS
    sudo_users = [ 7011929837, -1002172500762, -1002205027579, 1195351595, 1596559467, -1002222878830, -1002151706087]
    session = "Aryanmadebot"
    session2 = "NiteshTeamUniverse"
    token_timeout = 3600
    TESTOVER = True
    bot_creater = "Not Known"  # Don't Remove if you Respect the DEV

    bot_creater_id = "@team"  # Don't Remove if you Respect the DEV


class UPLOAD_CONGIF:
    upload_to = "tg" #tg, ftp, gdrive
    default_upload_to = "tg"


class GDRIVE_CONFIG:
    #for Gdrive (Leave it as Empty String if not Gdrive Upload is turned ON)
    root_folder_id = ""

    #keep it empty if you don't have index link or don't touch
    indexlink_format = "https://example.workers.dev/0:/{}/{}"

    is_making_drive_files_public = True


class GD_SHARER_CONFIG:

    is_uploading_to_filepress = False

    #Don't add a trailing slash at the end (keep in this format only - https://new5.filepress.store)
    filepress_url = "https://new9.filepress.store"
    
    cookie_path = dirPath + "/cookies/filepress.txt"
    _, dict_cookies = get_cookies(cookie_path)
    
    filepress_connect_sid_cookie_value = dict_cookies.get("connect.sid")


class PROXY_CONFIG:
    #Keep it as a empty string if you don't have proxy
    proxy_url = ""
    USE_PROXY_WHILE_DOWNLOADING = False


class FTP_CONFIG:
    #FTP Creds
    ftp_url = ""

    ftp_domain = ""
    
    ftp_user = ""
    
    ftp_password = ""


class FILENAME_CONFIG:

    filename_format = "non-p2p"  # p2p or non-p2p

    p2p_audio_bitrate = "K"

    non_p2p_audio_bitrate = "Kbps"

    underscore_before_after_group_tag = "__"

    language_order = ['hi', 'ta', 'te', 'bn', 'gu', 'pa', 'as', 'or',
                    'ml', 'mr', 'kn', 'th', 'ja', 'th', 'id', 'ms', 'ko', 'bho', 'bh', 'en']

    default_group_tag = "M💓S" # Don't change it if you Respect the DEV

    #Dict made to add Group Tag according to the user requesting to DL (according to there TG ID) if not in list then takes the default_group_tag
    group_tag_mapping = {
        '7172796863': 'M💓S',
        '1596559467' : 'M💓S'
    }


DL_DONE_MSG = """
✅ <b> Task Completed In </b> <code>{}</code>

<b>FileName : </b> <code>{}</code>
<b>OTT : </b> <code>{}</code>
<b>Size : </b> <code>{}</code>
"""


START_MSG = """
<b>Hello <code>@{}</code>,
A TG WEB-DL Bot</b>

> <code>{}</code>

<b>Made by @maheshsirop</b>
"""

SIMPLE_CAPTION = '''<code>{}</code>'''

LOG_MESSAGE = "<code>[+]</code> <b>{}</b>\n<b><code>[+]</code> <b>{} : </b><code>{}</code>"


proxies = {
    "https": PROXY_CONFIG.proxy_url,
    "http": PROXY_CONFIG.proxy_url
} if PROXY_CONFIG.proxy_url and PROXY_CONFIG.proxy_url.strip() else None

tplay_path = os.path.join(
    dirPath, "static", "tplay.json")

languages_info_file_path = os.path.join(
    dirPath, "static", "languages_info.json")

client_secrets_json = os.path.join(dirPath, "static", "client_secrets.json")

token_file = os.path.join(dirPath, "static", "session")

dl_folder = os.path.join(dirPath, "downloads")  

os.makedirs(dl_folder) if not os.path.exists(dl_folder) else None

iswin = 1 if os.name == "nt" else 0


if iswin == 0:
    aria2c = dirPath + "/binaries/aria2c"
    mp4decrypt = dirPath + "/binaries/mp4decrypt"
    ytdlp = dirPath + "/binaries/yt-dlp"

    os.system(f"chmod 777 {aria2c} {mp4decrypt} {ytdlp}")
else:
    aria2c = dirPath + "/binaries/aria2c.exe"
    mp4decrypt = dirPath + "/binaries/mp4decrypt.exe"
    ytdlp = dirPath + "/binaries/yt-dlp.exe"


gauth = GoogleAuth()
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_secrets_json
