class myclass:
    def __init__(shri, name):      # type:ignore
        shri.name = name
        print(f"Hello {shri.name}")

myobject = myclass('Shriyansh')