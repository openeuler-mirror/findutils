Name: findutils
Epoch: 2
Version: 4.8.0
Release: 4
Summary: The GNU Find Utilities
License: GPLv3+
URL: http://www.gnu.org/software/findutils/
Source0: https://ftp.gnu.org/pub/gnu/findutils/%{name}-%{version}.tar.xz

# resolve test failures when ran as root
# https://savannah.gnu.org/bugs/?57762
Patch1:        backport-findutils-xautofs.patch
# rhbz #1252549 #1299169
Patch2:        backport-findutils-leaf-opt.patch
Patch3:        backport-maint-fix-typo-in-comments-in-parser.c.patch
%ifarch sw_64
Patch4:        findutils-4.8.0-sw.patch
%endif

Buildrequires: gcc autoconf gettext-devel texinfo libselinux-devel dejagnu automake gdb

Requires(post): info
Requires(preun):info

Provides: /bin/find
Provides: bundled(gnulib)

%description
The GNU Find Utilities are the basic directory searching utilities of
the GNU operating system. These programs are typically used in
conjunction with other programs to provide modular and powerful
directory search and file locating capabilities to other commands.

The tools supplied with this package are:

find - search for files in a directory hierarchy
locate - list files in databases that match a pattern
updatedb - update a file name database
xargs - build and execute command lines from standard input

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

autoreconf -fiv

%build
%ifarch aarch64
CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%endif
%configure

%make_build

%check
make check

%install
%make_install

rm -f %{buildroot}%{_infodir}/dir

%find_lang %{name}

%pre

%preun help
if [ $1 = 0 ]; then
  if [ -f %{_infodir}/find.info.gz ]; then
    /sbin/install-info --delete %{_infodir}/find.info.gz %{_infodir}/dir || :
  fi
fi

%post help
if [ -f %{_infodir}/find.info.gz ]; then
  /sbin/install-info %{_infodir}/find.info.gz %{_infodir}/dir || :
fi

%postun

%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS TODO
%license COPYING
%{_bindir}/find
%{_bindir}/xargs
%exclude %{_bindir}/{locate,updatedb}
%exclude %{_prefix}/libexec/frcode
%exclude %{_libdir}/find
%exclude %{_prefix}/lib/debug/usr/bin/locate*.debug
%exclude %{_prefix}/lib/debug/usr/libexec/frcode*.debug

%files help
%{_mandir}/man1/find.1*
%{_mandir}/man1/xargs.1*
%{_infodir}/find.info*
%{_infodir}/find-maint.info.gz
%exclude %{_mandir}/man1/{locate.1*,updatedb.1*}
%exclude %{_mandir}/man5/locatedb.5*

%changelog
* Tue Oct 25 2022 zhoushuiqing <zhoushuiqing2@huawei.com> - 2:4.8.0-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix typo in comments in parser.c

* Sat Feb 26 2022 shixuantong <shixuantong@h-partners.com> - 2:4.8.0-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix test_localeconv fail in aarch64 machine

* Tue Dec 21 2021 shixuantong <shixuantong@huawei.com> - 2:4.8.0-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add -fsigned-char to %check

* Mon Aug 30 2021 shixuantong <shixuantong@huawei.com> - 2:4.8.0-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update version to 4.8.0

* Fri Mar 19 2021 shixuantong <shixuantong@huawei.com> - 2:4.7.0-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix test_localeconv fail in aarch64 machine

* Thu Apr 23 2020 openEuler Buildteam <buildteam@openeuler.org> - 2:4.7.0-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:revert remove S_MAGIC_XFS and remove NOSTAT_LEAF_OPTIMIZATION to fix coredump

* Fri Apr 10 2020 openEuler Buildteam <buildteam@openeuler.org> - 2:4.7.0-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:remove S_MAGIC_XFS fix coredump

* Tue Feb 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 2:4.7.0-4
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Fix test failures ran as root and enable -xautofs and disable leaf opt

* Wed Jan 22 2020 openEuler Buildteam <buildteam@openeuler.org> - 2:4.7.0-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:resolve self-build problem

* Tue Jan 7 2020 openEuler Buildteam <buildteam@openeuler.org> - 2:4.7.0-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:delete redundant file

* Tue Dec 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.7.0-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update to 4.7.0

* Fri Dec 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.6.0-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add build requires and requires

* Mon Oct 28 2019 shenyangyang <shenyangyang4@huawei.com> - 2:4.6.0-4
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add build requires of texinfo and gettext-devel to slove the build problem

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.6.0-3
- Adjust requires

* Fri Sep 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.6.0-2
- Delete redundant information

* Thu Aug 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.6.0-1
- Package init
