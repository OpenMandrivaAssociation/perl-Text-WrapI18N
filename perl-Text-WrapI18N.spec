Summary:	Text-WrapI18N module for perl
Name:		perl-Text-WrapI18N
Version:	0.06
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
Source0:	Text-WrapI18N-%{version}.tar.bz2
URL:		http://www.cpan.org
BuildRequires:	perl-devel
BuildRequires:	perl(Text::CharWidth)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n Text-WrapI18N-%{version} 

# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null

make

make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Text/WrapI18N.pm
%{_mandir}/man3/*

