# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/slantsc
# catalog-date 2008-11-25 08:48:49 +0100
# catalog-license lppl
# catalog-version 2.10
Name:		texlive-slantsc
Version:	2.10
Release:	1
Summary:	Access different-shaped small-caps fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/slantsc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package enables the use of small capitals in different
font shapes, e.g., slanted or bold slanted for all fonts that
provide appropriate font shapes. (Note that a separate .fd file
is needed to define font shapes such as 'scsl' or 'scit'.).

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
%{_texmfdistdir}/tex/latex/slantsc/slantsc.sty
%doc %{_texmfdistdir}/doc/latex/slantsc/README
%doc %{_texmfdistdir}/doc/latex/slantsc/getversion.tex
%doc %{_texmfdistdir}/doc/latex/slantsc/slantsc.pdf
%doc %{_texmfdistdir}/doc/latex/slantsc/slantsc.xml
%doc %{_texmfdistdir}/doc/latex/slantsc/testslantsc.tex
#- source
%doc %{_texmfdistdir}/source/latex/slantsc/Makefile
%doc %{_texmfdistdir}/source/latex/slantsc/slantsc.dtx
%doc %{_texmfdistdir}/source/latex/slantsc/slantsc.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}