#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : karchive
Version  : 5.51.0
Release  : 8
URL      : https://download.kde.org/stable/frameworks/5.51/karchive-5.51.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.51/karchive-5.51.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.51/karchive-5.51.0.tar.xz.sig
Summary  : No detailed summary available
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
%setup -q -n karchive-5.51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539613541
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539613541
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/karchive
cp COPYING %{buildroot}/usr/share/package-licenses/karchive/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/karchive/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/karchive.categories

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
/usr/lib64/libKF5Archive.so.5.51.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/karchive/COPYING
/usr/share/package-licenses/karchive/COPYING.LIB
