import boto3
import json

services = ['PDC-BackendDjango-dev', 'PDC-FrontAdminDev', 'PDC-FrontDev', 'PDC-SocialFront-dev']

def scale_in_ecs(event, instanceECS):
    if instanceECS == 0:
        for service in services:
            event = 'start'
    elif instanceECS > 1:
        for service in services:
            event = 'stop'
    return None
# services - PDC-BackendDjango-dev, PDC-FrontAdminDev, PDC-FrontDev, PDC-SocialFront-dev in ECS
# 9 - 18 - quantas instâncias do ECS estão ligadas?

]