import pathlib

print(help(pathlib))

print (dir(pathlib))

from pathlib import Path
print (dir(Path))

help(pathlib.Path.iterdir)


path = Path(".")
print(type(path))


print(dir(path))

print(path.iterdir.__doc__)

