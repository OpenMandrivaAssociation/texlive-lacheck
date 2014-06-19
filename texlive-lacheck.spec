# revision 33818
# category TLCore
# catalog-ctan /support/lacheck
# catalog-date 2012-06-24 00:35:21 +0200
# catalog-license gpl
# catalog-version 1.26
Name:		texlive-lacheck
Version:	1.26
Release:	10
Summary:	LaTeX checker
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/lacheck
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lacheck.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lacheck.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-lacheck.bin

%description
Lacheck is a tool for finding common mistakes in LaTeX
documents. The distribution includes sources, and executables
for OS/2 and Win32 environments.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/lacheck.1*
%doc %{_texmfdistdir}/doc/man/man1/lacheck.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
