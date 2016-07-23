%global decname Cutegram

%global commit0 7294861b65861adb401668291d85970c5900fc5b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: cutegram
Version: 3.0
Release: 0.1git%{shortcommit0}%{?dist}
Summary: Cutegram is a telegram client by Aseman Land

License: GPLv3+ and MIT
URL: https://github.com/Aseman-Land/%{decname}/
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0: build_bin.patch

BuildRequires: gcc-c++

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtquick1-devel
BuildRequires: qt5-qtmultimedia-devel

BuildRequires: /usr/bin/desktop-file-validate

Requires: hicolor-icon-theme

%description
A different telegram client from Aseman team. Cutegram forked from Sigram
by Sialan Labs. Cutegram project are released under the terms of the GPLv3
license.

%prep
%autosetup -n %{decname}-%{commit0} -p1
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %qmake_qt5 PREFIX=%{_prefix} .. CONFIG+=binaryMode
  %make_build
popd

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{decname}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license LICENSE GPL.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{decname}.desktop

%changelog
* Sat Jul 23 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0-0.1git7294861
- Initial commit.
