Summary:	Qt Architect
Summary(pl):	Architekt Qt
Name:		qtarch
Version:	2.2
%define	vrel	1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Group(de):	X11/Entwicklung/Werkzeuge
Group(fr):	X11/Development/Outils
Group(pl):	X11/Programowanie/Narzêdzia
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/qtarch/%{name}-%{version}-%{vrel}.tar.gz
Patch:		%{name}-opt.patch
URL:		http://qtarch.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Qt Architect - screen architect for the Qt widget set.

%description -l pl
Architekt Qt - projektant ekranu dla zestawu widgetów Qt.

%prep
%setup -q
%patch -p1

%build
%{__make} BUILD_RELEASE=1 MAKE="make" OPT="%{rpmcflags}" \
	INCDIR="-I%{_includedir}/qt -I`pwd` -I. -Iexpat/xmltok" QTDIR=%{_prefix}

#cd module/kde
#%{__make} BUILD_RELEASE=1 MAKE="make" OPT="%{rpmcflags}" \
#	INCDIR="-I%{_includedir}/qt -I`pwd` -I. -Iexpat/xmltok" QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

install qtarch $RPM_BUILD_ROOT%{_bindir}
#install module/kde/KDEModule.so $RPM_BUILD_ROOT%{_libdir}

gzip -9nf TODO README doc/QtArch.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtarch
#%attr(755,root,root) %{_libdir}/KDEModule.so
%doc *.gz doc/*.gz misc/{DlgEdit.Template.Makefile,dlgUpdate.pl}
%doc help/*.html module/module-howto.html
