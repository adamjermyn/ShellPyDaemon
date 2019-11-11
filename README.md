# What it is

This daemon provides a way to run shell commands in python without forking the python process.
This is useful when your main python process is memory-intensive.
**The daemon reads shell commands from a file and runs them. There is no sanitization or safety checking.**

# How it works

On posix-compliant systems, files have advisory `lock` attributes that allow processes to claim access to them.
Every so often, the daemon attempts to acquire a lock on a `commands` file.
If the file isn't empty, the daemon interprets the first line in it as a shell command and runs it.
The daemon then empties the `commands` file.
The daemon then acquires a lock on a `results` file and writes the return code to the first line in that file.
Finally the daemon releases both locks.

At the same time, your code uses the `submit_command` method to send a command to the daemon.
This method, defined in `helper.py`, attempts to acquire a lock on the `commands` file.
Once it has a lock, it writes the specified command to the first line of that file.
It then releases its lock on the file.
Next, it attempts to acquire a lock on the `results` file.
Once it succeeds, it checks if there are any results in the first line.
If there are not, it gives up the lock, waits, tries to re-acquire the lock, and checks again.
This repeats until there is a result in the `results` file, at which point `submit_command` empties the `results` file and returns the result.

In the above all lock acquisition is done within a loop with a `sleep` statement.
If a lock is not acquired, the relevant method waits an amount of time specified by the `sleep_time` argument that both the daemon and `submit_command` accept.
It then tries again.


# Usage

To run the daemon, use

```
python daemon.py path_to_results_file path_to_commands_file sleep_time
```

You can then issue commands to the daemon using the `submit_command` function provided by `helper.py`.
As in,

```
from helper import submit_command
submit_command('ls -lah', 'path_to_commands_file', 'path_to_results_file', sleep_time)
```

The `sleep_time` is specified in seconds. Paths may be relative or absolute, but must be the same for both the submitter and the daemon.
