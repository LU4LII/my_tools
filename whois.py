import urllib.request
import urllib.parse

# whois scanner for.br domains
# version 1.0
# developer: LU4XLII

#função pra parser a resp da request
def decrypt(resp):
    lugar = resp.find("<pre>")
    final1 = resp.find("</pre>")
    resp = resp[lugar:final1]
    lugar = resp.find('<a href')
    while(lugar != -1):
        text1 = resp[0:lugar-1]
        final2 = resp.find('</a>')
        text2 = resp[final2+4:]
        resp = text1 + text2      
        lugar = resp.find("<a href")
    return(resp)

domain =  input("dominio: ")
domain = str.encode(domain)

#P.O.G. simples pra ter certeza que tá gerando o tipo de dado correto
print(type(domain))

#valores para a request
url = 'https://registro.br/cgi-bin/whois/'
values = {}
values['qr'] = domain

#outro P.O.G. simples
print(type(values))

#request via POST
data = urllib.parse.urlencode(values)

#P.O.G. de novo
print(type(data))
data = str.encode(data)

resp = urllib.request.urlopen(url, data).read()
resp = resp.decode('iso-8859-1')
whois = decrypt(resp)
print(whois)

#tava com preguiça de fazer um sistema  de salvamento mais complexo
teste = input("Deseja salvar? [s-sim]\n")
if(teste == 's'):
    teste = input("Digite o nome do arquivo: ")
    teste = teste + '.txt'
    arq = open(teste, "w")
    arq.write(whois)
    arq.close()
