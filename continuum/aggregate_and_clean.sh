#!/bin/bash
git clone https://github.com/pyiron/pyiron_continuum "$HOME"/pyiron_continuum/
cp "$HOME"/pyiron_continuum/notebooks/fenics_tutorial.ipynb "$HOME"/
cp "$HOME"/pyiron_continuum/notebooks/damask_tutorial.ipynb "$HOME"/

rm -r "$HOME"/pyiron_continuum
rm "$HOME"/*.yml
rm "$HOME"/Dockerfile
rm "$HOME"/*.sh
