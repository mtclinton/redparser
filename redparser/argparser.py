import sys
import re
import ipaddress
from collections import namedtuple

from .validator import *

help = '''
usage: ./util.py [OPTION]... [FILE]
usage: cat [FILE] | ./util.py [OPTION]
usage: mmap-logparser [OPTION]... [FILE]
usage: cat [FILE] | mmap-logparser[OPTION]

Parse logs of various kinds

optional arguments:
  -h, --help            show this help message and exit
  -f, --first NUM       Print first NUM lines
  -l, --last NUM        Print last NUM lines
  -t, --timestamps      Print lines that contain a timestamp in HH:MM:SS format
  -i, --ipv4 IP         Print lines that contain an IPv4 address, matching IPs (Optional) highlighted
  -I, --ipv6 IP         Print lines that contain an IPv6 address, matching IPs (Optional) highlighted

'''


class Arguments():

    def __init__(self):
        self.first = None
        self.last = None
        self.timestamps = None
        self.ipv4 = None
        self.ipv6 = None

def arg_error(error=None):
    if error:
        print(error)
    print(help)
    sys.exit(1)

def argparser(terminalargs, mmap_possible):

    args = Arguments()

    def argcheck(key):
        if hasattr(key, 'property'):
            arg_error("Please only enter command once\n")

    len_termargs = len(terminalargs)
    if len_termargs == 0:
        arg_error()

    if mmap_possible:
        len_termargs -= 1
        terminalargs = terminalargs[:len_termargs]

    if len_termargs == 0:
        arg_error("Please input commands\n")

    else:
        i = 0
        while i < len_termargs:
            if terminalargs[i] == '--first' or terminalargs[i] == '-f':

                argcheck(terminalargs[i])
                if i +1 >= len_termargs or not validate_first(terminalargs[i+1]):
                    arg_error("Input a positive number for the --first command\n")

                args.first = int(terminalargs[i+1])
                i += 2

            elif terminalargs[i] == '--last' or terminalargs[i] == '-l':

                argcheck(terminalargs[i])
                if i +1 > len_termargs or not validate_last(terminalargs[i+1]):
                    arg_error("Input a positive number for the --last command\n")

                args.last = int(terminalargs[i+1])
                i += 2

            elif terminalargs[i] == '--timestamps' or terminalargs[i] == '-t':

                argcheck(terminalargs[i] )
                args.timestamps = "-1"
                i+=1

            elif terminalargs[i] == '--ipv4' or terminalargs[i] == '-i':

                argcheck(terminalargs[i] )
                invalids = ['--first', '-f','--last', 'l', '--timestamps', '-t', '-i', '--ipv4', '-I', '--ipv6']

                if i +1 < len_termargs and (terminalargs[i+1] not in invalids):
                    if not validate_ipv4(terminalargs[i+1]):
                        arg_error("Input a valid ipv4 address for the --ipv4 command\n")

                    args.ipv4 = terminalargs[i+1]
                    i += 2

                else:
                    args.ipv4 = "-1"
                    i += 1

            elif terminalargs[i] == '--ipv6' or terminalargs[i] == '-I':
                argcheck(terminalargs[i] )
                invalids = ['--first', '-f','--last', 'l', '--timestamps', '-t', '-i', '--ipv4', '-I', '--ipv6']
                if i +1 < len_termargs and (terminalargs[i+1] not in invalids):
                    if not validate_ipv6(terminalargs[i+1]):
                        arg_error("Input a valid ipv6 address for the --ipv6 command\n")
                    args.ipv6 = terminalargs[i+1]
                    i += 2
                else:
                    args.ipv6 = "-1"
                    i += 1

            else:
                arg_error("You inputted an unknown commands\n")

    return args