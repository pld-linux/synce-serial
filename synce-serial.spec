Summary:	Helper scripts for setting up a serial connection for use with SynCE
Summary(pl):	Skrypty pomocnicze do nawi±zywania po³±czenia szeregowego dla SynCE
Name:		synce-serial
Version:	0.9.0
Release:	1
License:	MIT
Group:		Libraries
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	3042891c850fa685e40b1216debc34f9
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains helper scripts for setting up a serial connection
for use with SynCE. They are basically wrappers around pppd.

%description -l pl
Ten modu³ zawiera skrypty pomocnicze do nawi±zywania po³±czenia
szeregowego dla SynCE. S± one zasadniczo obudowaniem pppd.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/synce
%{_mandir}/man8/*.8*
