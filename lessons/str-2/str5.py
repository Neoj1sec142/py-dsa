# ######## 2.18 ###########
'''
You have a string that you want 
to parse left to right into a 
stream of tokens.
'''
# text = 'foo = 23 + 42 * 10'
# tokens = [('NAME', 'foo'), ('EQ', '='), 
#           ('NUM', '23'), ('PLUS', '+'),
#           ('NUM', '42'), ('TIMES', '*'),
#           ('NUM', '10')]
# import re
# NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
# NUM = r'(?P<NUM>\d+)'
# PLUS = r'(?P<PLUS>\+)'
# TIMES = r'(?P<TIMES>\*)'
# EQ = r'(?P<EQ>=)'
# WS = r'(?P<WS>\s+)'
# master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
# scanner = master_pat.scanner('foo = 42')
# print(scanner.match())
# To clean this up we can package it into
# a generator:
# from collections import namedtuple
# Token = namedtuple('Token', ['type', 'value'])
# def generate_tokens(pat, text):
#     scanner = pat.scanner(text)
#     for m in iter(scanner.match, None):
#         yield Token(m.lastgroup, m.group())

# IN USE W/ Filter
# tokens = (tok for tok in 
#           generate_tokens(master_pat, text)
#           if tok.type != 'WS')
# for token in tokens:
#     print(token)


# ######## 2.19 ###########
'''
You need to parse text according 
to a set of grammar rules and perform 
actions or build an abstract syntax 
tree representing the input. The 
grammar is small, so you'd prefer 
to just write the parser yourself as 
opposed to using some kind of framework.
a simple recipe that shows how to build 
a recursive descent expression evaluator:
'''
import re
import collections
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>\/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))
Token = collections.namedtuple('Token', ['type', 'value'])
def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser. Each Method
    implements a single grammar rule.  Use the ._accept() method
    to test and accept the current lookahead token.  Use the ._expect()
    method to exactly match and discard the next token on on the input
    (or raise a SyntaxError if it doesn't match).
    '''
    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()
    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False
    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected', toktype)
    def expr(self):
        "expression ::= term { ('+'|'-') term }*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval
    def term(self):
        "term ::= factor { ('*'|'/') } factor"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval
    def factor(self):
        "factor ::= NUM | ( expr )"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else: 
            raise SyntaxError('Expected a NUMBER or LPAREN')
        
# e = ExpressionEvaluator()
# print(e.parse('2'))
# print(e.parse('2 * 3 + 3'))
# print(e.parse('2 * (3 + 3)'))
'''
If you want to do something other than pure
evaluation, you need to change the class, EX:
'''
class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        "expression ::= term { ('+'|'-') term }"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval
    def term(self):
        "term ::= factor { ('*'|'/') factor }"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval
    def factor(self):
        'factor ::= NUM | ( expr )'
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected a NUMBER or LPAREN')
# IN USE
# e = ExpressionTreeBuilder()
# print(e.parse('2 + 3'))
# print(e.parse('2 + 3 * 4'))
# print(e.parse('2 + (3 + 4) * 5'))
# print(e.parse('2 + 3 + 4'))
# ######## 2.20 ###########
''''''
