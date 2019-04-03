# MicroBiome API Listing

Hello! This is an API for listing entries of a given [*.fasta*](https://pt.wikipedia.org/wiki/FASTA) file. It was made using the [Django Rest Framework](https://www.django-rest-framework.org/), a powerful and flexible toolkit for building Web APIs.

## Introduction

This API is the result of a job task. The task description is in a pdf file called *BackendTest.pdf*. You can check it out with details before you get started or just go for it and follow the instructions below.

## Getting started

In order to run this API locally, you must download the zip file containg this code and have installed in your computer python3.

### Prerequisites

 - Download Python3: https://www.python.org/downloads/

I also recommend you create a virtual environment in order to install the dependences for this project. You can see how in [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).

### Installing and running

Now we need to set our dependences, and that couldn't be easier. Just go to the root folder of the project (the one with the manage.py file) and type the following in your prompt:

```
pip install -r requirements.txt
```

See, told you. Easy peasy.

You should be able to run this without a problem with `python manage.py runserver`

## Checking it out

Great! We have our database filled with **plenty** of information and we can access it by the following endpoints:

- *localhost:8000/entries-table/* - Here can see a table with all the entries;
- *localhost:8000/entry/* - This is an Django Rest Framework API screen for all the Entry objects;
- *localhost:8000/entry/id* - This is an Django Rest Framework API screen for the specific Entry object id given.

We can get the data in a JSON format:

- *localhost:8000/entry/?format=json*
- *localhost:8000/entry/id/?format=json*

Or filter by kingdom/specie:

- *localhost:8000/entry/?kingdon__label=Bacteria*

## Creating our own database

This project has it's database already filled with the informations needed, but we can do it ourselves from scratch or download a different *fasta.gz* file and get new data into API.

### Starting from scratch

To download ourselves the data from the url, we should follow the next steps:

1. Delete the db.sqlite3 file in our root project folder (the one with the manage.py file)
2. Now, we need to make the migrations of our project. Run:

```
python manage.py migrate
```
3. For last, we need to import data to our database. For the purpose of this test, I've created a command for the manage.py file called `importgzfile`. It imports the information from a given url that has a *.fasta* file compressed in a *.gz* file and load the information to the database. This is the given url used for this project: https://www.arb-silva.de/fileadmin/silva_databases/release_128/Exports/SILVA_128_LSURef_tax_silva.fasta.gz

So you need to prompt:

```
python manage.py importgzfile https://www.arb-silva.de/fileadmin/silva_databases/release_128/Exports/SILVA_128_LSURef_tax_silva.fasta.gz
```

A little warning. This is a large file, so this process may take a couple of minutes, depending on your pc and internet connection speed.


### Downloand new content

We can download new information to our API automatically if we have a download link of a *fasta.gz*. Then, we just have to run:

```
python manage.py importgzfile <url>
```


## Example

Here you can see an example of it running online:

http://davidbarenco.pythonanywhere.com/

*Valid until Wednesday 03 July 2019*



## Author

[David Barenco](https://www.linkedin.com/in/david-barenco-7b84a012a/)
