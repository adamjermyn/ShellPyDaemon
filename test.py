from helper import submit_command

sleep_time = 0.5 # seconds
submit_command('cat test.py > fi', 'commands.txt', 'results.txt', sleep_time)
submit_command('cat test.py > fi2', 'commands.txt', 'results.txt', sleep_time)
submit_command('pwd', 'commands.txt', 'results.txt', sleep_time)
submit_command('ls -lah', 'commands.txt', 'results.txt', sleep_time)