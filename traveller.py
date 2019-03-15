import math, dice


def traveltime(km, g):
    da = (km * 1000) / (g * 9.80665)
    secs = 2 * (math.sqrt(da))
    return 'Hrs: {}  Days: {}'.format(secs / 3600, secs / 86400)


def cargos(chances, dm):
    major = minor = incidental = []
    if not len(chances) == 3:
        return None
    if chances[0]:
        major = [x * 10 for x in dice.roll('{}d6'.format(dice.roll(chances[0]) + dm))]
    if chances[1]:
        minor = [x * 5 for x in dice.roll('{}d6'.format(dice.roll(chances[0]) + dm))]
    if chances[2]:
        incidental = [x * 1 for x in dice.roll('{}d6'.format(dice.roll(chances[0]) + dm))]
    print('Major cargo ({}): {}\nMinor cargo ({}): {}\nIncidental cargo ({}): {}'.format(
        len(major), major, len(minor), minor, len(incidental), incidental))
    return major, minor, incidental


def passengers(chances, dm):
    high = middle = low = ''
    if not len(chances) == 3:
        return None
    if chances[0]:
        high = max(0, dice.roll(chances[0]) + dm)
    if chances[1]:
        middle = max(0, dice.roll(chances[1]) + dm)
    if chances[2]:
        low = max(0, dice.roll(chances[1]) + dm)
    print('High passengers: {}, Middle passengers: {}, Low passengers: {}'.format(
        high, middle, low))
    return high, middle, low
