import click

import style

def get(obj, attr):
    return getattr(obj, attr, click.style("---",fg='red'))

def array(obj, attrs, withId = False):
    res = []
    for attr in attrs:
        res.append(get(obj, attr))
    if withId:
        res[0] = style.tableId(res[0])
    return res

def iter(obj):
    if hasattr(obj, '__iter__'):
        return obj
    else:
        return [obj]
