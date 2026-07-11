%global tl_name plantuml
%global tl_revision 79512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.0
Release:	%{tl_revision}.1
Summary:	Support for rendering UML diagrams using PlantUML
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/plantuml
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plantuml.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plantuml.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PlantUML is a program which transforms text into UML diagrams. This
LaTeX package allows for embedding PlantUML diagrams using the PlantUML
source. Currently, this project runs with LuaLaTeX only.

