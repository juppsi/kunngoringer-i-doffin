'''
Kodesnutt som laster ned enheter og underenheter dataene fra api-ene til Brønnøysundregisteret.
Funksjonene hentEnheter() og hentUnderenheter() laster ned de respektive dataene fra api-et til Brønnøysundregisteret med riktig header-informasjon.
Filen som lastes ned er en json fil som er komprimert. Ordner tilslutt opp i datatypene til kolonnene.

Deretter slår vi sammene disse to datasettene (dataframene) til en dataframe og lagrer det som en csv-fil. 

Les mer om datasettene: https://data.norge.no/datasets/68d08f28-a16d-4fab-a953-ed4ab08ce2e2
Dokumentasjon om api-ene: https://data.brreg.no/enhetsregisteret/api/docs/index.html
'''

import pandas as pd
import requests
import gzip
import numpy as np
import json

def hentEnheter():  
    enheter_url = "https://data.brreg.no/enhetsregisteret/api/enheter/lastned"
    enheter_headers= {'Accept': 'application/vnd.brreg.enhetsregisteret.enhet.v1+gzip;charset=UTF-8'}
    enheter_data= requests.get(enheter_url, headers=enheter_headers)

    hent_enheter = json.loads(gzip.decompress(enheter_data.content).decode('utf-8'))
    
    df_enheter= pd.json_normalize(hent_enheter).convert_dtypes()
    df_enheter.info()
    for i in ['registrertIMvaregisteret', 'registrertIFrivillighetsregisteret', 'registrertIForetaksregisteret',
            'registrertIStiftelsesregisteret', 'konkurs', 'underAvvikling', 'underTvangsavviklingEllerTvangsopplosning']:
        df_enheter[i] = df_enheter[i].astype('boolean')

    for i in ['registreringsdatoEnhetsregisteret']:
        df_enheter[i] = pd.to_datetime(df_enheter[i])
        
    return df_enheter


def hentUnderenhter():
    underenheter_url = "https://data.brreg.no/enhetsregisteret/api/underenheter/lastned"
    underenheter_headers= {'Accept': 'application/vnd.brreg.enhetsregisteret.underenhet.v1+gzip;charset=UTF-8'}
    underenheter_data= requests.get(underenheter_url, headers=underenheter_headers)

    hent_underenheter = json.loads(gzip.decompress(underenheter_data.content).decode('utf-8'))

    df_underenheter= pd.json_normalize(hent_underenheter).convert_dtypes()

    for i in ['registrertIMvaregisteret']:
        df_underenheter[i] = df_underenheter[i].astype('boolean')

    for i in ['registreringsdatoEnhetsregisteret','oppstartsdato', 'datoEierskifte', 'nedleggelsesdato']:
        df_underenheter[i] = pd.to_datetime(df_underenheter[i])

    return df_underenheter

df_enheter= hentEnheter()

df_underenheter = hentUnderenhter()

enhetsregister = pd.concat([df_enheter, df_underenheter], ignore_index=True)


# NB - husk å endre filstien til en lagringsplass på datamaskinen din
enhetsregister.to_csv("C:/Users/0-jasr/OneDrive - DFO/Python/nedlastninger/enhetsregister.csv", index = False, encoding= 'utf-8', header = True, sep =';') 
