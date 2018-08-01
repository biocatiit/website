# BioCAT Website

This git contains the (not-yet-released) BioCAT website. The website is
made using pelican, with the pelican-boostrap3 theme and the boostrap-rst
plugins. It represents a ground up redesign of the previous website, and
is designed with a mobile-first approach.

## Cloning

The repository contains two submodules, themes which links to the pelican-themes
github repostitory and plugins which links to the pelican-plugins github repository.
In order to get the contents of these submodules when you clone the repository
you should use the command:

```
git clone --recurse-submodules
```

If you've already cloned it with a standard clone command, you can use

```
git submodule init
git submodule update
```

to get contents of the submodules.

## Building

### Install pelican

The website is built using the pelican static site generator. This is python
based, so you need to have python installed. In addition to python, in order to build
the website from the source, first install the pelican, markdown, and typogrify
python modules, for example you can:
```
pip install pelican Markdown typogrify
```

### Build and dispaly the html (pelican/python)

Once those modules are installed, in the top level of the repository (the
directory containing the contents directory) you can build the website simply
by running
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

### Build and display the html (make)

Probably the best approach for development purposes is to use make to build and
display the html. If you run
```
make devserver
```

This will both build the source and serve it up, as well as continuously rebuilding
the website when you make changes. This way you can make changes to your
document and then just refresh the local page in your browser to see the results
of those changes. To stop the devserver run
```
./develop_server.sh stop
```

## Notes about image formats

Staff images should be cropped to a square (1:1 aspect ratio)
Carousel images should be cropped to a 2:1 aspect ratio.

## Useful links

* [Pelican documenation](http://docs.getpelican.com/en/stable/)
* [Pelican-boostrap3 theme documenation](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)
* [Pelican bootstrap-rst plugin documenation](https://github.com/getpelican/pelican-plugins/tree/master/bootstrap-rst)
    * [boostrap-rst demo](https://rougier.github.io/bootstrap-rst/)
* [Basics of rst](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
* [Basics of markdown](https://www.markdownguide.org/)
