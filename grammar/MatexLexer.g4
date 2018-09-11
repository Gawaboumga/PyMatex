lexer grammar MatexLexer;

PLUS:      '+';
MINUS:     '-';
MUL:       '*';
DIV:       '/';

L_PAREN:   '(';
R_PAREN:   ')';
L_BRACE:   '{';
R_BRACE:   '}';
L_BRACKET: '[';
R_BRACKET: ']';
COMMA:     ',';
DOT:       '.';

BAR: '|';

FUNC_LIM:  '\\lim';
LIM_APPROACH_SYM: '\\to' | '\\rightarrow' | '\\Rightarrow' | '\\longrightarrow' | '\\Longrightarrow';
FUNC_INT:  '\\int';
FUNC_SUM:  '\\sum';
FUNC_PROD: '\\prod';

FUNC_LOG:  BACKSLASH? 'log';
FUNC_LN:   BACKSLASH? 'ln';
FUNC_SIN:  BACKSLASH? 'sin';
FUNC_COS:  BACKSLASH? 'cos';
FUNC_TAN:  BACKSLASH? 'tan';
FUNC_CSC:  BACKSLASH? 'csc';
FUNC_SEC:  BACKSLASH? 'sec';
FUNC_COT:  BACKSLASH? 'cot';

FUNC_ARCSIN: BACKSLASH? 'arcsin';
FUNC_ARCCOS: BACKSLASH? 'arccos';
FUNC_ARCTAN: BACKSLASH? 'arctan';
FUNC_ARCCSC: BACKSLASH? 'arccsc';
FUNC_ARCSEC: BACKSLASH? 'arcsec';
FUNC_ARCCOT: BACKSLASH? 'arccot';

FUNC_SINH: BACKSLASH? 'sinh';
FUNC_COSH: BACKSLASH? 'cosh';
FUNC_TANH: BACKSLASH? 'tanh';
FUNC_ARCSINH: BACKSLASH? 'arsinh';
FUNC_ARCCOSH: BACKSLASH? 'arcosh';
FUNC_ARCTANH: BACKSLASH? 'artanh';

FUNC_SQRT: BACKSLASH? 'sqrt';

CMD_TIMES: '\\times';
CMD_CDOT:  '\\cdot';
CMD_DIV:   '\\div';
CMD_FRAC:  '\\frac';

UNDERSCORE: '_';
CARET: '^';
COLON: ':';
BACKSLASH: '\\';

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
NUMBER: '-'? DIGIT* '.'? DIGIT+ ([eE][-+]? DIGIT+)?;

VARIABLE: LETTER+;
MIXNUMBER: NUMBER VARIABLE;

PI: '\\pi';
INFINITY: '\\infty';

EQ: '=';
LT: '<';
LTE: '\\leq';
GT: '>';
GTE: '\\geq';

BANG: '!';

SYMBOL: '\\' [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip;