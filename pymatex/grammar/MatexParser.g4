parser grammar MatexParser;

options {tokenVocab = MatexLexer;}

math: expr EOF;

megaExpr:
    subtractionExpr MUL? specialExpr
    | implicitMultiplicationExpr MUL? specialExpr
    | megaExpr PLUS specialExpr
    | megaExpr MINUS specialExpr
    | megaExpr MUL specialExpr
    | specialExpr;

specialExpr:
    integralExpr
    | continuedFactionExpr
    | continuedFactionInequalityExpr
    | continuedFactionSetExpr
    | summationExpr
    | summationInequalityExpr
    | summationSetExpr
    | productExpr
    | productInequalityExpr
    | productSetExpr;

expr:
    subtractionExpr
    | implicitMultiplicationExpr
    | megaExpr;

integralExpr: FUNC_INT subexpr supexpr L_BRACE expr DERIVATIVE R_BRACE
              | FUNC_INT subexpr supexpr expr DERIVATIVE;
continuedFactionExpr: FUNC_FRAC funcParams tailExpr;
continuedFactionInequalityExpr: FUNC_FRAC funcIneqParams tailExpr;
continuedFactionSetExpr: FUNC_FRAC funcSetParams tailExpr;
summationExpr: FUNC_SUM funcParams tailExpr;
summationInequalityExpr: FUNC_SUM funcIneqParams tailExpr;
summationSetExpr: FUNC_SUM funcSetParams tailExpr;
productExpr: FUNC_PROD funcParams tailExpr;
productInequalityExpr: FUNC_PROD funcIneqParams tailExpr;
productSetExpr: FUNC_PROD funcSetParams tailExpr;

tailExpr:
    expr
    | bracedExpr;

funcParams: subeq supexpr;
funcIneqParams: subIneq supexpr?;
funcSetParams: subSet supexpr?;

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
    | exactDivision
    | factorial
    | binomial
    | brackExpr
    | parenExpr;

variable: VARIABLE | GREEKLETTER;

indexedVariable: VARIABLE subexpr;

constant: INFINITY;

number: NUMBER;

absolute: BAR expr BAR;

exactDivision: VARIABLE BAR VARIABLE;

factorial:
    parenExpr BANG
    | number BANG
    | variable BANG;

binomial: FUNC_BINOMIAL bracedExpr bracedExpr;

func:
    funcname bracedMultiExpr
    | funcname parenMultiExpr
    | (LETTERFUNCTIONBRACE | GREEKFUNCTIONBRACE) multiExpr R_BRACE
    | (LETTERFUNCTIONPAREN | GREEKFUNCTIONPAREN) multiExpr R_PAREN;

funcname:
    FUNC_LOG | FUNC_LN | FUNC_SQRT
    | FUNC_SIN | FUNC_COS | FUNC_TAN
    | FUNC_CSC | FUNC_SEC | FUNC_COT
    | FUNC_ARCSIN | FUNC_ARCCOS | FUNC_ARCTAN
    | FUNC_ARCCSC | FUNC_ARCSEC | FUNC_ARCCOT
    | FUNC_SINH | FUNC_COSH | FUNC_TANH
    | FUNC_ARCSINH | FUNC_ARCCOSH | FUNC_ARCTANH
    | FUNC_ECOS | FUNC_EDELTAAMPLITUDE | FUNC_ESIN
    | FUNC_ARCECOS | FUNC_ARCEDELTAAMPLITUDE | FUNC_ARCESIN;


bracedMultiExpr: L_BRACE multiExpr R_BRACE;
parenMultiExpr: L_PAREN multiExpr R_PAREN;
multiExpr:
    expr
    | multiExpr (COMMA | SEMICOLON) expr;

bracedExpr: L_BRACE expr R_BRACE;
brackExpr: L_BRACKET expr R_BRACKET;
parenExpr: L_PAREN expr R_PAREN;

subexpr: UNDERSCORE bracedExpr;
supexpr: CARET bracedExpr;
subeq: UNDERSCORE L_BRACE equality R_BRACE;

subIneq: UNDERSCORE L_BRACE inequality R_BRACE;
subSet: UNDERSCORE L_BRACE setExpr R_BRACE;

equality: variable EQ expr;
inequality:
    (variable | number) INEQUALITIES (variable | number)
    | inequality INEQUALITIES (variable | number);
setExpr:
    variable SET_IN variable
    | variable SET_IN setDifferenceExpr;
setDifferenceExpr: variable (SET_DIFFERENCE L_BRACE (number | variable) R_BRACE);
