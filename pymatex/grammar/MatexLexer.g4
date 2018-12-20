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

UNDERSCORE: '_';
CARET: '^';
COLON: ':';
fragment BACKSLASH: '\\';

FUNC_LIM:  '\\lim';
LIM_APPROACH_SYM: '\\to' | '\\rightarrow' | '\\Rightarrow' | '\\longrightarrow' | '\\Longrightarrow';
FUNC_FRAC: 'K';
FUNC_INT:  '\\int';
FUNC_SUM:  '\\sum';
FUNC_PROD: '\\prod';

fragment ARC: 'arc';

FUNC_LOG: BACKSLASH? 'log';
FUNC_LN:  BACKSLASH? 'ln';
FUNC_SIN: BACKSLASH? 'sin';
FUNC_COS: BACKSLASH? 'cos';
FUNC_TAN: BACKSLASH? 'tan';
FUNC_CSC: BACKSLASH? 'csc';
FUNC_SEC: BACKSLASH? 'sec';
FUNC_COT: BACKSLASH? 'cot';

FUNC_ARCSIN: BACKSLASH? ARC FUNC_SIN;
FUNC_ARCCOS: BACKSLASH? ARC FUNC_COS;
FUNC_ARCTAN: BACKSLASH? ARC FUNC_TAN;
FUNC_ARCCSC: BACKSLASH? ARC FUNC_CSC;
FUNC_ARCSEC: BACKSLASH? ARC FUNC_SEC;
FUNC_ARCCOT: BACKSLASH? ARC FUNC_COT;

FUNC_SINH: BACKSLASH? 'sinh';
FUNC_COSH: BACKSLASH? 'cosh';
FUNC_TANH: BACKSLASH? 'tanh';
FUNC_ARCSINH: BACKSLASH? ARC FUNC_SINH;
FUNC_ARCCOSH: BACKSLASH? ARC FUNC_COSH;
FUNC_ARCTANH: BACKSLASH? ARC FUNC_TANH;

FUNC_ECOS: BACKSLASH? 'cn';
FUNC_ESIN: BACKSLASH? 'sn';
FUNC_EDELTAAMPLITUDE: BACKSLASH? 'dn';
FUNC_ARCECOS: BACKSLASH? ARC FUNC_ECOS;
FUNC_ARCESIN: BACKSLASH? ARC FUNC_ESIN;
FUNC_ARCEDELTAAMPLITUDE: BACKSLASH? ARC FUNC_EDELTAAMPLITUDE;

FUNC_SQRT: BACKSLASH? 'sqrt';
FUNC_BINOMIAL: BACKSLASH? 'binom';

CMD_TIMES: '\\times';
CMD_CDOT:  '\\cdot';
CMD_DIV:   '\\div';
CMD_FRAC:  '\\frac';

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
NUMBER: DIGIT* '.'? DIGIT+ ([eE][-+]? DIGIT+)?;
DERIVATIVE: 'd' LETTER;

VARIABLE: LETTER;
MIXNUMBER: NUMBER VARIABLE+;
WORD: VARIABLE+;

INFINITY: '\\infty';

EQ: '=';
fragment LT: '<';
fragment LTE: '\\leq';
fragment GT: '>';
fragment GTE: '\\geq';
INEQUALITIES: LT | LTE | GT | GTE;

BANG: '!';

fragment ALPHA: '\\alpha' | '\\Alpha';
fragment BETA: '\\beta' | '\\Beta';
fragment GAMMA: '\\gamma' | '\\Gamma';
fragment DELTA: '\\delta' | '\\Delta';
fragment EPSILON: '\\epsilon' | '\\Epsilon';
fragment ZETA: '\\zeta' | '\\Zeta';
fragment ETA: '\\eta' | '\\Eta';
fragment THETA: '\\theta' | '\\Theta';
fragment IOTA: '\\iota' | '\\Iota';
fragment KAPPA: '\\kappa' | '\\Kappa';
fragment LAMBDA: '\\lambda' | '\\Lambda';
fragment MU: '\\mu' | '\\Mu';
fragment NU: '\\nu' | '\\Nu';
fragment XI: '\\xi' | '\\Xi';
fragment OMICRON: '\\omicron' | '\\Omicron';
fragment PI: '\\pi' | '\\Pi';
fragment RHO: '\\rho' | '\\Rho';
fragment SIGMA: '\\sigma' | '\\Sigma';
fragment TAU: '\\tau' | '\\Tau';
fragment UPSILON: '\\upsilon' | '\\Upsilon';
fragment PHI: '\\phi' | '\\Phi';
fragment CHI: '\\chi' | '\\Chi';
fragment PSI: '\\psi' | '\\Psi';
fragment OMEGA: '\\omega' | '\\Omega';

GREEKLETTER:
    ALPHA | BETA | GAMMA | DELTA | EPSILON | ZETA | ETA |
    THETA | IOTA | KAPPA | LAMBDA | MU | NU | XI |  OMICRON |
    PI | RHO | SIGMA | TAU | UPSILON | PHI | CHI | PSI | OMEGA;

fragment INDICED: (UNDERSCORE L_BRACE (VARIABLE | NUMBER | GREEKLETTER) R_BRACE);

LETTERFUNCTIONBRACE: LETTER INDICED? L_BRACE;
LETTERFUNCTIONPAREN: LETTER INDICED? L_PAREN;
GREEKFUNCTIONBRACE: GREEKLETTER INDICED? L_BRACE;
GREEKFUNCTIONPAREN: GREEKLETTER INDICED? L_PAREN;

WS: [ \t\r\n]+ -> skip;
