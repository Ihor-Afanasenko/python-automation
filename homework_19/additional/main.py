from carbon import Carbon
from oxygen import Oxygen
from hydrogen import Hydrogen

if __name__ == '__main__':
    # E.g.
    carbon = Carbon(4)
    hydrogen = Hydrogen()
    oxygen = Oxygen()

    diethyl_ether = 2 * carbon + hydrogen * 5
    hydrogen_two = Hydrogen()
    hydroxide = hydrogen_two + oxygen

    alcohol = diethyl_ether + hydroxide
    print(alcohol)
