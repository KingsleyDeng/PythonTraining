import os

def file_generator():
    for filename in os.listdir(r'.'):
        if filename.endswith(".py"):
            yield filename

if __name__ == '__main__':
    fg = file_generator()
    print(next(fg))
    print(next(fg))
    for el in fg:
        print(el, end=" ")