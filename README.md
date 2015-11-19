# contra-scraper

Work in progress.

The aim of the project is to create a database of many contradances, including their choreography. With all that data in a computer-friendly format, one could build all sorts of applications--including search by figure.

The project relies heavily on [Michael Dyck's Contradance Index](http://www.ibiblio.org/contradance/index/) which is a hand-curated effort to index all contradance publications and their dances. One can search thousands of dances by title and author. Much gratitude goes to that project. Without it, this one couldn't exist.

Unfortunatly, Michael Dyck's index doesn't collect choreography information (probably for copyright reasons), but it *does* link to the original publications that do. This makes it very useful. 

# Project status

Currently,

1. it visits [Michael Dyck's Contradance Index](http://www.ibiblio.org/contradance/index/),
2. downloads all the raw data found there,
3. parses it,
4. and stores it in MongoDB.

It's capable of syncing data changed since the website's last update. When doing so, it only downloads changed data. Hopefully, this minimizes stress on the website.

# Future goals

5. download third-party publications,
6. parse them for dances,
7. store the dances in MongoDB

The tricky part of this is that the publications have no specific format. There is no standard notation for contradances, though there are patterns and de facto conventions. The fact that the dances are stored in poorly-formatted HTML and PDF documents doesn't help either. Each publication will have a different format. 

# Future-future goals

8. parse the choregraphy itself such that a computer could interpret a dance
9. provide supplementary info such that a computer could reason about and validate most dances
