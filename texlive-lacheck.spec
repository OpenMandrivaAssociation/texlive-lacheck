Name:		texlive-lacheck
Version:	1.26
Release:	1
Summary:	LaTeX checker
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/lacheck
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lacheck.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-lacheck.bin
Conflicts:	texlive-texmf <= 20110705-3

%description
Lacheck is a tool for finding common mistakes in LaTeX
documents. The distribution includes sources, and executables
for OS/2 and Win32 environments.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/lacheck.1*
%{_texmfdir}/doc/man/man1/lacheck.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
