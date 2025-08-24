import wikipedia


def main():
    print("Wikipedia Search Program")
    print("========================")

    while True:
        search_term = input("Enter page title: ").strip()

        # Exit if user enters blank input
        if not search_term:
            print("Thank you.")
            break

        try:
            # First, try to get suggestions for the search term
            suggestions = wikipedia.search(search_term)

            # If no suggestions found
            if not suggestions:
                print(f'Page id "{search_term}" does not match any pages. Try another id!')
                continue

            # Try to get the page with autosuggest disabled to avoid automatic redirection
            try:
                page = wikipedia.page(search_term, autosuggest=False)
                display_page_info(page)

            except wikipedia.DisambiguationError as e:
                # Handle disambiguation error
                print(f"We need a more specific title. Try one of the following, or a new search:")
                # Show first 10 options to avoid overwhelming output
                for option in e.options[:10]:
                    print(f"- {option}")
                if len(e.options) > 10:
                    print(f"... and {len(e.options) - 10} more options")
                print()

            except wikipedia.PageError:
                # If the exact page doesn't exist, try with autosuggest enabled
                try:
                    page = wikipedia.page(search_term, autosuggest=True)
                    display_page_info(page)
                except wikipedia.PageError:
                    print(f'Page id "{search_term}" does not match any pages. Try another id!')
                except wikipedia.DisambiguationError as e:
                    print(f"We need a more specific title. Try one of the following, or a new search:")
                    for option in e.options[:10]:
                        print(f"- {option}")
                    if len(e.options) > 10:
                        print(f"... and {len(e.options) - 10} more options")
                    print()

        except wikipedia.WikipediaException as e:
            print(f"An error occurred: {e}")


def display_page_info(page):
    """Display information about a Wikipedia page"""
    print(page.title)
    print(wikipedia.summary(page.title, sentences=3))  # Show first 3 sentences
    print(page.url)
    print()


if __name__ == "__main__":
    main()