%define upstream_name    Dist-Zilla-Plugin-CopyTo
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Copy to other places plugin for Dist::Zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Dist-Zilla-Plugin-CopyTo
Source0:	https://cpan.metacpan.org/authors/id/R/RE/REDICAPS/Dist-Zilla-Plugin-CopyTo-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildArch:	noarch

%description
Copy to other places plugin for Dist::Zilla.

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
%doc LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

