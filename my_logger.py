from typing import Callable, List

class Logger:
    class effect:
        DEFAULT = "0"
        HIGHLIGHT = "1"
        UNDERLINE = "4"
        BLINK = "5"
        INVERSE = "7"
        INVISIBLE = "8"

    class color:
        BLACK = 0
        RED = 1
        GREEN = 2
        YELLOW = 3
        BLUE = 4
        PURPLE = 5
        CYAN = 6
        WHITE = 7
    
    @classmethod
    def cstr(cls, message: str, color: int = None, background: int = None, effect: str = effect.DEFAULT) -> str:
        def check_param_validity(param):
            if not isinstance(param, int): return False
            if param < 0 or param > 7: return False
            return True

        mc = f";3{color}" if color and check_param_validity(color)  else ""
        bgc = f";4{background}" if check_param_validity(background) else ""
        return f"\033[{effect}{mc}{bgc}m{message}\033[0m"

    @classmethod
    def clog(cls, message: str, color: int = None, background: int = None, effect: str = effect.DEFAULT, ender: str = "\n\r") -> None:
        print(Logger.cstr(message, color, background, effect), end=ender)
    
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
                    tag_color:int = None, tag_background: int = None, tag_effect: str = effect.DEFAULT,
                    message_color:int = None, message_background:int = None, message_effect: str = effect.DEFAULT,
                    message_decorator: Callable[[str], str] = None, ender: str = "\n\r"
                    ) -> None:
        if message_decorator == None:
            message_decorator = Logger.make_message_decorator(["[", "]"], 1)
        Logger.clog(message_decorator(tag), tag_color, tag_background, tag_effect, ender="")
        Logger.clog(delimiter, ender="")
        Logger.clog(message, message_color, message_background, message_effect, ender=ender)
        

if __name__ == "__main__":
    Logger.clog("clog test", Logger.color.GREEN, Logger.color.RED, Logger.effect.UNDERLINE, ender="\nender\n")
    Logger.clog_with_tag("tag", "clog_with_log test", delimiter=">>>", tag_effect=Logger.effect.UNDERLINE, tag_background=Logger.color.BLUE, message_effect=Logger.effect.HIGHLIGHT, message_background=Logger.color.PURPLE)
