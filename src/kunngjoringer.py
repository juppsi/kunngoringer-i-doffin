'''
Kodesnutt som laster ned kunngjøringsdataene fra felles datakatalog (data.norge.no) - for hvert år. Filene er laget som url-er.
Lagrer disse dataene i en dataframe med en ny kolonne som definerer året. Ordner deretter datatypene til dataene i dataframen.

Tilslutt lagres dataene som en csv-fil. 

Les mer om datasettene: https://data.norge.no/datasets/a77b0408-85f9-3e12-8a66-8d500b492e9d
Informasjon om kunngjøringer: https://anskaffelser.no/anskaffelsesprosessen/anskaffelsesprosessen-steg-steg/konkurransegjennomforing/invitasjon-til-konkurranse/kunngjore-konkurranse-sende-invitasjon
Dokumentasjon om doffin: https://doffin.no/
'''

import pandas as pd

all_data = pd.DataFrame()

for aar in ['2018', '2019', '2020', '2021', '2022']:
    url = f"https://adaapnedataprodst.blob.core.windows.net/kunngjoringer/{aar}/Kunngjoringer_{aar}.csv"
    
    kunngjoringer = pd.read_csv(url, delimiter=";", header=0, encoding='Windows-1252')

    kunngjoringer['aar'] = aar

    all_data = pd.concat([all_data, kunngjoringer])

for i in ['publisering_dato','tilbudsfrist_dato']:
        all_data[i] = pd.to_datetime(all_data[i])

for i in ['cpv_hoved_kode', 'skjema_nr']:
        all_data[i] = all_data[i].astype('str')


all_data.to_csv("C:/Users/0-jasr/OneDrive - DFO/Python/nedlastninger/kunngjoringer.csv", index = False, sep=";", header=True, encoding='Windows-1252')