Name:		texlive-plantuml
Version:	55214
Release:	1
Summary:	Support for rendering UML diagrams using the syntax and tool of PlantUML
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plantuml
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plantuml.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plantuml.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for rendering UML diagrams using
the syntax and tools of PlantUML. The PlantUML syntax is very
short and thus enables quickly specifying UML diagrams. Using
dot, PlantUML layouts the diagrams.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/plantuml
%doc %{_texmfdistdir}/doc/lualatex/plantuml

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
