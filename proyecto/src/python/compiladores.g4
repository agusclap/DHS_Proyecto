grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

//INST : (LETRA | DIGITO | {,()();+=-}) '\n' ;
PA     : '(' ;
PC     : ')' ;
LLA    : '{' ;
LLC    : '}' ;
PYC    : ';' ;
SUMA : '+' ;
RESTA : '-';
MULT : '*';
DIV : '/';
MOD : '%';
AND : '&&';
OR : '||';
ORX : '^';

ASIG   : '=' ;
IGUAL  : '==' ;
MAYOR  : '>'  ;
MENOR  : '<'  ;
MENORIG : '<=';
MAYORIG : '>=';

NUMERO : DIGITO+ ;

INT    : 'int'   ;
WHILE  : 'while' ;
FOR    : 'for'   ;
IF     : 'if'    ;



ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \t\n\r] -> skip;

OTRO : . ;

// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
//   | WHILE   {print("WHILE ->" + $WHILE.text + "<--") }     s
//   | EOF
//   ;

  /*si : s EOF;

  s : PA s PC s
    |
    ;*/
// Verifica el balance de los parentesis lo de aca arriba


programa : instrucciones EOF;  // desde aca arranca el parser ( se puede cambiar )

instrucciones : instruccion instrucciones 
              |
              ;

//instruccion : INST {print($INST.text[:-1])} ; 

instruccion : declaracion
            | iwhile
            |ifor
            |iif 
            | bloque
            | asignacion
            | PYC
            ;

declaracion : INT ID PYC 
            | INT ID ASIG opal;

asignacion : ID ASIG opal;

opal : exp ; // completar

exp : term e;

e :   SUMA term e
    | RESTA term e
    |
    ;

term : factor t;
t    : MULT factor t
      |DIV factor t
      |MOD factor t
      |
      ;

factor :  NUMERO
      | ID
      | PA exp PC
      ;




iwhile : WHILE PA ID PC instruccion;
bloque : LLA instrucciones LLC ;

ifor : FOR PA init PYC cond PYC iter PC instruccion ;

 init : asignacion ;
 cond : (ID|NUMERO) MENOR (ID|NUMERO)
        | (ID|NUMERO) MAYOR (ID|NUMERO)
        | (ID|NUMERO) MAYORIG (ID|NUMERO)
        | (ID|NUMERO) MENORIG (ID|NUMERO)
        | (ID|NUMERO) IGUAL (ID|NUMERO);
iter : ID exp 
      |ID SUMA SUMA
      | SUMA SUMA ID
      | ID RESTA RESTA
      | RESTA RESTA ID;

iif : IF PA cond PC LLA instruccion PYC LLC;