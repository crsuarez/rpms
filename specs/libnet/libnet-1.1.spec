# $Id$

# Authority: dag

Summary: Routines to help with network packet contruction and handling
Name: libnet
Version: 1.0.2a
Release: 0%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.packetfactory.net/projects/libnet/

Source: http://www.packetfactory.net/libnet/dist/libnet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libnet is a high-level API (toolkit) allowing the application programmer to
construct and inject network packets. It provides a portable and simplified
interface for low-level network packet shaping, handling and injection.

Libnet hides much of the tedium of packet creation from the application
programmer such as multiplexing, buffer management, arcane packet header
information, byte-ordering, OS-dependent issues, and much more. Libnet
features portable packet creation interfaces at the IP layer and link layer,
as well as a host of supplementary and complementary functionality.

Using libnet, quick and simple packet assembly applications can be whipped up
with little effort. With a bit more time, more complex programs can be written
(Traceroute and ping were easily rewritten using libnet and libpcap).

%prep
%setup -n Libnet-latest

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BIN_PREFIX="%{buildroot}%{_bindir}" \
	INC_PREFIX="%{buildroot}%{_includedir}" \
	LIB_PREFIX="%{buildroot}%{_libdir}" \
	MAN_PREFIX="%{buildroot}/%{_mandir}/man3"
%{__install} -Dp -m0755 libnet-config %{buildroot}%{_bindir}/libnet-config

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man3/*
%{_bindir}/*
%{_libdir}/*
%{_includedir}/libnet.h
%{_includedir}/libnet/
#%{_libdir}/libpwrite

%changelog
* Mon Dec 16 2002 Dag Wieers <dag@wieers.com> - 1.0.2
- Updated to 1.0.2a (1.1.0 does not work with 1.1.0)

* Thu Aug 02 2001 Dag Wieers <dag@wieers.com> - 1.0.1
- Initial package
