from src.scraping import scrape
from src.transform import transform


def automate(params, writer ,begin, end, groupby):
    """automation script to control the scrapping"""
    provinces = [ 'Jakarta', 'Aceh', 'Bali', 'Banten','Bengkulu', 'Yogyakarta',
                  'Gorontalo','Jambi', 'Jawa Barat', 'Jawa Tengah',
                 'Jawa Timur','Kalimantan Barat', 'Kalimantan Selatan',
                 'Kalimantan Tengah', 'Kalimantan Timur', 'Kalimantan Utara',
                 'Bangka', 'Kepulauan Riau', 'Lampung', 'Maluku', 'Maluku Utara',
                 'Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Papua', 'Papua Barat',
                 'Riau', 'Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Tengah', 'Sulawesi Tenggara',
                 'Sulawesi Utara', 'Sulawesi Barat'
                 ]
    # provinces = ['Aceh']
    # provinces = ['Aceh']
    # for year in range(begin,end+1):
    #     params['tahunAwal'] = year
    #     params['tahunAkhir'] = year
    year = params['tahunAkhir']
    for province in provinces:
        print('Scraping website province: {} | year: {}'.format(province, year))
        params['provinsi'] = province
        df_pmdn, df_pma = scrape(params)
        transform(df_pmdn, writer, "PMDN_{}_{}".format(province, year))
        transform(df_pma, writer, "PMA_{}_{}".format(province, year))

    return True

