#!/usr/bin/env python3

import cgitb
import cgi

''' cgitb.enable: enables exception handling in HTML format for CGI errors.
display=0: error details will only be logged in
a log file, which is specified by logdir. '''
cgitb.enable(display=0, logdir="./")


''' form: has all the data sent by the HTML form and -> form.getvalue(): gets the value
associated with each field on the form.

received: retrieves the value to be converted.
unity1: retrieves the unit the value is in.
unity2: retrieves the unit the value will be placed in.
result_final: initializes the final result variable initially as an empty string.'''
form = cgi.FieldStorage()
received = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
result_final = ''

def analyze_value(value):
    '''analyze_value: converts the received value (value) into an integer.
     return: returns -1 if the value cannot be converted.'''

    if value:
        return int(value)
    return -1

try:
    '''analyze_value: parses the value of the 'value' parameter and if there is an exception
    the value is defined as'typeError'.'''
    value = analyze_value(received)
except:
    value = 'typeError'

def convert_units(value, unity1, unity2):
    '''convert_units: receives the value, unity1 and unity2 to perform checks and conversions
     of the units.
    
    parameters:
      value: value chosen to be converted.
      unity1: unit in which the value is located.
      unity2: unit in which the value should be converted.
    
    returns: returns error messages if values are invalid or the result of conversions.'''

    if value == -1:
        return 'Erro: Campos sem valores!'
    elif value == 'typeError':
        return 'Erro: Tipo de valor inesperado!'
    elif unity1 == 'sel' or unity2 == 'sel':
        return 'Erro: Selecione uma unidade!'
    elif unity1 == unity2 and unity1 != 'sel':
        if unity1 == 'cel':
            return 'Unidades iguais => {:.2f} Graus Celsius'.format(value)
        elif unity1 == 'kel':
            return 'Unidades iguais => {:.2f} Kelvin'.format(value)
        else:
            return 'Unidades iguais => {:.2f} Graus Fahrenheit'.format(value)
    elif unity1 == 'cel':
        if unity2 == 'kel':
            return '{} Graus Celsius = {:.2f} Kelvin'.format(value, (value + 273.15))
        elif unity2 == 'fah':
            return '{} Graus Celsius = {:.2f} Graus Fahrenheit'.format(value, ((1.8 * value) + 32))
    elif unity1 == 'fah':
        if unity2 == 'cel':
            return '{} Graus Fahrenheit = {:.2f} Graus Celsius'.format(value, ((value - 32) / 1.8))
        elif unity2 == 'kel':
            return '{} Graus Fahrenheit = {:.2f} Kelvin'.format(value, (((value - 32) * 5) / 273.15))
    elif unity1 == 'kel':
        if unity2 == 'cel':
            return '{} Kelvin = {:.2f} Graus Celsius'.format(value, (value - 273.15))
        elif unity2 == 'fah':
            return '{} Kelvin = {:.2f} Graus Fahrenheit'.format(value, ((value - 273.15) * 1.8) + 32)
    return 'Erro: Selecione uma unidade!'

try:
    '''when performing unit conversion, if an exception occurs,
     the value of result_final is defined as 'Erro Inesperado'.'''
    result_final = convert_units(value, unity1, unity2)
except:
    result_final = 'Erro inesperado.'

'''prints: print the header and body of the HTML response, displaying the 
result and error message, if any.'''
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Temperatura</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(result_final))
print('<a class="back" href="../temperatura.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")