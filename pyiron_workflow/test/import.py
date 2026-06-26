from pyiron_atomistics import Project
Project('.').create.structure.bulk("Fe").repeat(2).plot3d()
