# revision 21460
# category Package
# catalog-ctan /support/fragmaster
# catalog-date 2011-02-18 08:51:11 +0100
# catalog-license gpl
# catalog-version 1.6
Name:		texlive-fragmaster
Version:	1.6
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Fragmaster enables you to use psfrag with PDFLaTeX. It takes
EPS files and psfrag substitution definition files, and
produces PDF and EPS files with the substitutions included.

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
%doc %{_tlpkgobjdir}/*.tlpobj

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
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
