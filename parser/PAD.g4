grammar PAD;

formula    : quants qfexpr ;

quants     : quant=('E' | 'A') VARIABLE quants  # RecQuant
           | quant=('E' | 'A') VARIABLE ':'     # Quant
	   ;

qfexpr     : qfexpr '&&' qfexpr       # AndQFExpr
           | qfexpr '||' qfexpr       # OrQFExpr
           | neg='~'? '(' qfexpr ')'  # UnaQFExpr
	   | neg='~'? predicate       # UnaPred
	   ;

predicate  : polynomial pred=('=' | '!=' | '<' | '<=' | '>' | '>=' | '|') polynomial  # Pred
	   ;

polynomial : polynomial '*' polynomial    # MultPoly
           | polynomial '+' polynomial    # SumPoly
           | polynomial '-' polynomial    # SubPoly
           | neg='-'? '(' polynomial ')'  # UnaPoly
           | neg='-'? atom                # UnaAtom
           ;

atom : INT | VARIABLE;

VARIABLE : LETTER ( LETTER | DIGIT )*;
INT      : DIGIT+;
WS       : [ \t\r\n]+ -> skip;

fragment LETTER : [a-zA-Z];
fragment DIGIT  : [0-9];
