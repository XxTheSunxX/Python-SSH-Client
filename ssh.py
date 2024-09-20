import paramiko

def ssh_connect():
    flag = True
    while  flag == True:
        host = "" # see if I need to make a string for host, username, and password variables
        host = input("What is the host address: ")
        username = ""
        username = input("What is the username: ")
        password = ""
        password = input("What is the password: ")
        
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        
        print(f"Connected to: {host}")
        # client.invoke_shell(term='vt100', width=80, height=24, width_pixels=0, height_pixels=0, environment=None)
        answer = input("Run command? (yes/no)")
        
        while answer == "yes" or flag == True:
            command = input(">>>")
            _stdin, _stdout,_stderr = client.exec_command(command)
            print(_stdout.read().decode())
            flag == True
        else:
            client.close()

ssh_connect()