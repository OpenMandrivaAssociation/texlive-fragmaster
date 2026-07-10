%global tl_name fragmaster
%global tl_revision 26313

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
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(fragmaster.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Fragmaster enables you to use psfrag with pdfLaTeX. It takes EPS files
and psfrag substitution definition files, and produces PDF and EPS files
with the substitutions included.

