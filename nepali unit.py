import math
def convertor(x):
    values = ' '
    ropani= x / 508.74
    values += str(math.trunc(ropani)) + ' R - '
    diff = ropani - math.trunc(ropani)
    if diff>0:
        ana = diff *16
        values += str(math.trunc(ana)) + ' A - '
        ana_diff = ana - math.trunc(ana)
        if ana_diff > 0:
            paisa = ana_diff * 4
            values += str(math.trunc(paisa)) + ' D - '
            paisa_diff = paisa - math.trunc(paisa)
            if paisa_diff >0:
                daam = round(paisa_diff * 4, 2)
                values += str (daam) + ' P '
    return values

import math
def convertor(x):
    values = ' '
    ropani= x / 508.74
    values += str(math.trunc(ropani)) + '- '
    diff = ropani - math.trunc(ropani)
    if diff>0:
        ana = diff *16
        values += str(math.trunc(ana)) + '- '
        ana_diff = ana - math.trunc(ana)
        if ana_diff > 0:
            paisa = ana_diff * 4
            values += str(math.trunc(paisa)) + '- '
            paisa_diff = paisa - math.trunc(paisa)
            if paisa_diff >0:
                daam = round(paisa_diff * 4, 2)
                values += str (daam)
    return values
print(convertor(570))