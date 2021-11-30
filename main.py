import check as ch
import check_alz as ch_alz
import check_dep as ch_dep
# import check_kemarin as ch_kmrn
import t_notif as tn
import json
import configparser
import sys, os
from datetime import datetime


if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    # application_path = sys._MEIPASS
    application_path = os.path.dirname(sys.executable)
    print('run as exe')
else:
    print('run as py script')
    application_path = os.path.dirname(os.path.abspath(__file__))


t_token = ch.read_config_file('t_notif','t_token')
t_ch_id = ch.read_config_file('t_notif','t_ch_id')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

check_stat, naik_ps = ch.main()
a = (json.dumps(check_stat, indent = 2))

check_stat_dep, naik_dep = ch_dep.main()
b = (json.dumps(check_stat_dep, indent = 2))

check_stat_alz, naik_alz = ch_alz.main()
c = (json.dumps(check_stat_alz, indent = 2))

message = f"""Selamat sore
Berikut report Data Sales Toko
{current_time}

PS | belum naik:
{a}

DEPSTORE | belum naik:
{b}

ALZ | belum naik: 
{c}"""

naik_file_msg = f"""Data Sales yg Sudah Naik

PS:
{(json.dumps(naik_ps, indent = 2))}

DEPSTORE:
{(json.dumps(naik_dep, indent = 2))}

ALZ: 
{(json.dumps(naik_alz, indent = 2))}"""

t_status = ch.read_config_file('t_notif', 'v')
if (bool(t_status)):
    tn.notify_ending(application_path, message, t_token, t_ch_id)
    tn.notify_ending(application_path, naik_file_msg, t_token, t_ch_id)

"""
selamat sore
berikut report data sales toko

17:20:00
PS | belum naik:
ARTO-L1-2021-11-23.zip Tue Nov 23 16:40:41 2021 belum naik
MEFA-L1-2021-11-23.zip Tue Nov 23 16:41:58 2021 belum naik
NIPAH-L1-2021-11-23.zip Tue Nov 23 10:40:49 2021 belum naik

DEPSTORE | belum naik:
CWALK-L1-2021-11-23.zip Tue Nov 23 16:33:42 2021 belum naik

ALZ | yang sudah naik hari:
ALQMAL

"""
