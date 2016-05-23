import pdfquery
import requests
import csv
from io import BytesIO



def main():
    with open('english_councils.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[3] is not '' and 'http' in row[3]:
                pdf = requests.get(row[3], stream=True)
                pdf.raw.decode_content = True
                if pdf.headers['Content-Type'] == 'application/pdf':
                    # Invoke our pdf converters
                    import pdb; pdb.set_trace()

                    rt = pdfquery.PDFQuery(BytesIO(pdf.raw.data))





if __name__ == '__main__':
    main()
