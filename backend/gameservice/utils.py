import subprocess
import logging
import signal
__author__ = 'Mushtaque Ahamed'

def bash(cmd, split=True, strip=False, filter_empty=True, stdin=''):
    """Given a shell command as a string, executes that as a subprocess
        and returns the string output from STDOUT. Also does further
        processing of the output, that is splitting and stripping if
        specified in the kwargs.

    Args:
        cmd (str): The shell command to be executed.
        split (bool, optional): If true, the output string is split
            into a list of strings, with \n being the delimiting character.
        strip (bool, optional): If true, then the leading and trailing
            whitespace characters are remove from the lines of the output.

    Returns:
        A str or a list of str that was obtained from the STDOUT.

    Example:
        >>> from utils import bash
        >>> bash('echo \"hello world\"', strip=True)
        'hello world'
        >>>
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    if stdin:
        process.stdin.write(stdin)
    stdout = ''.join(map(chr, process.communicate()[0]))
    process.stdin.close()

    if split:
        stdout = stdout.split('\n')

    if strip:
        if isinstance(stdout, str):
            stdout = stdout.strip()
        elif isinstance(stdout, list):
            stdout = map(str.split, stdout)

    if filter_empty:
        stdout = [x for x in stdout if x]

    return stdout

def bashrt(command, send_process_back=False, shell=True, stderr=False):
    if stderr:
        process = subprocess.Popen(command, shell=shell,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
        process = subprocess.Popen(command, shell=shell,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if send_process_back:
        yield process

    while True:
        output = process.stdout.readline().strip()
        if process.poll() is not None:
            break
        yield output.decode('utf-8')

logging.basicConfig(level=logging.INFO)

def Logger(name):
    return logging.getLogger(name)

class TimedOutExc(Exception):
  pass

def deadline(timeout, *args):
  def decorate(f):
    def handler(signum, frame):
      raise TimedOutExc()

    def new_f(*args):

      signal.signal(signal.SIGALRM, handler)
      signal.alarm(float(timeout)/1000.0))
      return f(*args)
      signa.alarm(0)

    new_f.__name__ = f.__name__
    return new_f
  return decorate