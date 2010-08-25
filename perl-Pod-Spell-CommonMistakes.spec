%define upstream_name    Pod-Spell-CommonMistakes
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Holds the wordlist data for Pod::Spell::CommonMistakes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Pod::Spell)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


