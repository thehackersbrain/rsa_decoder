import argparse
from colorama import Fore, Style
import pyfiglet
from sys import argv, exit


def banner():
    bn = pyfiglet.figlet_format(" RSA Decrypter", font='slant')
    print(f"{Fore.GREEN}{bn}{Style.RESET_ALL}")
    print(f"\t\t\t\tAuthor : {Fore.GREEN}HackersBrain{Style.RESET_ALL}\n")


def help():
    banner()
    print(" Uses : \n\t python3 main.py -f <file> -d <key> -m <modulus> > output.txt\n\n"
          " flags : \n\t-f <file> - Encrypted File\n"
          "\t-d <key> - Private Key for Decoding\n"
          "\t-m <modulus> - Modulus Key\n\n"
          " example : \n\t python3 main.py -f enc_file.txt -d xxxx -m xxxx > output.txt\n")


if len(argv) != 7:
    help()
    exit()

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="The file containing the excrypted text")
parser.add_argument("-d", "--decrypt", help=" The Private Key", type=int)
parser.add_argument("-m", "--modulus", help=" The Modulus Key", type=int)
args = parser.parse_args()

with open(args.file, "r") as coded:
    data = [int(i.strip("\n")) for i in coded.read().split(" ")]

for i in data:
    print(chr((i**args.decrypt % args.modulus)), end="")
print()
