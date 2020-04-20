Name:		msgpack
Version:	3.1.0
Release:	3%{?dist}
Summary:	Binary-based efficient object serialization library

License:	Boost
URL:		http://msgpack.org
Source0:	https://github.com/msgpack/msgpack-c/releases/download/cpp-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.


%package devel
Summary:	Libraries and header files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for %{name}

%prep
%setup -q  -n %{name}-%{version}/upstream

%build
if test ! -e "obj"; then
  mkdir obj
fi
pushd obj

%cmake .. -DCMAKE_INSTALL_LIBDIR=%{_libdir} -Dlibdir=%{_libdir} -DBUILD_SHARED_LIBS=ON
%make_build %{?_smp_mflags}

popd

%install
make install/fast DESTDIR=$RPM_BUILD_ROOT -C obj

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/msgpack.pc
%{_libdir}/cmake/msgpack
