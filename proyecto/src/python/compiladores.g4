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

DIF : '=!';
ASIG   : '=' ;
IGUAL  : '==' ;
MAYOR  : '>'  ;
MENOR  : '<'  ;
MENORIG : '<=';
MAYORIG : '>=';
COMA    : ',';

NUMERO : DIGITO+ | DIGITO+ '.' DIGITO+ ;

INT    : 'int'   ;
DOUBLE : 'double';
LONG   : 'long'  ;
CHAR   : 'char'  ;
STRING : 'string';
WHILE  : 'while' ;
FOR    : 'for'   ;
IF     : 'if'    ;
ELSE   : 'else'  ;
RETURN : 'return';
VOID   : 'void'  ;



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


programa : declaracion* funcion*  EOF;  // desde aca arranca el parser ( se puede cambiar )

tfuncion : VOID | INT | DOUBLE | CHAR;


funcion: tfuncion ID PA parametro PC bloque;



parametro: tdato ID parametros
          |
          ;

parametros: COMA parametro parametros
            |
            ;


usofuncion : ID PA (argumentos) PC;

argumentos : opal argumentosp
            |;
argumentosp : COMA argumentos argumentosp 
            |;

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
            |usofuncion
            | return
            | PYC
            ;

return : RETURN opal PYC;

tdato : INT | DOUBLE;

declaracion : tdato ID PYC 
            | tdato ID ASIG opal PYC;

asignacion : ID ASIG opal PYC;

opal : lor; // completar

comparadores : MAYOR | MENOR | IGUAL | MENORIG | MAYORIG | DIF;

// Expresion logica

lor : land lorp;

lorp : OR land lorp
  |
  ;

land : comp landp;

landp : AND comp landp
  |
  ;

// Comparacion
comp : exp comparadores exp
  | exp;


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
      | usofuncion
      | PA exp PC
      ;




iwhile : WHILE PA opal PC instruccion;
bloque : LLA instrucciones LLC ;

ifor : FOR PA init PYC cond PYC (opal| ID SUMA SUMA | SUMA SUMA ID) PC instruccion ;

init : ID ASIG opal
      | ID
      | tdato ID 
      | tdato ID ASIG opal
      | 
      ;

cond: opal
    |
    ;

iif : IF PA opal PC instruccion (ELSE instruccion |);
  
