import os

from .exceptions import MissingEnvironmentVariable


def load_credentials():
    credentials = {
        "artifactory_password": os.getenv('ARTIFACTORY_PASSWORD'),
        "artifactory_username": os.getenv('ARTIFACTORY_USERNAME'),
        "artifactory_url": os.getenv('ARTIFACTORY_URL')
    }

    for key in credentials:
        if credentials[key] is None:
            raise MissingEnvironmentVariable(key.upper())

    return credentials

def load_slack_credentials():
    """Get slack credentials from environment variables
    
    Returns False if no credentials set.

    """

    slack_credentials = {
        "api_token": os.getenv('SLACK_API_TOKEN', False),
        "slack_channel": os.getenv('SLACK_CHANNEL', False)
    }

    if not slack_credentials['api_token'] and not slack_credentials['slack_channel']:
        slack_credentials = False

    return slack_credentials