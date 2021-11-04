#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : killbots
Version  : 21.08.3
Release  : 34
URL      : https://download.kde.org/stable/release-service/21.08.3/src/killbots-21.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.3/src/killbots-21.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.3/src/killbots-21.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: killbots-bin = %{version}-%{release}
Requires: killbots-data = %{version}-%{release}
Requires: killbots-license = %{version}-%{release}
Requires: killbots-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n killbots-21.08.3
cd %{_builddir}/killbots-21.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636065860
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1636065860
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/killbots
cp %{_builddir}/killbots-21.08.3/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/killbots/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/killbots-21.08.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/killbots/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang killbots

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/package-licenses/killbots/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/killbots/7697008f58568e61e7598e796eafc2a997503fde

%files locales -f killbots.lang
%defattr(-,root,root,-)

