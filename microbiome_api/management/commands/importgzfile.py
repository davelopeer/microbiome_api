import urllib
import gzip
from django.core.management.base import BaseCommand
from microbiome_api.models import Kingdom, Specie, Entry


class Command(BaseCommand):
    help = "Extract, read and import to database data from a 'fasta' file"

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        content = ""
        print("Processing file...")
        print("This may take a few seconds...")

        # Getting file from url and unpacking the gz file
        file = urllib.request.urlopen(url)
        with gzip.open(file, 'rb') as f_in:
            file_content = f_in.read()
            file_content = bytes.decode(file_content)
            content = file_content

        new_entry = content.split(">")
        new_entry.pop(0)

        for entry in new_entry[:5000]:
            # Removing line breakers
            entry_elements = entry.split("\n")
            # Getting the specie data (all data except the DNA sequences)
            specie_data = entry_elements[0]

            # Getting the taxonomy for this specie and making a list
            # of every rank entry
            taxonomy = specie_data.split(' ', 1)[1]
            taxonomy = taxonomy.split(";")

            # Creating the datas for the DataBase
            access_id = specie_data.split(' ', 1)[0]
            kingdom = taxonomy[0]
            specie = taxonomy[-1]
            sequence = entry_elements[1]

            # Creating an entry for the Kingdom class, if it not exist
            if not Kingdom.objects.filter(label=kingdom):
                db_kingdom = Kingdom()
                db_kingdom.label = kingdom
                db_kingdom.save()

            # Creating an entry for the Specie class, if it not exist
            if not Specie.objects.filter(label=specie):
                db_specie = Specie()
                db_specie.label = specie
                db_specie.save()

            # Getting the Kingdom and Specie objects
            kingdom_object = Kingdom.objects.get(label=kingdom)
            specie_object = Specie.objects.get(label=specie)

            # Creating an entry for the Entry class, if it not exist
            if not Entry.objects.filter(access_id=access_id):
                db_entry = Entry()
                db_entry.access_id = access_id
                db_entry.kingdom = Kingdom.objects.get(id=kingdom_object.id)
                db_entry.specie = Specie.objects.get(id=specie_object.id)
                db_entry.sequence = sequence
                db_entry.save()

        return "Successfully imported data"
