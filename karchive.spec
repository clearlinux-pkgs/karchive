#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : karchive
Version  : 5.110.0
Release  : 77
URL      : https://download.kde.org/stable/frameworks/5.110/karchive-5.110.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.110/karchive-5.110.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.110/karchive-5.110.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-2.0
Requires: karchive-data = %{version}-%{release}
Requires: karchive-lib = %{version}-%{release}
Requires: karchive-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : bzip2-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(libzstd)
BuildRequires : xz-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KArchive
Reading, creating, and manipulating file archives
## Introduction
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

%package data
Summary: data components for the karchive package.
Group: Data

%description data
data components for the karchive package.


%package dev
Summary: dev components for the karchive package.
Group: Development
Requires: karchive-lib = %{version}-%{release}
Requires: karchive-data = %{version}-%{release}
Provides: karchive-devel = %{version}-%{release}
Requires: karchive = %{version}-%{release}

%description dev
dev components for the karchive package.


%package lib
Summary: lib components for the karchive package.
Group: Libraries
Requires: karchive-data = %{version}-%{release}
Requires: karchive-license = %{version}-%{release}

%description lib
lib components for the karchive package.


%package license
Summary: license components for the karchive package.
Group: Default

%description license
license components for the karchive package.


%prep
%setup -q -n karchive-5.110.0
cd %{_builddir}/karchive-5.110.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694444611
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
export SOURCE_DATE_EPOCH=1694444611
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/karchive
cp %{_builddir}/karchive-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/karchive/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/karchive-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/karchive/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/karchive-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/karchive/20079e8f79713dce80ab09774505773c926afa2a || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/de/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/es/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/id/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/it/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/karchive5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/karchive5_qt.qm
/usr/share/qlogging-categories5/karchive.categories
/usr/share/qlogging-categories5/karchive.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KArchive/K7Zip
/usr/include/KF5/KArchive/KAr
/usr/include/KF5/KArchive/KArchive
/usr/include/KF5/KArchive/KArchiveDirectory
/usr/include/KF5/KArchive/KArchiveEntry
/usr/include/KF5/KArchive/KArchiveFile
/usr/include/KF5/KArchive/KCompressionDevice
/usr/include/KF5/KArchive/KFilterBase
/usr/include/KF5/KArchive/KFilterDev
/usr/include/KF5/KArchive/KRcc
/usr/include/KF5/KArchive/KTar
/usr/include/KF5/KArchive/KZip
/usr/include/KF5/KArchive/KZipFileEntry
/usr/include/KF5/KArchive/k7zip.h
/usr/include/KF5/KArchive/kar.h
/usr/include/KF5/KArchive/karchive.h
/usr/include/KF5/KArchive/karchive_export.h
/usr/include/KF5/KArchive/karchive_version.h
/usr/include/KF5/KArchive/karchivedirectory.h
/usr/include/KF5/KArchive/karchiveentry.h
/usr/include/KF5/KArchive/karchivefile.h
/usr/include/KF5/KArchive/kcompressiondevice.h
/usr/include/KF5/KArchive/kfilterbase.h
/usr/include/KF5/KArchive/kfilterdev.h
/usr/include/KF5/KArchive/krcc.h
/usr/include/KF5/KArchive/ktar.h
/usr/include/KF5/KArchive/kzip.h
/usr/include/KF5/KArchive/kzipfileentry.h
/usr/lib64/cmake/KF5Archive/KF5ArchiveConfig.cmake
/usr/lib64/cmake/KF5Archive/KF5ArchiveConfigVersion.cmake
/usr/lib64/cmake/KF5Archive/KF5ArchiveTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Archive/KF5ArchiveTargets.cmake
/usr/lib64/libKF5Archive.so
/usr/lib64/qt5/mkspecs/modules/qt_KArchive.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Archive.so.5.110.0
/usr/lib64/libKF5Archive.so.5
/usr/lib64/libKF5Archive.so.5.110.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/karchive/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/karchive/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/karchive/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
