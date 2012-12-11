%define upstream_name    Text-WrapI18N
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Text-WrapI18N module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Text::CharWidth)
BuildArch:	noarch

%description
Text::WrapI18N - Line wrapping module with support for multibyte, fullwidth,
and combining characters and languages without whitespaces between words.

This module intends to be a better Text::Wrap module. This module is needed to
support multibyte character encodings such as UTF-8, EUC-JP, EUC-KR, GB2312,
and Big5. This module also supports characters with irregular widths, such as
combining characters (which occupy zero columns on terminal, like diacritical
marks in UTF-8) and fullwidth characters (which occupy two columns on terminal,
like most of east Asian characters). Also, minimal handling of languages which
doesn't use whitespaces between words (like Chinese and Japanese) is supported.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Text/WrapI18N.pm
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 405718
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-4mdv2009.0
+ Revision: 258634
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-3mdv2009.0
+ Revision: 246644
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.06-1mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 0.06-1mdv2007.0
- initial Mandriva package

