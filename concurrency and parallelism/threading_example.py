# good for downloading multiple files 
import threading
import time

def download(file):
    print(f"downloading {file} ....")
    time.sleep(2)
    print(f"finished downloading {file}")

files = ["file1", "file2","file3","file4"]
threads = []

for file in files :
    t = threading.Thread(target=download, args=(file,))
    t.start()
    threads.append(t)

for t in threads :
    t.join()
