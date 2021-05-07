#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	PRSG
Summary:	Math::PRSG - Perl interface to pseudo random sequence generator function
Summary(pl.UTF-8):	Math::PRSG - interfejs Perla do funkcji generatora ciągów pseudolosowych
Name:		perl-Math-PRSG
Version:	1.0
Release:	23
# if used in a product, Systemics should be given attribution as the author
License:	free use, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f0c32973d5b03d2a665b6ac6ec04b9c
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Math-PRSG/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::PRSG is a Perl interface to pseudo random sequence generator
function. It implements a (159, 31, 0) LFSR, giving a period of 160
bits. This can then be used as a RNG if seeded well (ie. with 160 bits
of entropy) and if the output is fed through a message digest function
(in order to prevent any prediction).

%description -l pl.UTF-8
Math::PRSG to perlowy interfejs do funkcji generatora ciągów
pseudolosowych. Implementuje funkcję LFSR (159, 31, 0) mającą okres
160-bitowy. Może być używany jako generator liczb losowych jeśli
zostanie dobrze zasilony (160 bitami entropii), a wyjście jest
przekazywane przez funkcję skrótu (w celu uniknięcia
przewidywalności).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Math/PRSG/PRSG.so
%{_mandir}/man3/*
