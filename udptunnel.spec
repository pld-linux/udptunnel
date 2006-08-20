Summary:	Tunnels UDP over a TCP connection
Summary(pl):	Tunelowanie UDP po po³±czeniu TCP
Name:		udptunnel
Version:	1.1
Release:	1
License:	BSD-like
Group:		Applications/Networking
Source0:	ftp://ftp.cs.columbia.edu/pub/lennox/udptunnel/%{name}-%{version}.tar.gz
# Source0-md5:	1e64753a502f2c12386fa0b7baaf50ba
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

%description -l pl
UDPTunnel jest ma³ym programem, który umo¿liwia dwukierunkowe
tunelowanie pakietów UDP w po³±czeniu TCP. G³ównym celem (i motywacj±)
by³o umo¿liwienie multimedialnym konferencjom pokonywania firewalli,
które pozwala³y jedynie na ruch wychodz±cy. Dzia³a najprawdopodobniej
tylko z ruchem RTP.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README udptunnel.html
%attr(755,root,root) %{_bindir}/*
