Name:		texlive-fragmaster
Version:	26313
Release:	2
Summary:	Using psfrag with PDFLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/fragmaster
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragmaster.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fragmaster.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/fragmaster/fragmaster.pl fragmaster
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
