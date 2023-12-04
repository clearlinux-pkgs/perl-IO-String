#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-String
Version  : 1.08
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/IO-String-1.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/IO-String-1.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-handle-util-perl/libio-handle-util-perl_0.01-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-IO-String-license = %{version}-%{release}
Requires: perl-IO-String-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
IO::String is an IO::File (and IO::Handle) compatible class that read
or write data from in-core strings.  It is really just a
simplification of what I needed from Eryq's IO-stringy modules.  As
such IO::String is a replacement for IO::Scalar.

%package dev
Summary: dev components for the perl-IO-String package.
Group: Development
Provides: perl-IO-String-devel = %{version}-%{release}
Requires: perl-IO-String = %{version}-%{release}

%description dev
dev components for the perl-IO-String package.


%package license
Summary: license components for the perl-IO-String package.
Group: Default

%description license
license components for the perl-IO-String package.


%package perl
Summary: perl components for the perl-IO-String package.
Group: Default
Requires: perl-IO-String = %{version}-%{release}

%description perl
perl components for the perl-IO-String package.


%prep
%setup -q -n IO-String-1.08
cd %{_builddir}
tar xf %{_sourcedir}/libio-handle-util-perl_0.01-2.debian.tar.xz
cd %{_builddir}/IO-String-1.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-String-1.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-String
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-String/c7cbead4fc445ef2748335e1d1a81a21d992aad2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::String.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-String/c7cbead4fc445ef2748335e1d1a81a21d992aad2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
