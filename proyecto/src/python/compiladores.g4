grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

INST : (LETRA | DIGITO | {,()();+=-}) '\n' ;
PA     : '(' ;
PC     : ')' ;
LLA    : '{' ;
LLC    : '}' ;
PYC    : ';' ;

ASIG   : '=' ;
IGUAL  : '==' ;

NUMERO : DIGITO+ ;

INT    : 'int'   ;
WHILE  : 'while' ;
FOR    : 'for'   ;
IF     : 'if'    ;

WS : [ \t\n\r] -> skip;

OTRO : . ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

s : ID     {print("ID ->" + $ID.text + "<--") }         s
  | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
  | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  | WHILE   {print("WHILE ->" + $WHILE.text + "<--") }     s
  | EOF
  ;

  /*si : s EOF;

  s : PA s PC s
    |
    ;*/
// Verifica el balance de los parentesis lo de aca arriba


programa : instrucciones EOF;

instrucciones : instruccion instrucciones 
              |
              ;

//instruccion : INST {print($INST.text[:-1])} ; 

instruccion : declaracion
            | iwhile
            | bloque
            ;

declaracion : INT ID PYC ;
iwhile : WHILE PA ID PC ;
bloque : LLA instrucciones LLC ;