import operator
import os
import re
#
from gub import context
from gub import misc
from gub import target

'''
Module 'solenv' delivered successfully. 0 files copied, 1 files unchanged
Module 'stlport' delivered successfully. 0 files copied, 8 files unchanged
Module 'soltools' delivered successfully. 0 files copied, 14 files unchanged
Module 'external' delivered successfully. 0 files copied, 30 files unchanged
Module 'libwpd' delivered successfully. 0 files copied, 12 files unchanged
Module 'xml2cmp' delivered successfully. 0 files copied, 5 files unchanged
Module 'sal' delivered successfully. 10 files copied, 100 files unchanged
Module 'vos' delivered successfully. 0 files copied, 31 files unchanged
Module 'sandbox' delivered successfully. 0 files copied, 2 files unchanged
Module 'afms' delivered successfully. 0 files copied, 2 files unchanged
Module 'beanshell' delivered successfully. 0 files copied, 2 files unchanged
Module 'cppunit' delivered successfully. 4 files copied, 65 files unchanged
Module 'testshl2' delivered successfully. 0 files copied, 12 files unchanged
Module 'salhelper' delivered successfully. 0 files copied, 12 files unchanged
Module 'extras' delivered successfully. 0 files copied, 70 files unchanged
Module 'fondu' delivered successfully. 0 files copied, 2 files unchanged
Module 'hsqldb' delivered successfully. 0 files copied, 2 files unchanged
Module 'hunspell' delivered successfully. 0 files copied, 15 files unchanged
Module 'hyphen' delivered successfully. 0 files copied, 5 files unchanged
Module 'icc' delivered successfully. 0 files copied, 2 files unchanged
Module 'libtextcat' delivered successfully. 0 files copied, 81 files unchanged
Module 'libwpg' delivered successfully. 0 files copied, 16 files unchanged
Module 'libwps' delivered successfully. 0 files copied, 6 files unchanged
Module 'libxmlsec' delivered successfully. 0 files copied, 1 files unchanged
Module 'lucene' delivered successfully. 0 files copied, 1 files unchanged
Module 'np_sdk' delivered successfully. 0 files copied, 9 files unchanged
Module 'o3tl' delivered successfully. 0 files copied, 5 files unchanged
Module 'psprint_config' delivered successfully. 0 files copied, 1 files unchanged
Module 'rhino' delivered successfully. 0 files copied, 2 files unchanged
Module 'sane' delivered successfully. 0 files copied, 2 files unchanged
Module 'store' delivered successfully. 0 files copied, 8 files unchanged
Module 'registry' delivered successfully. 0 files copied, 23 files unchanged
Module 'idlc' delivered successfully. 0 files copied, 7 files unchanged
Module 'udkapi' delivered successfully. 1 files copied, 417 files unchanged
Module 'offapi' delivered successfully. 3 files copied, 3518 files unchanged
Module 'codemaker' delivered successfully. 0 files copied, 23 files unchanged
Module 'offuh' delivered successfully. 0 files copied, 5518 files unchanged
Module 'cppu' delivered successfully. 0 files copied, 47 files unchanged
Module 'cppuhelper' delivered successfully. 0 files copied, 65 files unchanged
Module 'rdbmaker' delivered successfully. 0 files copied, 4 files unchanged
Module 'ucbhelper' delivered successfully. 0 files copied, 35 files unchanged
Module 'comphelper' delivered successfully. 0 files copied, 107 files unchanged
Module 'basegfx' delivered successfully. 0 files copied, 69 files unchanged
Module 'ridljar' delivered successfully. 0 files copied, 5 files unchanged
Module 'jurt' delivered successfully. 0 files copied, 4 files unchanged
Module 'jvmaccess' delivered successfully. 0 files copied, 6 files unchanged
Module 'bridges' delivered successfully. 1 files copied, 9 files unchanged
Module 'jvmfwk' delivered successfully. 0 files copied, 15 files unchanged
Module 'stoc' delivered successfully. 0 files copied, 28 files unchanged
Module 'cli_ure' delivered successfully. 0 files copied, 6 files unchanged
Module 'unoil' delivered successfully. 0 files copied, 5 files unchanged
Module 'javaunohelper' delivered successfully. 0 files copied, 3 files unchanged
Module 'cpputools' delivered successfully. 0 files copied, 13 files unchanged
Module 'oovbaapi' delivered successfully. 0 files copied, 2 files unchanged
Module 'sax' delivered successfully. 0 files copied, 9 files unchanged
Module 'animations' delivered successfully. 0 files copied, 5 files unchanged
Module 'i18nutil' delivered successfully. 0 files copied, 8 files unchanged
Module 'io' delivered successfully. 0 files copied, 12 files unchanged
Module 'jut' delivered successfully. 0 files copied, 3 files unchanged
Module 'remotebridges' delivered successfully. 0 files copied, 17 files unchanged
Module 'bean' delivered successfully. 0 files copied, 4 files unchanged
Module 'embedserv' delivered successfully. 0 files copied, 1 files unchanged
Module 'eventattacher' delivered successfully. 0 files copied, 2 files unchanged
Module 'hwpfilter' delivered successfully. 0 files copied, 4 files unchanged
Module 'package' delivered successfully. 0 files copied, 6 files unchanged
Module 'regexp' delivered successfully. 0 files copied, 4 files unchanged
Module 'i18npool' delivered successfully. 1 files copied, 40 files unchanged
Module 'tools' delivered successfully. 14 files copied, 92 files unchanged
Module 'unotools' delivered successfully. 3 files copied, 44 files unchanged
Module 'transex3' delivered successfully. 11 files copied, 22 files unchanged
Module 'sot' delivered successfully. 4 files copied, 17 files unchanged
Module 'fileaccess' delivered successfully. 1 files copied, 3 files unchanged
Module 'officecfg' delivered successfully. 1 files copied, 224 files unchanged
Module 'setup_native' delivered successfully. 1 files copied, 57 files unchanged
Module 'rsc' delivered successfully. 2 files copied, 6 files unchanged
Module 'oox' delivered successfully. 1 files copied, 8 files unchanged
Module 'psprint' delivered successfully. 0 files copied, 14 files unchanged
Module 'pyuno' delivered successfully. 0 files copied, 21 files unchanged
Module 'sysui' delivered successfully. 4 files copied, 128 files unchanged
Module 'UnoControls' delivered successfully. 1 files copied, 1 files unchanged
Module 'dtrans' delivered successfully. 3 files copied, 9 files unchanged
Module 'idl' delivered successfully. 1 files copied, 2 files unchanged
Module 'readlicense_oo' delivered successfully. 0 files copied, 12 files unchanged
Module 'sccomp' delivered successfully. 1 files copied, 3 files unchanged
Module 'scp2' delivered successfully. 9 files copied, 82 files unchanged
Module 'testtools' delivered successfully. 0 files copied, 1 files unchanged
Module 'unodevtools' delivered successfully. 0 files copied, 4 files unchanged
Module 'unoxml' delivered successfully. 0 files copied, 3 files unchanged
Module 'ure' delivered successfully. 0 files copied, 9 files unchanged
Module 'vigra' delivered successfully. 0 files copied, 83 files unchanged
Module 'basebmp' delivered successfully. 0 files copied, 37 files unchanged
Module 'wizards' delivered successfully. 0 files copied, 27 files unchanged
Module 'x11_extensions' delivered successfully. 0 files copied, 7 files unchanged
Module 'vcl' delivered successfully. 3 files copied, 140 files unchanged
Module 'toolkit' delivered successfully. 2 files copied, 55 files unchanged
Module 'svtools' delivered successfully. 15 files copied, 300 files unchanged
Module 'uui' delivered successfully. 2 files copied, 4 files unchanged
Module 'goodies' delivered successfully. 27 files copied, 62 files unchanged
Module 'xmloff' delivered successfully. 3 files copied, 124 files unchanged
Module 'ucb' delivered successfully. 0 files copied, 35 files unchanged
Module 'canvas' delivered successfully. 3 files copied, 41 files unchanged
Module 'configmgr' delivered successfully. 0 files copied, 9 files unchanged
Module 'connectivity' delivered successfully. 11 files copied, 71 files unchanged
Module 'xmlscript' delivered successfully. 0 files copied, 12 files unchanged
Module 'fpicker' delivered successfully. 5 files copied, 7 files unchanged
Module 'framework' delivered successfully. 6 files copied, 35 files unchanged
Module 'xmlhelp' delivered successfully. 0 files copied, 10 files unchanged
Module 'accessibility' delivered successfully. 1 files copied, 5 files unchanged
Module 'cppcanvas' delivered successfully. 2 files copied, 15 files unchanged
Module 'embeddedobj' delivered successfully. 1 files copied, 4 files unchanged
Module 'helpcontent2' delivered successfully. 1 files copied, 12 files unchanged
Module 'padmin' delivered successfully. 0 files copied, 4 files unchanged
Module 'scaddins' delivered successfully. 2 files copied, 5 files unchanged
Module 'shell' delivered successfully. 4 files copied, 24 files unchanged
Module 'sj2' delivered successfully. 3 files copied, 3 files unchanged
Module 'basic' delivered successfully. 7 files copied, 45 files unchanged
Module 'sfx2' delivered successfully. 4 files copied, 119 files unchanged
Module 'avmedia' delivered successfully. 2 files copied, 9 files unchanged
Module 'linguistic' delivered successfully. 2 files copied, 11 files unchanged
Module 'svx' delivered successfully. 5 files copied, 637 files unchanged
Module 'dbaccess' delivered successfully. 69 files copied, 1 files unchanged
Module 'automation' delivered successfully. 18 files copied, 2 files unchanged
Module 'basctl' delivered successfully. 17 files copied, 1 files unchanged
Module 'chart2' delivered successfully. 12 files copied, 0 files unchanged
124
'''

