# revision 25007
# category Package
# catalog-ctan /macros/latex/contrib/slantsc
# catalog-date 2012-01-02 14:24:13 +0100
# catalog-license lppl
# catalog-version 2.11
Name:		texlive-slantsc
Version:	2.11
Release:	3
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.11-1
+ Revision: 759066
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.10-2
+ Revision: 756068
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.10-1
+ Revision: 719550
- texlive-slantsc
- texlive-slantsc
- texlive-slantsc
- texlive-slantsc

