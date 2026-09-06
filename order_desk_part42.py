# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: OrderDesk
import sys, os

if sys.platform != "win32":
    os.environ["TERM"] = "xterm-256color"

class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    FG_DEFAULT = "\033[39m"
    BG_DEFAULT = "\033[49m"
    FG_RED = "\033[91m"
    FG_GREEN = "\033[92m"
    FG_YELLOW = "\033[93m"
    FG_BLUE = "\033[94m"
    FG_MAGENTA = "\033[95m"
    FG_CYAN = "\033[96m"
    FG_WHITE = "\033[97m"

def colorize(text, fg=None, bg=None, bold=False, dim=False, underline=False, blink=False, reverse=False, hidden=False):
    if not colors_enabled():
        return text
    codes = []
    if bold: codes.append(C.BOLD)
    if dim: codes.append(C.DIM)
    if underline: codes.append(C.UNDERLINE)
    if blink: codes.append(C.BLINK)
    if reverse: codes.append(C.REVERSE)
    if hidden: codes.append(C.HIDDEN)
    if fg: codes.append(fg)
    if bg: codes.append(bg)
    codes.append(C.RESET)
    return "".join(codes) + text

def colors_enabled():
    if os.environ.get("ORDERDESK_NO_COLOR"):
        return False
    if sys.platform == "win32":
        return True
    return True
