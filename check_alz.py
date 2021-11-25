import os
import time
from datetime import datetime, timedelta
# import glob
import sys
import configparser
# import itertools
# import threading

# def toko_loading_nama(nama_toko):
# 	return nama_toko

# done = False
# def animate():
# 	for c in itertools.cycle(['|', '/', '-', '\\']):
# 		if done:
# 			break
# 		sys.stdout.write('\rloading ' + c)
# 		sys.stdout.flush()
# 		time.sleep(0.1)
# 	sys.stdout.write('\rDone!     ')
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

def find_files():
	env = read_config_file('user_info', 'env')
	if env == 'dev':
		rootDir = 'D:\Development\DATAHEAD'
	if env == 'prod':
		rootDir = read_config_file('user_info', 'dir_alz')
	
	naik = []
	belum_naik = []
	file_tidak_ada = []
	folder_tidak_ada = []
	belum_naik_copy = []
	toko_count = 0
	with open("daftartokoalz.txt", "r") as a_file:
		
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print("Current Time =", current_time)

		current_minute = now.minute
		print(current_minute)
		
		#check time. 
		#1. jika waktu skrg kurang dari xjam 10 menit, maka expected mod time adalah x-1jam 40ish menit.
		if current_minute < 10:
			now = datetime.now()
			expected_mod_time = now.replace(hour=now.hour-1, minute=40, second=0).strftime("%H:%M:%S")
			print("modified date yang diekspektasikan %s" %expected_mod_time)
		#2. jika waktu skrg lebih dari xjam 10 menit dan kurang dari xjam 40 menit, maka expected mod time adalah xjam 10ish menit.
		elif current_minute > 10 and current_minute < 40:
			now = datetime.now()
			expected_mod_time = now.replace(hour=now.hour, minute=10, second=0).strftime("%H:%M:%S")
			print("modified date yang diekspektasikan %s" %expected_mod_time)
		#3. jika waktu skrg lebih dari x jam 40 menit, maka expected mod time adalah xjam 40ish menit.
		else:
			now = datetime.now()
			expected_mod_time = now.replace(hour=now.hour, minute=40, second=0).strftime("%H:%M:%S")
			print("modified date yang diekspektasikan %s" %expected_mod_time)

		#tanggal h-1
		before_h = 1
		get_yesterday = now - timedelta(days=before_h)
		yesterday = get_yesterday.strftime('%Y-%m-%d')
		print(yesterday)

		for line in a_file:
			stripped_line = line.strip()
			toko = stripped_line+'-L1'
			# if stripped_line == 'str':
			# 	break

			namaFile = toko + '-' + datetime.today().strftime('%Y-%m-%d') + '.zip'
			namaFile_kemarin = toko + '-' + yesterday + '.zip'

			direktori = rootDir + "\\" + toko + "\\" +"backup"

			full_file_path = direktori + "\\" + namaFile
			full_file_path_kemarin = direktori + "\\" + namaFile_kemarin
			# print(direktori)
			check_dir_exist = os.path.isdir(direktori)
			

			if check_dir_exist:
				fullPath = direktori + "\\" + namaFile
				if os.path.isfile(fullPath):
					time_temp1 = time.ctime(os.path.getmtime(full_file_path))
					time_temp2 = time.strptime(time_temp1)
					modified_time_file = time.strftime('%H:%M:%S', (time_temp2))
					# print(modified_time_file)
					if expected_mod_time > modified_time_file:
						str_1 = ("%s %s belum naik" % (namaFile, time.ctime(os.path.getmtime(full_file_path))))
						belum_naik.append(str_1)
						belum_naik_copy.append(stripped_line)
						print(str_1)
						# break
					else:
						str_1 = ("%s %s" % (namaFile, time.ctime(os.path.getmtime(full_file_path))))
						naik.append(str_1)
						print(str_1)
					# print(naik);
				else:
					#check data kemarin ada tidak
					fullPath = direktori + "\\" + namaFile_kemarin
					if os.path.isfile(fullPath):
						str_2 = ("%s not found | data kemarin: %s" % (namaFile_kemarin, time.ctime(os.path.getmtime(full_file_path_kemarin))))
						file_tidak_ada.append(str_2)
					else:
						str_2 = (namaFile + ' not found')
						file_tidak_ada.append(str_2)
					print(str_2)
			else:
				tidak_ada_foler = ('folder ' + toko + ' tidak ada')
				folder_tidak_ada.append(tidak_ada_foler)
			toko_count += 1
		
			
	print("\n")
	print("modified date yang diekspektasikan | %s" %expected_mod_time)
	print("\n")
	print("Toko yang sudah naik | %s" %len(naik))
	print(naik)
	print("\n")
	print("Toko yang belum naik | %s" %len(belum_naik))
	print(belum_naik)
	print("\n")
	print("Toko file backupnya tidak ada | %s" %len(file_tidak_ada))
	print(file_tidak_ada)
	print("\n")
	print("Toko yang foldernya tidak ada | %s" %len(folder_tidak_ada))
	print(folder_tidak_ada)
	print("\n")
	print("Toko yang belum naik | %s" %len(belum_naik))
	print(belum_naik_copy)
	print("\n")

	d = dict()
	if len(naik) == toko_count:
		d['status'] = 'ps naik semua'
		return d
	elif len(naik) < toko_count:
		d['belum_naik'] = belum_naik
		d['file_tidak_ada'] = file_tidak_ada
		d['folder_tidak_ada'] = folder_tidak_ada
		return d
	else:
		return 'ama'
	# return toko_count


# opsi untuk exclude loading

def read_config_file(section, item):
    # this line is for read configuration file. Please set your db toko root dir on the config.ini file.
    config = configparser.ConfigParser()
    path_config = os.path.join(application_path, 'config.ini')
    # print(repr(path_config))
    config.read(path_config)
    if (section == 'user_info'):
        user_info = config[section]
        user_config = user_info[item]
        return user_config
    elif (section == 't_notif'):
        t_info = config[section]
        t_info_conf = t_info[item]
        return t_info_conf
    else:
        log_txt = "no such section and item on config file"
        exit()

def main():
	a = find_files()
	return a

if __name__=="__main__":
    main()


