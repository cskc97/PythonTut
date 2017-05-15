import grequests
import requests
import json
from multiprocessing import Process
from multiprocessing import Manager
import operator

# Contributions are counted as follows -
# Issues, pull requests, forks, commits

#Getting commits as follows -
# https://api.github.com/users/cskc97/repos - will give a list of all repos
# for each repo name we will then have to call https://api.github.com/repos/cskc97/PythonTut/stats/commit_activity
# where pythotut will be replaced by the repo name
# the resulting array would span 365 days and have all the commits for each of those 365 days


class GhContributions:
    def __init__(self,username):
        self.userName = username


    def getRepos(self): #this function returns the users repos
        apiUrl = "https://api.github.com/users/"+self.userName+"/repos";

        returnList=[]
        request=requests.get(apiUrl)
        jsonString = request.text

        data = json.loads(jsonString)
        for obj in data:
            returnList.append(obj["name"])
        print(returnList)

        return returnList

    def getRepoCommits(self,repoName,shared_dict):
        apiURL = "https://api.github.com/repos/cskc97/"+repoName+"/stats/commit_activity"
        request = requests.get(apiURL)
        jsonString = request.text
        data=json.loads(jsonString)
        returnList = []
        for week in data:
            returnList.append(week['days'])
        else:
            shared_dict[repoName]=returnList



    def getCommits(self):
        repoList = self.getRepos()
        returnList = [0]*365

        manager = Manager()
        shared_dict=manager.dict()

        processList=[]
        for repo in repoList:
            process = Process(target=self.getRepoCommits,args=(repo,shared_dict))
            processList.append(process)
            process.start()


        for proc in processList:
            proc.join()

        for key in shared_dict:
            returnList=map(operator.add(),returnList,shared_dict[key])

        return returnList


     






if __name__ == '__main__':

    gh = GhContributions("cskc97")
    gh.getRepos()
    dict = gh.getCommits()
    for key in dict:
        print(key,dict[key])










