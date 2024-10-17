def talaba_info(ism, familiya, **info):
    info['ism'] = ism
    info['familiya'] = familiya
    return info

talaba = talaba_info('olim', 'olimov', t_yil=2000, fakultet='It', yonalish="AT")
print(talaba)


def kopaytirish(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(kopaytirish(3,7,10))