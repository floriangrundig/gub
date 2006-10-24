import os
import re

import download
import misc
import targetpackage

class Ghostscript (targetpackage.TargetBuildSpec):
    def __init__ (self, settings):
        targetpackage.TargetBuildSpec.__init__ (self, settings)
        xsf = re.sub ('version\)s', 'version)s-gpl', download.sf)
        assert (xsf != download.sf)
        if self.settings.platform == 'linux-64':
            self.with (version='8.54',
                   mirror='ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/GPL/gs854/ghostscript-8.54-gpl.tar.bz2',
                   format='bz2')
        else:
            self.with (version='8.50',
                   ## TODO: see if any of these diffs fixes it...
                   ## http://ftp.de.debian.org/debian/pool/main/g/gs-gpl/gs-gpl_8.54.dfsg.1-5.diff.gz
                   ## 8.54 causes piano braces to go bad.
                   #mirror='ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/GPL/gs850/ghostscript-8.54-gpl.tar.bz2',
                   mirror=xsf,
                   format='bz2')

    def license_file (self):
        return '%(srcdir)s/LICENSE' 

    def get_build_dependencies (self):
        return ['libjpeg-devel', 'libpng-devel']

    def get_dependency_dict (self):
        return {'': ['libjpeg', 'libpng']}

    def get_subpackage_names (self):
        return ['doc', '']
    
    def srcdir (self):
        return re.sub ('-source', '', targetpackage.TargetBuildSpec.srcdir (self))

    def builddir (self):
        return re.sub ('-source', '', targetpackage.TargetBuildSpec.builddir (self))

    def name (self):
        return 'ghostscript'

    # FIXME: C&P.
    def ghostscript_version (self):
        return '.'.join (self.ball_version.split ('.')[0:2])

    def patch (self):
        if self.version == '8.50':
            self.system ('cd %(srcdir)s/ && patch --force -p2 < %(patchdir)s/ghostscript-8.50-encoding.patch')
            self.system ('cd %(srcdir)s/ && patch --force -p2 < %(patchdir)s/ghostscript-8.50-ttf.patch')
        if self.version == '8.54':
            self.system ('cd %(srcdir)s/ && patch --force -p1 < %(patchdir)s/05_gxfcopy_qsort_64bit_clean.dpatch')
            self.system ('cd %(srcdir)s/ && patch --force -p1 < %(patchdir)s/gs-r7029.patch')
        
        substs = [(r'\$\(%s\)' % d, '$(DESTDIR)$(%s)' % d) for d in
                  ['bindir', 'datadir', 'gsdir', 'gsdatadir', 'docdir',
                   'mandir', 'scriptdir', 'exdir']]
                
        self.file_sub (substs, '%(srcdir)s/src/unixinst.mak')

    def fixup_arch (self):
        substs = []
        arch = self.settings.target_architecture

        cache_size = 1024*1024
        big_endian = 0
        can_shift = 1
        
        if arch.find ('powerpc') >= 0:
            big_endian = 1
            can_shift = 1
            cache_size = 2097152
        elif re.search ('i[0-9]86', arch):
            big_endian = 0
            can_shift = 0
            cache_size = 1048576
            
        substs = [('#define ARCH_CAN_SHIFT_FULL_LONG .',
             '#define ARCH_CAN_SHIFT_FULL_LONG %d' % can_shift),
             ('#define ARCH_CACHE1_SIZE [0-9]+',
             '#define ARCH_CACHE1_SIZE %d' % cache_size),
             ('#define ARCH_IS_BIG_ENDIAN [0-9]',
             '#define ARCH_IS_BIG_ENDIAN %d' % big_endian)]
        
        self.file_sub (substs, '%(builddir)s/obj/arch.h')

    def compile_command (self):
        return targetpackage.TargetBuildSpec.compile_command (self) + " INCLUDE=%(system_root)s/usr/include/ PSDOCDIR=/usr/share/doc/ PSMANDIR=/usr/share/man "
        
    def compile (self):
        self.system ('''
cd %(builddir)s && (mkdir obj || true)
cd %(builddir)s && make CC=cc CCAUX=cc C_INCLUDE_PATH= CFLAGS= CPPFLAGS= GCFLAGS= LIBRARY_PATH= obj/genconf obj/echogs obj/genarch obj/arch.h
''')
        self.fixup_arch ()
        targetpackage.TargetBuildSpec.compile (self)
        
    def configure_command (self):
        return (targetpackage.TargetBuildSpec.configure_command (self)
            + misc.join_lines ('''
--with-drivers=FILES
--without-x
--disable-cups
--without-ijs
--without-omni
'''))

    def configure (self):
        targetpackage.TargetBuildSpec.configure (self)
        self.file_sub ([
            ('-Dmalloc=rpl_malloc', ''),
            ('GLSRCDIR=./src', 'GLSRCDIR=%(srcdir)s/src'),
            ('PSSRCDIR=./src', 'PSSRCDIR=%(srcdir)s/src'),
            ('PSLIBDIR=./lib', 'PSLIBDIR=%(srcdir)s/lib'),
            ('ICCSRCDIR=icclib', 'ICCSRCDIR=%(srcdir)s/icclib'),
            # ESP-specific: addonsdir, omit zillion of
            # warnings (any important ones may be noticed
            # easier).
            ('ADDONSDIR=./addons', 'ADDONSDIR=%(srcdir)s/addons'),
            (' -Wmissing-prototypes ', ' '),
            (' -Wstrict-prototypes ', ' '),
            (' -Wmissing-declarations ', ' '),

            ## ugh:  GS compile adds another layer of shell expansion. Yuck.
            (r'\$\${ORIGIN}', '\\$${ORIGIN}'),
            ],
               '%(builddir)s/Makefile')

    def install_command (self):
        return (targetpackage.TargetBuildSpec.install_command (self)
                + ' install_prefix=%(install_root)s'
                + ' mandir=/usr/share/man/ '
                + ' docdir=/usr/share/doc/ghostscript/doc '
                + ' exdir=/usr/share/doc/ghostscript/examples '
                )

    def install (self):
        targetpackage.TargetBuildSpec.install (self)
        self.system ('mkdir -p %(install_root)s/usr/etc/relocate/')
        self.dump ('''

prependdir GS_FONTPATH=$INSTALLER_PREFIX/share/ghostscript/%(version)s/fonts
prependdir GS_FONTPATH=$INSTALLER_PREFIX/share/gs/fonts
prependdir GS_LIB=$INSTALLER_PREFIX/share/ghostscript/%(version)s/Resource
prependdir GS_LIB=$INSTALLER_PREFIX/share/ghostscript/%(version)s/lib

''', '%(install_root)s/usr/etc/relocate/gs.reloc')

