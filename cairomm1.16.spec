#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C++ wrapper for cairo
Summary(pl.UTF-8):	Interfejs C++ do cairo
Name:		cairomm1.16
Version:	1.18.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://www.cairographics.org/releases/cairomm-%{version}.tar.xz
# Source0-md5:	4c7afc4ab5177655724ea4b31794db30
URL:		https://www.cairographics.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	doxygen >= 1:1.8.9
BuildRequires:	graphviz
BuildRequires:	libsigc++3-devel >= 1:3.0.0
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mm-common >= 0.9.12
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	cairo >= 1.14.0
Requires:	libsigc++3 >= 1:3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrapper for cairo.

%description -l pl.UTF-8
Interfejs C++ do cairo.

%package devel
Summary:	Development files for cairomm library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki cairomm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.14.0
Requires:	libsigc++3-devel >= 1:3.0.0
Requires:	libstdc++-devel >= 6:7

%description devel
Development files for cairomm library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki cairomm.

%package static
Summary:	Static cairomm library
Summary(pl.UTF-8):	Statyczna biblioteka cairomm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cairomm library.

%description static -l pl.UTF-8
Statyczna biblioteka cairomm.

%package apidocs
Summary:	cairomm API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki cairomm
Group:		Documentation
BuildArch:	noarch

%description apidocs
API and internal documentation for cairomm library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki cairomm.

%prep
%setup -q -n cairomm-%{version}

%build
mm-common-prepare --copy --force
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcairomm-1.16.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/libcairomm-1.16.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcairomm-1.16.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcairomm-1.16.so
%{_libdir}/cairomm-1.16
%{_includedir}/cairomm-1.16
%{_pkgconfigdir}/cairomm-1.16.pc
%{_pkgconfigdir}/cairomm-ft-1.16.pc
%{_pkgconfigdir}/cairomm-pdf-1.16.pc
%{_pkgconfigdir}/cairomm-png-1.16.pc
%{_pkgconfigdir}/cairomm-ps-1.16.pc
%{_pkgconfigdir}/cairomm-svg-1.16.pc
%{_pkgconfigdir}/cairomm-xlib-1.16.pc
%{_pkgconfigdir}/cairomm-xlib-xrender-1.16.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcairomm-1.16.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/cairomm-1.16
%{_datadir}/devhelp/books/cairomm-1.16
