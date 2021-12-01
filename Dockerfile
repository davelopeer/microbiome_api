FROM python:3
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY src/ /app/
RUN python manage.py migrate
RUN python manage.py importgzfile https://www.arb-silva.de/fileadmin/silva_databases/release_128/Exports/SILVA_128_LSURef_tax_silva.fasta.gz
