from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_korting =(prijs - (prijs * korting))
    
    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_korting:.2f} euro."
    return aanbieding

def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = 0
    for el in inkomsten:
        totaal_inkomsten += el
    
    berekend_btw = totaal_inkomsten * btw
    tekst =f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {berekend_btw:.2f} euro btw betaald dient te worden"

    return tekst

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)

    list =[laag, hoog]

    return list

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst)/len(mijn_lijst)
    tekst =f"De gemiddelde inkomsten van deze week zijn {gemiddelde} euro."
    return tekst

def meervoudig(invoer_lijst):
   return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst =  laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)

