Summary:	Helper scripts for setting up a serial connection for use with SynCE
Summary(pl):	Skrypty pomocnicze do nawi±zywania po³±czenia szeregowego dla SynCE
Name:		synce-serial
Version:	0.9.1
Release:	3
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	77f8879486469118386fb7429ec5a794
Source1:	synce-device
Patch0:		%{name}-iptables.patch
URL:		http://www.synce.org/
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--bindir=%{_sbindir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/ppp/peers
install %{SOURCE1} $RPM_BUILD_ROOT/etc/ppp/peers/synce-device

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%attr(755,root,root) %{_sbindir}/synce-serial-abort
%attr(755,root,root) %{_sbindir}/synce-serial-chat
%attr(755,root,root) %{_sbindir}/synce-serial-config
%attr(755,root,root) %{_sbindir}/synce-serial-start
%config(noreplace) %verify(not md5 mtime size) /etc/ppp/peers/synce-device
%{_datadir}/synce
%{_mandir}/man8/*.8*
