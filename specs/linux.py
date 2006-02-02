import glob
import os
import re

import cross
import download
import framework
import gub
import targetpackage

class Libc6 (gub.Binary_package, gub.Sdk_package):
	pass

class Libc6_dev (gub.Binary_package, gub.Sdk_package):
	def untar (self):
		gub.Binary_package.untar (self)
		# Ugh, rewire absolute names and symlinks.
		# Better to create relative ones?

		# FIXME: this rewiring breaks ld badly, it says
		#     i686-linux-ld: cannot find /home/janneke/bzr/gub/target/i686-linux/system/lib/libc.so.6 inside /home/janneke/bzr/gub/target/i686-linux/system/
		# although that file exists.  Possibly rewiring is not necessary,
		# but we can only check on non-linux platform.
		# self.file_sub ([(' /', ' %(system_root)s/')],
		#	       '%(srcdir)s/root/usr/lib/libc.so')

		for i in glob.glob (self.expand ('%(srcdir)s/root/usr/lib/lib*.so')):
			if os.path.islink (i):
				s = os.readlink (i)
				if s.startswith ('/'):
					os.remove (i)
					os.symlink (self.settings.system_root
						    + s, i)
		for i in ('pthread.h', 'bits/sigthread.h'):
			self.file_sub ([('__thread', '___thread')],
				       '%(srcdir)s/root/usr/include/%(i)s',
				       env=locals ())

		self.system ('rm -rf  %(srcdir)s/root/usr/include/asm/  %(srcdir)s/root/usr/include/linux ')
			
class Linux_kernel_headers (gub.Binary_package, gub.Sdk_package):
	pass

def get_packages (settings):
	packages = [
		Libc6 (settings).with (version='2.2.5-11.8', mirror=download.glibc_deb, format='deb'),
		Libc6_dev (settings).with (version='2.2.5-11.8', mirror=download.glibc_deb, format='deb'),
		Linux_kernel_headers (settings).with (version='2.6.13+0rc3-2', mirror=download.lkh_deb, format='deb'),
		cross.Binutils (settings).with (version='2.16.1', format='bz2'),
		cross.Gcc (settings).with (version='4.0.2',
					   mirror=download.gcc, format='bz2',
					   depends=['binutils']),
		]
	return packages



def change_target_packages (packages):
	cross.change_target_packages (packages)
	for p in packages:
		if isinstance (p, targetpackage.Target_package):
			gub.change_target_dict (p,
						{'LD': '%(target_architecture)s-ld --as-needed',
						 'LDFLAGS': '-Wl,--as-needed',
						 })

	cross.set_framework_ldpath ([p for p in packages if isinstance (p, targetpackage.Target_package)])
