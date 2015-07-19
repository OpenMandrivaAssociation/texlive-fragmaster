# revision 26313
# category Package
# catalog-ctan /support/fragmaster
# catalog-date 2011-02-18 08:51:11 +0100
# catalog-license gpl
# catalog-version 1.6
Name:		texlive-fragmaster
Version:	1.6
Release:	11
Summary:	Using psfrag with PDFLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/fragmaster
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragmaster.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragmaster.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-fragmaster.bin = %{EVRD}

%description
Fragmaster enables you to use psfrag with PDFLaTeX. It takes
EPS files and psfrag substitution definition files, and
produces PDF and EPS files with the substitutions included.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/fragmaster
%{_texmfdistdir}/scripts/fragmaster/fragmaster.pl
%doc %{_texmfdistdir}/doc/support/fragmaster/AUTHORS
%doc %{_texmfdistdir}/doc/support/fragmaster/COPYING
%doc %{_texmfdistdir}/doc/support/fragmaster/CREDITS
%doc %{_texmfdistdir}/doc/support/fragmaster/Changes
%doc %{_texmfdistdir}/doc/support/fragmaster/README
%doc %{_texmfdistdir}/doc/support/fragmaster/README.de
%doc %{_texmfdistdir}/doc/support/fragmaster/example/document.pdf
%doc %{_texmfdistdir}/doc/support/fragmaster/example/document.ps
%doc %{_texmfdistdir}/doc/support/fragmaster/example/document.tex
%doc %{_texmfdistdir}/doc/support/fragmaster/example/parabel.eps
%doc %{_texmfdistdir}/doc/support/fragmaster/example/parabel.pdf
%doc %{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm
%doc %{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm.eps
%doc %{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm.gp
%doc %{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm.pdf
%doc %{_texmfdistdir}/doc/support/fragmaster/fragmaster.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/fragmaster/fragmaster.pl fragmaster
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-3
+ Revision: 812266
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 752091
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 718501
- texlive-fragmaster
- texlive-fragmaster
- texlive-fragmaster
- texlive-fragmaster

