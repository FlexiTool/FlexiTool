import os
import json

class tmplr:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__))
        
        with open(os.path.join(path, 'lowercases.json'), 'r', encoding='UTF-8') as f:
            self.lowercases = json.load(f)
        
        with open(os.path.join(path, 'uppercases.json'), 'r', encoding='UTF-8') as f:
            self.uppercases = json.load(f)
        
        with open(os.path.join(path, 'numbers.json'), 'r', encoding='UTF-8') as f:
            self.numbers = json.load(f)
        
        self.chars = {**self.lowercases, **self.uppercases, **self.numbers}
    
    def transform(self, text: str):
        result:tuple[str, str, str, str] = ['', '', '', '']
        
        for char in text:
            if char in self.chars:
                result[0] += self.chars[char][0]
                result[1] += self.chars[char][1]
                result[2] += self.chars[char][2]
                result[3] += self.chars[char][3]
                
                result[0] += ' '
                result[1] += ' '
                result[2] += ' '
                result[3] += ' '
            else:
                result[0] += '  '
                result[1] += '  '
                result[2] += '  '
                result[3] += '  '
    
        return result