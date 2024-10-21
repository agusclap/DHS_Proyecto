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
COMA    : ',';

NUMERO : DIGITO+ | DIGITO+ '.' DIGITO+ ;

INT    : 'int'   ;
DOUBLE : 'double';
WHILE  : 'while' ;
FOR    : 'for'   ;
IF     : 'if'    ;
ELSE   : 'else'  ;
RETURN : 'return';



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


tdato : INT | DOUBLE;

declaracion : tdato ID PYC 
            | tdato ID ASIG opal;

asignacion : ID ASIG opal;

opal : lor; // completar

comparadores : AND || OR;

// Expresion logica

lor : land lorp;

lorp : OR land lor
  | land
  |
  ;

land : comp landp;

landp : AND comp land
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
      | PA exp PC
      ;




iwhile : WHILE PA opal PC instruccion;
bloque : LLA instrucciones LLC ;

ifor : FOR PA asignacion PYC opal PYC opal PC instruccion ;


iif : IF PA opal PC LLA instruccion PYC LLC ( |ielse);

ielse: ELSE bloque;
