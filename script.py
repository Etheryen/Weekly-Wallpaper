# 03.02.2019
# version 1.1

import ctypes
import datetime
import sys
from pathlib import Path

def wallpaper(numer):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(Path(("PNG/{}.png").format(numer)).resolve()), 3)

wallpaper(datetime.datetime.today().weekday() + 1)

sys.exit()
