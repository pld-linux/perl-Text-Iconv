#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Text
%define		pnam	Iconv
Summary:	Text::Iconv - Perl interface to iconv() codeset conversion function
Summary(pl.UTF-8):	Text::Iconv - perlowy interfejs do funkcji przekodowującej iconv()
Name:		perl-Text-Iconv
Version:	1.7
Release:	20
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81b26e069eaebb084e91ea3c009b67ae
URL:		https://metacpan.org/dist/Text-Iconv
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the iconv() codeset
conversion function, as defined by the Single UNIX Specification. For
more details see the POD documentation embedded in the file Iconv.pm,
which will also be installed as Text::Iconv(3) man page.

%description -l pl.UTF-8
Ten moduł dostarcza interfejs Perla do funkcji iconv() konwertującej
pomiędzy kodowaniami znaków, zgodnej z Single UNIX Specification.
Więcej informacji znajduje się w manualu Text::Iconv(3).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorarch}/Text/Iconv.pm
%dir %{perl_vendorarch}/auto/Text/Iconv
%{perl_vendorarch}/auto/Text/Iconv/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Iconv/Iconv.so
%{_mandir}/man3/Text::Iconv.3pm*
