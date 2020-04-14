import csv

filename='testcsv.csv'
rows=[]
fields=[]
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    fields=next(csvreader)
    for row in csvreader:
        rows.append(row)

min_authors=[]
min_books=[]
books_and_authors={}
rows.sort(key=lambda x:len(x[1]),reverse=True)

for row in rows:
    book=row[0]
    authors=row[1].split(', ')
    books_and_authors[book]=[]
    for author in authors:
        if author not in min_authors:
            min_authors.append(author)
            min_books.append(book)
            books_and_authors[book].append(author)

min_books=list(set(min_books))

fields=['Book']
filename='output1.csv'
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    for book in min_books:
        csvwriter.writerow([book])

fields=['Book','Author']
filename='output2.csv'
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    for book in min_books:
        for author in books_and_authors[book]:
            csvwriter.writerow([book,author])
