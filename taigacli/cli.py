#!/usr/bin/env python

from taiga import TaigaAPI
from terminaltables import AsciiTable
import click

import style
import headers
import content
import config
import safe


api = TaigaAPI(host=config.apiHost())

@click.group()
@click.option("--username", "-u", prompt=True, help="taiga useername or email")
@click.option("--password", "-p", prompt=True, hide_input=True, help="taiga password")
def cli(username, password):
    """The taiga command interface."""
    if config.check():
        api.auth(username=username, password=password)
    else:
        exit()

@cli.command()
def projects():
    """ Get project list """
    table_data = [style.headers(headers.project())]
    for project in api.projects.list():
        table_data.append(content.project(project))
    table = AsciiTable(table_data)
    click.echo(table.table)

@cli.command()
@click.option("--isOpened", "-o", "isOpened", is_flag=True, help="Show only opened userstories")
@click.option("--onlyNonPoints", "-p", "onlyNonPoints", is_flag=True, help="Show only zero points userstories")
def userstories(isOpened, onlyNonPoints):
    """ Get userstories list """
    table_data = [style.headers(headers.userstory())]
    points = api.points.list()
    projects = api.projects.list()
    users = api.users.list()

    usList  = []
    if isOpened:
        usList = api.user_stories.list().get(is_closed=False)
    else:
        usList = api.user_stories.list()

    with click.progressbar(safe.iter(usList)) as bar:
        for us in bar:
            if onlyNonPoints:
                if content.pointsCount(us, points) == 0:
                    table_data.append(content.userstory(us, projects, users, points))
            else:
                table_data.append(content.userstory(us, projects, users, points))
    table = AsciiTable(table_data)
    click.echo(table.table)

if __name__ == "__main__":
    cli()
