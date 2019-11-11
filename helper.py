import fcntl
import time

def try_read(file, sleep_time=0.5):
	while True:

		try:
			# Open the file
			fi = open(file, 'r')

			# Try to lock the file
			fcntl.flock(fi, fcntl.LOCK_EX)

			# Read the file
			cmd = fi.readline()
			fi.close()
			return cmd
		except OSError:
			# Means the file is in use. Sleep and try again later.
			time.sleep(sleep_time)
		except NameError:
			# Means the file doesn't exist. Sleep and try again later.
			time.sleep(sleep_time)

def try_write(file, string, sleep_time=0.5):
	while True:

		try:
			# Open the file
			fi = open(file, 'w+')

			# Try to lock the file
			fcntl.flock(fi, fcntl.LOCK_EX)

			# Write the file
			fi.write(string)
			fi.close()
			return
		except OSError:
			# Means the file is in use. Sleep and try again later.
			time.sleep(sleep_time)	


def submit_command(command, command_name, result_name, sleep_time==0.5):
	try_write(command_name, command, sleep_time=sleep_time)

	res = try_read(result_name)
	while len(res) == 0:
		res = try_read(result_name)
	try_write('results.txt', '', sleep_time)
	return res