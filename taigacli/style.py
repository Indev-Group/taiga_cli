import click

def headers(headers):
    res = []
    for header in headers:
        res.append(click.style("{}".format(header),fg='green'))
    return res

def bool(obj):
    if obj == False:
        return click.style("False",fg='red')
    return click.style("True",fg='green')

def tableId(tableId):
    return click.style("{}".format(tableId),fg='yellow')
