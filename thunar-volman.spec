#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : thunar-volman
Version  : 4.16.0
Release  : 18
URL      : http://archive.xfce.org/src/xfce/thunar-volman/4.16/thunar-volman-4.16.0.tar.bz2
Source0  : http://archive.xfce.org/src/xfce/thunar-volman/4.16/thunar-volman-4.16.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: thunar-volman-bin = %{version}-%{release}
Requires: thunar-volman-data = %{version}-%{release}
Requires: thunar-volman-license = %{version}-%{release}
Requires: thunar-volman-locales = %{version}-%{release}
BuildRequires : intltool
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxfconf-0)

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/xfce/thunar-volman/-/blob/master/COPYING)

%package bin
Summary: bin components for the thunar-volman package.
Group: Binaries
Requires: thunar-volman-data = %{version}-%{release}
Requires: thunar-volman-license = %{version}-%{release}

%description bin
bin components for the thunar-volman package.


%package data
Summary: data components for the thunar-volman package.
Group: Data

%description data
data components for the thunar-volman package.


%package license
Summary: license components for the thunar-volman package.
Group: Default

%description license
license components for the thunar-volman package.


%package locales
Summary: locales components for the thunar-volman package.
Group: Default

%description locales
locales components for the thunar-volman package.


%prep
%setup -q -n thunar-volman-4.16.0
cd %{_builddir}/thunar-volman-4.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609177652
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1609177652
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/thunar-volman
cp %{_builddir}/thunar-volman-4.16.0/COPYING %{buildroot}/usr/share/package-licenses/thunar-volman/dfac199a7539a404407098a2541b9482279f690d
%make_install
%find_lang thunar-volman

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/thunar-volman
/usr/bin/thunar-volman-settings

%files data
%defattr(-,root,root,-)
/usr/share/applications/thunar-volman-settings.desktop
/usr/share/icons/hicolor/128x128/apps/org.xfce.volman.png
/usr/share/icons/hicolor/16x16/apps/org.xfce.volman.png
/usr/share/icons/hicolor/24x24/apps/org.xfce.volman.png
/usr/share/icons/hicolor/32x32/apps/org.xfce.volman.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.volman.png
/usr/share/icons/hicolor/scalable/apps/org.xfce.volman.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/thunar-volman/dfac199a7539a404407098a2541b9482279f690d

%files locales -f thunar-volman.lang
%defattr(-,root,root,-)

