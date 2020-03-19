import os.path
import requests
import difflib
from bs4 import BeautifulSoup

# Parameters
url  = 'https://www.cne.cl/nuestros-servicios/licitaciones-y-suministros/licitacion-2019/'
file = 'licitacion_2019'

webs = [['https://www.cne.cl/nuestros-servicios/licitaciones-y-suministros/licitacion-2019/', 'licitacion_2019'],
        ['https://www.cne.cl/normativas/electrica/procesos-normativos/'                     , 'procesos_normativos_cne'],
        ['https://www.energia.gob.cl/mini-sitio/reglamentos/'                               , 'procesos_noramitovs_ministerio_de_energía'],
        ['https://www.df.cl/'                                                               , 'df'],
        ['https://www.google.com/search?q=coronavirus&rlz=1C1GCEU_esCL890CL890&oq=coronavirus&aqs=chrome..69i57j0j69i65l3j69i60l3.2343j0j9&sourceid=chrome&ie=UTF-8', 'coronavirus']
]




def scan_web(url,file):
    # Initial data
    if not os.path.isfile(file + "_old.txt"):
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        prettySoup = soup.prettify()
        with open(file + "_old.txt", "w") as output:
            output.write(prettySoup)

    with open(file + "_old.txt", "r") as input:
        old_html = input.read()

    # New data
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    new_html = soup.prettify()
    #print (new_html)
    #print("----------------------")
    #print (soup.html.contents[0])
    #print("++++++++++++++++++++++")
    #print(soup.html.findAll(text=True, recursive=False))
    with open(file+"_new.txt", "w") as output:
        output.write(new_html)

    # Diff
    with open(file + "_old.txt") as f1:
        old_text = f1.read()
    with open(file + "_new.txt") as f2:
        new_text = f2.read()

    print("Differences are:")
    for line in difflib.unified_diff(old_text, new_text, fromfile='old', tofile='new', lineterm=''):
        print(line)

for url,file in webs:
    print("Scanning: ", file)
    scan_web(url,file)
    print()
print("Done.")