class Openoffice (target.AutoBuild):
#    source = 'svn://svn.gnome.org/svn/ooo-build&branch=trunk&revision=14327'
#    source = 'svn://svn.gnome.org/svn/ooo-build&branch=trunk'

    # fresh try.  wait for mingw dupes
    source = 'svn://svn.gnome.org/svn/ooo-build&branch=trunk&revision=14412'
    patches = ['openoffice-srcdir-build.patch']
    upstream_patches = ['openoffice-config_office-cross.patch', 'openoffice-config_office-gnu-make.patch', 'openoffice-solenv-cross.patch', 'openoffice-solenv.patch', 'openoffice-sal-cross.patch', 'openoffice-soltools-cross.patch', 'openoffice-icc-cross.patch', 'openoffice-i18npool-cross.patch']
    def __init__ (self, settings, source):
        target.AutoBuild.__init__ (self, settings, source)
        # let's keep source tree around
        def tracking (self):
            return True
        self.source.is_tracking = misc.bind_method (tracking, self.source)
    def get_build_dependencies (self):
        return ['tools::autoconf', 'boost-devel', 'curl-devel', 'cppunit-devel', 'db-devel', 'expat-devel', 'fontconfig-devel', 'libicu-devel', 'libjpeg-devel', 'libpng-devel', 'liblpsolve-devel', 'python-devel', 'redland-devel', 'saxon-java', 'xerces-c', 'zlib-devel']
    def stages (self):
        return misc.list_insert_before (target.AutoBuild.stages (self),
                                        'compile',
                                        ['dotslash_download', 'make_unpack', 'patch_upstream'])
    def dotslash_download (self):
        self.system ('mkdir -p %(downloads)s/openoffice-src')
        self.system ('cd %(builddir)s && ln %(downloads)s/openoffice-src/* src || :')
        self.system ('cd %(builddir)s && ./download')
        self.system ('cd %(builddir)s && ln src/* %(downloads)s/openoffice-src || :')
    @context.subst_method
    def cvs_tag (self):
        return 'ooo300-m9'
    @context.subst_method
    def upstream_dir (self):
        return '%(builddir)s/build/%(cvs_tag)s'
    @context.subst_method
    def OOO_TOOLS_DIR (self):
        # TODO: either make all ooo-tools (soltools: makedepend..., transex3: transex3 ...)
        # self-hosting or compile them as Openoffice__tools package...
        # Shortcut: use precompiled tools from user's system

        # There's possibly another shortcut: use wine, works for regcomp.
        if not os.environ.has_key ('OOO_TOOLS_DIR'):
            print '''Set OOO_TOOLS_DIR to a recent pre-compiled native solver, I do
export OOO_TOOLS_DIR=/suse/home/janneke/vc/ooo300-m7/build/ooo300-m7/solver/300/unxlngx6.pro/bin
'''
            raise Exception ('OOO_TOOLS_DIR not set')
        return os.environ['OOO_TOOLS_DIR']
    @context.subst_method
    def LD_LIBRARY_PATH (self):
        return '%(OOO_TOOLS_DIR)s/../lib' + misc.append_path (os.environ.get ('LD_LIBRARY_PATH', ''))
    def autoupdate (self):
        # Why is build.py:Build:patch() not doing this?
        map (self.apply_patch, self.__class__.patches)
        self.system ('cd %(srcdir)s && NOCONFIGURE=1 ./autogen.sh --noconfigure')
    def config_cache_overrides (self, str):
        return str + '''
ac_cv_file__usr_share_java_saxon9_jar=${ac_cv_file__usr_share_java_saxon9_jar=yes}
ac_cv_file__usr_share_java_saxon_jar=${ac_cv_file__usr_share_java_saxon_jar=yes}
ac_cv_db_version_minor=${ac_cv_db_version_minor=7}
ac_cv_icu_version_minor=${ac_cv_icu_version_minor=3.81}
'''
#    @context.subst_method
#    def ANT (self):
#        return 'ant'
    def configure_command (self):
        return (target.AutoBuild.configure_command (self)
                + misc.join_lines ('''
--with-additional-sections=MinGW
--with-vendor=\"GUB -- http://lilypond.org/gub\"
--disable-Xaw
--disable-access
--disable-activex
--disable-activex-component
--disable-atl
--disable-binfilter
--disable-build-mozilla
--disable-cairo
--disable-crypt-link
--disable-cups
--disable-dbus
--disable-directx
--disable-epm
--disable-evolution2
--disable-extensions
--disable-fontooo
--disable-gio
--disable-gnome-vfs
--disable-gstreamer
--disable-gtk
--disable-kde
--disable-kdeab
--disable-largefile
--disable-layout
--disable-ldap
--disable-ldap
--disable-libsn
--disable-lockdown
--disable-mathmldtd
--disable-mono
--disable-mozilla
--disable-neon
--disable-odk
--disable-opengl
--disable-pam
--disable-pasf
--disable-pch
--disable-qadevooo
--disable-randr
--disable-rpath
--disable-scsolver
--disable-systray
--disable-vba
--disable-vba 
--disable-xrender-link
--disable-atl

--enable-fontconfig
--enable-verbose

--without-gpc
--without-agg
--without-java
--without-myspell-dicts

--with-system-boost
--with-system-cairo
--with-system-curl
--with-system-db
--with-system-expat
--with-system-icu
--with-system-jpeg
--with-system-libxslt
--with-system-lpsolve
--with-system-neon
--with-system-odbc-headers
--with-system-portaudio
--with-system-redland
--with-system-sablot
--with-system-saxon
--with-system-sndfile
--with-system-xalan
--with-system-xerces
--with-system-xml-apis
--with-system-xrender-headers
--with-saxon-jar=%(system_prefix)s/share/java/saxon9.jar
--without-system-mozilla

--cache-file=%(builddir)s/config.cache

--with-ant-home=/usr/share/ant
--with-tools-dir=%(OOO_TOOLS_DIR)s

'''))

