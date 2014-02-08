# revision 26689
# category TLCore
# catalog-ctan /support/lacheck
# catalog-date 2010-12-21 21:15:21 +0100
# catalog-license gpl
# catalog-version 1.26
Name:		texlive-lacheck
Version:	1.26
Release:	4
Summary:	LaTeX checker
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/lacheck
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lacheck.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-lacheck.bin

%description
Lacheck is a tool for finding common mistakes in LaTeX
documents. The distribution includes sources, and executables
for OS/2 and Win32 environments.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.26-3
+ Revision: 812339
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.26-2
+ Revision: 753108
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.26-1
+ Revision: 718802
- texlive-lacheck
- texlive-lacheck
- texlive-lacheck
- texlive-lacheck

