# whois scanner for.br domains
# version 1.0
# developer: LU4XLII

from urllib import request, parse


# função pra parser a resp da request
def decrypt(resp):
    lugar = resp.find("<pre>")
    final1 = resp.find("</pre>")
    resp = resp[lugar:final1]
    lugar = resp.find('<a href')
    while lugar != -1:
        text1 = resp[0:lugar - 1]
        final2 = resp.find('</a>')
        text2 = resp[final2 + 4:]
        resp = text1 + text2
        lugar = resp.find("<a href")
    return resp


domain = input("dominio: ")
domain = str.encode(domain)

if not isinstance(domain, bytes):
    print("Wrong type, expected 'bytes' instead of %s" %(type(domain)))
    exit(-1)

# valores para a request
url = 'https://registro.br/cgi-bin/whois/'
values = {'qr': domain}

if not isinstance(values, dict):
    print("Wrong type, expected 'dict' instead of %s" %(type(values)))
    exit(-1);

# request via POST
data = parse.urlencode(values)

if not isinstance(data, str):
    print("Wrong type, expected 'str' instead of %s" %(type(data)))
    exit(-1)

data = str.encode(data)

resp = request.urlopen(url, data).read()
resp = resp.decode('iso-8859-1')
whois = decrypt(resp)
print(whois)

# tava com preguiça de fazer um sistema  de salvamento mais complexo
teste = input("Deseja salvar? [s-sim]\n")
if teste == 's':
    teste = input("Digite o nome do arquivo: ")
    teste += '.txt'
    arq = open(teste, "w")
    arq.write(whois)
    arq.close()
