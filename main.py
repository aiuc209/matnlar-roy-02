def eng_uzun_sozi_top(matnlar):
    eng_uzun_sozi_royxati = []
    for matn in matnlar:
        sozlar = matn.split()
        eng_uzun_soz = max(sozlar, key=len)
        eng_uzun_sozi_royxati.append(eng_uzun_soz)
    return eng_uzun_sozi_royxati

matnlar = ["Men yaxshi oqiyman", "Siz ham yaxshi oqiyssiz", "Ular juda yaxshi oqiylar"]
print(eng_uzun_sozi_top(matnlar))
