Summary:	C++ wrapper for cairo
Summary(pl.UTF-8):	Interfejs C++ do cairo
Name:		cairomm
Version:	1.2.4
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	5d862facfbd0098c9bae618b61f7c8e6
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.2.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
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
Requires:	cairo-devel >= 1.2.2
Requires:	libstdc++-devel

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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libcairomm-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libcairomm-1.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/reference/html/*
%attr(755,root,root) %{_libdir}/libcairomm-1.0.so
%{_libdir}/libcairomm-1.0.la
%{_includedir}/cairomm-1.0
%{_pkgconfigdir}/cairomm-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcairomm-1.0.a
