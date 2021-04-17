/*
Copyright 2021 Guillermo A. Perez

This file is part of pad-tools.

pad-tools is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pad-tools is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pad-tools. If not, see <https://www.gnu.org/licenses/>.
*/
grammar PAD;

formula    : quants qfexpr ;

quants     : QUANT VARIABLE quants  # RecQuant
           | QUANT VARIABLE ':'     # Quant
	   ;

qfexpr     : qfexpr '&&' qfexpr       # AndQFExpr
           | qfexpr '||' qfexpr       # OrQFExpr
           | neg='~'? '(' qfexpr ')'  # UnaQFExpr
	   | neg='~'? predicate       # UnaPred
	   ;

predicate  : polynomial BINOP polynomial  # Pred
	   ;

polynomial : polynomial '*' polynomial    # MultPoly
           | polynomial '+' polynomial    # SumPoly
           | polynomial '-' polynomial    # SubPoly
           | neg='-'? '(' polynomial ')'  # UnaPoly
           | neg='-'? INT                 # UnaInt
           | neg='-'? VARIABLE            # UnaVar
           ;

QUANT    : 'A' | 'E';
BINOP    : '=' | '!=' | '<' | '<=' | '>' | '>=' | '%';
VARIABLE : LETTER ( LETTER | DIGIT )*;
INT      : DIGIT+;
WS       : [ \t\r\n]+ -> skip;

fragment LETTER : [a-zA-Z];
fragment DIGIT  : [0-9];
