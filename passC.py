##by MelonRind
import string
import sys
import random
import optparse
import argparse

def banner():
    print("                      _____")
    print("                     / ____|")
    print(" _ __   __ _ ___ ___| |")
    print("| '_ \ / _` / __/ __| |")
    print("| |_) | (_| \__ \__ \ |____")
    print("| .__/ \__,_|___/___/\_____|")
    print("| |")
    print("|_|    Powered by MelonRind\n\n")

def passCreate(length,num = True,punctuation = True,upper = True,lower = True):
    num_list = ''.join(string.digits)
    punctuation_list = ''.join(string.punctuation)
    upper_list = ''.join(string.ascii_uppercase)
    lower_list = ''.join(string.ascii_lowercase)
    pass_list = ''
    password = ''
    if num == True:
        pass_list = pass_list.join(num_list)
    if punctuation ==True:
        pass_list = pass_list+''.join(punctuation_list)
    if upper == True:
        pass_list = pass_list+''.join(upper_list)
    if lower == True:
        pass_list = pass_list+''.join(lower_list)
    for i in range(0,length):
        password = password+random.choice(pass_list)
    return password



if __name__ == "__main__":
    # print(passCreate(15,num=True,punctuation = ,upper = False,lower = False))
    banner()
    parser = argparse.ArgumentParser()
    # parser.add_argument()

    #
    # parser = optparse.OptionParser('usage: passC.py -l <password length> [--] <pathspec>...')
    parser.add_argument('-l','--length',dest='length',type=int,help='password length')
    parser.add_argument('-n','--number',dest='num',default='yes',help='Does the password require no digits?(yes/no)default yes')
    parser.add_argument('-p','--punctua',dest='punc',default='yes',help='Does the password require no symbol?(yes/no)default yes')
    parser.add_argument('-u','--upper',dest='upper',default='yes',help='Does the password require no uppercase?(yes/no)default yes')
    parser.add_argument('-o','--lower',dest='lower',default='yes',help='Does the password require no lowercase?(yes/no)default yes')
    options=parser.parse_args()
    num = True
    punc = True
    upper = True
    lower = True
    if options.length == None:
        parser.print_help()
        sys.exit(1)
    if options.num == 'no':
        num = False
    if options.punc == 'no':
        punc = False
    if options.upper == 'no':
        upper = False
    if options.lower == 'no':
        lower = False
    print(passCreate(options.length,num,punc,upper,lower))