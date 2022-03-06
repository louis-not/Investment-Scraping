"""
Run This script only
Change main function according to the needs,
use params to modified the result from the scraping
"""

from src.scraping import scrape
from src.transform import transform

def main():
    params = {
        'url': 'https://nswi.bkpm.go.id/integrator/dataumum/index.php?lang=ID',
        'field': 'Sektor',
        'periode': 'Per Tahun',
        'tahunAwal': 2020,
        'tahunAkhir': 2020,
        'negara': 'Indonesia',
        'provinsi': 'Daerah Khusus Ibukota Jakarta',
        'kabupaten': None,
        'sektor': None,
        'kbli': None
    }
    # uncomment for checking passing parameter
    # check_params(params)
    df = scrape(params)
    transform(df)

    return 0


if __name__ == '__main__':
    main()
