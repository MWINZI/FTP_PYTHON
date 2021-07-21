import ftplib
import logging
from tqdm import tqdm
import os

logger = logging.getLogger("Ftp client [_+_]")
logger.setLevel(logging.DEBUG)

log_handler = logging.StreamHandler()

log_formatter = logging.Formatter(' %(levelname)s -- %(name)s -- %(message)s')

# add formatter to the handler
log_handler.setFormatter(log_formatter)
# add handler to the logger
logger.addHandler(log_handler)
def _catch_exception(operation):
    try:
        operation()
    except ftplib.all_errors as err:
        print("Error : ", str(err))


def dir_list():
    files = []
    ftp.dir(files.append)
    print(files)


# getting size of text file
def get_size():
    logger.info("You started module to get size of a file on the server ")
    filename = input("[ _+_ ] File name >> ")
    logger.info(f"Getting file size of {filename.upper()}")
    ftp.sendcmd('TYPE I')  # FOR ASCII MODE TYPE A
    size = ftp.size(filename=filename)
    logger.info("Got the size")
    print(size)

def download():
    orig_file = input("File to copy >> ")
    file_size = os.stat(orig_file).st_size
    with open(input("Save file as >> "), 'wb') as fp:
        tqdm(file_size)
        # retrieving a file named text.text and saving it as te.txt
        ftp.retrbinary('RETR ' + orig_file, fp.write)
        print("Copied with Success ...")


# uploading file
def upload_file():
    try:
        file_name = input("File to upload >> ")
        file = open(file_name, 'rb')
        ftp.storbinary('STOR ' + input("Save as >> "), file)
        print('Done successfully')
    except Exception as err:
        print("Error : ", str(err), str(type(err)))
        # local_file = open(file_name, 'wb')



def delete():
    ftp.delete(filename=input("Enter file name >> "))
def rename():
    ftp.rename(fromname=input("File to rename >> "), toname=input("Rename to >> "))
def make_dir():
    ftp.mkd(dirname=input("Enter the Dir Name"))
def remove_dir():
    ftp.rmd(dirname=input("Dir to delete >> "))
def _quit():
    ftp.quit()
def change_dir():
    ftp.cwd(dirname=input("Enter directory name >> "))
with ftplib.FTP() as ftp:
    ftp.connect('127.0.0.1', 2121)
    ftp.login('user', '12345')
    # logger.info(f"[ + ]Connected Successfully {ftp.source_address} \n [ + ]Logged in Successfully\nCurrent Working Dir is {ftp.pwd()}")
    logger.info(ftp.getwelcome())
    # dir listing


    while True:
        user_operation = input("Enter the operation name >> ").lower().strip()
        if user_operation == 'dir listing':
            dir_list()
            continue
        elif user_operation == 'get size':
            _catch_exception(get_size)
            continue
        elif user_operation == 'download':
            _catch_exception(download)
            continue
        elif user_operation == 'upload':
            _catch_exception(upload_file)
            continue
        elif user_operation == 'rename file' or 'change name':
            _catch_exception(rename)
            continue
        elif user_operation == '6':
            _catch_exception(delete)
            continue
        elif user_operation == 'make dir':
            _catch_exception(make_dir)
            continue
        elif user_operation == 'remove dir' or "delete dir":
            _catch_exception(remove_dir)
            continue
        elif user_operation == 'quit' or 'exit' or 'close':
            _quit()
            continue
        elif user_operation == 'help':
            continue
        elif user_operation is None:
            continue


        else:
            print("Unknown code ")
            continue