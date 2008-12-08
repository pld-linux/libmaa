Summary:	Low-level data structures which are helpful for writing compilers
Summary(pl.UTF-8):	Struktury niskiego poziomu pomocne do tworzenia kompilatorów
Name:		libmaa
Version:	1.1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/dict/%{name}-%{version}.tar.gz
# Source0-md5:	d1883d09f65179a3b6aa16579cb5a7e9
URL:		http://sourceforge.net/projects/dict
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libmaa library provides many low-level data structures which are
helpful for writing compilers, including hash tables, sets, lists,
debugging support, and memory management. Although libmaa was designed
and implemented as a foundation for the kheperalong, the data
structures are generally applicable to a wide range of programming
problems.

The memory management routines are especially helpful for improving
the performance of memory-intensive applications.


%description -l pl.UTF-8
Biblioteka libmaa udostępnia wiele struktur niskiego poziomu
pomocnych do tworzenia kompilatorów, włączając w to tablice
mieszające, zestawy, listy, wspomaganie odpluskwiania oraz
zarządzania pamięcią.

%package devel
Summary:	Header files for libmaa library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmaa
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmaa library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmaa.

%package static
Summary:	Static libmaa library
Summary(pl.UTF-8):	Statyczna biblioteka libmaa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmaa library.

%description static -l pl.UTF-8
Statyczna biblioteka libmaa.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/maa.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
