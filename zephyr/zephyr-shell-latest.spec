%global debug_package %{nil}
%define __strip /bin/true

%define targetname      qemu_x86_64
%define targettoolchain x86_64
%define firmwarename    shell
%define filename        zephyr-%{firmwarename}-%{targetname}

Name: zephyr-shell
Version: 0.0.0
Release: 0%{?dist}
Summary: Zephyr shell application

License: _TO_COMPLETE_
URL: https://github.com/iotbzh/zephyr-shell/tree/latest
Source0: %{name}-%{version}.tar.gz

# Required Zephyr packages
%if "%{targetname}" == "qemu_x86_64"
BuildRequires: zephyr-kernel-board-qemu_x86_64
%elif "%{targetname}" == "imx8mp_evk/mimx8ml8/m7"
BuildRequires: zephyr-kernel-board-imx8mp_evk_mimx8ml8_m7
%else
BuildRequires: zephyr-kernel
BuildRequires: zephyr-kernel-hal
BuildRequires: zephyr-toolchain-%{targettoolchain}
%endif

%description
Zephyr shell application

%prep
%autosetup

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
- Package Zephyr shell app tag: latest
