def conversao(celsius):
    celsius = int (celsius)
    fahrenheit = (9/5) * celsius + 32
    int (fahrenheit)
    return fahrenheit
celsius = input('digite a temperatura em celsius e converta pra faranheit ')
print (conversao(celsius)) 
