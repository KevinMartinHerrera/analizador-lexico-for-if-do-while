from tokens import Token,TokenType
class Scanner:
    def __init__(self,text):
        self.it = iter(text) #iterar el texto
        self.curr= None # caracter actual que va iterando 
        self.advance()
        
    
    def advance(self): #ir avanzando el texto
        try:
            self.curr = next(self.it)
        except StopIteration:
            self.curr = None
        
    
    def scan(self):
        while self.curr is not None:
            if self.curr in (' ', '\n', '\t'):
                self.advance()
            elif self.curr == '(':
                return Token(TokenType.LPAREN,'(')
            elif self.curr == ')':
                return Token(TokenType.RPAREN, ')')
            elif self.curr =='f':
                self.verify('for')
                return Token(TokenType.FOR,'for')
            elif self.curr =='d':
                self.verify('do')
                return Token(TokenType.DO,'do')
            elif self.curr =='w':
                self.verify('while')
                return Token(TokenType.WHILE,'while')
            elif self.curr =='i':
                self.verify('if')
                return Token(TokenType.IF,'if')
            else:
                unknown_sequence = self.curr
                self.advance()
                while self.curr is not None and self.curr.isalpha():
                    unknown_sequence += self.curr
                    self.advance()

                return Token(TokenType.ERROR, unknown_sequence)
            
        return None
            
    
    def scanAll(self):
        tokens=[]
        while True:
            token =self.scan()
            if token is None:
                break
            tokens.append(token)
        return tokens
        
    def verify(self, text):
        for c in text:
            if self.curr is None or self.curr != c:
                raise Token(TokenType.ERROR, {text})
            self.advance()

                