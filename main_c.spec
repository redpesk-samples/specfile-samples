%global debug_package %{nil}

Name:    main_c
Version: 1.0.0
Release: 0%{?dist}
License: APL2.0
Summary: A simple application written in C set to be used in redpesk
URL:     https://github.com/redpesk-samples/specfile-samples
Source0: %{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++

%description
A simple application written in C set to be used in redpesk

%prep
%autosetup -p 1

%build
${CC} main.c -o main_c

%install
install -d 0755 %{buildroot}/%{_bindir}
install -m 0755 main_c %{buildroot}/%{_bindir}

%files
%{_bindir}/main_c

%check

%clean

%changelog
