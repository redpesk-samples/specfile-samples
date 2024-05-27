%global debug_package %{nil}
%define __strip /bin/true

%define targetname      qemu_x86_64
%define targettoolchain x86_64
%define firmwarename    hello-world
%define filename        zephyr-%{firmwarename}-%{targetname}

Name: zephyr-hello-world
Version: 0.0.0
Release: 0%{?dist}
Summary: Zephyr hello world application

License: _TO_COMPLETE_
URL: https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/hello_world

# Required Zephyr packages
BuildRequires: zephyr-kernel
BuildRequires: zephyr-kernel-modules-common
BuildRequires: zephyr-toolchain-%{targettoolchain}

%description
Zephyr in tree hello-world application

%prep
cp -a %{_zephyrkerneldir}/samples/hello_world/. .

%build
%{westbuild} -b %{targetname} .
%if "%{targetname}" == "qemu_x86_64"
cd build && ninja qemu_locore_image_target qemu_main_image_target
%endif

%install
%{__install} -d %{buildroot}/lib/firmware
%{__install} -m 755 build/zephyr/zephyr.elf %{buildroot}/lib/firmware/%{filename}.elf | true
%{__install} -m 755 build/zephyr/zephyr.bin %{buildroot}/lib/firmware/%{filename}.bin | true
%{__install} -m 755 build/zephyr/zephyr.hex %{buildroot}/lib/firmware/%{filename}.hex | true
%if "%{targetname}" == "qemu_x86_64"
%{__install} -m 755 build/zephyr/zephyr*qemu*.elf %{buildroot}/lib/firmware/ | true
%endif

%files
/lib/firmware

%changelog
* Thu Feb 22 2024 Aymeric Aillet <aymeric.aillet@iot.bzh> - 0.0.0-0
- Package in tree Zephyr hello world app
