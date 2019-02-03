# 25.01.2019
# version 1.0

import ctypes
import datetime
import sys
from pathlib import Path

def wallpaper(numer):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(Path(("PNG/{}.png").format(numer)).resolve()), 0)

wallpaper(datetime.datetime.today().weekday() + 1)

sys.exit()
