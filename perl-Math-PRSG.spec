%include	/usr/lib/rpm/macros.perl
Summary:	Math-PRSG perl module
Summary(pl):	Modu³ perla Math-PRSG
Name:		perl-Math-PRSG
Version:	1.0
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-PRSG-%{version}.tar.gz
Patch:		perl-Math-PRSG-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-PRSG - interface to pseudo random sequence generator function. 

%description -l pl
Math-PRSG - interfejs do funkcji generowania pseudolosowych sekwencji.

%prep
%setup -q -n Math-PRSG-%{version}
%patch -p1

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Math/PRSG/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/PRSG
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples/prsg_driver.pl

%{perl_sitearch}/Math/PRSG.pm

%dir %{perl_sitearch}/auto/Math/PRSG
%{perl_sitearch}/auto/Math/PRSG/.packlist
%{perl_sitearch}/auto/Math/PRSG/PRSG.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/PRSG/PRSG.so

%{_mandir}/man3/*
