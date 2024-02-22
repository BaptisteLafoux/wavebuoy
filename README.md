# Smart wave-buoy with smartphones
## Install
Create a venv, source it and install requirements
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Development
```bash
pre-commit install
```
## Run
- Connect phone(s) and your computer to the same wifi network.
- run `python read_data_phone.py`



--------
# TODO
- récupérer les données en continu (sans trou). Ajd c'est aléatoirement long -> async / await ??``
- récupérer tout à la fin ça ne marche pas pcq trop gros sur du wifi
- afficher les plots en direct sur l'ordi
- arriver à changer le taux d'acquisition à distance

SINON
- arriver à dump les résultats de l'xp dans un fichier TMP sur le tel
- ensuite le récupérer sur l'ordi via un adb pull

SINON
- récup les résultats à la fin en faisant plein de mini get


- autre sujet : arriver à trouver comment mettre synchrones 2 tel différents

## Sources
https://github.com/Turbotice/icewave/tree/main/icewave/pyphone_v2
https://phyphox.org/wiki/index.php/Remote-interface_communication
