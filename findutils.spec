Name: findutils
Epoch: 2
Version: 4.7.0
Release: 1
Summary: The GNU Find Utilities
License: GPLv3+
URL: http://www.gnu.org/software/findutils/
Source0: https://ftp.gnu.org/pub/gnu/findutils/%{name}-%{version}.tar.xz

Patch:  findutils-4.4.2-xautofs.patch

Buildrequires: gcc autoconf gettext-devel texinfo libselinux-devel dejagnu

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
