#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8
Version  : 3.5.0
Release  : 51
URL      : http://pypi.debian.net/flake8/flake8-3.5.0.tar.gz
Source0  : http://pypi.debian.net/flake8/flake8-3.5.0.tar.gz
Summary  : the modular source code checker: pep8, pyflakes and co
Group    : Development/Tools
License  : MIT
Requires: flake8-bin
Requires: flake8-python3
Requires: flake8-license
Requires: flake8-python
Requires: configparser
Requires: mccabe
Requires: pycodestyle
Requires: pyflakes
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : mccabe-python
BuildRequires : nose-python
BuildRequires : pep8-python
BuildRequires : pyflakes-python
BuildRequires : pytest-runner
Patch1: gitsnap.patch

%description
Flake8
        ========

%package bin
Summary: bin components for the flake8 package.
Group: Binaries
Requires: flake8-license

%description bin
bin components for the flake8 package.


%package license
Summary: license components for the flake8 package.
Group: Default

%description license
license components for the flake8 package.


%package python
Summary: python components for the flake8 package.
Group: Default
Requires: flake8-python3

%description python
python components for the flake8 package.


%package python3
Summary: python3 components for the flake8 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the flake8 package.


%prep
%setup -q -n flake8-3.5.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533568648
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/flake8
cp LICENSE %{buildroot}/usr/share/doc/flake8/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flake8

%files license
%defattr(-,root,root,-)
/usr/share/doc/flake8/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
