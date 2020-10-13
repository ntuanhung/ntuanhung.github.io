#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
import pandas as pd
from time import strptime
import string, html, os, re, codecs

bib_filepath = "202010_HUNG_papers.bib"

journal_info = pd.read_csv("journal_info.tsv", sep="\t", header=0)
print(journal_info, type(journal_info))

codebase_ref = pd.read_csv("codebase_ref.tsv", sep="\t", header=0)
print(codebase_ref, type(codebase_ref))

database_ref = pd.read_csv("database_ref.tsv", sep="\t", header=0)
print(database_ref, type(database_ref))

# print(journal_info.columns)
# print(journal_info.loc['Pattern Recognition']['wos_quartile'])
# print(journal_info.loc['Pattern Recognition']['impact_factor'])

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "article":{
        "file": bib_filepath,
        "keyword": "article",
        "venuekey" : "journal",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
    "proceedings": {
        "file" : bib_filepath,
        "keyword": "inproceedings",
        "venuekey": "booktitle",
        "venue-pretext": "In: ",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
    "book":{
        "file": bib_filepath,
        "keyword": "incollection",
        "venuekey" : "booktitle",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
    "techreport":{
        "file": bib_filepath,
        "keyword": "techreport",
        "venuekey" : "booktitle",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    },
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


def parse_fields_by_paper_type(target_type, paper_entry):
    
    if publist[target_type]["keyword"]!=paper_entry.type:
        # print("WARNING: Skipping entry %s has type=%s NOT matched type=%s."%(paper_entry.key, paper_entry.type, publist[target_type]["keyword"]))
        return
    
    b = paper_entry.fields
    #reset default date
    pub_year = "1900"
    pub_month = "01"
    pub_day = "01"
    
    try:
        pub_year = f'{b["year"]}'

        #todo: this hack for month and day needs some cleanup
        if "month" in b.keys(): 
            if(len(b["month"])<3):
                pub_month = "0"+b["month"]
                pub_month = pub_month[-2:]
            elif(b["month"] not in range(12)):
                tmnth = strptime(b["month"][:3],'%b').tm_mon   
                pub_month = "{:02d}".format(tmnth) 
            else:
                pub_month = str(b["month"])
        if "day" in b.keys(): 
            pub_day = str(b["day"])

            
        pub_date = pub_year+"-"+pub_month+"-"+pub_day
        
        #strip out {} as needed (some bibtex entries that maintain formatting)
        clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    

        url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
        url_slug = url_slug.replace("--","-")

        md_filename = (str(pub_date) + "-" + url_slug + ".md").replace("--","-")
        html_filename = (str(pub_date) + "-" + url_slug).replace("--","-")

        #Build Citation from text
        citation = ""

        #citation authors - todo - add highlighting for primary author?
        for author in bibdata.entries[bib_id].persons["author"]:
            citation = citation+" "+author.first_names[0]+" "+author.last_names[0]+", "

        #citation title
        citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

        #add venue logic depending on citation type
        venue = publist[pubsource]["venue-pretext"]+b[publist[pubsource]["venuekey"]].replace("{", "").replace("}","").replace("\\","")

        citation = citation + " " + html_escape(venue)
        citation = citation + ", " + pub_year + "."

        
        ## YAML variables
        md = "---\nlayout: 'publication'" 
        md += "\ntitle: \""   + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + "\""
        
        md += """\ncollection: """ +  publist[pubsource]["collection"]["name"]

        md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
        
        note = False
        if "note" in b.keys():
            if len(str(b["note"])) > 5:
                md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
                note = True

        md += "\ndate: " + str(pub_date) 

        md += "\nvenue: '" + html_escape(venue) + "'"

        url = False
        if "url" in b.keys():
            if len(str(b["url"])) > 5:
                md += "\npaperurl: '" + b["url"] + "'"
                url = True

        md += "\npapertype: '" + target_type + "'"

        if target_type == "article":
            # print("Finding journal %s in database"%(b["journal"]))
            # print(journal_info.loc['Pattern Recognition']['wos_quartile'])
            # print(journal_info.loc['Pattern Recognition']['impact_factor'])

            wos_quartile = journal_info.loc[b["journal"].strip()]["wos_quartile"]
            impact_factor = journal_info.loc[b["journal"].strip()]["impact_factor"]
            if wos_quartile.strip()!="":
                md += "\nwosq: '" + wos_quartile + "'"
            if impact_factor.strip()!="":
                md += "\nimpactfactor: '" + impact_factor + "'"
        
        

        if "abstract" in b.keys() and b["abstract"].strip()!="":
            md += "\nabstract: '" + html_escape(b["abstract"].strip()) + "'"

        md += "\ncitation: '" + html_escape(citation) + "'"

        md += "\n---"

        
        ## Markdown description for individual page
        if note:
            md += "\n" + html_escape(b["note"]) + "\n"

        md += "\nAccess to "
        if url:
            md += "[paper](" + b["url"] + "){:target=\"_blank\"}"
        else:
            md += "[paper](https://scholar.google.com/scholar?q="+html.escape(clean_title.replace("-","+"))+"){:target=\"_blank\"}"
        
        if paper_entry.key in codebase_ref.index:
            # found = df[df['Column'].str.contains('Text_to_search')]
            # print(found.count())
            codeurl = codebase_ref.loc[paper_entry.key.strip()]["url"]
            md += " [code](" + codeurl + "){:target=\"_blank\"}" 
            print("Detected codeurl.")

        if paper_entry.key in database_ref.index:
            # found = df[df['Column'].str.contains('Text_to_search')]
            # print(found.count())
            dataurl = database_ref.loc[paper_entry.key.strip()]["url"]
            md += " [data](" + dataurl + "){:target=\"_blank\"}" 
            print("Detected dataurl.")

        # if "codeurl" in b.keys() and b["codeurl"].strip()!="":
        #     md += " [code](" + b["codeurl"] + "){:target=\"_blank\"}" 
        
        md_filename = os.path.basename(md_filename)

        with codecs.open("../_publications/" + md_filename, 'w', encoding="utf8") as f:
            f.write(md)
        print(f'SUCESSFULLY PARSED {bib_id}: \"', paper_entry.key, b["title"][:60],"..."*(len(b['title'])>60),"\"")
    # field may not exist for a reference
    except KeyError as e:
        print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', paper_entry.key, b["title"][:30],"..."*(len(b['title'])>30),"\"")
        return

for pubsource in publist:
    parser = bibtex.Parser()
    bibdata = parser.parse_file(publist[pubsource]["file"])

    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        # print(bibdata.entries[bib_id].type, bibdata.entries[bib_id].key)
        parse_fields_by_paper_type(pubsource, bibdata.entries[bib_id])