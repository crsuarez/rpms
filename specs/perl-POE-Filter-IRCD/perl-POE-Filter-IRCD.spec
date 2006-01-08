# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-IRCD

Summary: POE filter for the IRC protocol
Name: perl-POE-Filter-IRCD
Version: 1.5
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-IRCD/

Source: http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/POE-Filter-IRCD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module implements a POE filter for the IRC protocol.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/POE/Filter/IRCD.pm

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
