Summary:	Tunnels UDP over a TCP connection
Summary(pl.UTF-8):	Tunelowanie UDP po połączeniu TCP
Name:		udptunnel
Version:	1.1
Release:	2
License:	BSD-like
Group:		Applications/Networking
Source0:	http://www1.cs.columbia.edu/~lennox/udptunnel/%{name}-%{version}.tar.gz
# Source0-md5:	1e64753a502f2c12386fa0b7baaf50ba
# from Debian
Source1:	%{name}.1
Patch0:		%{name}-no-explicit-nis.patch
URL:		http://www1.cs.columbia.edu/~lennox/udptunnel/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UDPTunnel is a small program which can tunnel UDP packets
bi-directionally over a TCP connection. Its primary purpose (and
original motivation) is to allow multi-media conferences to traverse a
firewall which allows only outgoing TCP connections. Works most
probably only with RTP traffic.

%description -l pl.UTF-8
UDPTunnel jest małym programem, który umożliwia dwukierunkowe
tunelowanie pakietów UDP w połączeniu TCP. Głównym celem (i motywacją)
było umożliwienie multimedialnym konferencjom pokonywania firewalli,
które pozwalały jedynie na ruch wychodzący. Działa najprawdopodobniej
tylko z ruchem RTP.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -Dp %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/udptunnel.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README udptunnel.html
%attr(755,root,root) %{_bindir}/udptunnel
%{_mandir}/man1/udptunnel.1*
