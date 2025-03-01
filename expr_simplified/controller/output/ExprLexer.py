# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,
        5,1,5,1,6,4,6,33,8,6,11,6,12,6,34,1,7,1,7,1,8,4,8,40,8,8,11,8,12,
        8,41,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,2,
        1,0,48,57,3,0,9,10,13,13,32,32,46,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,21,1,0,0,0,5,23,1,0,0,0,7,25,1,0,
        0,0,9,27,1,0,0,0,11,29,1,0,0,0,13,32,1,0,0,0,15,36,1,0,0,0,17,39,
        1,0,0,0,19,20,5,43,0,0,20,2,1,0,0,0,21,22,5,45,0,0,22,4,1,0,0,0,
        23,24,5,42,0,0,24,6,1,0,0,0,25,26,5,47,0,0,26,8,1,0,0,0,27,28,5,
        40,0,0,28,10,1,0,0,0,29,30,5,41,0,0,30,12,1,0,0,0,31,33,3,15,7,0,
        32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,14,1,
        0,0,0,36,37,7,0,0,0,37,16,1,0,0,0,38,40,7,1,0,0,39,38,1,0,0,0,40,
        41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,6,8,0,
        0,44,18,1,0,0,0,3,0,34,41,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUBTRACT = 2
    MULTI = 3
    DIVI = 4
    LEFT_PARENTH = 5
    RIGHT_PARENTH = 6
    ID = 7
    DIGIT = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUBTRACT", "MULTI", "DIVI", "LEFT_PARENTH", "RIGHT_PARENTH", 
            "ID", "DIGIT", "WS" ]

    ruleNames = [ "ADD", "SUBTRACT", "MULTI", "DIVI", "LEFT_PARENTH", "RIGHT_PARENTH", 
                  "ID", "DIGIT", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


