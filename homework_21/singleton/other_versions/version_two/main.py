from singleton import Singleton

if __name__ == '__main__':
    # E.g.
    s = Singleton()
    print(s)
    s1 = Singleton.getInstance()
    print(s1)
    s2 = Singleton.getInstance()
    print(s2)
    print(id(s) == id(s1))
    s3 = Singleton()
    print(s3)
