from telethon import errors
from telethon import TelegramClient, events
import datetime
from loguru import logger
import asyncio


# ---------------------------------- CREATING TELEGRAM CLIENT--------------------------------------------------------
api_id = 11283879
api_hash = '82c6793ac822d0ad61d08d3db2f62add'
client = TelegramClient('Get', api_id, api_hash)

# ------------------------------------ LOGGER -----------------------------------------------------------------------
logger.add("logs/logs.log", level='DEBUG')
logger.info("Время запуска скрипта = {}".format(datetime.datetime.now().strftime("Дата: %d/%m/%Y  Время: %H:%M:%S")))

# ---------------------------------- DICTS ---------------------------------------------------------------------------
bad_strings = open('bad.txt', 'r', encoding='utf8').readlines()
channels = {
    'https://t.me/Aliexpress_en': 'https://t.me/Aliexpress_dw',
    'https://t.me/sextoysali': 'https://t.me/Aliexpress_dw',
    'https://t.me/animeShopLandd': 'https://t.me/animeShopLands',
    'https://t.me/chinaalii': 'https://t.me/chinaalil',
    -1001688186792: 'https://t.me/you_cargoodd',
    -1001333917558: 'https://t.me/instruments_man',
    'https://t.me/wowsoali': 'https://t.me/wowsoall',
    'https://t.me/AliExpressvStyle': 'https://t.me/wowsoall',
    'https://t.me/cdcd119': -1001937248684,
    'https://t.me/nengbi': -1001937248684,
    'https://t.me/Zueseng5': -1001937248684,
    ('https://t.me/daixiu333', -1001873721818, 'https://t.me/fetmistress', -1001728693507): 'https://t.me/bondage_sm',
    (-1001651360534, -1001616424054, 'https://t.me/daddysstories', -1001553839094, -1001538299689,
     -1001596613104): 'https://t.me/teen_gir1',
    -1001491865780: -1001985387920,
    ('https://t.me/asmr3322', 'https://t.me/ASMRQQQ', 'https://t.me/ycfml'): 'https://t.me/chatasmrx',
    ('https://t.me/Faust_plan', 'https://t.me/kesshanonatsu'): 'https://t.me/exlolicons',
    (-1001365578413, 'https://t.me/insbox', 'https://t.me/guochan112233'): 'https://t.me/holyfcuk1AA',
    ('https://t.me/jsgg3', 'https://t.me/dysp666', 'https://t.me/soulzzx4'): 'https://t.me/tuyazhee',
    ('https://t.me/avActress', 'https://t.me/japanmega'): 'https://t.me/jks0001',
    (-1001411943229, 'https://t.me/DoO_o'): 'https://t.me/japan_girl_group',
    ('https://t.me/xquav0', 'https://t.me/xquth0'): 'https://t.me/shaofufulia',
    ('https://t.me/bobofishJPclub', -1001577951330, 'https://t.me/Haotv555'): 'https://t.me/qj20222',
    (-1001676303766, 'https://t.me/xxootv66'): 'https://t.me/whorescum',
    (
        'https://t.me/yande_hot', -1001594316407, 'https://t.me/anime4_tyan',
        -1001531851171): 'https://t.me/anime4_tyanka',
    (-1001374412393, 'https://t.me/acgr18', 'https://t.me/mmd_ecchi', 'https://t.me/hanimeclub',
     'https://t.me/hentai_ch4n'): -1001819199484,
    ('https://t.me/shemaleh', 'https://t.me/TranssexualPorn999', -1001397631074): 'https://t.me/live_pna',
    ('https://t.me/d1rtym0uth', -1001447342209, 'https://t.me/publicnudexxx'): 'https://t.me/publicnudex',
    (-1001484858978, -1001452910675, 'https://t.me/YunRan1314', 'https://t.me/KonachanPopular',
     'https://t.me/czdbxiuche1', 'https://t.me/ghswomenzuizhuanye'): 'https://t.me/hentaicomicsiimangaaa',
    (-1001554789901, 'https://t.me/freetuya', 'https://t.me/cjg4096'): 'https://t.me/hentaicomicsiimangaaa',
    ('https://t.me/fulifuliai', 'https://t.me/tg_coser', 'https://t.me/douza23333', 'https://t.me/Cosplay_18s',
     'https://t.me/bkyss233', 'https://t.me/Dailyshejing_cos'): 'https://t.me/cosplaysharegroup0'
}
tags_dict = {

}

# ----------------------------------------- Временные -----------------------------------------------------------------
textForPosting = open('keyword.txt', 'r', encoding='utf8').readlines()
textForPosting_anime = open('keyword_anime.txt', 'r', encoding='utf8').readlines()


def id_found(id):
    for channel in channels.keys:
        if channel == id:
            return True
    return False


def log(level=None, myId=None, donorId=None):
    """
    :param level:
        None -> start function
        0 -> success
        1 -> FloodWait Error
        2 -> Any Error
    :param user: username channel
    :param id: id channel
    :return: None
    """
    if level is None:
        logger.info("[*] Дата запуска =", datetime.datetime.now().strftime("Дата: %d/%m/%Y  Время: %H:%M:%S"))
        logger.info("[*] My channel = ", myId)
        logger.info("[*] Donor channel = ", donorId)
    elif level == 0:
        logger.info("[+] Сообщение успешно отправлено")
        logger.info("")
    elif level == 1:
        logger.debug("[!] FloodWait Error")
        logger.info("")
    elif level == 2:
        logger.debug("[!] Ошибка в работе скрипта")
        logger.info("")


def get_tag(id):
    return str(tags_dict[id])


with TelegramClient('Get', api_id, api_hash) as client:
    @client.on(events.NewMessage(outgoing=False))
    async def message(event):
        text = event.raw_text + '\n' + get_tag(channels[id])
        id = event.user_id
        if id_found(id) and not [element for element in bad_strings if event.raw_text.lower().__contains__(element)]:
            log(id=channels[id], user=event.chat.username)
            try:
                if not event.grouped_id:
                    await client.send_message(
                        entity=channels[id],
                        file=event.message.media,
                        message=text,
                        parse_mode='md',
                        link_preview=False)
                    log(level=0)
                elif event.message.text and event.message.media is None and not event.grouped_id:
                    await client.send_message(
                        entity=channels[id],
                        message=text,
                        parse_mode='md',
                        link_preview=False)
                elif event.message.forward:
                    await event.message.forward_to(channels[id])
            except errors.FloodWaitError as e:
                log(level=1)
                await asyncio.sleep(e.seconds)
            except Exception as e:
                log(level=2)


    @client.on(events.Album())
    async def album(event):
        text = event.original_update.message.message + '\n' + get_tag(channels[id])
        id = event.user_id
        if id_found(id) and not [element for element in bad_strings if event.raw_text.lower().__contains__(element)]:
            log(id=channels[id], user=event.chat.username)
            try:
                await client.send_message(
                    entity=channels[id],
                    file=event.messages,
                    message=text,
                    parse_mode='md',
                    link_preview=False)
            except errors.FloodWaitError as e:
                log(level=1)
                await asyncio.sleep(e.seconds)
            except Exception as e:
                log(level=2)


    client.start()
    client.run_until_disconnected()