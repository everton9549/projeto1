import tagui as t

login = ['7038157994']
cont = len(login)
aux = 0
while aux != cont:
    t.init()
    t.url('http://servicos.coelba.com.br/servicos-ao-cliente/Pages/login-av.aspx?UrlUc=http://servicos.coelba.com.br/servicos-ao-cliente/Pages/2-via-de-conta-coelba.aspx')
    t.click('ctl00$m$g_2d0a0930_51e9_4b08_addf_fccd4023f2e8$ctl00$txtContaContrato')
    t.type('ctl00$m$g_2d0a0930_51e9_4b08_addf_fccd4023f2e8$ctl00$txtContaContrato', login[aux])
    captcha = t.read('textCaptcha')
    t.click('ctl00$m$g_2d0a0930_51e9_4b08_addf_fccd4023f2e8$ctl00$txtCaptcha')
    t.type('ctl00$m$g_2d0a0930_51e9_4b08_addf_fccd4023f2e8$ctl00$txtCaptcha', captcha)
    t.click('ctl00$m$g_2d0a0930_51e9_4b08_addf_fccd4023f2e8$ctl00$btnAutenticar')


    t.close()
    aux += 1

