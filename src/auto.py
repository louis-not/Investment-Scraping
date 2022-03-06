from src.scraping import scrape
from src.transform import transform


def automate(params, writer ,begin, end, groupby):
    """automation script to control the scrapping"""
    provinces = ['Aceh', 'Bali', 'Banten','Bengkulu', 'Daerah Istimewa Yogyakarta',
                 'Jakarta', 'Gorontalo','Jambi', 'Jawa Barat',
                 'Jawa Tengah', 'Jawa Timur','Kalimantan Barat', 'Kalimantan Selatan',
                 'Kalimantan Tengah', 'Kalimantan Timur', 'Kalimantan Utara',
                 'Bangka', 'Kepulauan Riau', 'Lampung', 'Maluku', 'Maluku Utara',
                 'Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Papua', 'Papua Barat',
                 'Riau', 'Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Tengah', 'Sulawesi Tenggara',
                 'Sulawesi Utara', 'Sulawesi Barat'
                 ]
    for year in range(begin,end+1):
        params['tahunAwal'] = year
        params['tahunAkhir'] = year
        for province in provinces:
            print('Scraping website province: {} | year: {}'.format(province, year))
            params['provinsi'] = province
            df = scrape(params)
            transform(df, writer, str(year)+'_'+province)

    return True