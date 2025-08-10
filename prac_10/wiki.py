import wikipedia

def main():
    invalid_title = False
    while not invalid_title:
        title = input("Enter page title: ").strip()
        
        if title == "":
            invalid_title = True
        
        else:
            try:
                # From Ny example in quickstart
                page = wikipedia.page(title, auto_suggest=False)
                print(page.title)
                print(page.summary)
                print(page.url)
                
            except wikipedia.exceptions.DisambiguationError as e: # From quickstart
                print("We need a more specific title. Try one of the following, or a new search: \n (BeautifulSoup warning)")
                print(e.options)
                
            except wikipedia.exceptions.PageError:
                print(f'Page id "{title}" does not match any pages. Try another id!')

    print("Thank you.")
    
main()