#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8
Version  : 3.3.0
Release  : 24
URL      : http://pypi.debian.net/flake8/flake8-3.3.0.tar.gz
Source0  : http://pypi.debian.net/flake8/flake8-3.3.0.tar.gz
Summary  : the modular source code checker: pep8, pyflakes and co
Group    : Development/Tools
License  : MIT
Requires: flake8-bin
Requires: flake8-python
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
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
========
Flake8
========
Flake8 is a wrapper around these tools:
- PyFlakes
- pycodestyle
- Ned Batchelder's McCabe script

%package bin
Summary: bin components for the flake8 package.
Group: Binaries

%description bin
bin components for the flake8 package.


%package python
Summary: python components for the flake8 package.
Group: Default
Requires: mccabe-python
Requires: pyflakes-python

%description python
python components for the flake8 package.


%prep
%setup -q -n flake8-3.3.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487185912
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487185912
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flake8

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
