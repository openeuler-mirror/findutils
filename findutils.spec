Name: findutils
Epoch: 2
Version: 4.6.0
Release: 3
Summary: The GNU Find Utilities
License: GPLv3+
URL: http://www.gnu.org/software/findutils/
Source0: https://ftp.gnu.org/pub/gnu/findutils/%{name}-%{version}.tar.gz

# prevent mbrtowc tests from failing (#1294016)
Patch0: findutils-4.6.0-mbrtowc-tests.patch

# do not build locate
Patch1: findutils-4.5.15-no-locate.patch

# fix build failure with glibc-2.28
# https://lists.gnu.org/r/bug-gnulib/2018-03/msg00000.html
Patch2: findutils-4.6.0-gnulib-fflush.patch

# add a new option -xautofs to find to not descend into directories on autofs
# file systems
Patch3: findutils-4.4.2-xautofs.patch

# eliminate compile-time warnings
Patch4: findutils-4.5.13-warnings.patch

# clarify exit status handling of -exec cmd {} + in find(1) man page (#1325049)
Patch5: findutils-4.6.0-man-exec.patch

# make sure that find -exec + passes all arguments (upstream bug #48030)
Patch6: findutils-4.6.0-exec-args.patch

# fix build failure with glibc-2.25+
Patch7: findutils-4.6.0-gnulib-makedev.patch

# avoid SIGSEGV in case the internal -noop option is used (#1346471)
Patch9: findutils-4.6.0-internal-noop.patch

# test-lock: disable the rwlock test
Patch10: findutils-4.6.0-test-lock.patch

# import gnulib's FTS module from upstream commit 281b825e (#1544429)
Patch11: findutils-4.6.0-fts-update.patch

# implement the -noleaf option of find (#1252549)
Patch12: findutils-4.6.0-leaf-opt.patch

#upstream patches
Patch6000: Remove-the-enable-id-cache-configure-option.patch
Patch6001: find-Fix-a-number-of-compiler-warnings-mostly-const-.patch
Patch6002: lib-Update-the-width-of-the-st_nlink-field-and-fix-s.patch
Patch6003: regexprops-Fix-compiler-warnings-and-update-copyrigh.patch
Patch6004: Fix-bug-48314-find-fix-type-option-regression-on-som.patch
Patch6005: maint-remove-ChangeLog-2013-from-distribution-tarbal.patch
Patch6006: find-handle-more-readdir-3-errors.patch
Patch6007: find-fix-memory-leak-in-mount-list-handling.patch
Patch6008: find-fix-printf-h-for-arguments-with-one-or-more-tra.patch
Patch6009: xargs-add-o-open-tty-option.patch
Patch6010: find-avoid-strftime-s-non-portable-F-specifier.patch
Patch6011: find-avoid-usage-in-more-error-cases.patch
Patch6012: find-give-helpful-hint-for-unquoted-patterns-errors.patch
Patch6013: find-avoid-buffer-overflow-with-printf-T.patch
Patch6014: regexprops-fix-dangling-reference-to-the-ed-regular-.patch
Patch6015: find-make-delete-honour-the-ignore_readdir_race-opti.patch
Patch6016: Shorten-output-of-qmark_chars-after-replacing-a-mult.patch
Patch6017: find-process-unreadable-directories-with-depth.patch
Patch6018: ftsfind.c-avoid-buffer-overflow-in-D-code.patch
Patch6019: find-fix-printf-Y-output-to-N-for-broken-links.patch
Patch6020: print.c-move-else-into-ifdef-S_ISLNK.patch
Patch6021: find-printf-Y-handle-ENOTDIR-also-as-broken-symlink.patch
Patch6022: find-improve-warning-diagnostic-for-the-name-iname-w.patch
Patch6023: find-make-pred_empty-safer-and-avoid-fd-leaks.patch

Buildrequires: gcc autoconf

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

# needed because of findutils-4.5.15-no-locate.patch
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

%files help
%{_mandir}/man1/find.1*
%{_mandir}/man1/xargs.1*
%{_infodir}/find.info*
%{_infodir}/find-maint.info.gz


%changelog
* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.6.0-3
- Adjust requires

* Fri Sep 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.6.0-2
- Delete redundant information

* Thu Aug 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:4.6.0-1
- Package init
