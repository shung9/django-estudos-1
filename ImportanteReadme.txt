# Anotei erros
# Primeiro na organização do site
  ## um aplicativo nao pode ter outros aplicativos por razões de organização e pra nao confundir django
  ## tem uma repetição das mesmas coisas escritas em forma diferente, mas o resultado é o mesmo 
  ## é recomendado usar 'templates' e 'static' mesmo quando queres redefinir a organização dos static files e templates

 
# melhor tens de escolher gerenciar todos os aplicativos no app principal ou cada aplicativo genrenciar o seu próprio urls 
# no caso, pretendes genrenciar todos os app no app principal, nao é preciso usar enclude() e nao é preciso cria urls.py em cada app
# no caso de gerenciar o url de cada app no próprio app, podes usar o include()
   ### code, urls.py app principal ;
   ... import include
   path('', include('nom_do_app.urls')), # um aplicativo 
   
   path('', include('nom_do_outro_app.urls')), 
   #nao tem um número limite, quando cria um novo aplicativo é preciso cria o path(...)
   
#settings
# em default django defini o 'static' e 'templates'
#Pra poder usar em default, basta cria o 'static' ou 'templates' no raiz do app
#exemplo;
📂$Arquivo raiz
     📂$aplicativo principal


     📂$applicativo 1
        ...
        📂static
        📂templates 
           📂css 
           ...
     📂$outro aplicativo 
        ... mesma coisa

# No caso queres personalizar o 'static' e 'template'
# exemplo;
  📂$Arquivo raiz
     📂$aplicativo principal 
     📂$outro aplicativo 
     📂$um outro aplicativo 
     📂$templates 
        📂outro_aplicativo
          index.html
          etc...
     📂$static
     ...
     manage.py
     etc...
# E recomendo colocar os templates num arquivo com o nome do aplicativo em questão, pra evitar confusões     
   
# Para gerenciar os static files, image etc...   
#settings , localhost
#com a nova versão de django podes usar BASE_DIR esta definido

#settings.py
# Pra genrenciar as imagens 

code;
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIRS / 'media'

#css, js etc...
code;
STATICFILES_DIRS = [
   BASE_DIR / 'static' 
]

#IMPORTANTE
#vi que criaste um arquivo admin em static file, nao sei por que, 
# O django ja tem um interface admin pronta pra genrenciar o dite 
#admin.py podes personalizar o interface, basta criar um superuser
 
 ## o django é so uma questão de organização 
# depois disso nao vais ter mais error 
# espero ter ajudado 

   
   
   
   
   
   
