##Taiga CLI

####Install

```
pip install taigacli
```

####Setup

Set up local variables in taiga_cli.py

Maximum avaible points for Userstory
```
export US_TIME_MAX=4
```

Address of your taiga server
```
export TAIGACLI_API_HOST='https://taiga.io'
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
