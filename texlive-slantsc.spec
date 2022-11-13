Name:		texlive-slantsc
Version:	25007
Release:	1
Summary:	Access different-shaped small-caps fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/slantsc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/slantsc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables the use of small capitals in different
font shapes, e.g., slanted or bold slanted for all fonts that
provide appropriate font shapes. (Note that a separate .fd file
is needed to define font shapes such as 'scsl' or 'scit'.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/slantsc/slantsc.sty
%doc %{_texmfdistdir}/doc/latex/slantsc/ChangeLog
%doc %{_texmfdistdir}/doc/latex/slantsc/Makefile
%doc %{_texmfdistdir}/doc/latex/slantsc/README
%doc %{_texmfdistdir}/doc/latex/slantsc/getversion.tex
%doc %{_texmfdistdir}/doc/latex/slantsc/slantsc.pdf
%doc %{_texmfdistdir}/doc/latex/slantsc/testslantsc.tex
#- source
%doc %{_texmfdistdir}/source/latex/slantsc/slantsc.dtx
%doc %{_texmfdistdir}/source/latex/slantsc/slantsc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
