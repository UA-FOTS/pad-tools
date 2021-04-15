grammar PAD;

formula    : quants qf_expr ;

quants     : ( 'E' | 'A' ) VARIABLE quants
           | ( 'E' | 'A' ) VARIABLE ':'
	   ;

qf_expr    : qf_expr ( '||' | '&&' ) qf_expr
           | '~'? '(' qf_expr ')'
	   | '~'? predicate
	   ;

predicate  : polynomial ( '=' | '!=' ) polynomial
           | polynomial ( '<' | '<=' ) polynomial
	   | polynomial ( '>' | '>=' ) polynomial
	   | polynomial '%' polynomial
	   ;

polynomial : polynomial '*' polynomial
           | polynomial ( '+' | '-' ) polynomial
           | '-'? '(' polynomial ')'
           | '-'? atom 
           ;

atom : INT | VARIABLE;

VARIABLE : LETTER ( LETTER | DIGIT )*;
INT      : DIGIT+;
WS       : [ \t\r\n]+ -> skip;

fragment LETTER : [a-zA-Z];
fragment DIGIT  : [0-9];
