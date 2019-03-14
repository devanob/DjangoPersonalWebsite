
import os
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
from datetime import datetime
import urllib.request
from urllib.request import Request, urlopen
from celery import shared_task
import json
from ProjectUser.models import ProjectUser
@shared_task
#Return The Git User Repos List As An Array Of Dictionary Then Returns ProjectUser
def getUsers(userModel):
	try:
		userProject = ProjectUser.objects.get(username=userModel)
		gitUser = userProject.gitUser
		print(gitUser)
	except:
		logger.info("User Couldnt Not Be Found:{}".format(userModel))
		raise Exception("User Couldnt Not Be Found:{}".format(userModel))
	    #Do nothing User Not Found Raise Error
	urlRestApiGit = "https://api.github.com/users/{}/repos".format(gitUser)
	try:
		url_request = Request(urlRestApiGit, 
						headers = {"User-Agent": "Mozilla/5.0"})
		contents = urlopen(url_request).read()
	except:
		logger.info("Git User Couldnt Not Be Found Or Connection Erorr:{}".format(gitUser))
		raise Exception("Git User Couldnt Not Be Found Or Connection Erorr:{}".format(gitUser))
	currentUserRepos= {} # // intially empty 
	jsonContentRepos =  json.loads(contents)
	for reposInfo in jsonContentRepos: 
		oodict = {key: value
			    for key, value in reposInfo.items()
			    if key in ['id','description', 'html_url', 'created_at', 'updated_at', 'name']
			  }
		currentUserRepos[oodict['name']] = oodict
	#print(currentUserRepos)
	for key,repos in currentUserRepos.items():
		#print(repos)
		repos["created_at"] = datetime.strptime(repos["created_at"], "%Y-%m-%dT%H:%M:%SZ")
		#repos["created_at"] = repos["created_at"].strftime('%Y-%m-%d %H:%M:%S+00:00')
		repos["updated_at"] = datetime.strptime(repos["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
		#repos["updated_at"] = repos["updated_at"].strftime('%Y-%m-%d %H:%M:%S+00:00')
	logger.info("Sucess Getting Project")
	#print(currentUserRepos)
	return currentUserRepos,userProject 

@shared_task
def generateProjects(userModelString):
	listRepos,modelUser = getUsers(userModelString)
	currentUserProjects = modelUser.projectUserHandlier.all()
	for key, repo in listRepos.items():
		project, created  = currentUserProjects.get_or_create(
			projectName = key,
			defaults={
				'created': repo['created_at'],
				'last_updated': repo['updated_at'],
				'imglink' : "{}.jpg".format(key), 
				'description': repo['description'],
				'project_link' : repo['html_url'], 
				'projectHandlier' : modelUser



				}
		)
		if (created):
			print(project)
			print('Created')
	