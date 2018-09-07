# BioCAT Website

This git contains the (not-yet-released) BioCAT website. The website is
made using pelican, with the pelican-boostrap3 theme and the boostrap-rst
plugins. It represents a ground up redesign of the previous website, and
is designed with a mobile-first approach.

## Cloning

Clone the repository using:

```
git clone <gihub_url>
```

The github URL can be obtained by clicking on the 'Clone or download' button
near the top of the main page for the repository. Currently the command would look
like this:
```
git clone https://github.com/biocatiit/website.git
```

## Building

### Install pelican

The website is built using the pelican static site generator. This is python
based, so you need to have python installed. In addition to python, in order to build
the website from the source, first install the pelican, markdown, and typogrify
python modules, for example you can:
```
pip install pelican Markdown typogrify beautifulsoup4
```

### Build and display the html (make)

The best approach for development purposes is to use make to build and
display the html. In the top level of the repository, run
```
make devserver
```

This displays the website at [http://localhost:8000/](http://localhost:8000/).

The make command will both build the source and serve it up, and it continuously rebuilds
the website when you make changes. This way you can make changes to your
document and then just refresh the local page in your browser to see the results
of those changes. To stop the devserver run
```
./develop_server.sh stop
```

If the make command doesn't work for you (for example you don't have the make
utility installed), see the next section.

### Build and display the html (pelican/python)

An alternative way you can build the website is to run the following command in
the top level of the repository directory:
```
pelican -d
```

This writes the output html files to the output directory.

To display the output locally (for testing and development), cd into the
output directory and run
```
python -m SimpleHTTPServer
```

This displays the website at [http://localhost:8000/](http://localhost:8000/).
(note: this is the python 2 way, python 3 requires a different command)


## Notes about image formats

* Staff images should be cropped to a square (1:1 aspect ratio), 750x750 px
* Carousel images and top of page images should be cropped to a 2:1 aspect ratio, 1200x600
* Thumbnail images should be 750x500 px

## Useful links

* [Pelican documenation](http://docs.getpelican.com/en/stable/)
* [Pelican-boostrap3 theme documenation](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
* [Pelican bootstrap-rst plugin documenation](https://github.com/getpelican/pelican-plugins/tree/master/bootstrap-rst)
    * [boostrap-rst demo](https://rougier.github.io/bootstrap-rst/)
* [Basics of rst](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
* [Basics of markdown](https://www.markdownguide.org/)