class Ghostscript__mingw (Ghostscript):
    def __init__ (self, settings):
        Ghostscript.__init__ (self, settings)
        # Configure (compile) without -mwindows for console
        # FIXME: should add to CPPFLAGS...
        self.target_gcc_flags = '-mms-bitfields -D_Windows -D__WINDOWS__'

    def patch (self):
        Ghostscript.patch (self)
        self.system ("cd %(srcdir)s/ && patch --force -p1 < %(patchdir)s/ghostscript-8.15-cygwin.patch")
        self.system ("cd %(srcdir)s/ && patch --force -p1 < %(patchdir)s/ghostscript-8.50-make.patch")
        self.system ("cd %(srcdir)s/ && patch --force -p1 < %(patchdir)s/ghostscript-8.50-unix-aux.mak.patch")
        self.system ("cd %(srcdir)s/ && patch --force -p1 < %(patchdir)s/ghostscript-8.50-gs_dll.h.patch")

    def configure (self):
        Ghostscript.configure (self)
        self.file_sub ([('^(EXTRALIBS *=.*)', '\\1 -lwinspool -lcomdlg32 -lz')],
               '%(builddir)s/Makefile')

        self.file_sub ([('^unix__=.*', misc.join_lines ('''unix__=
$(GLOBJ)gp_mswin.$(OBJ)
$(GLOBJ)gp_wgetv.$(OBJ)
$(GLOBJ)gp_stdia.$(OBJ)
$(GLOBJ)gsdll.$(OBJ)
$(GLOBJ)gp_ntfs.$(OBJ)
$(GLOBJ)gp_win32.$(OBJ)
'''))],
               '%(srcdir)s/src/unix-aux.mak')
        self.file_sub ([('^(LIB0s=.*)', misc.join_lines ('''\\1
$(GLOBJ)gp_mswin.$(OBJ)
$(GLOBJ)gp_wgetv.$(OBJ)
$(GLOBJ)gp_stdia.$(OBJ)
$(GLOBJ)gsdll.$(OBJ)
$(GLOBJ)gp_ntfs.$(OBJ)
$(GLOBJ)gp_win32.$(OBJ)
'''))],
               '%(srcdir)s/src/lib.mak')

        self.dump ('''
GLCCWIN=$(CC) $(CFLAGS) -I$(GLOBJDIR)
PSCCWIN=$(CC) $(CFLAGS) -I$(GLOBJDIR)
include $(GLSRCDIR)/win32.mak
include $(GLSRCDIR)/gsdll.mak
include $(GLSRCDIR)/winplat.mak
include $(GLSRCDIR)/pcwin.mak
''',
             '%(builddir)s/Makefile',
             mode='a')

    def install (self):
        Ghostscript.install (self)
        if self.settings.lilypond_branch == 'lilypond_2_6':
            self.lily_26_kludge()

    def lily_26_kludge (self):
        gs_prefix = '/usr/share/ghostscript/%(ghostscript_version)s'
        fonts = ['c059013l', 'c059016l', 'c059033l', 'c059036l']
        for i in self.read_pipe ('locate %s.pfb' % fonts[0]).split ('\n'):
            dir = os.path.dirname (i)
            if os.path.exists (dir + '/' + fonts[0] + '.afm'):
                break
        fonts_string = ','.join (fonts)
        self.system ('''
mkdir -p %(install_root)s/%(gs_prefix)s/fonts
cp %(dir)s/{%(fonts_string)s}{.afm,.pfb} %(install_root)s/%(gs_prefix)s/fonts
''', locals ())

class Ghostscript__freebsd (Ghostscript):
    def get_dependency_dict (self):
        d = Ghostscript.get_dependency_dict (self)
        d[''].append ('libiconv')
        return d

