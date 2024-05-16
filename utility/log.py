from phoenix.settings_server import DEBUG
def leolog(*args, **kwargs):
    if not DEBUG:
        return
    print("")
    print("")
    print(80*"#")
    for a in kwargs:
        print(a)
        print(80*"-")
        print(kwargs[a])
        print(80*"#")
    print("")
    print("")