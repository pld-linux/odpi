Summary:	Oracle Database Programming Interface for Drivers and Applications
Name:		odpi
Version:	4.1.0
Release:	1
License:	Apache v2.0, UPL v1.0
Group:		Libraries
Source0:	https://github.com/oracle/odpi/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5347adc5519ba97aaa11b946a2ae0847
URL:		https://oracle.github.io/odpi/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oracle Database Programming Interface for C (ODPI-C) is an open source
library of C code that simplifies access to Oracle Database for
applications written in C or C++. It is a wrapper over Oracle Call
Interface (OCI) that makes applications and language interfaces easier
to develop.


%package devel
Summary:	Header files for odpi library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for odpi library.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="-Iinclude -fPIC %{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_LIB_DIR="$RPM_BUILD_ROOT%{_libdir}" \
	INSTALL_INC_DIR="$RPM_BUILD_ROOT%{_includedir}" \
	INSTALL_SHARE_DIR="$RPM_BUILD_ROOT%{_datadir}/%{name}"

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/{LICENSE.md,README.md,samples,test}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md LICENSE.md README.md
%attr(755,root,root) %{_libdir}/libodpic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libodpic.so.4

%files devel
%defattr(644,root,root,755)
%{_includedir}/dpi.h
%attr(755,root,root) %{_libdir}/libodpic.so
