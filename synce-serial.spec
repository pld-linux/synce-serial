# NOTE: since 0.16 it's integrated into synce-core.spec
Summary:	Helper scripts for setting up a serial connection for use with SynCE
Summary(pl.UTF-8):	Skrypty pomocnicze do nawiązywania połączenia szeregowego dla SynCE
Name:		synce-serial
Version:	0.11
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	a83f20eb59c845de192645158d051062
Source1:	synce-device
Patch0:		%{name}-iptables.patch
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains helper scripts for setting up a serial connection
for use with SynCE. They are basically wrappers around pppd.

%description -l pl.UTF-8
Ten moduł zawiera skrypty pomocnicze do nawiązywania połączenia
szeregowego dla SynCE. Są one zasadniczo obudowaniem pppd.

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
%doc ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/synce-serial-abort
%attr(755,root,root) %{_sbindir}/synce-serial-abort-device
%attr(755,root,root) %{_sbindir}/synce-serial-config
%attr(755,root,root) %{_sbindir}/synce-serial-hotplug
%attr(755,root,root) %{_sbindir}/synce-serial-start
%attr(755,root,root) %{_sbindir}/synce-serial-start-device
%attr(755,root,root) %{_sbindir}/synce-serial-udev-add
%attr(755,root,root) %{_sbindir}/synce-serial-udev-remove
%attr(755,root,root) %{_libexecdir}/synce-serial-chat
%config(noreplace) %verify(not md5 mtime size) /etc/ppp/peers/synce-device
# dir shared among some synce-* apps
%dir %{_datadir}/synce
%{_datadir}/synce/synce-serial-common
%{_datadir}/synce/synce-serial.conf
%{_datadir}/synce/synce-udev.rules
%{_datadir}/synce/synce.usermap
%{_mandir}/man8/synce-serial-abort.8*
%{_mandir}/man8/synce-serial-chat.8*
%{_mandir}/man8/synce-serial-config.8*
%{_mandir}/man8/synce-serial-start.8*
