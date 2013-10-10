# revision 30653
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-sr
Version:	20131009
Release:	1
Summary:	TeX Live manual (Serbian)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-sr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-sr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-sr package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/README-SR.txt
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/images/tl2013-install-tl-collections-freebsd-sr.png
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/images/tl2013-install-tl-expert-gui-freebsd-sr.png
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/images/tl2013-install-tl-wizard-win32-sr.png
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/images/tl2013-tlmgr-main-screen-freebsd-sr.png
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/images/tl2013-tlmgr-options-freebsd-sr.png
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/images/tl2013-tlmgr-paper-options-freebsd-sr.png
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/texlive-sr.css
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/texlive-sr.html
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/texlive-sr.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/texlive-sr.sty
%doc %{_texmfdistdir}/doc/texlive/texlive-sr/texlive-sr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
