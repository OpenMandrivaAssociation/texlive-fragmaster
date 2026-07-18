%global tl_name fragmaster
%global tl_revision 26313
%global tl_bin_links fragmaster:%{_texmfdistdir}/scripts/fragmaster/fragmaster.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Using psfrag with pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/fragmaster
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fragmaster.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fragmaster.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fragmaster.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Fragmaster enables you to use psfrag with pdfLaTeX. It takes EPS files
and psfrag substitution definition files, and produces PDF and EPS files
with the substitutions included.

