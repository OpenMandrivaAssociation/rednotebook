Name:           rednotebook
Version:        2.19
Release:        1
Summary:        A desktop diary
Group:          Office
License:        GPLv2+
URL:            http://rednotebook.sourceforge.net
Source0:        https://github.com/jendrikseipp/rednotebook/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	python3dist(setuptools)
BuildRequires:	desktop-file-utils

Requires:	python3dist(pyyaml)
Requires:	python3dist(pygobject)
Requires:	python3dist(chardet)
Recommends:	python3dist(pyenchant)
Recommends:	python3dist(pygtkspellcheck)

%description
RedNotebook is a desktop diary that makes it very easy for you
to keep track of the stuff you do and the thoughts you have. This
journal software helps you to write whole passages or just facts,
and does so in style.

%prep
%setup -q

%build
%py_build

%install
%py_install

desktop-file-install \
	--add-category="Calendar" \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
