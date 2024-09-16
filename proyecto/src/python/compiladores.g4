grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

PA     : '(' ;
PC     : ')' ;
PYC    : ';' ;

ASIG   : '=' ;
IGUAL  : '==' ;

NUMERO : DIGITO+ ;

WHILE  : 'while' ;
FOR    : 'for'   ;
IF     : 'if'    ;

WS : [ \t\n\r] -> skip;
/* 
OTRO : . ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

s : ID     {print("ID ->" + $ID.text + "<--") }         s
  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  | WHILE   {print("WHILE ->" + $WHILE.text + "<--") }     s
  | EOF
  ;*/

  si : s EOF;

  s : PA s PC s
    |
    ;
// Verifica el balance de los parentesis lo de aca arriba