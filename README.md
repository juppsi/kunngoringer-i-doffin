# Analyse av kunngjøringer i Doffin 

I dag kjøper offentlige og private virksomheter varer og tjenester for store summer. Hvem som kjøper, hva som kjøpes og hvem som selger er viktig styringsinformasjon for samfunnet, særlige offentlige virksomheter 
som bruker offentlige midler. Regjeringen mener at anskaffelser er et viktig virkemiddel for å bidra til effektivisering, redusere klimautslipp, innovasjon og utvikling av næringslivet. Omfanget av anskaffelser i ulike områder er viktig for utviklingen av næringslivet. 

Doffin er den nasjonale kunngjøringsdatabasen for kunngjøring av offentlige anskaffelser. Alle kunngjøringer lik eller over den nasjonale terskelverdien på kr 1,3 mill ekskl. mva må kunngjøres i Doffin.

## Dokumentasjon

* [Doffin](https://doffin.no/)
* [Kunngjøringer](https://anskaffelser.no/anskaffelsesprosessen/anskaffelsesprosessen-steg-steg/konkurransegjennomforing/invitasjon-til-konkurranse/kunngjore-konkurranse-sende-invitasjon)
* [Enhetsregister](https://www.brreg.no/om-oss/registrene-vare/om-enhetsregisteret/)

## Datamodell

Viser koblingen mellom datasettene, se 

## Kildekode

* [Filen kunngjøringer](https://github.com/juppsi/kunngoringer-i-doffin/blob/main/src/kunngjoringer.py) laster ned og vasker kunngjøringsdataene. Deretter lagres dette som en csv-fil.
* [Filen enhetsregister](https://github.com/juppsi/kunngoringer-i-doffin/blob/main/src/enhetsregister.py) laster ned og vasker enheter- og underenheter dataene. Sammenstiller dem som et enhetstregister datasett. Deretter lagres dette som en csv-fil.

Merk at inneholdet i output filene kan endre seg da enhetsregisterdataene kan endre seg. Grunnet størrelsen på enhetsregister-output filen som er større enn 100 MB, grense som GitHub takler, har 
vi lagt filen på [DropBox](https://www.dropbox.com/scl/fo/u4swhs7pzhso6neuj9l6z/h?dl=0&rlkey=vnk4mp5i0sr72fngcs8rfnkko). 

## Nedlastninger

[Last ned](https://www.tableau.com/products/reader) Tableau Reader gratis for å lese dataprodukt-filen, som er en pakket Tableau workbook. Dette er en gratis desktop applikasjon som er laget for 
å lese Tableau filer. 

## Dataprodukt

Dataproduktet er laget i analyseverktøyet [Tableau](https://www.tableau.com/why-tableau/what-is-tableau). Dette er et analyseverktøy som henter inn og analyserer data. Dette BI-verktøyet brukes for blant annet å lage dynamiske dashboard. Dataproduktet kobler sammen de vaskede kunngjøring- og enhetsregister [filene](https://www.dropbox.com/scl/fo/u4swhs7pzhso6neuj9l6z/h?dl=0&rlkey=vnk4mp5i0sr72fngcs8rfnkko).



