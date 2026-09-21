# 3-MAVZU: PYTHON UYGA VAZIFA
# Abdulatif Abdirafikov


# 1. CPython, PyPy va boshqa Python interpretatorlari
#
# CPython Python dasturlash tilining eng mashhur va standart
# implementatsiyasi hisoblanadi. U C dasturlash tilida yozilgan.
# Python.org saytidan o‘rnatiladigan odatiy Python interpretatori
# CPython hisoblanadi. Ko‘pgina Python kutubxonalari va frameworklari
# CPython bilan ishlashga moslashtirilgan.
#
# PyPy Python dasturlarini tezroq bajarishga yo‘naltirilgan
# implementatsiyalardan biridir. Uning asosiy xususiyatlaridan biri
# JIT (Just-In-Time) kompilyatsiya texnologiyasidan foydalanishidir.
# JIT dastur ishlayotgan vaqtda kodni optimallashtirishi mumkin.
#
# CPython keng qo‘llab-quvvatlanishi va ko‘plab kutubxonalar bilan
# mosligi bilan ajralib turadi. PyPy esa ayrim uzoq davom etadigan
# dasturlarda yaxshi ishlash tezligini berishi mumkin. Biroq barcha
# kutubxonalar PyPy bilan CPython kabi bir xil darajada mos kelmasligi
# mumkin.
#
# Jython va IronPython kabi boshqa implementatsiyalar ham mavjud.
# Jython Java platformasi bilan, IronPython esa .NET platformasi
# bilan ishlash uchun mo‘ljallangan.


# 2. venv, virtualenv va Poetry taqqoslash
#
# | Vosita     | Afzalligi                         | Kamchiligi              |
# |------------|-----------------------------------|-------------------------|
# | venv       | Python bilan birga keladi         | Imkoniyatlari cheklangan|
# | virtualenv | Moslashuvchan va tez ishlaydi     | Alohida o‘rnatiladi     |
# | Poetry     | Dependencylarni boshqaradi        | O‘rganish murakkabroq   |
#
# venv oddiy loyihalar uchun qulay.
# virtualenv virtual muhit yaratish uchun ko‘proq imkoniyat beradi.
# Poetry dependency va package managementni bir joyda boshqaradi.


# 3. argparse subparsers bilan CLI skript
#
# cli.py faylida ikkita buyruq yaratildi:
#
# python3 cli.py start
# python3 cli.py stop
#
# start -> Service started
# stop  -> Service stopped


# 4. requirements.txt yaratish va yangi virtual muhitda sinash
#
# requirements.txt yaratish:
#
# pip freeze > requirements.txt
#
# Yangi virtual muhit yaratish:
#
# python3 -m venv testenv
#
# Faollashtirish:
#
# source testenv/bin/activate
#
# Paketlarni o‘rnatish:
#
# pip install -r requirements.txt


# 5. CLI skriptni crontab orqali avtomatik ishga tushirish
#
# crontabni ochish:
#
# crontab -e
#
# Misol:
#
# */5 * * * * /usr/bin/python3 /path/to/cli.py start
#
# Uchragan qiyinchiliklar:
#
# - Cron oddiy terminaldan boshqa muhitda ishlashi mumkin.
# - PATH o‘zgaruvchisi farq qilishi mumkin.
# - Virtual environment avtomatik faollashmaydi.
# - Python faylining to‘liq yo‘lini ko‘rsatish kerak bo‘lishi mumkin.
# - Relative path o‘rniga absolute path ishlatish qulayroq.