# TODO:
# --with-system-libwpd
# --with-system-libwps
# --with-system-libwpg

    def make_unpack (self):
        # FIXME: python detection is utterly broken, should use python-config
        self.system ('cd %(builddir)s && make unpack')
        self.system ('cd %(builddir)s && make patch.apply')
    def apply_upstream_patch (self, name, strip_component=0):
        patch_strip_component = str (strip_component)
        self.system ('''
cd %(builddir)s/build/%(cvs_tag)s && patch -p%(patch_strip_component)s < %(patchdir)s/%(name)s
''', locals ())
    def upstream_patched_files (self):
        def files_in_patch (patch):
            string = file (self.expand ('%(patchdir)s/%(patch)s', locals ())).read ()
            def file_name (chunk):
                if chunk.find ('\n+++ ') >= 0:
                    return re.search ('\n[+]{3}\s+([.]/)?([^\s]+)', chunk).group (2)
                return ''
            return map (file_name, ('\n' + string).split ('\n---')[1:])
        files_with_patches = map (files_in_patch, self.upstream_patches)
        return reduce (operator.__add__, files_with_patches)
    def upstream_patch_reset (self):
        upstream_dir = self.upstream_dir ()
        for f in self.upstream_patched_files ():
            self.system ('cp -p %(upstream_dir)s/%(f)s.pristine %(upstream_dir)s/%(f)s || cp -p %(upstream_dir)s/%(f)s %(upstream_dir)s/%(f)s.pristine' % locals ())
    def patch_upstream (self):
        self.upstream_patch_reset ()
        map (self.apply_upstream_patch, self.__class__.upstream_patches)

        # FIXME: neutralize silly GNU make check
        # self.system ('''sed -i -e "s@' 3[.]81'@'gpuhleez, we are not even building mozilla'@" %(upstream_dir)s/config_office/configure.in')

        # configure blindly adds /usr includes, even when not necessary
        self.system ('sed -i -e "s@=/usr/include@=%(system_prefix)s/include@" %(upstream_dir)s/config_office/configure.in')

        # configure.in uses AC_CHECK_FILE, which simply assert-fails
        # when cross compiling slated for removal in ~2000
        # http://www.mail-archive.com/autoconf@gnu.org/msg02857.html
        self.system ('sed -i -e "s@AC_CHECK_FILE(@AC_CHECK_FILE_CROSS(@" %(upstream_dir)s/config_office/configure.in')

        # TODO: ASM is handled in individual solenv/inc/*mk
        self.system (misc.join_lines ('''sed -i.guborig
-e 's@\<ar\>@$(AR)@g'
-e 's@\<dlltool\>@$(DLLTOOL)@g'
-e 's@\<ld\>\([^-]\|$\)@$(LD)\\1@g'
-e 's@\<nm\>@$(NM)@g'
-e 's@\<ranlib\>@$(RANLIB)@g'
-e 's@\<windres\>@$(WINDRES)@g'
%(upstream_dir)s/solenv/inc/*mk'''))

        self.system ('chmod +x %(upstream_dir)s/solenv/bin/build.pl %(upstream_dir)s/solenv/bin/deliver.pl')

        have_wine = True
        disable_modules = [
            'bean', # com_sun_star_comp_beans_LocalOfficeWindow.c:39:18: error: jawt.h: No such file or directory
            'embedserv', # uses ATL http://article.gmane.org/gmane.comp.gnu.mingw.user/18483
            ]

        # ~/.wine/system.reg
        # "PATH"=str(2):"C:/windows/system32;C:/windows;z:/home/janneke/vc/gub/target/mingw/build/openoffice-trunk/build/ooo300-m9/solver/300/bin/wntgcci.pro/bin;z:/home/janneke/vc/gub/target/mingw/root/usr/bin;z:/home/janneke/vc/gub/target/mingw/root/usr/lib;"
        wine_modules = [
            'testtools',
            'goodies',
            # Hmmm
            # wine   ../../../solver/300/wntgcci.pro/bin/regcomp.exe -register -r applicat.rdb -c i18npool.uno.dll
        ]

        for module in disable_modules:
            self.file_sub ([('(^[^#].*[ \t](all|n|w|w,vc[0-9])[ \t])', r'#\1')], '%(upstream_dir)s/%(module)s/prj/build.lst', env=locals ())

        module = 'setup_native'
        self.file_sub ([('^([^#]pk.*customactions)', '#\1')], '%(upstream_dir)s/%(module)s/prj/build.lst', env=locals ())

        # uses oledb.h from psdk 
        module = 'connectivity'
        self.file_sub ([(r'^([^#].*drivers.ado.*[ \t]w[ \t])', '#\1')], '%(upstream_dir)s/%(module)s/prj/build.lst', env=locals ())

    def makeflags (self):
        return misc.join_lines ('''
NASM=nasm
CC_FOR_BUILD=cc
CXX_FOR_BUILD=c++
LDFLAGS_FOR_BUILD=
C_INCLUDE_PATH=
LIBRARY_PATH=
EXECPOST=
LD_LIBRARY_PATH=%(LD_LIBRARY_PATH)s
''')
##main configure barfs
##CPPFLAGS=
                
