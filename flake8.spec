#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8
Version  : 3.5.0
Release  : 42
URL      : http://pypi.debian.net/flake8/flake8-3.5.0.tar.gz
Source0  : http://pypi.debian.net/flake8/flake8-3.5.0.tar.gz
Summary  : the modular source code checker: pep8, pyflakes and co
Group    : Development/Tools
License  : MIT
Requires: flake8-bin
Requires: flake8-python3
Requires: flake8-python
Requires: configparser
Requires: mccabe
Requires: pycodestyle
Requires: pyflakes
Requires: setuptools
BuildRequires : mccabe-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : pytest-runner

BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Flake8
        ========

%package bin
Summary: bin components for the flake8 package.
Group: Binaries

%description bin
bin components for the flake8 package.


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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528561836
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flake8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
