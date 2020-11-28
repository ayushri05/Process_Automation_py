import pysftp
import datetime
from datetime import date
import os
import fnmatch
from dotenv import load_dotenv

load_dotenv()


def share_file():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    Host = os.getenv("Host")
    username = os.getenv("username")
    password = os.getenv("password")

    srv = pysftp.Connection(Host, username=username,
                            password=password, cnopts=cnopts)
    # with srv.cd('public'): #chdir to public
    # upload file to nodejs/
    # filepath = 'C: \Users\Ayushri\Documents\'

    # latest_file = S.Join(Directory.GetFiles(filepath, '*.csv/ZuoraToEncompass orders*', SearchOption.AllDirectories).OrderByDescending(Function(d) New FileInfo(d).CreationTime).Take(1))

    Current_date = date.today()

    filepath = "ZuoraToEncompass orders"+str(Current_date)

    print(filepath)

    for file_name in os.listdir(r'C:\\Users\\Ayushri\\Documents\\'):
        if fnmatch.fnmatch(file_name, 'filepath*.txt'):
            print(file_name)
    #now = datetime.now()

    #print("now =", now)

    # dd/mm/YY H:M:S
    #dt_string = now.strftime("%Y-/%m-/%d %H-%M")
    file = r"C:\\Users\\Ayushri\\Documents\\" + file_name

    #srv.put(r'C:\Users\Ayushri\Documents\ZuoraToEncompassorders2020-09-28 02-42.txt')
    srv.put(file)
    # Closes the connection
    srv.close()
