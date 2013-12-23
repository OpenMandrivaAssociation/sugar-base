# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name:		sugar-base
Version:	0.88.0
Release:	4
Summary:	Base Sugar library
License:	LGPLv2
Group:		Graphical desktop/Other
Url:		http://sugarlabs.org/

Source0:	http://download.sugarlabs.org/sources/sucrose/glucose/sugar-base/sugar-base-0.88.0.tar.bz2

Requires:	python-dbus  
Requires:	python-decorator  
Requires:	gnome-python-gconf  
Requires:	python-gobject >= 2.15
Requires:	pygtk2.0  
Requires:	python  
Requires:	unzip  

BuildRequires:	perl-XML-Parser  
BuildRequires:	gettext  
BuildRequires:	intltool >= 0.33
BuildRequires:	pkgconfig  
BuildRequires:	python-gobject-devel >= 2.15
BuildRequires:	pygtk2.0-devel  
BuildRequires:	python-devel  


%description
The base libary for Sugar. It provides helpers for the development
of services and activities.

%prep
%setup -q -n sugar-base-0.88.0


%build
%configure2_5x
%make

%install
make DESTDIR=%{buildroot} install
install -d -m 0755 %{buildroot}/%{_datadir}/sugar/activities
%find_lang sugar-base


%files -f sugar-base.lang
%dir %{_datadir}/sugar
%dir %{_datadir}/sugar/activities
%{python_sitelib}/*
%doc COPYING NEWS


