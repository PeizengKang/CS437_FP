import numpy as np
from github import Github
import time
import tkinter as tk
import requests
    
# repo number
repoNum = 0
# Total repo Num
repoMax = 0
# repo list
repoList = []    
    
def show_repo():
    global user 
    global repoList
    global l
    global repoNum
    print("In show repo")
    repo = user.get_repo(repoList[repoNum])
    repoInfo = print_repo(repo)
    #print(repoInfo)
    l.config(text = repoInfo)
    l.after(1000, show_repo)

def repo_change(event):
    global repoNum
    global repoMax
    repoNum += 1
    if repoNum >= repoMax:
        repoNum = 0
    print("max", repoMax)
    print("cur", repoNum)


def print_repo(repo):
    allText = ""
    allText += "-"*50 + "\n"
    allList = []

    # current time
    curTime = "Current time is: " + str(time.asctime(time.localtime(time.time())))
    allList.append(curTime)

    # repository full name
    repName = "Repo Full name:" + str(repo.full_name)
    allList.append(repName)

    # repository description
    repDesv = "Description:" + str(repo.description)
    allList.append(repDesv)
    
    # the date of when the repo was created
    repDate = "Date created:" + str(repo.created_at)
    allList.append(repDate)

    # the date of the last git push
    repUpdateTime = "Date of last push:" + str(repo.pushed_at)
    allList.append(repUpdateTime)

    # home website (if available)
    repHome = "Home Page:" + str(repo.homepage)
    allList.append(repHome)

    # programming language
    repLang = "Language:" + str(repo.language)
    allList.append(repLang)

    # number of forks
    repFork = "Number of forks:" + str(repo.forks)
    allList.append(repFork)

    # number of stars
    repStar = "Number of stars:" + str(repo.stargazers_count)
    allList.append(repStar)

    # repository content (files & directories)
    # The content will let the API exceed the limit
    #repCont = "Contents: "
    #contents = repo.get_contents("")
    #while contents:
    #    file_content = contents.pop(0)
    #    if file_content.type == "dir":
    #        contents.extend(repo.get_contents(file_content.path))
    #    else:
    #        repCont += str(file_content)
    #allList.append(repCont)
    
    # View times Total
    # The View times need to set API token first
    #view = repo.get_views_traffic(per="day")
    #view = str(view["count"])
    #allList.append(view)

    # Assemble all info
    allText += "\n".join(allList)
    return allText

#def main():
# user name
username = "PeizengKang"
# initialize git struct
g = Github("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")
# get info of git
user = g.get_user()

# Get all repo in list
repos = user.get_repos()
for repo in repos:
    repoList.append(str(repo.name))
repoMax = len(repoList) - 1
print(repoList)
# initialize window struct
window = tk.Tk()
# full screen
window.attributes('-fullscreen', True)
# window name
window.title('GitHub Repo Tracker')
# window size
window.geometry('320x480')

# Quit Button
quitButton = tk.Button(window, text="Quit", command=window.quit)
# Button position
quitButton.pack(side="bottom")

# label
l = tk.Label(window)
l.pack()
#print("Initialization Finished!")

l.bind("<Button>", repo_change)
show_repo()
#print("Show repo Finished!")
window.mainloop()

if __name__ == "__main__":
    pass