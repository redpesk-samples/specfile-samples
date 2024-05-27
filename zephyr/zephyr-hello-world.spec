%global debug_package %{nil}
%define __strip /bin/true

%define targetname     rcar_h3ulcb_cr7
%define firmwarename   hello-world
%define filename       zephyr-%{firmwarename}-%{targetname}

Name: zephyr-hello-world
#Hexsha: 3c4ce801fdf6d7fe8babf3c3cf0255c5a57a646a
Version: 0.0.0
Release: 0%{?dist}
Summary: Zephyr hello world application

License: _TO_COMPLETE_
URL: https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/hello_world

#Main Zephyr require
BuildRequires: zephyr-kernel
BuildRequires: zephyr-kernel-modules-common
#Needed Zephyr toolchain
BuildRequires: zephyr-toolchain-arm

%description
Zephyr in tree hello-world application

%prep
cp -a %{_zephyrkerneldir}/samples/hello_world/. .

%build
%{westbuild} -b %{targetname} .

%install
%{__install} -d %{buildroot}/lib/firmware
%{__install} -m 755 build/zephyr/zephyr.bin %{buildroot}/lib/firmware/%{filename}.bin
%{__install} -m 755 build/zephyr/zephyr.elf %{buildroot}/lib/firmware/%{filename}.elf

%files
/lib/firmware

%changelog
* Thu Feb 22 2024 Aymeric Aillet <aymeric.aillet@iot.bzh> - 0.0.0-0
- Package in tree Zephyr hello world app
