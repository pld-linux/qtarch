Summary:	Qt Architect
Name:		qtarch
Version:	1.4-4
Release:	1
Source0:	http://www.primenet.com/~jtharris/qtarch/%{name}-%{version}.tar.gz
License:	GPL
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
URL:		http://www.primenet.com/~jtharris/qtarch/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Architect

%prep
%setup -q -n %{name}-1.4

%build
%{__make} BUILD_RELEASE=1 MAKE="make" CFLAGS="$RPM_OPT_FLAGS -W -Wall -pipe" \
	INCDIR="-I%{_prefix}/X11R6/include/X11/qt -I`pwd`" QTDIR=%{_prefix}/X11R6

cd module/kde
%{__make} BUILD_RELEASE=1 MAKE="make" CFLAGS="$RPM_OPT_FLAGS -W -Wall -pipe" \
	INCDIR="-I%{_prefix}/X11R6/include/X11/qt -I`pwd`" QTDIR=%{_prefix}/X11R6

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

install -s qtarch $RPM_BUILD_ROOT%{_bindir}
install -s module/kde/KDEModule.so $RPM_BUILD_ROOT%{_libdir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtarch
%attr(755,root,root) %{_libdir}/KDEModule.so
%doc COPYING
%doc TODO
%doc README
%doc misc/DlgEdit.Template.Makefile
%doc misc/dlgUpdate.pl
%doc help/*.html
%doc doc/QtArch.ps
%doc module/module-howto.html
%doc module/kde/README.KDEModule
