from typing import Callable, List

class Logger:
    class effect:
        DEFAULT = "0"
        HIGHLIGHT = "1"
        UNDERLINE = "4"
        BLINK = "5"
        INVERSE = "7"
        INVISIBLE = "8"

    class fg:
        DEFAULT = ""
        BLACK = ";30"
        RED = ";31"
        GREEN = ";32"
        YELLOW = ";33"
        BLUE = ";34"
        PURPLE = ";35"
        CYAN = ";36"
        WHITE = ";37"

    class bg:
        DEFAULT = ""
        BLACK = ";40"
        RED = ";41"
        GREEN = ";42"
        YELLOW = ";43"
        BLUE = ";44"
        PURPLE = ";45"
        CYAN = ";46"
        WHITE = ";47"
    
    @classmethod
    def cstr(cls, message: str, message_color: str = fg.DEFAULT, message_background: str = bg.DEFAULT, message_effect: str = effect.DEFAULT) -> str:
        return f"\033[{message_effect}{message_color}{message_background}m{message}\033[0m" 

    @classmethod
    def clog(cls, message: str, message_color: str = bg.DEFAULT, message_background: str = bg.DEFAULT, message_effect: str = effect.DEFAULT, ender: str = "\n\r") -> None:
        print(Logger.cstr(message, message_color, message_background, message_effect), end=ender)
    
    @classmethod
    def make_message_decorator(cls, decorators: List[str], index: int = 0) -> Callable[[str], str]:
        assert index >= 0 and index < len(decorators)

        def func(message: str) -> str:
            tmp = decorators.copy()
            tmp.insert(index, message)
            return "".join(tmp)
        return func

    @classmethod
    def clog_with_tag(cls, tag: str, message: str, delimiter: str=":",
                    tag_color: str = fg.DEFAULT, tag_background: str = bg.DEFAULT, tag_effect: str = effect.DEFAULT,
                    message_color: str = fg.DEFAULT, message_background: str = bg.DEFAULT, message_effect: str = effect.DEFAULT,
                    message_decorator: Callable[[str], str] = None, ender: str = "\n\r"
                    ) -> None:
        if message_decorator == None:
            message_decorator = Logger.make_message_decorator(["[", "]"], 1)
        Logger.clog(message_decorator(tag), tag_color, tag_background, tag_effect, ender="")
        Logger.clog(delimiter, ender="")
        Logger.clog(message, message_color, message_background, message_effect, ender=ender)
        

if __name__ == "__main__":
    Logger.clog("clog test", Logger.fg.GREEN, Logger.bg.RED, Logger.effect.UNDERLINE, ender="\nender\n")
    Logger.clog_with_tag("tag", "clog_with_log test", delimiter=">>>", tag_effect=Logger.effect.UNDERLINE, tag_background=Logger.bg.BLUE, message_effect=Logger.effect.HIGHLIGHT, message_background=Logger.bg.PURPLE)
