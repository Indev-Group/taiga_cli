import click

import style
import safe
import config

def project(project):
    return safe.array(project, ["id", "slug", "name"], withId=True)

def point(point):
    return safe.array(point, ["id", "name", "value"], withId=True)

def userstory(us, projects, users, points):
    project = projects.get(id=us.project)
    owner = users.get(id=us.owner)
    assigned = users.get(id=us.assigned_to)
    count = pointsCount(us, points)
    color = "red"
    if (count > config.usPointsMax()):
        color = "yellow"
    elif (count > 0):
        color = "green"
    pointsResult = click.style("{}".format(count),fg=color)
    return safe.array(us, ["id", "subject"], withId=True)\
        + [safe.get(assigned, "username") \
          ,style.bool(us.is_closed) \
          ,pointsResult] \
        +  safe.array(project, ["name"])

def pointsCount(us, points):
    pointsCount = 0
    for roleId in us.points:
        point = points.get(id=us.points[roleId])
        pointsCount += 0 if point.value is None else point.value
    return pointsCount
