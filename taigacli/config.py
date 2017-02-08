import os
import click

ENV_API_HOST_KEY = "TAIGACLI_API_HOST"
ENV_US_TIME_MAX = "TAIGACLI_US_TIME_MAX"

US_TIME_MAX_DEFAULT = 4 # hours

def check():
    if ENV_API_HOST_KEY not in os.environ:
        click.echo("Please setup ${}".format(ENV_API_HOST_KEY))
        return False

    return True

def usPointsMax():
    if ENV_US_TIME_MAX in os.environ:
        return os.environ.get(ENV_US_TIME_MAX)
    return US_TIME_MAX_DEFAULT

def apiHost():
    if ENV_API_HOST_KEY not in os.environ:
        click.echo("Please setup ${}".format(ENV_API_HOST_KEY))
        exit()
        return None

    return os.environ.get(ENV_API_HOST_KEY)
