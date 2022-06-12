# ===== Path Scanner by Hezi A ===== #
import platform
import os.path
import urllib3

if platform.system().lower() == "windows" or platform.system().lower() == "linux":
    
url = input("Enter URL: ") #    https://hack-yourself-first.com

while True:
    wordlist_path = input("Enter Wordlist FullPath: ") #    C:\Users\Shai\Desktop\asdg.txt

    os.path.exists(wordlist_path)
    if os.path.exists(wordlist_path):
        if wordlist_path.endswith('.txt'):
            wordlist = []
            with open(wordlist_path, "r") as file:
                for j in file:
                    list = file.readlines()
                    j = "".join(str(list).replace("\\n", ""))
                    wordlist.append(j)

                http = urllib3.PoolManager()
                request = http.request("GET", url)

                if request.status == 200:
                    print(f"You requested to scan {url} website, Request status: {request.status}\n")

                    counter = 1
                    for i in wordlist:
                        request = http.request("GET", f"{url}/{i}")
                        if request.status == 200:
                            print(f"[{counter}] | {url}/{i} | Page Found")
                        elif request.status == 404:
                            print(f"[{counter}] | {url}/{i} | Page Not Found")
                        counter += 1
                elif request.status > 400 or request.status < 499:
                    print(f"You requested to scan {url} website, Request status: {request.status}\n")
                elif request.status > 500 or request.status < 599:
                    print(f"You requested to scan {url} website, Request status: {request.status}\n")
                else:
                    print(f"Something went wrong\n")
        else:
            wordlist_path_splited = str(wordlist_path).split("\\")
            print(f"Your file [{wordlist_path_splited[-1]}] is not .txt file")
    else:
        print(f"Your path [{wordlist_path}] does not exist")

# ===== Path Scanner by Hezi A ===== #
