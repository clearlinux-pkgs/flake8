#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8
Version  : 4.0.1
Release  : 94
URL      : https://files.pythonhosted.org/packages/e6/84/d8db922289195c435779b4ca3a3f583f263f87e67954f7b2e83c8da21f48/flake8-4.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e6/84/d8db922289195c435779b4ca3a3f583f263f87e67954f7b2e83c8da21f48/flake8-4.0.1.tar.gz
Summary  : the modular source code checker: pep8 pyflakes and co
Group    : Development/Tools
License  : MIT
Requires: flake8-bin = %{version}-%{release}
Requires: flake8-license = %{version}-%{release}
Requires: flake8-python = %{version}-%{release}
Requires: flake8-python3 = %{version}-%{release}
Requires: mccabe
Requires: pycodestyle
Requires: pyflakes
BuildRequires : buildreq-distutils3
BuildRequires : mccabe
BuildRequires : mccabe-python
BuildRequires : pep8-python
BuildRequires : pycodestyle
BuildRequires : pyflakes
BuildRequires : pyflakes-python

%description
.. image:: https://github.com/PyCQA/flake8/workflows/main/badge.svg
:target: https://github.com/PyCQA/flake8/actions?query=workflow%3Amain
:alt: build status

%package bin
Summary: bin components for the flake8 package.
Group: Binaries
Requires: flake8-license = %{version}-%{release}

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
Requires: flake8-python3 = %{version}-%{release}

%description python
python components for the flake8 package.


%package python3
Summary: python3 components for the flake8 package.
Group: Default
Requires: python3-core
Provides: pypi(flake8)
Requires: pypi(mccabe)
Requires: pypi(pycodestyle)
Requires: pypi(pyflakes)

%description python3
python3 components for the flake8 package.


%prep
%setup -q -n flake8-4.0.1
cd %{_builddir}/flake8-4.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635727899
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flake8
cp %{_builddir}/flake8-4.0.1/LICENSE %{buildroot}/usr/share/package-licenses/flake8/a2566e0d5e0f401fe89c88d497209f7e58ad1f80
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flake8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flake8/a2566e0d5e0f401fe89c88d497209f7e58ad1f80

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
