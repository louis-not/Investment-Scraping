"""
Run This script only
Change main function according to the needs,
use params to modified the result from the scraping
"""
import sys
sys.path.insert(0, 'E:\Python\InvestmentScraping')

from src.auto import automate
import pandas as pd
import os



def main():
    """ edit here """
    groupby = 'year'    # NOT DONE YET! (year / sector / province)
    outputname = 'report_2017.xlsx'
    yearBegin = None
    yearEnd = None
    year = 2017

    """ don't edit here """
    testparams = {
        'url': 'https://nswi.bkpm.go.id/integrator/dataumum/index.php?lang=ID',
        'field': 'Sektor',
        'periode': 'Per Tahun',
        'tahunAwal': year,
        'tahunAkhir': year,
        'negara': '',
        'provinsi': 'Daerah Khusus Ibukota Jakarta',
        'kabupaten': None,
        'sektor': None,
        'kbli': None
    }
    outputdirectory = os.path.dirname(__file__)
    outputdirectory = outputdirectory[:len(outputdirectory)-7] + '/output/'
    writer = pd.ExcelWriter(outputdirectory+outputname, engine='xlsxwriter')
    automate(testparams, writer, yearBegin, yearEnd, groupby)
    writer.save()

    return 0


if __name__ == '__main__':
    main()
