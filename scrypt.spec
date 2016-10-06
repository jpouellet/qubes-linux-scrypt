%if 0%{?qubes_builder}
%define _sourcedir %(pwd)
%define _builddir %(pwd)
%endif

Name:		scrypt
Version:	1.2.0
Release:	0.1%{?dist}
Summary:	A simple password-based encryption utility

Group:		System Environment/Base
License:	BSD
URL:		https://www.tarsnap.com/scrypt.html
Source0:	https://www.tarsnap.com/scrypt/scrypt-%{version}.tgz
Source1:	https://www.tarsnap.com/scrypt/scrypt-sigs-%{version}.asc

# backports from master branch
Patch0:		0001-Show-command-synopsis-in-usage.patch
Patch1:		0001-Add-v-option-to-print-N-r-p-and-memory-cpu-limits.patch
Patch2:		0001-Add-scrypt-version.patch
Patch3:		0001-scrypt-1-Document-passphrase-reading-behaviour.patch
Patch4:		0002-Provide-P-option-to-read-password-from-stdin.patch
Patch5:		0003-Reword-man-documentation-about-P.patch

BuildRequires:	openssl-devel
#Requires:	

%description
A simple password-based encryption utility is available as a demonstration of
the scrypt key derivation function. On modern hardware and with default
parameters, the cost of cracking the password on a file encrypted by scrypt enc
is approximately 100 billion times more than the cost of cracking the same
password on a file encrypted by openssl enc; this means that a five-character
password using scrypt is stronger than a ten-character password using openssl. 

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc
/usr/bin/scrypt
/usr/share/man/man1/scrypt.1.gz

%changelog

