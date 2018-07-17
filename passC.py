##by MelonRind
import string
import sys
import random
import optparse

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

    parser = optparse.OptionParser('usage: passC.py -l <password length> [--] <pathspec>...')
    parser.add_option('-l','--length',dest='length',type='int',help='password length')
    parser.add_option('-n','--number',dest='num',type='string',default='yes',help='Does the password require no digits?(yes/no)default yes')
    parser.add_option('-p','--punctua',dest='punc',type='string',default='yes',help='Does the password require no symbol?(yes/no)default yes')
    parser.add_option('-u','--upper',dest='upper',type='string',default='yes',help='Does the password require no uppercase?(yes/no)default yes')
    parser.add_option('-o','--lower',dest='lower',type='string',default='yes',help='Does the password require no lowercase?(yes/no)default yes')
    (options,args)=parser.parse_args()
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