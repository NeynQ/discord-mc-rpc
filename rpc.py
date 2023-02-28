from pypresence import Presence
from yandex_music import Client
import time

server = input("Введите адрес сервера: ")
version = input("Введите версию Minecraft : ")

client_id = "1080098980765110362"
RPC = Presence(client_id)
RPC.connect()

while True:
    RPC.update(
        state = "Версия: " + version,
        details = "Сервер: " + server,
        start = time.time(),
        large_image = "mc_avatar",
        large_text = "Minecraft"
    )
    time.sleep(15)
