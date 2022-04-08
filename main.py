from distutils.util import split_quoted
import check as ch
import check_alz as ch_alz
import check_dep as ch_dep
import helper as hp
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

x_sale = ch.read_config_file('x_sale_opt','v')
print(x_sale)
if (bool(x_sale)):
    import check_xsale as ch_xsale
    check_stat_xsale, naik_xsale = ch_xsale.main()
    x = (json.dumps(check_stat_xsale, indent = 2))
    x_sale_datanaik = (json.dumps(naik_xsale, indent = 2))
else:
    x = "xsale opt is not true"
    x_sale_datanaik = "xsale opt is not true"


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
c2 = (json.dumps(naik_alz, indent = 2))

message = f"""Selamat sore
Berikut report Data Sales Toko
{current_time}

PS | belum naik:
{a}

DEPSTORE | belum naik:
{b}

ALZ | yang sudah naik: 
{c2}

XSALE | belum naik: 
{x}
"""

naik_file_msg = f"""Data Sales yg Sudah Naik

PS:
{(json.dumps(naik_ps, indent = 2))}

DEPSTORE:
{(json.dumps(naik_dep, indent = 2))}

ALZ: yang belum naik
{c}

XSALE:
{x_sale_datanaik} 
"""


print(len(message))
print(len(naik_file_msg))

t_status = ch.read_config_file('t_notif', 'v')
if (bool(t_status)):
    # if(len(message) > 4096):
    #     message01 = message[:len(message)//2]
    #     message02 = message[len(message)//2:]

    #     tn.notify_ending(application_path, message01, t_token, t_ch_id)
    #     tn.notify_ending(application_path, message02, t_token, t_ch_id)
    # else:
    #     tn.notify_ending(application_path, message, t_token, t_ch_id)

    # if(len(naik_file_msg) > 4096):
    #     naik_file_msg01 = naik_file_msg[:len(naik_file_msg)//2]
    #     naik_file_msg02 = naik_file_msg[len(naik_file_msg)//2:]

    #     tn.notify_ending(application_path, naik_file_msg01, t_token, t_ch_id)
    #     tn.notify_ending(application_path, naik_file_msg02, t_token, t_ch_id)
    # else:
    #     tn.notify_ending(application_path, naik_file_msg, t_token, t_ch_id)
    splitted_msg = hp.devide_message(message, 4096)
    for msg in splitted_msg:
        tn.notify_ending(application_path, msg, t_token, t_ch_id)

    splitted_msg_naik = hp.devide_message(naik_file_msg, 4096)
    for msg in splitted_msg_naik:
        tn.notify_ending(application_path, msg, t_token, t_ch_id)


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
