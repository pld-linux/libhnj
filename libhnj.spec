Summary:	Libhnj Library
Summary(pl):	Biblioteka Libhnj
Name:		libhnj
Version:	0.1.1
Release:	2
License:	LGPL/MPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/libhnj/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Libhnj is a library for high quality hyphenation and justification.

%description -l pl
Libhnj jest bibliotek± wysokiej jako¶ci hypenacji i justyfikacji.

%package devel
Summary:	Header files etc to develop libhnj applications
Summary(pl):	Pliki nag³ówkowe i inne dla libhnj
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop libhnj applications.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe i inne dla libhnj niezbêdne przy
tworzeniu aplikacji opartych o t± bibliotekê.

%package static
Summary:	Static libhnj libraries
Summary(pl):	Biblioteka statyczna libhnj
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libhnj libraries.

%description -l pl static
Biblioteka statyczna libhnj.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf AUTHORS ChangeLog NEWS README*

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README*}.gz
%attr(755,root,root) %{_bindir}/libhnj-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/libhnj
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
