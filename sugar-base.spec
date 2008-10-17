%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Base Sugar library
Name: sugar-base
Version: 0.82.2
Release: 1%{?dist}
URL: http://dev.laptop.org/
Source0: http://dev.laptop.org/pub/sugar/sources/sugar-base/%{name}-%{version}.tar.bz2
License: LGPLv2
Group: System Environment/Libraries
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libpython-devel
BuildRequires: python-gobject-devel
BuildRequires: pygtk2.0-devel
BuildRequires: gettext
BuildRequires: perl-XML-Parser

%description

The base libary for Sugar, the user interface of the One Laptop Per
Child project. It provides helpers for the development of services and
activities.

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)

%{python_sitelib}/*

