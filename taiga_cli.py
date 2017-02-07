#!/usr/bin/env python

from taiga import TaigaAPI
from terminaltables import AsciiTable
import click

US_TIME_MAX = 4 # hours

API_HOST = "" #Host address https://taiga.com/
api = TaigaAPI(host=API_HOST)


@click.group()
@click.option("--username", "-u", prompt=True, help="taiga useername or email")
@click.option("--password", "-p", prompt=True, hide_input=True, help="taiga password")
def cli(username, password):
    """The taiga command interface."""
    api.auth(username=username, password=password)

@cli.command()
def projects():
    """ Get project list """
    table_data = [styleHeaders(projectTableHeaders())]
    for project in api.projects.list():
        table_data.append(projectTable(project))
    table = AsciiTable(table_data)
    click.echo(table.table)

@cli.command()
@click.option("--isOpened", "-o", "isOpened", is_flag=True, help="Show only opened userstories")
@click.option("--onlyNonPoints", "-p", "onlyNonPoints", is_flag=True, help="Show only zero points userstories")
def userstories(isOpened, onlyNonPoints):
    """ Get userstories list """
    table_data = [styleHeaders(userStoryHeaders())]
    points = api.points.list()
    projects = api.projects.list()
    users = api.users.list()

    usList  = []
    if isOpened:
        usList = api.user_stories.list().get(is_closed=False)
    else:
        usList = api.user_stories.list()

    with click.progressbar(usList) as bar:
        for us in bar:
            if onlyNonPoints:
                if pointsCount(us, points) == 0:
                    table_data.append(userStoryTable(us, projects, users, points))
            else:
                table_data.append(userStoryTable(us, projects, users, points))
    table = AsciiTable(table_data)
    click.echo(table.table)

def styleHeaders(headers):
    res = []
    for header in headers:
        res.append(click.style("{}".format(header),fg='green'))
    return res

def styleBool(obj):
    if obj == False:
        return click.style("False",fg='red')
    return click.style("True",fg='green')

def safeGet(obj, attr):
    return getattr(obj, attr, click.style("---",fg='red'))

def safeArray(obj, attrs, withId = False):
    res = []
    for attr in attrs:
        res.append(safeGet(obj, attr))
    if withId:
        res[0] = tableId(res[0])
    return res

def tableId(tableId):
    return click.style("{}".format(tableId),fg='yellow')

def projectTable(project):
    return safeArray(project, ["id", "slug", "name"], withId=True)

def pointTable(point):
    return safeArray(point, ["id", "name", "value"], withId=True)

def userStoryTable(us, projects, users, points):
    project = projects.get(id=us.project)
    owner = users.get(id=us.owner)
    assigned = users.get(id=us.assigned_to)
    count = pointsCount(us, points)
    color = "red"
    if (count > US_TIME_MAX):
        color = "yellow"
    elif (count > 0):
        color = "green"
    pointsResult = click.style("{}".format(count),fg=color)
    return safeArray(us, ["id", "subject"], withId=True)\
        + [safeGet(assigned, "username") \
          ,styleBool(us.is_closed) \
          ,pointsResult] \
        +  safeArray(project, ["name"])

def pointsCount(us, points):
    pointsCount = 0
    for roleId in us.points:
        point = points.get(id=us.points[roleId])
        pointsCount += 0 if point.value is None else point.value
    return pointsCount

def pointTableHeaders():
    return ["ID", "Name", "Value"]

def projectTableHeaders():
    return ["Project ID", "Slug", "Name"]

def userStoryHeaders():
    return ["ID", "Subject", "Assigned", "Closed", "Time"] + ["Project"]

if __name__ == "__main__":
    cli()
