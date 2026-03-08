from time import sleep
import os
import requests
from rich import print

site_st = "<err>: The website is not online."
err_msg = "<err>: We were unable to contact the website."
nt_f = "not found..."
err_r = "<err>: The data is empty in the def."
err_i = "<err>: ?"

def check_process_by_status(url="", name=""):
    if url != "" or name != "":
        try:
            process = requests.get(url)

            if process.status_code == 200:
                resp = url
            elif process.status_code == 404 or process.status_code == 403:
                resp = nt_f
            else:
                resp = err_i
                
            return f"{name}: {resp}"    
        except:
            return err_msg    
    else:
        return err_r        

def check_process(url="", password="", name=""):
    if url != "" and password != "" and name != "":
        try:
            process = requests.get(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"})
            html = process.text

            if process.status_code == 200 or 302:

                if password.lower() in html.lower():
                    resp = url
                else:
                    resp = nt_f

                return f"{name}: {resp}"

            else:
                return site_st

        except:
            return err_msg
    else:
        return err_r


def tiktok(user):
    play = check_process(url=f"https://www.tiktok.com/@{user}", password='"statusCode":0', name="Tiktok")
    return play

def instagram(user):
    play = check_process(url=f"https://www.instagram.com/{user}/", password=f'"username":"{user}"', name="Instagram")
    return play

def github(user):
    play = check_process_by_status(url=f"https://github.com/{user}", name="Github")
    return play

def gitlab(user):
    play = check_process_by_status(url=f"https://gitlab.com/{user}", name="Gitlab")
    return play
      
def youtube(user):
    play = check_process_by_status(url=f"https://m.youtube.com/{user}", name="Youtube")
    return play

def xbox(user):
    play = check_process(url=f"https://xboxgamertag.com/search/{user}", password=user, name="Xbox")
    return play

def all(user):
    tiktok_r = tiktok(user)
    instagram_r = instagram(user)
    github_r = github(user)
    gitlab_r = gitlab(user)
    youtube_r = youtube(user)
    xbox_r = xbox(user)
    linkedin_r = linkedin(user)

    return f"{tiktok_r}\n{instagram_r}\n{github_r}\n{gitlab_r}\n{youtube_r}\n{xbox_r}"
    
