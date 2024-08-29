from os import system, name
from colorama import Fore as colors
from pyfiglet import Figlet

class Classic:
    def __init__(self, title:str):
        self.space = ' '*10
        self.title:tuple[str, str, str, str] = Figlet(font='block', justify='center').renderText(title)
        self.fields:list[tuple[str, callable]] = []
    
    def _clear(self):
        system('cls' if name == 'nt' else 'clear')
    
    def _base(self):
        self._clear()
        print(f'\n{colors.WHITE}{self.title}{colors.RESET}')
    
    def add_field(self, field: str, func: callable):
        self.fields.append((field, func))
    
    def menu(self):
        self._base()
        
        for i, field in enumerate(self.fields):
            print(f'{self.space}{colors.LIGHTBLACK_EX}{str(i+1).zfill(2)}. {colors.WHITE}{field[0]}')
        
        result = input(f'\n{self.space[:9]}{colors.LIGHTBLACK_EX} • {colors.WHITE}')
        if result.isdigit() and 0 < int(result) <= len(self.fields):
            self._clear()
            self._base()
            self.fields[int(result)-1][1]()
        else:
            print(f'\n{self.space}{colors.RED}Veuillez entrer un nombre valide !{colors.RESET}')
        
        input(f'\n{self.space}{colors.WHITE}Appuyez sur ENTRER pour continuer...{colors.RESET}')