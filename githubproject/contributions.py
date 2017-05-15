from github import Github
from github.AuthenticatedUser import AuthenticatedUser
from github.StatsCommitActivity import StatsCommitActivity
from github import GithubObject
import requests
import json
from multiprocessing import Process
from multiprocessing import Manager
import operator
import datetime

# Contributions are counted as follows -
# Issues, pull requests, forks, commits

#Getting commits as follows -
# https://api.github.com/users/cskc97/repos - will give a list of all repos
# for each repo name we will then have to call https://api.github.com/repos/cskc97/PythonTut/stats/commit_activity
# where pythotut will be replaced by the repo name
# the resulting array would span 365 days and have all the commits for each of those 365 days


today = datetime.datetime.now()


print(type(int(today.strftime('%j'))))


class GhContributions:
    def __init__(self,username,password):
        self.userName = username
        self.password = password
        r = requests.get('https://api.github.com/user', auth=('username', 'password'))
        self.authenticatedUser = Github(username,password).get_user()


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

    def getContributions(self):
        commitList = self.getCommits()
        issues = self.authenticatedUser.get_user_issues()
        for issue in issues:
            datetimeVal = issue.created_at
            intDate = int(today.strftime('%j'))
            commitList[intDate]+=1

        return commitList













if __name__ == '__main__':

    gh = GhContributions("username","password")
    gh.getRepos()
    print(gh.getCommits())











