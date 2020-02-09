#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : karchive
Version  : 5.67.0
Release  : 33
URL      : https://download.kde.org/stable/frameworks/5.67/karchive-5.67.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.67/karchive-5.67.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.67/karchive-5.67.0.tar.xz.sig
Summary  : Qt 5 addon providing access to numerous types of archives
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: karchive-data = %{version}-%{release}
Requires: karchive-lib = %{version}-%{release}
Requires: karchive-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : bzip2-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev

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
%setup -q -n karchive-5.67.0
cd %{_builddir}/karchive-5.67.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581276222
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581276222
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/karchive
cp %{_builddir}/karchive-5.67.0/COPYING %{buildroot}/usr/share/package-licenses/karchive/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/karchive-5.67.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/karchive/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/karchive.categories

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
/usr/include/KF5/karchive_version.h
/usr/lib64/cmake/KF5Archive/KF5ArchiveConfig.cmake
/usr/lib64/cmake/KF5Archive/KF5ArchiveConfigVersion.cmake
/usr/lib64/cmake/KF5Archive/KF5ArchiveTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Archive/KF5ArchiveTargets.cmake
/usr/lib64/libKF5Archive.so
/usr/lib64/qt5/mkspecs/modules/qt_KArchive.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Archive.so.5
/usr/lib64/libKF5Archive.so.5.67.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/karchive/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/karchive/9a1929f4700d2407c70b507b3b2aaf6226a9543c
