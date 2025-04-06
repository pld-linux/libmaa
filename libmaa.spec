Summary:	Low-level data structures which are helpful for writing compilers
Summary(pl.UTF-8):	Struktury niskiego poziomu pomocne do tworzenia kompilatorów
Name:		libmaa
Version:	1.5.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/dict/%{name}-%{version}.tar.gz
# Source0-md5:	9ebbdc4e9bf5ad02fc924f011a389433
URL:		https://sourceforge.net/projects/dict/
BuildRequires:	mk-configure
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
export PREFIX=%{_prefix}
export LIBDIR=%{_libdir}
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
export CPPFLAGS="%{rpmcppflags}"
mkcmake \
	COPTS=" "

%install
rm -rf $RPM_BUILD_ROOT

export PREFIX=%{_prefix}
export LIBDIR=%{_libdir}
mkcmake install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{LICENSE,NEWS,TODO}
%attr(755,root,root) %{_libdir}/libmaa.so.*.*
%ghost %{_libdir}/libmaa.so.4

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmaa.so
%{_includedir}/maa.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmaa.a
