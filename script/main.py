"""
Run This script only
Change main function according to the needs,
use params to modified the result from the scraping
"""

from scraping.scraping import scrape
from scraping.scraping import check_params


def main():
    params = {
        'url': "https://nswi.bkpm.go.id/data_statistik",
        'field': 'Negara',
        'periode': 'Per Tahun',
        'tahunAwal': 2017,
        'tahunAkhir': 2018,
        'negara': 'Indonesia',
        'provinsi': 'Daerah Khusus Ibukota Jakarta',
        'kabupaten': None,
        'sektor': None,
        'kbli': None
    }
    # uncomment for checking passing parameter
    # check_params(params)
    scrape(params)

    return 0


if __name__ == '__main__':
    main()
