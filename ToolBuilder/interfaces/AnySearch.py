from os import system, name
from colorama import Fore as colors
from ToolBuilder.fonts import tmplr

class AnySearch:
    def __init__(self, title:str, subtitles: list[str], color: str = colors.LIGHTRED_EX):
        self.space = ' '*10
        self.title:tuple[str, str, str, str] = tmplr().transform(title)
        self.subtitles = subtitles
        self.color = color
        self.fields:list[tuple[str, callable]] = []
    
    def _clear(self):
        system('cls' if name == 'nt' else 'clear')
    
    def _base(self):
        self._clear()
        
        print(
            f'\n{self.space}{self.color}{self.title[0]}{colors.RESET}',
            f'\n{self.space}{self.color}{self.title[1]}{colors.RESET}',
            f'\n{self.space}{self.color}{self.title[2]}{colors.RESET}',
            f'\n{self.space}{self.color}{self.title[3]}{colors.RESET}'
        )
        
        for subtitle in self.subtitles:
            print(f'{self.space}{self.color}⚡ {colors.WHITE}{subtitle}{colors.RESET}')
    
    def add_field(self, field: str, func: callable):
        self.fields.append((field, func))
    
    def menu(self):
        self._base()
        
        print('')
        for i, field in enumerate(self.fields):
            print(f'{self.space}{self.color}• {colors.WHITE}({self.color}{str(i+1).zfill(2)}{colors.WHITE}) {field[0]}')
        
        result = input(f'{self.space}{self.color}└─ • {colors.WHITE}')
        if result.isdigit() and 0 < int(result) <= len(self.fields):
            self._clear()
            self._base()
            print()
            self.fields[int(result)-1][1]()
        else:
            print(f'\n{self.space}{colors.RED}Veuillez entrer un nombre valide !{colors.RESET}')
        
        input(f'\n{self.space}{colors.WHITE}Appuyez sur ENTRER pour continuer...{colors.RESET}')