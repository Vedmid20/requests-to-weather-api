from abc import ABC, abstractmethod
import colorama


class Layout(ABC):
    @abstractmethod
    def parsing(self):
        pass


title = lambda text: f'{colorama.Fore.LIGHTYELLOW_EX + "- "+text+" -" + colorama.Style.RESET_ALL}'
pretty_date = lambda text: f'{colorama.Fore.LIGHTCYAN_EX + "- "+text+" -" + colorama.Style.RESET_ALL}'