# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-ISBN

Summary: Work with International Standard Book Numbers
Name: perl-Business-ISBN
Version: 2.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-ISBN/

Source: http://www.cpan.org/modules/by-module/Business/Business-ISBN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module you can work with ISBN numbers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README bad-isbn13s.txt bad-isbns.txt isbn13s.txt isbns.txt examples/
%doc %{_mandir}/man3/ISBN.3pm*
%doc %{_mandir}/man3/ISBN10.3pm*
%doc %{_mandir}/man3/ISBN13.3pm*
%dir %{perl_vendorlib}/Business/
#%{perl_vendorlib}/Business/ISBN/
%{perl_vendorlib}/Business/ISBN.pm
%{perl_vendorlib}/Business/ISBN10.pm
%{perl_vendorlib}/Business/ISBN13.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.84-1
- Updated to release 1.84.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.82-1
- Updated to release 1.82.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Updated to release 1.80.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 1.79-1
- Initial package.
