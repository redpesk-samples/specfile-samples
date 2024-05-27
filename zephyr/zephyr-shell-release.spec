%global debug_package %{nil}
%define __strip /bin/true

%define targetname     rcar_h3ulcb_cr7
%define firmwarename   shell
%define filename       zephyr-%{firmwarename}-%{targetname}

Name: zephyr-shell
#Hexsha: 3c4ce801fdf6d7fe8babf3c3cf0255c5a57a646a
Version: 3.5.0
Release: 0%{?dist}
Summary: Zephyr shell application

License: _TO_COMPLETE_
URL: https://github.com/iotbzh/zephyr-shell/tree/3.5.0
Source0: %{name}-%{version}.tar.gz

#Main Zephyr require
BuildRequires: zephyr-kernel
BuildRequires: zephyr-kernel-modules-common
#Needed Zephyr toolchain
BuildRequires: zephyr-toolchain-arm

%description
Zephyr shell application

%prep
%autosetup

%build
%{westbuild} -b %{targetname} .

%install
%{__install} -d %{buildroot}/lib/firmware
%{__install} -m 755 build/zephyr/zephyr.bin %{buildroot}/lib/firmware/%{filename}.bin
%{__install} -m 755 build/zephyr/zephyr.elf %{buildroot}/lib/firmware/%{filename}.elf

%files
/lib/firmware

%changelog
* Thu Feb 22 2024 Aymeric Aillet <aymeric.aillet@iot.bzh> - 3.5.0-0
- Package Zephyr shell app v3.5.0
