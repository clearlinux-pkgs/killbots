#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : killbots
Version  : 23.04.2
Release  : 55
URL      : https://download.kde.org/stable/release-service/23.04.2/src/killbots-23.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.2/src/killbots-23.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.2/src/killbots-23.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: killbots-bin = %{version}-%{release}
Requires: killbots-data = %{version}-%{release}
Requires: killbots-license = %{version}-%{release}
Requires: killbots-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==========================
Killbots C++ Style Guide
==========================
*******************************************************************************
Indentation
*******************************************************************************

%package bin
Summary: bin components for the killbots package.
Group: Binaries
Requires: killbots-data = %{version}-%{release}
Requires: killbots-license = %{version}-%{release}

%description bin
bin components for the killbots package.


%package data
Summary: data components for the killbots package.
Group: Data

%description data
data components for the killbots package.


%package doc
Summary: doc components for the killbots package.
Group: Documentation

%description doc
doc components for the killbots package.


%package license
Summary: license components for the killbots package.
Group: Default

%description license
license components for the killbots package.


%package locales
Summary: locales components for the killbots package.
Group: Default

%description locales
locales components for the killbots package.


%prep
%setup -q -n killbots-23.04.2
cd %{_builddir}/killbots-23.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686525498
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1686525498
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/killbots
cp %{_builddir}/killbots-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/killbots/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/killbots-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/killbots/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/killbots-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/killbots/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/killbots-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/killbots/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/killbots-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/killbots/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang killbots
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/killbots
/usr/bin/killbots

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.killbots.desktop
/usr/share/config.kcfg/killbots.kcfg
/usr/share/icons/hicolor/128x128/apps/killbots.png
/usr/share/icons/hicolor/16x16/apps/killbots.png
/usr/share/icons/hicolor/22x22/apps/killbots.png
/usr/share/icons/hicolor/32x32/apps/killbots.png
/usr/share/icons/hicolor/48x48/apps/killbots.png
/usr/share/icons/hicolor/64x64/apps/killbots.png
/usr/share/killbots/rulesets/classic.desktop
/usr/share/killbots/rulesets/daleks.desktop
/usr/share/killbots/rulesets/default.desktop
/usr/share/killbots/rulesets/easy.desktop
/usr/share/killbots/rulesets/energycrisis.desktop
/usr/share/killbots/themes/classic.desktop
/usr/share/killbots/themes/classic.png
/usr/share/killbots/themes/classic.svgz
/usr/share/killbots/themes/mountainadventure.desktop
/usr/share/killbots/themes/mountainadventure.png
/usr/share/killbots/themes/mountainadventure.svgz
/usr/share/killbots/themes/mummymadness.desktop
/usr/share/killbots/themes/mummymadness.png
/usr/share/killbots/themes/mummymadness.svgz
/usr/share/killbots/themes/robotkill.desktop
/usr/share/killbots/themes/robotkill.png
/usr/share/killbots/themes/robotkill.svgz
/usr/share/metainfo/org.kde.killbots.appdata.xml
/usr/share/qlogging-categories5/killbots.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/killbots/index.cache.bz2
/usr/share/doc/HTML/ca/killbots/index.docbook
/usr/share/doc/HTML/de/killbots/index.cache.bz2
/usr/share/doc/HTML/de/killbots/index.docbook
/usr/share/doc/HTML/de/killbots/status.png
/usr/share/doc/HTML/en/killbots/enemy.png
/usr/share/doc/HTML/en/killbots/fastenemy.png
/usr/share/doc/HTML/en/killbots/grid.png
/usr/share/doc/HTML/en/killbots/hero.png
/usr/share/doc/HTML/en/killbots/index.cache.bz2
/usr/share/doc/HTML/en/killbots/index.docbook
/usr/share/doc/HTML/en/killbots/junkheap.png
/usr/share/doc/HTML/en/killbots/status.png
/usr/share/doc/HTML/en/killbots/waitoutround.png
/usr/share/doc/HTML/es/killbots/index.cache.bz2
/usr/share/doc/HTML/es/killbots/index.docbook
/usr/share/doc/HTML/et/killbots/index.cache.bz2
/usr/share/doc/HTML/et/killbots/index.docbook
/usr/share/doc/HTML/fr/killbots/index.cache.bz2
/usr/share/doc/HTML/fr/killbots/index.docbook
/usr/share/doc/HTML/it/killbots/index.cache.bz2
/usr/share/doc/HTML/it/killbots/index.docbook
/usr/share/doc/HTML/nl/killbots/index.cache.bz2
/usr/share/doc/HTML/nl/killbots/index.docbook
/usr/share/doc/HTML/pl/killbots/index.cache.bz2
/usr/share/doc/HTML/pl/killbots/index.docbook
/usr/share/doc/HTML/pl/killbots/status.png
/usr/share/doc/HTML/pt/killbots/index.cache.bz2
/usr/share/doc/HTML/pt/killbots/index.docbook
/usr/share/doc/HTML/pt_BR/killbots/index.cache.bz2
/usr/share/doc/HTML/pt_BR/killbots/index.docbook
/usr/share/doc/HTML/sv/killbots/index.cache.bz2
/usr/share/doc/HTML/sv/killbots/index.docbook
/usr/share/doc/HTML/uk/killbots/index.cache.bz2
/usr/share/doc/HTML/uk/killbots/index.docbook
/usr/share/doc/HTML/uk/killbots/status.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/killbots/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/killbots/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/killbots/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/killbots/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/killbots/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f killbots.lang
%defattr(-,root,root,-)

