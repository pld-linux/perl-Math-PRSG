#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	PRSG
Summary:	Math::PRSG perl module
Summary(pl):	Modu³ perla Math::PRSG
Name:		perl-Math-PRSG
Version:	1.0
Release:	9
# if used in a product, Systemics should be given attribution as the author
License:	free use, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f0c32973d5b03d2a665b6ac6ec04b9c
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::PRSG - interface to pseudo random sequence generator function.

%description -l pl
Math::PRSG - interfejs do funkcji generowania pseudolosowych sekwencji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples/prsg_driver.pl
%{perl_vendorarch}/Math/PRSG.pm
%dir %{perl_vendorarch}/auto/Math/PRSG
%{perl_vendorarch}/auto/Math/PRSG/PRSG.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/PRSG/PRSG.so
%{_mandir}/man3/*
