%define		plugin		nbsp
Summary:	DokuWiki Syntax plugin for Non-breaking Space
Name:		dokuwiki-plugin-%{plugin}
Version:	20081122
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.mwat.de/dw/syntax_plugin_nbsp.zip
# Source0-md5:	10c5b0f226652cd70af15246cae75401
URL:		http://www.dokuwiki.org/plugin:nbsp
BuildRequires:	rpmbuild(macros) >= 1.520
BuildRequires:	unzip
Requires:	dokuwiki >= 20050713
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
A Syntax plugin to insert Non-breaking Space in documents.

%prep
%setup -qc
mv %{plugin}/* .

version=$(awk -F"'" '/date.*=>/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
