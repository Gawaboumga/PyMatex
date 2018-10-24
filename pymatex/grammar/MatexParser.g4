parser grammar MatexParser;

options {tokenVocab = MatexLexer;}

math: expr EOF;

megaExpr:
    (subtractionExpr MUL?)? specialExpr
    | (implicitMultiplicationExpr MUL?) specialExpr
    | megaExpr PLUS specialExpr
    | megaExpr MINUS specialExpr
    | megaExpr MUL specialExpr;

specialExpr:
    integralExpr
    | summationExpr
    | productExpr;

expr:
    subtractionExpr
    | implicitMultiplicationExpr
    | megaExpr;

integralExpr: FUNC_INT subexpr supexpr L_BRACE expr DERIVATIVE R_BRACE
              | FUNC_INT subexpr supexpr expr DERIVATIVE;
summationExpr: FUNC_SUM funcParams tailExpr;
productExpr: FUNC_PROD funcParams tailExpr;

tailExpr:
    expr
    | bracedExpr;

funcParams: subeq supexpr;

implicitMultiplicationExpr:
    subtractionExpr subtractionExpr
    | implicitMultiplicationExpr subtractionExpr;

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
    | multiplicationExpr (MUL | CMD_TIMES | CMD_CDOT) powExpr;

fracExpr: CMD_FRAC bracedExpr bracedExpr;

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
    | brackExpr
    | parenExpr;

variable: VARIABLE | GREEKLETTER;

indexedVariable: VARIABLE subexpr;

constant: INFINITY;

number: NUMBER;

absolute: BAR expr BAR;

factorial:
    parenExpr BANG
    | number BANG
    | variable BANG;

func:
    funcname bracedExpr
    | funcname parenExpr
    | GREEKFUNCTIONBRACE expr R_BRACE
    | GREEKFUNCTIONPAREN expr R_PAREN;

funcname:
    FUNC_LOG | FUNC_LN | FUNC_SQRT
    | FUNC_SIN | FUNC_COS | FUNC_TAN
    | FUNC_CSC | FUNC_SEC | FUNC_COT
    | FUNC_ARCSIN | FUNC_ARCCOS | FUNC_ARCTAN
    | FUNC_ARCCSC | FUNC_ARCSEC | FUNC_ARCCOT
    | FUNC_SINH | FUNC_COSH | FUNC_TANH
    | FUNC_ARCSINH | FUNC_ARCCOSH | FUNC_ARCTANH;

bracedExpr: L_BRACE expr R_BRACE;
brackExpr: L_BRACKET expr R_BRACKET;
parenExpr: L_PAREN expr R_PAREN;

subexpr: UNDERSCORE bracedExpr;
supexpr: CARET bracedExpr;
subeq: UNDERSCORE L_BRACE equality R_BRACE;

equality: variable EQ expr;

relop:
    EQ
    | LT
    | LTE
    | GT
    | GTE;
