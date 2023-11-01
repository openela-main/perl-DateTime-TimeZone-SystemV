# Run optionl test
%bcond_without perl_DateTime_TimeZone_SystemV_enables_optional_test

Name:           perl-DateTime-TimeZone-SystemV
Version:        0.010
Release:        3%{?dist}
Summary:        System V and POSIX timezone strings
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DateTime-TimeZone-SystemV/
Source0:        http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/DateTime-TimeZone-SystemV-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::ISO8601)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
%if %{with perl_DateTime_TimeZone_SystemV_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
%endif
# Dependencies
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
An instance of this class represents a timezone that was specified by means
of a System V timezone recipe or the POSIX extended form of the same
syntax. These can express a plain offset from Universal Time, or a system
of two offsets (standard and daylight saving time) switching on a yearly
cycle according to certain types of rule.

This class implements the DateTime::TimeZone interface, so that its instances
can be used with DateTime objects.

%prep
%setup -q -n DateTime-TimeZone-SystemV-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::TimeZone::SystemV.3*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - No longer include a Makefile.PL in the distribution
  - In META.{yml,json}, point to public bug tracker
  - In META.json, specify type of public repository
- Classify buildreqs by usage
- Make %%files list more specific
- Drop legacy Group: tag

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb  3 2014 Paul Howarth <paul@city-fan.org> - 0.009-1
- Update to 0.009
  - In META.{yml,json}, point to public git repository
  - Bugfix: permit time of day for a DST change to extend up to 24:59:59,
    which POSIX (unclearly) permits and is actually seen in the current
    rule for timezone Asia/Amman
  - Support the extended form of the recipe syntax that is used by
    version 3 of the tzfile(5) file format
  - Bugfix: correct ->offset_for_local_datetime for perpetual-DST ruleset
    that can arise with the tzfile3 system
- Don't need to remove empty directories from the buildroot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.006-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.006-2
- Perl 5.16 rebuild

* Sun Mar 11 2012 Iain Arnell <iarnell@gmail.com> 0.006-1
- update to latest upstream version
- drop Date::JD dependency

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Iain Arnell <iarnell@gmail.com> 0.005-1
- Specfile autogenerated by cpanspec 1.78.
