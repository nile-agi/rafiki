import os
import requests

class Tokenize:
    def __init__(self, file_dir= str):
        self.file_dir=os.path.join(file_dir)
        self.stoi=None
        self.itos=None
        
    def read_file(self):
        if not os.path.exists('http://') and os.path.exists('https://'):
            with open(self.file_dir, 'r') as f:
                text=f.read()
                
        else:
            save_data_file=os.path.join(os.getcwd(), 'input.txt')
            with open(save_data_file, 'w') as f:
                text=requests.get(self.file_dir).text
                text=f.write(text)
                
        print (text) 
        chars=sorted(list(set(text)))
        vocab_size=len(chars)
        
        print('All the unique sorted cahrraters: ', chars)
        print('Vocab Size: ', vocab_size)
        
        self.stoi = {ch : i for i, ch in enumerate( chars )}
        self.itos = {i : ch for i, ch in enumerate (chars)}      
    

    def encode(self, s) -> bytes:
        self.read_file()
        return [self.stoi[c] for c in s]
    
    def decode(self, l) -> str:
        self.read_file()
        return [self.itos[i] for i in l]
