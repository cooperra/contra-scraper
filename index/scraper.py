from bs4 import BeautifulSoup

# Prevents poor markup from breaking everything
# Requires python-html5lib installed
PARSER = 'html5lib'
ENCODING = 'ISO-8859-1'

def scrape_contra_index(sources_page):
    """Given a file or HTML string,
return a list containing one dict for each dance source. Each dict contains mappings between labels and data.
Links are labeled separately from their text. Their labels end with '_link'."""
    soup = BeautifulSoup(sources_page, PARSER)

    rows = soup.find_all('tr')
    headings = [t_heading.text.strip() for t_heading in rows[0].find_all('th')]

    def process_row(row):
        """Given a row (tr tag), extract data into a dictionary of headings to text.
If the field contains a link, extract the href of that link into its own field."""
        row_data = {}
        for heading, row_field in zip(headings, row.find_all('td')):
            row_data[heading] = row_field.text.strip()
            # Add link if available
            a = row_field.findChild('a')
            if a is not None:
                row_data[heading + "_link"] = a.attrs['href']
        return row_data

    return map(process_row, rows[1:])

if __name__ == '__main__':
    sources_data = scrape_contra_index(open("Michael Dyck's Contradance Index_ Sources.html", encoding=ENCODING))
