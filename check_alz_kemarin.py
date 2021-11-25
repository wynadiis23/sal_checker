import os
import time
from datetime import datetime, timedelta
# import glob
import sys
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

def find_files(environment):
	if environment == 'dev':
		rootDir = 'D:\Development\DATAHEAD'
	if environment == 'prod':
		rootDir = 'V:'	
	
	file_kemarin_ada = []
	file_kemarin_tidak_ada = []
	folder_tidak_ada = []
	with open("daftartokoalz.txt", "r") as a_file:
		
		now = datetime.now()
		# current_time = now.strftime("%H:%M:%S")
		# print("Current Time =", current_time)

		# current_minute = now.minute
		# print(current_minute)
		
		# #check time. 
		# #1. jika waktu skrg kurang dari xjam 10 menit, maka expected mod time adalah x-1jam 40ish menit.
		# if current_minute < 10:
		# 	now = datetime.now()
		# 	expected_mod_time = now.replace(hour=now.hour-1, minute=40, second=0).strftime("%H:%M:%S")
		# 	print("modified date yang diekspektasikan %s" %expected_mod_time)
		# #2. jika waktu skrg lebih dari xjam 10 menit dan kurang dari xjam 40 menit, maka expected mod time adalah xjam 10ish menit.
		# elif current_minute > 10 and current_minute < 40:
		# 	now = datetime.now()
		# 	expected_mod_time = now.replace(hour=now.hour, minute=10, second=0).strftime("%H:%M:%S")
		# 	print("modified date yang diekspektasikan %s" %expected_mod_time)
		# #3. jika waktu skrg lebih dari x jam 40 menit, maka expected mod time adalah xjam 40ish menit.
		# else:
		# 	now = datetime.now()
		# 	expected_mod_time = now.replace(hour=now.hour, minute=40, second=0).strftime("%H:%M:%S")
		# 	print("modified date yang diekspektasikan %s" %expected_mod_time)

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
				#check data kemarin ada tidak
				fullPath = direktori + "\\" + namaFile_kemarin
				if os.path.isfile(fullPath):
					str_2 = ("%s data kemarin: %s" % (namaFile_kemarin, time.ctime(os.path.getmtime(full_file_path_kemarin))))
					file_kemarin_ada.append(str_2)
				else:
					str_2 = (namaFile + ' not found')
					file_kemarin_tidak_ada.append(str_2)
				print(str_2)
			else:
				tidak_ada_foler = ('folder ' + toko + ' tidak ada')
				folder_tidak_ada.append(tidak_ada_foler)
		
			
	print("\n")
	print("Toko file backup kemarin | %s" %len(file_kemarin_ada))
	print(file_kemarin_ada)
	print("\n")
	print("Toko file backup kemarin tidak ada | %s" %len(file_kemarin_tidak_ada))
	print(file_kemarin_tidak_ada)
	print("\n")
	print("Toko yang foldernya tidak ada | %s" %len(folder_tidak_ada))
	print(folder_tidak_ada)
	print("\n")


# opsi untuk exclude loading

find_files(sys.argv[1])

