Summary:	Libhnj Library
Summary(pl):	Biblioteka Libhnj
Name:		libhnj
Version:	0.1.1
Release:	7
License:	MPL/LGPL
Group:		Libraries
# formerly ftp://ftp.gnome.org/pub/GNOME/stable/sources/libhnj/
Source0:	http://hkn.eecs.berkeley.edu/~dyoo/pyHnj/%{name}-%{version}.tar.gz
# Source0-md5:	29f5571af559690e916b1c7b1aa6aa1f
Patch0:		%{name}-const-error.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libhnj is a library for high quality hyphenation and justification.

%description -l pl
Libhnj jest bibliotek� wysokiej jako�ci hypenacji i justyfikacji.

%package devel
Summary:	Header files etc to develop libhnj applications
Summary(pl):	Pliki nag��wkowe i inne dla libhnj
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop libhnj applications.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe i inne dla libhnj niezb�dne przy
tworzeniu aplikacji opartych o t� bibliotek�.

%package static
Summary:	Static libhnj libraries
Summary(pl):	Biblioteka statyczna libhnj
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libhnj libraries.

%description static -l pl
Biblioteka statyczna libhnj.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README*
%attr(755,root,root) %{_bindir}/libhnj-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libhnj
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
