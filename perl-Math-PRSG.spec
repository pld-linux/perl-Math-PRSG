%define	pdir	Math
%define	pnam	PRSG
%include	/usr/lib/rpm/macros.perl
Summary:	Math-PRSG perl module
Summary(pl):	Modu� perla Math-PRSG
Name:		perl-Math-PRSG
Version:	1.0
Release:	6

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples/prsg_driver.pl
%{perl_sitearch}/Math/PRSG.pm
%dir %{perl_sitearch}/auto/Math/PRSG
%{perl_sitearch}/auto/Math/PRSG/PRSG.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/PRSG/PRSG.so
%{_mandir}/man3/*
