import os


def new_walk(path: str, level=0, indent=''):
    """
    Makes directories map for a relative path. Prints directories structure.
    """

    if level == 0:
        os.chdir(os.getcwd() + path)
        path = os.getcwd()
        root = path.split('/')[-1] + '\\̚'
        print(root)
        indent = root

    for node in os.listdir(path):
        if os.path.isdir(path + '/' + node):
            current_directory = ' ' * len(indent) + f'∟{node}\\̚'
            if not os.listdir(f'{path}/{node}/.'):
                current_directory = ' ' * len(indent) + f'∟{node}\\'
            print(current_directory)
            new_walk(f'{path}/{node}', level + 1, indent + f'∟{node}\\̚')
        else:
            print(' ' * len(indent) + f'+{node}')


new_walk('/..')  # E.g.
