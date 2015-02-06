%define upstream_name    Pod-Spell-CommonMistakes
%define upstream_version 1.000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Holds the wordlist data for Pod::Spell::CommonMistakes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Pod::Spell)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module looks for any typos in your POD. It differs from the Pod::Spell
manpage or the Test::Spelling manpage because it uses a custom wordlist and
doesn't use the system spellchecker. The idea for this came from the the
http://wiki.debian.org/Teams/Lintian manpage code in Debian, thanks!

To use this, just pass it a filename that has POD in it and you'll get a
hashref back. If the hashref is empty that means the checker found no
misspelled words. If it contains keys, then the keys are the bad words and
the values are the suggested spelling.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 657464
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1
+ Revision: 643451
- update to new version 1.000

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 573148
- import perl-Pod-Spell-CommonMistakes

