%global tl_name slantsc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.11
Release:	%{tl_revision}.1
Summary:	Access different-shaped small-caps fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/slantsc
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables the use of small capitals in different font shapes,
e.g., slanted or bold slanted for all fonts that provide appropriate
font shapes. (Note that a separate .fd file is needed to define font
shapes such as 'scsl' or 'scit'.)

