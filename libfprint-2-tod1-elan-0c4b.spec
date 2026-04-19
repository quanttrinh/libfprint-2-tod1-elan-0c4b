%global debug_package %{nil}

Name:           libfprint-2-tod1-elan-0c4b

Version:        0.1.0
Release:        %autorelease
Summary:        Repackaged Elan fingerprint reader driver module from Ubuntu for 04F3:0C4B

Provides:       %{name} == %{version}
Obsoletes:      %{name} < %{version}

License:        GPL-3.0-or-later
URL:            https://launchpad.net/~libfprint-tod1-group
Source0:        https://launchpad.net/~libfprint-tod1-group/+archive/ubuntu/ppa/+sourcefiles/libfprint-2-tod1-elan/%{version}+2404-0ubuntu1/libfprint-2-tod1-elan_%{version}+2404.orig.tar.gz
ExclusiveArch:  x86_64

BuildRequires:  systemd

%description
Repackaged Elan fingerprint reader driver module from Ubuntu for 04F3:0C4B

%prep
%autosetup -C

%build

%install
install -p -m 0755 -D usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-2-tod1-elan-0c4b-%{version}.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-2-tod1-elan-0c4b.so
install -p -m 0644 -D lib/udev/rules.d/60-libfprint-2-tod1-elan.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-tod1-elan-0c4b.rules

%check

%files
%defattr(-,root,root,-)
%{_libdir}/libfprint-2/tod-1/libfprint-2-tod1-elan-0c4b.so
%{_udevrulesdir}/60-libfprint-2-tod1-elan-0c4b.rules

%changelog
%autochangelog
