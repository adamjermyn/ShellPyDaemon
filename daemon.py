import os
import sys
from helper import try_read, try_write

resName = sys.argv[1]
cmdName = sys.argv[2]
sleep_time = float(sys.argv[3])

results = open(resName,'w')



while True:

	cmd = try_read(cmdName, sleep_time=sleep_time)
	if len(cmd) > 0:
		print('Shell output follows:')
		print('')

		res = os.system(cmd)

		print('')
		print('Daemon ran: ', cmd)
		print('Daemon result: ', res)
		try_write('commands.txt', '', sleep_time=sleep_time)
		try_write('results.txt', 'Success ' + str(res), sleep_time=sleep_time)

