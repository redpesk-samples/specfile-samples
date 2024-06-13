#---------------------------------------------
# spec file for package mustach
#---------------------------------------------

Name:           mustach
Version:        1.2.9
Release:        2%{?dist}
License:        ISC
Summary:        Tiny Mustach processor
Url:            https://gitlab.com/jobol/mustach
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(json-c)

%description
Tiny tool for processing JSON files with Mustache templates.

#---------------------------------------------
%package lib-core

Summary:        Core library of mustach

%description lib-core
Core library of mustach

#---------------------------------------------
%package lib-core-devel

Summary:        Core library of mustach - Development files
Requires:       %{name}-lib-core = %{version}

%description lib-core-devel
Core library of mustach - Development files


#---------------------------------------------
%package lib-json-c

Summary:        json-c library of mustach
Requires:       pkgconfig(json-c)
Provides:       pkgconfig(libmustach-json-c) = %{version}
Provides:       pkgconfig(libafbcli) = %{version}

%description lib-json-c
Development files for application Framework Binder core library

#---------------------------------------------
%package lib-json-c-devel

Summary:        json-c library of mustach - Development files
Requires:       %{name}-lib-json-c = %{version}
Provides:       pkgconfig(libmustach-json-c) = %{version}

%description lib-json-c-devel
Development files for application Framework Binder core library

#---------------------------------------------
%global pkgdir %{_libdir}/pkgconfig

%global mustach_conf tool=jsonc libs=split jsonc=yes cjson=no jansson=no

%global mustach_env  PREFIX=%{_prefix} DESTDIR=%{buildroot} BINDIR=%{_bindir} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir} MANDIR=%{_mandir} PKGDIR=%{pkgdir}

%global mustach_flags CFLAGS="-O2 -g"

%global mustach_make  %{mustach_flags} %__make %{?_smp_mflags} %mustach_conf %mustach_env

#---------------------------------------------
%prep
%setup -q -n %{name}-%{version}

%build
%mustach_make

%install
%mustach_make install

#---------------------------------------------
%files
%defattr(-,root,root)
%{_bindir}/mustach
%{_mandir}/man1/mustach.1.gz

#---------------------------------------------
%post lib-core
/sbin/ldconfig

%postun lib-core
/sbin/ldconfig

%files lib-core
%defattr(-,root,root)
%{_libdir}/libmustach-core.so.*

#---------------------------------------------
%files lib-core-devel
%defattr(-,root,root)
%{_libdir}/libmustach-core.so
%{pkgdir}/libmustach-core.pc
%{_includedir}/mustach/mustach.h
%{_includedir}/mustach/mustach-wrap.h

#---------------------------------------------
%post lib-json-c
/sbin/ldconfig

%postun lib-json-c
/sbin/ldconfig

%files lib-json-c
%defattr(-,root,root)
%{_libdir}/libmustach-json-c.so.*

#---------------------------------------------
%files lib-json-c-devel
%defattr(-,root,root)
%{_libdir}/libmustach-json-c.so
%{pkgdir}/libmustach-json-c.pc
%{_includedir}/mustach/mustach-json-c.h

#---------------------------------------------
%changelog

* Thu Jun 13 2024 Sébastien Douheret sebastien@iot.bzh 1.2.9
- Bump to 1.2.9

* Thu Oct 07 2021 José Bollo jose.bollo@iot.bzh 1.2.0
- Initial version
