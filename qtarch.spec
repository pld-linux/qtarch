Summary:	Qt Architect
Summary(pl):	Architekt Qt
Name:		qtarch
Version:	1.4.4
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://www.primenet.com/~jtharris/qtarch/%{name}-1.4-4.tar.gz
#Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/qtarch/%{name}-2.2-1.tar.gz
URL:		http://qtarch.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Architect - screen architect for the Qt widget set.

%description -l pl
Architekt Qt - projektant ekranu dla zestawu widgetów Qt.

%prep
%setup -q -n %{name}-1.4

%build
%{__make} BUILD_RELEASE=1 MAKE="make" CFLAGS="%{rpmcflags} -W -Wall -pipe" \
	INCDIR="-I%{_prefix}/X11R6/include/X11/qt -I`pwd`" QTDIR=%{_prefix}/X11R6

cd module/kde
%{__make} BUILD_RELEASE=1 MAKE="make" CFLAGS="%{rpmcflags} -W -Wall -pipe" \
	INCDIR="-I%{_prefix}/X11R6/include/X11/qt -I`pwd`" QTDIR=%{_prefix}/X11R6

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

install qtarch $RPM_BUILD_ROOT%{_bindir}
install module/kde/KDEModule.so $RPM_BUILD_ROOT%{_libdir}

gzip -9nf TODO README doc/QtArch.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtarch
%attr(755,root,root) %{_libdir}/KDEModule.so
%doc TODO.gz README.gz doc/QtArch.ps.gz
%doc misc/DlgEdit.Template.Makefile
%doc misc/dlgUpdate.pl
%doc help/*.html
%doc module/module-howto.html
%doc module/kde/README.KDEModule
