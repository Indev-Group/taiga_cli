##Taiga CLI

Install requirements:

```
pip install -r requirements.txt
```

Set up local variables in taiga_cli.py

Maximum avaible points for Userstory
```
US_TIME_MAX
```

Address your taiga server
```
API_HOST
```

####Usage

```
Usage: taiga_cli.py [OPTIONS] COMMAND [ARGS]...

  The taiga command interface.

Options:
  -u, --username TEXT  taiga useername or email
  -p, --password TEXT  taiga password
  --help               Show this message and exit.

Commands:
  projects     Get project list
  userstories  Get userstories list
    -o, --isOpened        Show only opened Userstories
    -p, --onlyNonPoints   Show only zero points Userstories
```
