%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-sudoku
Version:	43.0
Release:	1
Summary:	GNOME Sudoku game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Sudoku
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.28.3
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	python3
BuildRequires:  gtk-update-icon-cache
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:	pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:	pkgconfig(qqwing) >= 1.1.3
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	meson
BuildRequires:	vala
# For help
Requires:	yelp

Obsoletes:	gnome-sudoku < 3.8.1

%description
GNOME version of the popular Sudoku Japanese logic game.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Sudoku.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Sudoku.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Sudoku.service
%{_iconsdir}/*/*/apps/org.gnome.Sudoku*.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.Sudoku.appdata.xml
