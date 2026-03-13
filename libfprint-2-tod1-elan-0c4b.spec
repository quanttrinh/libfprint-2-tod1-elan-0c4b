%global debug_package       %{nil}

Name:           libfprint-2-tod1-elan-0c4b

Version:        0.1.0
Release:        %autorelease
Summary:        Repackaged driver module binary from Lenovo for Elan 04F3:0C4B fingerprint reader

License:        GPL-3.0
URL:            https://support.lenovo.com/us/en/downloads/ds560935-elan-fingerprint-driver-for-linux-thinkpad-e14-gen-4-thinkpad-e15-gen-4
Source0:        https://github.com/QuanTrinhCA/libfprint-2-tod1-elan-0c4b/archive/refs/tags/%{version}.tar.gz

Requires:       libfprint-tod
#For installing udev rules
BuildRequires:  systemd

%description
Repackaged Elan driver module from Lenovo for fingerprint reader to support 04F3:0C4B.

%prep
%setup -q -n libfprint-2-tod1-elan-0c4b-%{version}

%install
mv libfprint-2-tod1-elan-0c4b-%{version}/* %{_builddir}/libfprint-2-tod1-elan-0c4b-%{version}/
install -p -d -m 0755 %{buildroot}%{_libdir}/libfprint-2/tod-1/
install -m 0644 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-2-tod1-elan.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod1-elan.so
install -p -d -m 0755 %{buildroot}%{_udevrulesdir}
install -m 0644 lib/udev/rules.d/60-libfprint-2-tod1-elan.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-tod1-elan.rules

%files
%defattr(-,root,root,-)
%{_libdir}/libfprint-2/tod-1/libfprint-2-tod1-elan.so
%{_udevrulesdir}/60-libfprint-2-tod1-elan.rules
