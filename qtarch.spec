Summary:	Qt Architect
Summary(pl):	Architekt Qt - graficzny edytor kontrolek Qt
Name:		qtarch
Version:	2.2
%define	vrel	1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/qtarch/%{name}-%{version}-%{vrel}.tar.gz
# Source0-md5:	545f8b11252deb9c0b936f892c6dc271
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-opt.patch
URL:		http://qtarch.sourceforge.net/
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Architect - screen architect for the Qt widget set.

%description -l pl
Architekt Qt - projektant ekranu dla zestawu widgetów Qt.

%prep
%setup -q
%patch -p1

%build
%{__make} BUILD_RELEASE=1 \
	MAKE="make" OPT="%{rpmcflags} -fno-rtti" \
	INCDIR="-I%{_includedir}/qt -I`pwd` -I. -Iexpat/xmltok" \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Development}

install qtarch $RPM_BUILD_ROOT%{_bindir}
#install module/kde/KDEModule.so $RPM_BUILD_ROOT%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README doc/QtArch.ps misc/{DlgEdit.Template.Makefile,dlgUpdate.pl}
%doc help/*.html module/module-howto.html
%attr(755,root,root) %{_bindir}/qtarch
#%attr(755,root,root) %{_libdir}/KDEModule.so
%{_applnkdir}/Development/*
%{_pixmapsdir}/*
