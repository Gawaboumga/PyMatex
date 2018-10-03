parser grammar MatexParser;

options {tokenVocab = MatexLexer;}

math: expr EOF;

equality:
    expr EQ expr;

megaExpr:
    (variable MUL?)? specialExpr
    | megaExpr PLUS specialExpr
    | megaExpr MINUS specialExpr
    | megaExpr MUL specialExpr;

specialExpr:
    integralExpr
    | summationExpr
    | productExpr;

expr:
    subtractionExpr
    | megaExpr;

integralExpr: FUNC_INT subexpr supexpr L_BRACE expr DERIVATIVE R_BRACE
              | FUNC_INT subexpr supexpr expr DERIVATIVE;
summationExpr: FUNC_SUM funcParams tailExpr;
productExpr: FUNC_PROD funcParams tailExpr;

tailExpr:
    expr
    | L_BRACE expr R_BRACE;

funcParams: subeq supexpr;

subtractionExpr:
    additionExpr
    | subtractionExpr MINUS additionExpr;

additionExpr:
    divisionExpr
    | additionExpr PLUS divisionExpr;

divisionExpr:
    multiplicationExpr
    | divisionExpr (DIV | CMD_DIV) multiplicationExpr;

multiplicationExpr:
    powExpr
    | multiplicationExpr (MUL | CMD_TIMES | CMD_CDOT) powExpr
    | multiplicationExpr fracExpr
    | multiplicationExpr exponentiationExpr
    | multiplicationExpr atom;

fracExpr: CMD_FRAC L_BRACE expr R_BRACE L_BRACE expr R_BRACE;

powExpr:
    signedAtom
    | fracExpr
    | exponentiationExpr;

exponentiationExpr:
    signedAtom CARET number
    | signedAtom CARET variable
    | signedAtom supexpr;

signedAtom:
    negateAtom
    | localMultiplication
    | func
    | atom;

negateAtom: MINUS signedAtom;

localMultiplication: MIXNUMBER | WORD | DERIVATIVE;

atom:
    variable
    | indexedVariable
    | constant
    | number
    | absolute
    | factorial
    | L_BRACKET expr R_BRACKET
    | L_PAREN expr R_PAREN;

variable: VARIABLE | GREEKLETTER;

indexedVariable: VARIABLE subexpr;

constant: INFINITY;

number: NUMBER;

absolute: BAR expr BAR;

factorial:
    L_PAREN expr R_PAREN BANG
    | number BANG
    | variable BANG;

func:
    funcname L_BRACE expr R_BRACE
    | funcname L_PAREN expr R_PAREN;

funcname:
    FUNC_LOG | FUNC_LN | FUNC_SQRT
    | FUNC_SIN | FUNC_COS | FUNC_TAN
    | FUNC_CSC | FUNC_SEC | FUNC_COT
    | FUNC_ARCSIN | FUNC_ARCCOS | FUNC_ARCTAN
    | FUNC_ARCCSC | FUNC_ARCSEC | FUNC_ARCCOT
    | FUNC_SINH | FUNC_COSH | FUNC_TANH
    | FUNC_ARCSINH | FUNC_ARCCOSH | FUNC_ARCTANH;

subexpr: UNDERSCORE L_BRACE expr R_BRACE;
supexpr: CARET L_BRACE expr R_BRACE;
subeq: UNDERSCORE L_BRACE equality R_BRACE;
supeq: CARET L_BRACE equality R_BRACE;

relop:
    EQ
    | LT
    | LTE
    | GT
    | GTE;
