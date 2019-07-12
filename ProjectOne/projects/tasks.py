
from django.utils.timezone import make_aware
from django.conf import settings
from ProjectUser.models import ProjectUser
import json
from celery import shared_task
from urllib.request import Request, urlopen
import urllib.request
from datetime import datetime
import os
import logging
from celery.utils.log import get_task_logger
def get_celery_logger(name):
    logger = get_task_logger(name)
    logger.level = logging.INFO
    return logger

log = get_celery_logger(__name__)
@shared_task
def getUsers(userModel):
    try:
        userProject = ProjectUser.objects.get(username=userModel)
        gitUser = userProject.gitUser
    except Exception:
        log.info(traceback.print_exc())
        log.info("User Couldnt Not Be Found:{}\n".format(userModel))
        raise Exception("User Couldnt Not Be Found:{}\n".format(userModel))
    # Do nothing User Not Found Raise Error
    urlRestApiGit = "https://api.github.com/users/{}/repos".format(gitUser)
    try:
        url_request = Request(urlRestApiGit,
                              headers={"User-Agent": "Mozilla/5.0"})
        contents = urlopen(url_request).read()
    except:
        log.info(
            "Git User Couldnt Not Be Found Or Connection Erorr:{}\n".format(gitUser))
        raise Exception(
            "Git User Couldnt Not Be Found Or Connection Erorr:{}\n".format(gitUser))
    currentUserRepos = {}  # // intially empty
    jsonContentRepos = json.loads(contents)
    for reposInfo in jsonContentRepos:
        if "personalxmb" in reposInfo['name'].lower():
            continue
        oodict = {key: value
                  for key, value in reposInfo.items()
                  if key in ['id', 'description', 'html_url', 'created_at', 'updated_at', 'name']
                  }
        
        currentUserRepos[oodict['name']] = oodict
    # print(currentUserRepos)
    for key, repos in currentUserRepos.items():
        repos["created_at"] = make_aware(datetime.strptime(
            repos["created_at"], "%Y-%m-%dT%H:%M:%SZ"))
        #repos["created_at"] = repos["created_at"].strftime('%Y-%m-%d %H:%M:%S+00:00')
        repos["updated_at"] = make_aware(datetime.strptime(
            repos["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
        #repos["updated_at"] = repos["updated_at"].strftime('%Y-%m-%d %H:%M:%S+00:00')
        # print(repos["updated_at"].tzinfo)
        log.info("Sucess Getting Project {}\n".format(key))
    # print(currentUserRepos)
    return currentUserRepos, userProject


@shared_task
def generateProjects(userModelString):
    listRepos, modelUser = getUsers(userModelString)
    currentUserProjects = modelUser.projectUserHandlier.all()
    for key, repo in listRepos.items():
        project, created = currentUserProjects.get_or_create(
            projectName=key,
            defaults={
                'created': repo['created_at'],
                'last_updated': repo['updated_at'],
                'description': repo['description'] if repo['description'] is not None else " ",
                'project_link': repo['html_url'],
                'projectHandlier': modelUser,
                'project_image': None
            }
        )
        
        if project.last_updated != repo['updated_at']:
            project.last_updated = repo['updated_at']
            project.description = repo['description'] if repo['description'] is not None else " "
            project.save()
