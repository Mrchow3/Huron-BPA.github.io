#!/usr/bin/env python
import os, csv, requests
from os.path import dirname, join, abspath
website = dirname(dirname(abspath(__file__)))
with open(join(website, "other", "images.csv")) as csv_file:
    lines = csv.DictReader(csv_file)
    for line in lines:
        if not line['filename'] or not line['url']:
            continue
        ending = line['url'].split('.')[-1].lower()
        file_path = join(website, "assets", line['filename'] + f'.{ending}')
        citation = line['citation']
        with open(file_path, 'wb') as write:
            write.write(requests.get(line['url']).content)
            print(f'downloaded {line["filename"]}.{ending}')
            if citation is not None:
                print('adding citation', citation)
                citation = citation.replace('"',"\\\"",-1)
                os.system(f'magick convert "{file_path}" -fill white \
-font Times-New-Roman -pointsize 24 \
-undercolor "#00000080" -gravity South -annotate +0+0 "{citation}" "{file_path}"')
        print(line["url"])
