%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Iconv
Summary:	Text::Iconv perl module
Summary(pl):	Modu³ perla Text::Iconv
Name:		perl-Text-Iconv
Version:	1.2
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eb1bfd6f713024bbad95048b367abdf9
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the iconv() codeset
conversion function, as defined by the Single UNIX Specification. For
more details see the POD documentation embedded in the file Iconv.pm,
which will also be installed as Text::Iconv(3) man page.

%description -l pl
Ten modu³ dostarcza interfejs Perla do funkcji iconv() konwertuj±cej
pomiêdzy kodowaniami znaków, zgodnej z Single UNIX Specification.
Wiêcej informacji znajduje siê w manualu Text::Iconv(3).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Text/Iconv.pm
%dir %{perl_vendorarch}/auto/Text/Iconv
%{perl_vendorarch}/auto/Text/Iconv/autosplit.ix
%{perl_vendorarch}/auto/Text/Iconv/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Text/Iconv/*.so
%{_mandir}/man3/*
