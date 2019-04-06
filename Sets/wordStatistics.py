##Author Statistics##
##here we will take two books of an author and check how many
##different words he has used in his books. i.e checking his vocabulary
##in-short we will be doing web scrapping
import requests



def web_scrap(url):
    response = requests.get(url)
    return response


try:
    book1 = web_scrap("http://www.gutenberg.org/files/215/215-0.txt")
    book2 = web_scrap("http://www.gutenberg.org/cache/epub/910/pg910.txt")

    book1=set(book1.content.split())
    book2 = set(book2.content.split())

    print("Statistics")
    print("Unique Words Count")
    print("Book1: ",len(book1))
    print("Book2: ",len(book2))

    print("Total Unique Words Count: ", len(book1 | book2))
    print("Intersection Words Count",len(book1 & book2))
    print("Difference Count of Book1",len(book1 - book2))
    print("Difference Count of Book2", len(book2 - book1))
    print("Symmetric Difference Count of Book1 and Book2", len(book1.symmetric_difference(book2)))

except:
    print("error")