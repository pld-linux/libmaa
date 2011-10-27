Summary:	Low-level data structures which are helpful for writing compilers
Summary(pl.UTF-8):	Struktury niskiego poziomu pomocne do tworzenia kompilatorów
Name:		libmaa
Version:	1.3.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/dict/%{name}-%{version}.tar.gz
# Source0-md5:	04fcb72e8767c0795059bf397f5a0355
URL:		http://sourceforge.net/projects/dict/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libmaa library provides many low-level data structures which are
helpful for writing compilers, including hash tables, sets, lists,
debugging support, and memory management. Although libmaa was designed
and implemented as a foundation for the Khepera Transformation System,
the data structures are generally applicable to a wide range of
programming problems. The memory management routines are especially
helpful for improving the performance of memory-intensive
applications.

%description -l pl.UTF-8
Biblioteka libmaa udostępnia wiele struktur niskiego poziomu
pomocnych do tworzenia kompilatorów, włączając w to tablice
mieszające, zestawy, listy, wspomaganie odpluskwiania oraz
zarządzania pamięcią. Pierwotnie libmaa powstała jako podstawa dla
systemu przekształceń Khepera, ale struktury danych mają zastosowanie
przy wielu zagadnieniach programistycznych. Funkcje zarządzające
pamięcią są przydatne szczególnie przy poprawianiu wydajności
aplikacji intensywnie korzystających z pamięci.

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
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmaa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmaa.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmaa.so
%{_libdir}/libmaa.la
%{_includedir}/maa.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmaa.a
