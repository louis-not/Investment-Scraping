"""
Run This script only
Change main function according to the needs,
use params to modified the result from the scraping
"""

from src.scraping import scrape
from src.transform import transform
from src.auto import automate
import pandas as pd
import os


def main():
    groupby = 'year'    # year / sector / province
    testparams = {
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

    outputdirectory = os.path.dirname(__file__)
    outputdirectory = outputdirectory[:len(outputdirectory)-7] + '/output'
    writer = pd.ExcelWriter(outputdirectory+'/test.xlsx', engine='xlsxwriter')
    automate(testparams, writer, 2018, 2021, groupby)
    # df = scrape(testparams)
    # transform(df, writer, 'test')
    writer.save()

    return 0


if __name__ == '__main__':
    main()
