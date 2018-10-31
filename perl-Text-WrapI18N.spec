%define modname    Text-WrapI18N
%define modver 0.06

Summary:	Text-WrapI18N module for perl
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Text/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Text::CharWidth)
BuildRequires:  perl(Test::Simple)

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
%setup -qn %{modname}-%{modver}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Text/WrapI18N.pm
%{_mandir}/man3/*

