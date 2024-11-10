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


programa : (declaracionesp PYC)* funcion* prototipo*  EOF;  // desde aca arranca el parser ( se puede cambiar )

prototipo : tfuncion ID PA parametro PC PYC;

tfuncion : VOID | INT | DOUBLE | CHAR;


funcion: tfuncion ID PA parametro PC bloque
        ;


parametro: tdato ID parametros
          |
          ;

parametros: COMA parametro parametros
            |
            ;


usofuncion : ID PA argumentos PC;

argumentos : opal argumentosp
            |;
argumentosp : COMA argumentos argumentosp 
            |;

instrucciones : instruccion instrucciones 
              |
              ;

//instruccion : INST {print($INST.text[:-1])} ; 

instruccion : declaracionesp PYC
            | iwhile
            |ifor
            |iif 
            | bloque
            | asignacion PYC
            |usofuncion PYC
            | return PYC
            | opal PYC
            | PYC
            ;

return : RETURN opal;

tdato : INT | DOUBLE | CHAR;

declaracionesp: declaracion declaraciones;

declaraciones: COMA ID (ASIG opal)? declaraciones
              |
              ;


declaracion: tdato ID (ASIG opal)?;



asignacion : ID ASIG opal;

opal : lor; 

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

ifor : FOR PA init PYC cond PYC iter PC instruccion ;

init : asignacion
      | 
      ;

cond: opal
    |
    ;

iter : opal
      | ID SUMA SUMA 
      | SUMA SUMA ID
      | ID RESTA RESTA
      | RESTA RESTA ID
      | ID ASIG opal
      |;

iif : IF PA opal PC instruccion (ELSE instruccion |);
  