class Openoffice__mingw (Openoffice):
    Openoffice.upstream_patches += ['openoffice-config_office-mingw.patch', 'openoffice-solenv-mingw.patch', 'openoffice-sal-mingw.patch', 'openoffice-external-mingwheaders.patch', 'openoffice-cppunit-mingw.patch', 'openoffice-i18npool-mingw.patch', 'openoffice-tools-mingw.patch', 'openoffice-setup_native-mingw.patch', 'openoffice-pyuno-mingw.patch', 'openoffice-sysui-mingw.patch', 'openoffice-dtrans-mingw.patch', 'openoffice-fpicker-mingw.patch', 'openoffice-sccomp-mingw.patch', 'openoffice-vcl-mingw.patch', 'openoffice-connectivity-mingw.patch', 'openoffice-unotools-mingw.patch', 'openoffice-embeddedobj-mingw.patch', 'openoffice-shell-mingw.patch', 'openoffice-svx-mingw.patch', 'openoffice-dbaccess-mingw.patch', 'openoffice-desktop-mingw.patch']
    # external/mingwheaders seems a badly misguided effort.  It
    # patches header files and is thus strictly tied to a gcc version;
    # that can never build.  How can patching header files ever work,
    # when not patching the corresponding libraries?  Some patches
    # remove #ifdef checks that can be enabled by setting a #define.
    # Other patches only affect OO.o client code already inside
    # __MINGW32__ defines.  Why not fix OO.o makefiles and client
    # code?
    Openoffice.upstream_patches += ['openoffice-sal-mingw-c.patch']
    # Kendy's MinGW patches are already applied
    kendy = ['openoffice-transex3-mingw.patch', 'openoffice-soltools-mingw.patch']
    def get_build_dependencies (self):
        return Openoffice.get_build_dependencies (self) + ['libunicows-devel']
    def patch (self):
        Openoffice.patch (self)
        # disable Kendy's patch for Cygwin version of mingw
        self.file_sub ([('^(mingw-build-without-stlport-stlport.diff)', r'#\1')],
                       '%(srcdir)s/patches/dev300/apply')
        # setup wine hack
        wine_userdef = os.path.join (os.environ['HOME'], '.wine/user.reg')
        s = file (wine_userdef).read ()
        if not self.expand ('%(upstream_dir)s') in s:
            self.dump ('''
[Environment]
"PATH"="%(upstream_dir)s/solver/300/wntgcci.pro/bin;%(system_prefix)s/bin;%(system_prefix)s/lib;"
''',
                   wine_userdef, mode='a')
    def configure_command (self):
        return (Openoffice.configure_command (self)
                .replace ('--with-system-xrender-headers', '')
                + ' --disable-xrender-link'
                + ' --with-distro=Win32')
    def patch_upstream (self):
        self.system ('chmod -R ugo+w %(upstream_dir)s/dtrans %(upstream_dir)s/fpicker %(upstream_dir)s/dbaccess')
        Openoffice.patch_upstream (self)
        # avoid juggling of names for windows-nt
        self.system ('sed -i -e "s@WINNT@WNT@" %(upstream_dir)s/config_office/configure.in')
        self.file_sub ([
                ('( [.](type|size))', r'//\1'),
                ('( [.]note.*)', ''),
                ('(,@.*)', '')],
                       '%(upstream_dir)s/bridges/source/cpp_uno/mingw_intel/call.s')

        self.system ('chmod +x %(upstream_dir)s/solenv/bin/addsym-mingw.sh')
        
        self.system ('cp -f %(upstream_dir)s/sal/osl/w32/MAKEFILE.MK %(upstream_dir)s/sal/osl/w32/makefile.mk')

        self.dump ('''\
#! /bin/sh
set -e
in=$(eval echo '$'$#)
dir=$(dirname $in)
/usr/bin/wrc "$@"
if test "$dir" != "." -a -e $(basename $in .rc).res; then
    mv $(basename $in .rc).res $dir
fi
''',
             '%(upstream_dir)s/solenv/bin/wrc',
                   permissions=0755)

        self.system ('mkdir -p %(upstream_dir)s/solver/300/wntgcci.pro/inc')
        self.system ('cp -pv %(sourcefiledir)s/mingw-headers/*.h %(upstream_dir)s/solver/300/wntgcci.pro/inc')
