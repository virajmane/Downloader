from pytube import *
import wget
import re
import requests

def youtube(url):
    print("Fetching Results...")
    yt = YouTube(url)
    print(yt.title)
    availables = yt.streams
    i = 1
    for available in availables.filter(mime_type="video/mp4", progressive=True):
        print(str(i)+str(available))
        i+=1
    download = int(input("Download Choice: "))
    video = availables[download-1]
    print("Downloading...")
    video.download()
    print("Downloaded Successfully!")

def facebook(url):
    html = requests.get(url)
    ch = int(input("Enter the quality\n\t1)Standard\n\t2)high Definition\n> "))
    search = ''
    if ch==1:
        search = re.search('sd_src:"(.+?)"', html.text)[1]
    elif ch==2:
        search = re.search('hd_src:"(.+?)"', html.text)[1]
    print("Downloading...")
    wget.download(search)
    print("Downloaded!")

def instagram(url):
    if "ig_web_copy_link" in url:
        url = url.replace("?utm_source=ig_web_copy_link", "")
    choice = int(input('What are you trying download?\n\t1)Post\n\t2)Video\n\t3)Profile Picture\n> '))
    if choice==1:
        base_url = url + '?__a=1'
        url = requests.get(base_url)
        x = re.search(r'display_url\":\"([^\'\" >]+)', url.text)[1]
        wget.download(x)
        print("Downloaded Successfully!")
    elif choice==2:
        base_url = url + '?__a=1'
        url = requests.get(base_url)
        x = re.search(r'video_url\":\"([^\'\" >]+)', url.text)[1]
        wget.download(x)
        print("Downloaded Successfully!")
    elif choice==3:
        base_url = url + '?__a=1'
        url = requests.get(base_url)
        x = re.search(r'profile_pic_url_hd\":\"([^\'\" >]+)', url.text)[1]
        wget.download(x)
        print("Downloaded Successfully!")
    else:
        print("Wrong Choice")
print("Youtube, Instagram, Facebook Downloader")
url = input("Enter the URL: ")
if 'facebook' in url:
    facebook(url)
elif "youtube" in url:
    youtube(url)
elif "instagram" in url:
    instagram(url)
else:
    print("Enter a valid url")