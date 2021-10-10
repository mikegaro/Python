"""
    REGEX SYNTAX (Algunos)

    \d      -> digitos del 0-9
    \w      -> letra, digito u underscore
    \s      -> caracter de espacio en blanco ( )   
    \D      -> Not a digit
    \W      -> Not a word character
    \S      -> not a whitespace character
    .       -> any caracter except line break
    +       -> One or more
    {3}     -> Exactamete x veces {3} <- tres veces
    {3,5}   -> De tres a cinco veces
    {4,}    -> Cuatro o mas veces
    *       -> Cero o mas veces
    ?       -> Una o ninguna (opcional)
    ^       -> El inicio de una linea o de una string
    $       -> El final de una linea o string
    \b      -> Word boundary

    """
import re
pattern = re.compile('\\d{3} \\d{3} \\d{4}')
res = pattern.search("1234567890 jajajaja")
print(res)
res = pattern.search("llamame al 555 100 2773")
print(res.group())
res = re.search('\\d{3} \\d{3} \\d{4}',
                "llamame al 555 100 2773 o al 555 100 2772")
print(res.group())
res = re.findall('\\d{3} \\d{3} \\d{4}',
                 "llamame al 555 100 2773 o al 555 100 2772")
print(res)
