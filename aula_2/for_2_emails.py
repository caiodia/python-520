emails = [
	'petyfezygniyg@msddvqiytmpogire',
	'yjozbkgirsfchbjtlnigqqeohaj',
	'axukkfdcpemkruogaemqlcyfngun',
	'czmymzvhdyfltqe@rktzjljbs',
	'@yoeisikhawyno@b',
	'dfeydhfnlydwrlvpmsomi',
	'xogsqaxph@btippxiz',
	'hxkuqlyxreuwfzwypvw',
	'togaczelhzijnafhyg@czp@f',
	'jxtmqikapfv@uqqckowiz@hyi',
]

def verificar_se_e_email(email):
    contador = 0
    for letra in email:
        if letra == '@':
            contador = contador + 1

    if contador == 1:
        return True
    else:
        return False

for email in emails:
    e_email = verificar_se_e_email(email)
    print(email + ' ' + e_email)