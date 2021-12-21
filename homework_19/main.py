from carbon import Carbon
from hydrogen import Hydrogen

if __name__ == '__main__':
    # E.g.
    carbon = Carbon(4)
    hydrogen = Hydrogen()
    print(carbon + hydrogen * 4)

    carbon2 = Carbon(4)
    hydrogen2 = Hydrogen()
    print(4 * hydrogen2 + carbon2)
