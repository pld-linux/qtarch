Summary:	Qt Architect
Name:		qtarch
Version:	1.4-4
Release:	1
Source:		http://www.primenet.com/~jtharris/qtarch/%{name}-%{version}.tar.gz
Copyright:	GPL
Group:		Development/Tools
URL:		http://www.primenet.com/~jtharris/qtarch/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Qt Architect

%prep
%setup -q -n %{name}-1.4

%build
make BUILD_RELEASE=1 MAKE="make" CFLAGS="$RPM_OPT_FLAGS -W -Wall -pipe" \
	INCDIR="-I/usr/X11R6/include/X11/qt -I`pwd`" QTDIR=/usr/X11R6

cd module/kde
make BUILD_RELEASE=1 MAKE="make" CFLAGS="$RPM_OPT_FLAGS -W -Wall -pipe" \
	INCDIR="-I/usr/X11R6/include/X11/qt -I`pwd`" QTDIR=/usr/X11R6

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 -s qtarch $RPM_BUILD_ROOT/usr/bin

mkdir -p $RPM_BUILD_ROOT/usr/lib
install -m 755 -s module/kde/KDEModule.so $RPM_BUILD_ROOT/usr/lib

%files
%defattr(644 root root 755)
%attr (755,root,root) /usr/bin/qtarch
%attr (755,root,root) /usr/lib/KDEModule.so
%doc COPYING
%doc TODO
%doc README
%doc misc/DlgEdit.Template.Makefile
%doc misc/dlgUpdate.pl
%doc help/*.html
%doc doc/QtArch.ps
%doc module/module-howto.html
%doc module/kde/README.KDEModule
