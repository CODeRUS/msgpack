Name:           msgpack
Version:        0.5.9
Release:        0
Summary:        Efficient object serialization library for cross-language communication
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            http://msgpack.org
Source0:        https://github.com/msgpack/msgpack-c/releases/download/cpp-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.

%package -n libmsgpack3
Summary:        Efficient object serialization library for cross-language communication
Group:          System/Libraries

%description -n libmsgpack3
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.

%package -n libmsgpackc2
Summary:        Efficient object serialization library for cross-language communication
Group:          System/Libraries

%description -n libmsgpackc2
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.

%package -n libmsgpack-devel
Summary:        Development headers for libmsgpack C++ library
Group:          Development/Libraries/C and C++
Requires:       libmsgpack3 = %{version}

%description -n libmsgpack-devel
Provides development headers for the msgpack C++ library.

%package -n libmsgpackc-devel
Summary:        Development headers for libmsgpack C library
Group:          Development/Libraries/C and C++
Requires:       libmsgpackc2 = %{version}

%description -n libmsgpackc-devel
Provides development headers for the msgpack C library.

%prep
%setup -q  -n %{name}-%{version}/upstream

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post -n libmsgpackc2 -p /sbin/ldconfig

%postun -n libmsgpackc2 -p /sbin/ldconfig

%post -n libmsgpack3 -p /sbin/ldconfig

%postun -n libmsgpack3 -p /sbin/ldconfig

%files -n libmsgpackc2
%defattr(-,root,root)
%doc COPYING NOTICE README.md
%{_libdir}/libmsgpackc.so.*

%files -n libmsgpack3
%defattr(-,root,root)
%doc COPYING NOTICE README.md
%{_libdir}/libmsgpack.so.*

%files -n libmsgpackc-devel
%defattr(-,root,root)
%{_libdir}/libmsgpackc.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_includedir}/%{name}/*.h
#%{_includedir}/%{name}/predef/

%files -n libmsgpack-devel
%defattr(-,root,root)
%{_libdir}/libmsgpack.so
%{_includedir}/%{name}.hpp
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/type
%dir %{_includedir}/%{name}/type/tr1
%{_includedir}/%{name}/*.hpp
%{_includedir}/%{name}/type/*.hpp
%{_includedir}/%{name}/type/tr1/*.hpp
#%{_includedir}/%{name}/adaptor/
#%{_includedir}/%{name}/detail/
#%{_includedir}/%{name}/preprocessor/
