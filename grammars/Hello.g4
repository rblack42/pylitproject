// define a grammar called hello
grammar Hello;
r	: ID;
ID	: [a-z]+;
WS	: [ \t\r\n]+ -> skip;
