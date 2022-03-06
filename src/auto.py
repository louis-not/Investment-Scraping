from src.scraping import scrape
from src.transform import transform


def automate(params, writer ,begin, end, groupby):
    """automation script to control the scrapping"""
    provinces = ['Aceh', 'Bali', 'Banten','Bengkulu', 'Daerah Istimewa Yogyakarta',
                 'Daerah Khusus Ibukota Jakarta', 'Gorontalo','Jambi', 'Jawa Barat',
                 'Jawa Tengah', 'Jawa Timur','Kalimantan Barat', 'Kalimantan Selatan',
                 'Kalimantan Tengah', 'Kalimantan Timur', 'Kalimantan Utara',
                 'Kepulauan Bangka Belitung', 'Kepulauan Riau', 'Lampung', 'Maluku',
                 'Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Papua', 'Papua Barat',
                 'Riau', 'Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Tengah', 'Sulawesi Tenggara',
                 'Sulawesi Utara', 'Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Utara'
                 ]
    for year in range(begin,end+1):
        params['tahunAwal'] = year
        params['tahunAkhir'] = year
        for province in provinces:
            print('Scraping website province: {} | year: {}'.format(province, year))
            params['provinsi'] = province
            df = scrape(params)
            transform(df, writer, 'test_' + str(year))

    return True